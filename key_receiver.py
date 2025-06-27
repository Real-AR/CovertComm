import socket

def receive_key(port=9998):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.bind(('0.0.0.0', port))
            sock.listen(1)
            print(f"[+] Waiting to receive encryption key on port {port}...")
            conn, addr = sock.accept()
            with conn:
                print(f"[+] Connection established from {addr}")
                key = conn.recv(1024)
                print(f"[+] Encryption key received:\n{key.decode()}")
                return key
    except Exception as e:
        print(f"[!] Failed to receive key: {e}")
        return None
