import hashlib # for SHA256 computation
import binascii # for conversion between Hexa and bytes
import string
import random

# initializing size of string
N = 32

# using random.choices()
# generating random strings
res = ''.join(random.choices(string.hexdigits +
							string.digits, k = N))
entropy = str(res)

#print(entropy)
data = entropy.strip() #cleaning of data
data = binascii.unhexlify(data)
if len(data) not in [16, 20, 24, 28, 32]:
   raise ValueError(f"Data length should be one of the following: [16, 20, 24, 28, 32], but it is not {len(data)}.")

h = hashlib.sha256(data).hexdigest()
b = bin(int(binascii.hexlify(data),16))[2:].zfill(len(data)*8) + bin(int(h,16))[2:].zfill(256)[: len(data)* 8//32]

with open("wordlist/english.txt", "r") as f:
         wordlist = [w.strip() for w in f.readlines()]

seed = []
for i in range(len(b)//11):
    indx = int(b[11*i:11*(i+1)],2)
    seed.append(wordlist[indx])

def listToString(s): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in s: 
        str1 += ele+' '  
    
    # return string  
    return str1 

print("Mnemonic Phrase\n\n"+ listToString(seed)) 
