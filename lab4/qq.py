﻿from Crypto.PublicKey import RSA
from Crypto import Random
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)
key
public_key = key.publickey()
enc_data = public_key.encrypt('abcdefgh', 32)
enc_data