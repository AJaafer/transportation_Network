from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto import Random
inputmessage = input("please type a message:")
hash_sha1 = SHA.new(inputmessage.encode()).digest()
random_generator = Random.new().read
Bob_key = RSA.generate(1024,random_generator)
random_generator = Random.new().read
Alice_key = RSA.generate(1024,random_generator)
signature = Bob_key.sign(hash_sha1,'')
hasd_data_encry = Alice_key.publickey().encrypt(hash_sha1, 32)
hash_of_decrypted = Alice_key.decrypt(hasd_data_encry)
Bob_key.publickey().verify(hash_of_decrypted, signature)
signature_Alice = Alice_key.sign(hash_sha1,'')
hasd_data_encry = Bob_key.publickey().encrypt(hash_sha1, 32)
hash_of_decrypted = Bob_key.decrypt(hasd_data_encry)
Alice_key.publickey().verify(hash_of_decrypted, signature_Alice)
