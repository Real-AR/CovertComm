from PIL import Image
import argparse

def message_to_binary(message):
    """Convert string message to a binary string."""
    return ''.join(format(ord(char), '08b') for char in message)

def encode_image(input_image_path, output_image_path, secret_message):
    """Embed a secret message into the image using LSB steganography."""
    
    secret_message += "####"
    binary_message = message_to_binary(secret_message)
    msg_index = 0
    msg_length = len(binary_message)

    #Load image
    img = Image.open(input_image_path)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    pixels = img.load()

    width, height = img.size

    for y in range(height):
        for x in range(width):
            if msg_index >= msg_length:
                break
            
            r, g, b = pixels[x, y]

            #Modifying the LSB of each color channel
            r = (r & ~1) | int(binary_message[msg_index]) if msg_index < msg_length else r
            msg_index += 1
            g = (g & ~1) | int(binary_message[msg_index]) if msg_index < msg_length else g
            msg_index += 1
            b = (b & ~1) | int(binary_message[msg_index]) if msg_index < msg_length else b
            msg_index += 1

            pixels[x, y] = (r, g, b)

        if msg_index >= msg_length:
            break

    img.save(output_image_path)
    print(f"[+] Image saved to {output_image_path}")

    print(f"[+] Message encoded and saved as '{output_image_path}'")

#CLI
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LSB Image Steganography Encoder")
    parser.add_argument("input", help="Path to the input image (PNG recommended)")
    parser.add_argument("output", help="Path to save the output stego-image")
    parser.add_argument("message", help="Secret message to hide in the image")

    args = parser.parse_args()

    encode_image(args.input, args.output, args.message)

