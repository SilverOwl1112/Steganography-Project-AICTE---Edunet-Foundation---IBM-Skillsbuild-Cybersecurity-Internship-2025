import cv2
import os

path = input("Enter the image file path without quotes: ")
img = cv2.imread(path)  
if img is None:
    print("Error: Image not found or unable to load.")
    exit()

msg = input("Enter secret message:")
password = input("Enter a passcode:")

# Saves passcode and message length to text files
with open("passcode.txt", "w") as f:
    f.write(password)

with open("msg_length.txt", "w") as f:
    f.write(str(len(msg)))

msg_bytes = msg.encode("utf-8")
msg_bits = ''.join(format(byte, '08b') for byte in msg_bytes) + '1111111111111110'  # End marker

h, w, _ = img.shape
max_bits = h * w * 3  # Maximum bits available in the image

if len(msg_bits) > max_bits:
    print("Error: Image is too small to store the secret message.")
    exit()

bit_idx = 0
for i in range(h):
    for j in range(w):
        for k in range(3):  # Iterates over RGB channels
            if bit_idx < len(msg_bits):
                img[i, j, k] = (img[i, j, k] & 0xFE) | int(msg_bits[bit_idx])
                bit_idx += 1
            else:
                break

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")  # This is for Windows; on macOS use 'open' and on Linux use 'xdg-open'
print("Image Encryption Successful.")
