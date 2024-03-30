from pwn import *
from binascii import unhexlify

host = 'padding.challs.cyberchallenge.it'
port = 9030
challenge_server = remote(host, port)

def skip_intro():
    for i in range(5):
        challenge_server.recvline()

def send_encoded(input):
    challenge_server.recv()
    challenge_server.sendline(bytes(input, 'utf-8'))
    output = challenge_server.recvline()
    challenge_server.recvline()
    encoded_bytes = output[39:]
    decoded = "".join(encoded_bytes.decode())
    return decoded[96:128]

if __name__ == '__main__':
    skip_intro()
    flag = ''

    while True:
        payload = "0"*(63-len(flag))
        hex = send_encoded(payload)

        for i in range(33, 126):
            if  send_encoded(payload + flag + chr(i)) == hex:
                print(i)
                flag += chr(i)
                print("Flag: ", flag)
                break