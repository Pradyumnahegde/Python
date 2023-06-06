from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

message = "Hello, World!"

key = get_random_bytes(16)
iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

padded_message = message.encode(
    'utf-8') + b"\0" * (AES.block_size - len(message) % AES.block_size)

ciphertext = cipher.encrypt(padded_message)
# Encrypt
print("Encrypted message:", ciphertext)
print("Key:", key)
print("IV:", iv)
# Decrypt
decipher = AES.new(key, AES.MODE_CBC, iv)
decrypted_message = decipher.decrypt(ciphertext).rstrip(b"\0").decode('utf-8')

print("Decrypted message:", decrypted_message)
