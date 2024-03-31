from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
from pwn import *
import ast

def xor(plaintext, malicious):
    output = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        output[i] = plaintext[i] ^ malicious[i]
    
    return output

def main():
    challenge_server = remote('predictable.challs.cyberchallenge.it', 9034)
    challenge_server.recvuntil(b">")
    challenge_server.sendline(b"1")
    challenge_server.recvuntil(b"Insert your username:")
    challenge_server.sendline(b"")
    token = challenge_server.recvline().decode()[19:].rstrip()
    print(f"The user token is: {token}")
    challenge_server.recvuntil(b">")
    challenge_server.sendline(b"4")
    IVs = eval(challenge_server.recvuntil(b"}").decode())
    admin_IV = IVs['admin']
    user_IV = IVs['']
    print(f"The user iv is: {user_IV}")
    print(f"The admin iv is: {admin_IV}")
    print("Generating the command with user IV:")
    challenge_server.recvuntil(b">")
    challenge_server.sendline(b"2")
    challenge_server.recvuntil(b"token")
    print(len(token))
    challenge_server.sendline(token.encode())
    print("i'm here")
    print(challenge_server.recvline())
    challenge_server.recvuntil(b"execute? ")
    command = "get_flag".encode()

    padded_command = pad(command, 16)
    IV_difference = xor(bytes.fromhex(admin_IV), bytes.fromhex(user_IV))
    xored_command = xor(padded_command[:16], IV_difference)

    challenge_server.sendline(xored_command.hex())
    command_token = challenge_server.recvline().decode()[20:].rstrip()
    print(f"The command token is: {command_token}")

    print(f"The lenght of the actual command is: {len(bytes.fromhex(command_token[32:]))}")

    modified_command_token = admin_IV + command_token[32:64]
    print(f"The modified command token is: {modified_command_token}")

    challenge_server.recvuntil(b">")
    challenge_server.sendline(b"3")
    challenge_server.recvuntil(b"do? ")
    challenge_server.sendline(modified_command_token)
    print(challenge_server.recvline())

if __name__ == "__main__":
    main()