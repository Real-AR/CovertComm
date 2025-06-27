import socket

def send_key(key):
    host = input("Enter receiver IP for key transfer: ").strip()
    port = int(input("Enter port to send key on: ").strip())

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall(key)
            print("[+] Encryption key sent securely to receiver.")
    except Exception as e:
        print(f"[!] Failed to send key: {e}")