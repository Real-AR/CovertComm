from PIL import Image
from cryptography.fernet import Fernet

def binary_to_bytes(binary_data):
    return bytes(int(binary_data[i:i+8], 2) for i in range(0, len(binary_data), 8))

def decode_message():
    img_path = input("Enter image path to decode: ").strip()
    key_input = input("Enter the encryption key: ").strip()
    key = key_input.encode()
    fernet = Fernet(key)

    img = Image.open(img_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    pixels = img.load()
    width, height = img.size
    binary_data = ''

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    byte_data = binary_to_bytes(binary_data)
    end_index = byte_data.find(b'####')
    if end_index == -1:
        print("[!] No hidden message found.")
        return

    encrypted_msg = byte_data[:end_index]

    try:
        decrypted = fernet.decrypt(encrypted_msg).decode()
        print(f"[+] Hidden message:\n{decrypted}")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")