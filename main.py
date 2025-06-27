import argparse
from encoder import encode_message
from decoder import decode_message
from network_sender import send_image
from network_receiver import receive_image
from key_sender import send_key
from key_receiver import receive_key

def main():
    print('''
                                                                             
 ,-----.                               ,--.   ,-----.                            
'  .--./ ,---.,--.  ,--.,---. ,--.--.,-'  '-.'  .--./ ,---. ,--,--,--.,--,--,--. 
|  |    | .-. |\  `'  /| .-. :|  .--''-.  .-'|  |    | .-. ||        ||        | 
'  '--'\' '-' ' \    / \   --.|  |     |  |  '  '--'\' '-' '|  |  |  ||  |  |  | 
 `-----' `---'   `--'   `----'`--'     `--'   `-----' `---' `--`--`--'`--`--`--' 
                                                                                 

    ''')

    parser = argparse.ArgumentParser(
        description="StegoComm - A Covert Communication Tool",
        usage='''main.py <command> [<args>]

Available commands:
   encode         Embed a secret message into an image
   decode         Extract a hidden message from an image
   send           Send a stego image over the network
   receive        Receive a stego image from a remote host
   send-key       Send the encryption key securely to receiver
   receive-key    Receive the encryption key from sender''')

    parser.add_argument('command', help='Subcommand to run')
    args = parser.parse_args()

    if args.command == 'encode':
        encode_message()
    elif args.command == 'decode':
        decode_message()
    elif args.command == 'send':
        send_image()
    elif args.command == 'receive':
        receive_image()
    elif args.command == 'send-key':
        key = input("Paste the encryption key to send: ").strip().encode()
        send_key(key)
    elif args.command == 'receive-key':
        port = input("Enter port to listen on (default 9998): ").strip()
        port = int(port) if port else 9998
        received_key = receive_key(port)
        if received_key:
            with open("received_key.txt", "wb") as f:
                f.write(received_key)
            print("[+] Key saved to 'received_key.txt'")
    else:
        print(f"[!] Unknown command: {args.command}")
        parser.print_help()

if __name__ == '__main__':
    main()