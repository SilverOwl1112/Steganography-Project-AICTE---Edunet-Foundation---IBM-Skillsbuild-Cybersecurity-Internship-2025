import cv2
import numpy as np
import os

path = input("Enter the image file path without quotes (ONLY IN PNG FORMAT): ")
img = cv2.imread(path)  # Replace with the correct image path
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Save passcode and message length to text files
with open("passcode.txt", "w") as f:
    f.write(password)

with open("msg_length.txt", "w") as f:
    f.write(str(len(msg)))

msg_bytes = msg.encode("utf-8")
msg_bits = ''.join(format(byte, '08b') for byte in msg_bytes) + '1111111111111110'  # End marker

h, w, _ = img.shape
bit_idx = 0

for i in range(h):
    for j in range(w):
        for k in range(3):  # Iterate over RGB channels
            if bit_idx < len(msg_bits):
                img[i, j, k] = (img[i, j, k] & 0xFE) | int(msg_bits[bit_idx])
                bit_idx += 1
            else:
                break

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # Use 'start' to open the image on Windows
print("Image Encryption Successful.")
