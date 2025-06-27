import socket
import os

def send_image():
    host = input("Enter receiver IP address: ").strip()
    port = int(input("Enter port to send on: ").strip())
    image_path = input("Enter path to stego image: ").strip()

    if not os.path.exists(image_path):
        print("[!] Image file not found.")
        return

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print(f"[+] Connected to {host}:{port}")
            with open(image_path, 'rb') as img:
                data = img.read()
                sock.sendall(data)
            print("[+] Image sent successfully.")
    except Exception as e:
        print(f"[!] Error: {e}")
