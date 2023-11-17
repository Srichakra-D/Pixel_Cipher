Hi Everyone!

# Pixel Cipher

Pixel Cipher is a lightweight command-line steganography tool developed in Python as part of my internship with IBM SkillsBuild. 

This tool empowers users to embed and extract messages securely within images, utilizing the robust AES-128 encryption algorithm to ensure the security and confidentiality of the embedded messages.

## Features

1. Embedding Operation:

    python3 main.py -em -mf message.txt -cf demo_pic.png -sf stegoimage.png

    - `-em` : Initiates the embedding operation.
    - `-mf message.txt` : Specifies the file containing the message to be embedded.
    - `-cf demo_pic.png` : Specifies the cover file (original image) for embedding.
    - `-sf stegoimage.png` : Specifies the filename for the resulting stego image.

2. Extraction Operation:

    python3 main.py -ex -of stegoimage.png -xf decrypt.txt

    - `-ex` : Initiates the extraction operation.
    - `-of stegoimage.png` : Specifies the stego image file for message extraction.
    - `-xf decrypt.txt` : Specifies the output file for the extracted message.

Note: Do all operations with .png and .txt files only.

## Usage

1. Clone the Repository:
    ```
     git clone https://github.com/Srichakra-D/Pixel_Cipher.git
     cd pixel_cipher
     ```

2. Embedding:
    - Place the message to be embedded in a text file (e.g., `message.txt`).
    - Ensure that the cover file (`demo_pic.png`) is the image in which the message will be embedded.
    - Run the following command to embed the message:
    ```
    python3 main.py -em -mf message.txt -cf demo_pic.png -sf stegoimage.png
    ```
    - The resulting stego image will be saved with the specified filename (`stegoimage.png`).

3. Extraction:
    - Extract the message from the stego image (`stegoimage.png`).
    - Run the following command to extract and decrypt the message, saving it to `decrypt.txt`:
    ```
    python3 main.py -ex -of stegoimage.png -xf decrypt.txt
    ```
    - The extracted message will be saved in the specified output file (`decrypt.txt`) after decryption.



## Requirements

    - Python 3(or above)
    - Libraries:
        - [Fernet](https://cryptography.io/en/latest/fernet/)
        - [argparse](https://docs.python.org/3/library/argparse.html)
        - [cv2](https://pypi.org/project/opencv-python/)
        - [os](https://docs.python.org/3/library/os.html)



## Acknowledgments

Special thanks to the IBM SkillsBuild team for the opportunity and support throughout the Internship.

Feel free to contribute, report issues, and enhance the capabilities of Pixel Cipher!

