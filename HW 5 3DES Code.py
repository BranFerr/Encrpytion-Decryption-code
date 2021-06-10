from Crypto.Cipher import DES3
from Crypto import Random

#implementing a key of 16 bits.
key = 'Sixteen byte key'

#DES3.block_size==8, this is just a reminder for the programmer.
iv = Random.new().read(DES3.block_size)

Cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)

#padded with spaces so than len(plaintext) is multiple of 8 if not, it wouldn't work properly.
plaintext = 'Duffman says: Cant get enough of that wonderful Duff!'

encrypted_text = Cipher_encrypt.encrypt(plaintext)

#you can't reuse an object for encrypting or decrypting other data with the same key, it will crash and burn.
cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv) 
cipher_decrypt.decrypt(encrypted_text)
cipher_decrypt.decrypt(encrypted_text)

#for some reason this program is giving me a massive amount of trouble and i'm not sure how to fix it.
