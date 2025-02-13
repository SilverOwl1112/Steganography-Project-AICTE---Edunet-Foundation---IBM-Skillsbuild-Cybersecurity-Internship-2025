import cv2

path = input("Enter the encrypted image file path without quotes (ONLY IN PNG FORMAT): ")
img = cv2.imread(path)  # Replace with the correct image path
if img is None:
    print("Error: Encrypted image not found.")
    exit()

# Load the stored passcode
try:
    with open("passcode.txt", "r") as f:
        saved_password = f.read().strip()
except FileNotFoundError:
    print("Passcode file not found. Decryption aborted.")
    exit()

pas = input("Enter passcode for Decryption: ")
if pas == saved_password:
    h, w, _ = img.shape
    msg_bits = ""
    found_marker = False

    for i in range(h):
        for j in range(w):
            for k in range(3):  # Iterate over RGB channels
                msg_bits += str(img[i, j, k] & 1)
                if msg_bits.endswith("1111111111111110"):  # End marker
                    found_marker = True
                    msg_bits = msg_bits[:-16]
                    break
            if found_marker:
                break
        if found_marker:
            break

    msg_bytes = [msg_bits[i:i+8] for i in range(0, len(msg_bits), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in msg_bytes])
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
