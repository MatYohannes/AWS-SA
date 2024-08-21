import boto3
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


# Load encryption key from file
def load_key_from_file(file_path):
    with open(file_path, 'r') as key_file:
        base64_key = key_file.read().strip()
        # Decode Base64 key
        return base64.b64decode(base64_key)


# Encrypt the data
def encrypt_data(key, data):
    if len(key) not in {16, 24, 32}:
        raise ValueError(f"Invalid key size ({len(key)}) for AES.")
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    # Ensure data is a multiple of block size
    padded_data = data + (16 - len(data) % 16) * b'\x00'
    return encryptor.update(padded_data) + encryptor.finalize()


# Decrypt the data
def decrypt_data(key, encrypted_data):
    if len(key) not in {16, 24, 32}:
        raise ValueError(f"Invalid key size ({len(key)}) for AES.")
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_padded_data = decryptor.update(encrypted_data) + decryptor.finalize()
    # Remove padding
    return decrypted_padded_data.rstrip(b'\x00')


# AWS S3 client
s3 = boto3.client('s3')

bucket_name = 'encrypt-client-myy'
upload_key = 'encrypted_file.txt'  # Key for the encrypted file in S3
download_key = 'helloagain.txt'    # Key for the decrypted file

# Load the encryption key from file
key = load_key_from_file('encryption.key')

# Read the file to be encrypted
with open('hello.txt', 'rb') as file:
    data = file.read()

# Encrypt and upload the data
encrypted_data = encrypt_data(key, data)
s3.put_object(Bucket=bucket_name, Key=upload_key, Body=encrypted_data)

# Download the encrypted data
response = s3.get_object(Bucket=bucket_name, Key=upload_key)
encrypted_data_from_s3 = response['Body'].read()

# Decrypt the data
decrypted_data = decrypt_data(key, encrypted_data_from_s3)

# Save the decrypted data to a new file
with open(download_key, 'wb') as file:
    file.write(decrypted_data)

print('Decrypted file saved as', download_key)
