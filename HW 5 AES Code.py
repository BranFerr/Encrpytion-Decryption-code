import pyaes, pbkdf2, binascii, os, secrets

#Making a 256-bit AES encryption key from password (same as plaintext so it is easier to understand.)
password = "Duffman says: Cant get enough of that wonderful Duff!"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
print('AES encryption key:', binascii.hexlify(key)) #makes this key consist of 64 hex digits (32 bytes and salt is used through each iteration, so same key is derived.)

# Encrypt the plaintext with the given key, and generate a random 256-bit vector, to perform AES 256 encryption (This is the easiest way i could find....)
iv = secrets.randbits(256)
plaintext = "Duffman says: Cant get enough of that wonderful Duff!" #kept this for brevity.
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
print('Encrypted:', binascii.hexlify(ciphertext))

# Decrypt the ciphertext with the given key, with the input of ciphertext + encryption key + vector for CTR counter, and output plaintext.
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
decrypted = aes.decrypt(ciphertext)
print('Decrypted:', decrypted)

#I'm not even sure this is proper programming practice for encryption, but it works, so i'm thrilled.
