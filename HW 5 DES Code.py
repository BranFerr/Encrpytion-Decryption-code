from cryptography.fernet import Fernet
  
#I will be encryting the below string.
message = "Duffman says: ""Can't get enough of that wonderful Duff!"
  
#Then, generate a key for encryption and decryption using the fernet/ cryptography library to generate the key or use random key generaton; here I'm using fernet/cryptography to generate key
  
key = Fernet.generate_key()
  
# Instance the Fernet class with the key
  
fernet = Fernet(key)
  
# then use the Fernet class instance to encrypt the string string must must be encoded to byte string before encryption.
encMessage = fernet.encrypt(message.encode())
  
print("original message: ", message)
print("encrypted message: ", encMessage)
  
# decrypt the encrypted string with the Fernet class instance of the key, that was used for encrypting the string encoded byte string is returned by decrypt method, so decode it to string with decode method.
decMessage = fernet.decrypt(encMessage).decode()
  
print("decrypted message: ", decMessage)