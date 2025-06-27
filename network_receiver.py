import socket

def receive_image(save_as="received_image.png"):
    port = int(input("Enter port to listen on: ").strip())

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
            server_sock.bind(('0.0.0.0', port))
            server_sock.listen(1)
            print(f"[+] Listening on port {port}...")

            conn, addr = server_sock.accept()
            print(f"[+] Connection from {addr[0]}")

            with open(save_as, 'wb') as f:
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    f.write(data)

            print(f"[+] Image saved as {save_as}")
            conn.close()

    except Exception as e:
        print(f"[!] Error: {e}")
