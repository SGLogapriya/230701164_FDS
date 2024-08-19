from cryptography.fernet import Fernet
key=Fernet.generate_key()
f=Fernet(key)
token=f.encrypt(b'This is computer science department.')
token
b'...'
f.decrypt(token)
b'This is computer science department'
key=Fernet.generate_key()
cipher_suite=Fernet(key)
plain_text=b'This is computer science department.'
cipher_text=cipher_suite.encrypt(plain_text)
decrypted_text=cipher_suite.decrypt(cipher_text)
print('Original data:',plain_text)
print('Encrypted data:',cipher_text)
print('Decrypted data:',decrypted_text) 