import argparse
import cv2
import os
import En_De as ED  

# Dictionary mapping characters to their ASCII values and vice versa
d = {}
c = {}
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Encryption key
key = b'XFSn0xe3I9_IXrF3CFLiKLsYiHtexklllbu0KvwVoy4='

# Command-line argument parser
main_parser = argparse.ArgumentParser(description='Embed or extract a message from a cover file')

# Arguments for embedding
main_parser.add_argument('--embed', '-em', action='store_true', help='enables embedding')
main_parser.add_argument('--extract', '-ex', action='store_true', help='enables extracting')
main_parser.add_argument('--messagefile', '-mf', help='Input Message file')
main_parser.add_argument('--coverfile', '-cf', help='Input Cover file')
main_parser.add_argument('--stegofile', '-sf', help='output file')
main_parser.add_argument('--open', '-of', help='input file for extracting')
main_parser.add_argument('--extractfile', '-xf', help='extracted file')

args = main_parser.parse_args()

if args.embed:
    # Embedding process
    message_file = args.messagefile
    cover_file = args.coverfile
    stego_file = args.stegofile

    with open(f'{message_file}', 'r') as file:
        message = file.read()

    #Encoding the given message
    encoded_message = ED.Encrypt(key, message)

    img = cv2.imread(f"{cover_file}")

    m = 0
    n = 0
    z = 0

    # Embedding the encoded message into the image
    for i in range(len(encoded_message)):
        img[n, m, z] = d[encoded_message[i]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    
    cv2.imwrite(f"{stego_file}", img)

    os.system(f"open {stego_file}")

elif args.extract:
    # Extraction process
    open_file = args.open
    extract_file = args.extractfile

    img_ = cv2.imread(f"{open_file}")

    cipher_message = ""

    n = 0
    m = 0
    z = 0

    # Extracting the cipher message from the image
    while True:
        if c[img_[n, m, z]] == "%":
            break
        else:
            cipher_message = cipher_message + c[img_[n, m, z]]

            n = n + 1
            m = m + 1
            z = (z + 1) % 3

    #Decoding the message from cipher text
    decoded_message = ED.Decrypt(key, cipher_message)

    with open(f'{extract_file}', 'w') as file:
        file.write(decoded_message)

    os.system(f"open {extract_file}")
