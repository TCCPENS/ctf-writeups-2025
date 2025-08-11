#!/usr/bin/env python3
import sys, os
from Crypto.Cipher import AES

def unpad(s):
    if not s: return s
    pad = s[-1]
    if pad < 1 or pad > 16:
        return s
    return s[:-pad]

if len(sys.argv) != 2:
    print("Usage: python3 decrypt.py <password>")
    sys.exit(1)

password = sys.argv[1].encode()   # key got from logs httpd :3
iv = b"R4ND0MivR4ND0Miv"           # IV observed in logs also 

for fname in sorted(os.listdir('.')):
    if not fname.endswith('.enc'):
        continue
    with open(fname, 'rb') as f:
        data = f.read()
    cipher = AES.new(password, AES.MODE_CBC, iv)
    pt = cipher.decrypt(data)
    pt = unpad(pt)
    outname = fname[:-4]  # strip .enc
    with open(outname, 'wb') as out:
        out.write(pt)
    print(f"Decrypted {fname} -> {outname}")
print("Done.")
