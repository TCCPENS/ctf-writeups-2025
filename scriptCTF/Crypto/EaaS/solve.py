from pwn import remote, context, xor

context.log_level = "DEBUG"

p = remote("play.scriptsorcerers.xyz", 10127)

email = p.recvline_contains(b"Your Email is:").decode().split(":")[-1].strip()
print(email)

email_edited = (",a" + email[1:] + ",").encode()
payload = b"a" * 16 + email_edited + b"yellow__submarine@acript.sorcerer"
p.sendline(payload.hex().encode())

p.recvuntil(b"login: ")
enc = p.recvline()
enc = bytes.fromhex(enc.decode())

c1, c2, c3, c4, c5 = enc[:16], enc[16:32], enc[32:48], enc[48:64], enc[64:80]

delta1 = xor(email_edited[:16], b"," + email.encode()[:15])
delta2 = xor(b"@acript.sorcerer", b"@script.sorcerer")

c1_edit = xor(c1, delta1)
c4_edit = xor(c4, delta2)

final = c1_edit + c2 + c3 + c4_edit + c5

p.sendline(b"2")
p.sendline(final.hex().encode())
p.sendline(b"1")

p.interactive()
