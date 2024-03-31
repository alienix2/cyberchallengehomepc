from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os

def xor(plaintext, malicious):
    output = bytearray(len(plaintext))
    for i in range(len(plaintext)):
        output[i] = plaintext[i] ^ malicious[i]
    
    return output

key = os.urandom(16)
IV_admin = os.urandom(16)
IV_user = os.urandom(16)
plaintext = "get_flag"

cypher_admin = AES.new(key, AES.MODE_CBC, IV_admin)
cypher_user = AES.new(key, AES.MODE_CBC, IV_user)

encoded_plain = pad(plaintext.encode(), 16)
#encoded_plain = plaintext.encode()
IV_difference = xor(IV_admin, IV_user)
xored_plain = xor(encoded_plain[:16], IV_difference)
#xored_plain = pad(xored_plain, 16)
print(len(xored_plain))

xored_plain = pad(bytes.fromhex(xored_plain.hex()), 16)
print(len(xored_plain))
print(xored_plain)
crypted_user = cypher_user.encrypt(xored_plain)

decrypted_admin = unpad(cypher_admin.decrypt(crypted_user[:16]), 16)
#decrypted_admin = unpad(decrypted_admin, 16)

print(decrypted_admin)