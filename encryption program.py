
import random 
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)
keys = chars.copy()
random.shuffle(keys)
# print(f"chars :{chars}" )
# print(f"Keys :{keys}" )


# * Encrypting

plain_text = input("Enter a message to encrypt : ")
cipher_text = ""


for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]
    
print(cipher_text)

# * Decrypting

decrypt = ""
for letter in cipher_text:
    index = keys.index(letter)
    decrypt += chars[index]

print(decrypt)
    
