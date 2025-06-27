from PIL import Image
from cryptography.fernet import Fernet

def message_to_binary(message):
    return ''.join(format(byte, '08b') for byte in message)

def encode_message():
    img_path = input("Enter image path to encode: ").strip()
    output_path = input("Enter output image name: ").strip()
    secret = input("Enter the message to hide: ").strip()
    key = Fernet.generate_key()

    print(f"[+] Encryption key (save this for decoding):\n{key.decode()}")
    fernet = Fernet(key)
    encrypted_msg = fernet.encrypt(secret.encode()) + b'####'
    binary_data = message_to_binary(encrypted_msg)

    img = Image.open(img_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()
    width, height = img.size

    data_index = 0
    for y in range(height):
      for x in range(width):
        if data_index >= len(binary_data):
            break

        r, g, b = pixels[x, y]

        if data_index < len(binary_data):
            r = (r & ~1) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            g = (g & ~1) | int(binary_data[data_index])
            data_index += 1
        if data_index < len(binary_data):
            b = (b & ~1) | int(binary_data[data_index])
            data_index += 1

        pixels[x, y] = (r, g, b)

      if data_index >= len(binary_data):
        break


    img.save(output_path)
    print(f"[+] Message encoded and saved to {output_path}")