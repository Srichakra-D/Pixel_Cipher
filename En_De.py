from cryptography.fernet import Fernet

def Encrypt(key,plain_text):

    bite_text=plain_text.encode('utf-8')

    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(bite_text)

    cipher_text = cipher_text.decode('utf-8')
    cipher_text = cipher_text+'%'
        
    return cipher_text

def Decrypt(key,cipher_text):

    cipher_text=cipher_text.encode('utf-8')

    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(cipher_text)

    decrypted_text=decrypted_text.decode('utf-8')

    return decrypted_text

