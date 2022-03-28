from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import os

private_key = keccak_256(token_bytes(32)).digest()
public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
addr = keccak_256(public_key).digest()[-20:]

def clear():
    if os.name == 'nt':
        os.system("cls")
    else:
        os.system("clear")

def generate(p,a):
    print('ERC20 ADDRESS: 0x' + a.hex().upper())
    print('PRIVATE KEY:', p.hex())
    pass

def ui():
    #clear()
    choices = {
    '1' : '1', 
    '2' : '2'
    }

    print("1. Generate an address for me\n2. Generate 'n' addresses for me (BROKEN)")
    ad = 'invalid'
    id = ad
    while id == ad:
        id = input('\nSelect an option from above : ')
        id = choices.get(id,'invalid')
    if id == '1':
        generate(private_key,addr)
        exit()
    elif id == '2':
        n = input("Enter number of addresses to generate - ")
        n = int(n)
        ini = 1

        while(ini <= n):
            print(f'\n{ini}')
            generate(private_key,addr)
            print('\n')
            ini++1


if __name__ == "__main__":
    ui()