from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256
import os

private_key = keccak_256(token_bytes(32)).digest()
public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
addr = keccak_256(public_key).digest()[-20:]


def generate(p,a):
    print('ERC20 ADDRESS: 0x' + a.hex().upper())
    print('PRIVATE KEY:', p.hex())
    pass

generate(private_key,addr)
