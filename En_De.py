from cryptography.fernet import Fernet

def Encrypt(key, plain_text):
    
    # Encode the plain text to bytes
    byte_text = plain_text.encode('utf-8')

    # Create a Fernet cipher suite using the provided key
    cipher_suite = Fernet(key)
    
    # Encrypt the byte text
    cipher_text = cipher_suite.encrypt(byte_text)

    # Convert the encrypted byte text to a UTF-8 encoded string
    cipher_text = cipher_text.decode('utf-8')

    # Add a delimiter '%' at the end of the cipher text for later extraction
    cipher_text = cipher_text + '%'

    return cipher_text


def Decrypt(key, cipher_text):
    
    # Encode the cipher text to bytes
    cipher_text = cipher_text.encode('utf-8')

    # Create a Fernet cipher suite using the provided key
    cipher_suite = Fernet(key)

    # Decrypt the cipher text
    decrypted_text = cipher_suite.decrypt(cipher_text)

    # Convert the decrypted byte text to a UTF-8 encoded string
    decrypted_text = decrypted_text.decode('utf-8')

    return decrypted_text
