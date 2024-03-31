from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
from pwn import *

def xor(plaintext, malicious):
    output = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        output[i] = plaintext[i] ^ malicious[i]
    
    return output

def create_malicious(token):
    iv = token[:32]
    cyphertext = token[32:]

    print(f"The iv is: {iv}")
    print(f"The cyphertext is: {cyphertext}")

    real_text = pad("               usr=;is_admin=0".encode(), 32) #No clue of this,
    malicious_text = pad("               usr=;is_admin=1".encode(), 32) #I don't get why i must shift them by this much
    xored_bits = xor(malicious_text, real_text)
    print(f"The xored bits are {xored_bits}")
    malicious_iv = xor(iv.encode(), xored_bits)
    print(malicious_iv.decode())
    return malicious_iv.decode()+cyphertext

def main():
    challenge_server = remote('notadmin.challs.cyberchallenge.it', 9032)
    challenge_server.recvuntil(">")
    challenge_server.sendline("1")
    challenge_server.recv()
    challenge_server.recv()
    challenge_server.sendline("")
    token = challenge_server.recvline().decode()[18:]
    malicious_token = create_malicious(token)
    print(f"The malicious token is: {malicious_token}")
    challenge_server.recvuntil(">")
    challenge_server.sendline("2")
    challenge_server.recv()
    challenge_server.sendline(malicious_token)
    challenge_server.recvline()
    print(challenge_server.recvline().decode())

if __name__ == "__main__":
    main()
# print(len(malicious_token[32:]))
# cipher = AES.new(key, AES.MODE_CBC, bytes.fromhex(malicious_token[:32]))
# pt = unpad(cipher.decrypt(bytes.fromhex(malicious_token[32:])),16)
# print(pt.decode())