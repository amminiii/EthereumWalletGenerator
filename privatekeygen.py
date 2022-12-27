import os
import mnemonic
def ui():
   
    choices = {
    '1' : '1', 
    '2' : '2'
    }

    print("1. Generate an address for me\n2. Generate 'n' addresses\n3. Convert mnemonic to private key")
    ad = 'invalid'
    id = ad
    while id == ad:
        id = input('\nSelect an option from above : ')
        id = choices.get(id,'invalid')
    if id == '1':
        os.system('python3 pkhelper.py')
        exit()
    elif id == '2':
        n = int(input("Enter number of addresses to generate - "))
        print('')
        ini = 1
        while ini <= n:
            print(f'{ini}')
            os.system('python3 pkhelper.py')
            print('')
            ini+=1

    elif id == '3':
        mnemonic_phrase = input("Enter the mnemonic phrase - ")
        seed = mnemonic.Mnemonic.to_seed(mnemonic_phrase)

        # Use the seed to generate the private key
        private_key_bytes = hashlib.sha256(seed).digest()
        private_key = ecdsa.SigningKey.from_string(private_key_bytes, curve=ecdsa.SECP256k1)
        print(private_key.to_string().hex())


if __name__ == "__main__":
    ui()
