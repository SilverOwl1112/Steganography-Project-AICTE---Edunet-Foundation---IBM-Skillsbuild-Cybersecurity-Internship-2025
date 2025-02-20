# Steganography-Project-AICTE---Edunet-Foundation---IBM-Skillsbuild-Cybersecurity-Internship-2025
# Secure Data Hiding in Image Using Steganography with Python

## Overview
This project demonstrates image steganography using Python and OpenCV. It allows users to hide a secret message inside an image and later retrieve it using a passcode. The encryption process modifies the least significant bits (LSB) of the image pixels to store the message, ensuring minimal distortion of the image.

## Features
- **Encrypt a secret message**: Hide a text message inside a PNG image.
- **Decrypt the hidden message**: Extract the original message using the correct passcode.
- **Passcode Protection**: Only users with the correct passcode can retrieve the hidden message.
- **User Input for File Paths**: Users specify the image file path at runtime.

## Requirements
- Python 3.x
- OpenCV (`cv2`)

To install the required dependencies, run:
```bash
pip install opencv-python
```

## How to Use
### Encryption
1. Run `encrypt.py`:
   ```bash
   python encrypt.py
   ```
2. Enter the full path of the PNG image.
3. Enter the secret message you want to hide.
4. Enter a passcode for decryption.
5. The encrypted image (`encryptedImage.png`) will be saved in the same directory.

### Decryption
1. Run `decrypt.py`:
   ```bash
   python decrypt.py
   ```
2. Enter the full path of the encrypted PNG image.
3. Enter the passcode used during encryption.
4. If the passcode matches, the hidden message will be revealed.

## File Descriptions
- `encrypt.py` - Encrypts a message into an image.
- `decrypt.py` - Decrypts the message from the encrypted image.
- `passcode.txt` - Stores the passcode used for encryption.
- `msg_length.txt` - Stores the length of the hidden message.
- `encryptedImage.png` - Output image with the hidden message.

## Notes
- Only encrypted images of PNG format should be used for decryption since using JPG causes data loss during compression.
- The image should be large enough to store the message.
- Do not modify `passcode.txt` or `msg_length.txt`, as they are needed for decryption.
- When using the command prompt to run the python files, the present working directory has to be the same directory where the python files are located.

## License
This project is open-source and available for educational and research purposes. Feel free to modify and improve it!

## Author
Nithilan Valan

