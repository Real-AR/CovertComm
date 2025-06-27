from PIL import Image
import argparse

def binary_to_message(binary_data):
    # Trim excess bits that don't form a full byte
    if len(binary_data) % 8 != 0:
        binary_data = binary_data[:-(len(binary_data) % 8)]
    
    chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        chars.append(chr(int(byte, 2)))
    return ''.join(chars)

def decode_image(image_path):
    print(f"[DEBUG] Opening image: {image_path}")
    img = Image.open(image_path)
    
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    binary_data = ''
    pixels = img.load()
    width, height = img.size
    print(f"[DEBUG] Image size: {width} x {height}")

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)
            binary_data += str(g & 1)
            binary_data += str(b & 1)

    print(f"[DEBUG] Total bits collected: {len(binary_data)}")
    decoded_message = binary_to_message(binary_data)

    delimiter = '####'
    if delimiter in decoded_message:
        decoded_message = decoded_message.split(delimiter)[0]
        print(f"[+] Hidden message extracted:\n{decoded_message}")
    else:
        print("[!] Delimiter not found. Full message:")
        print(decoded_message[:100] + '...')  # Print preview if very long

    return decoded_message


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Decode hidden message from stego image")
    parser.add_argument("image", help="Path to the stego image file")

    args = parser.parse_args()
    decode_image(args.image)
