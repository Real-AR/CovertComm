## 🕵️ CovertComm 🕵️

CovertComm is a Python-based, CLI tool that uses Steganography to hide encrypted messages in lossless format (PNG) images and then transmits the images to the receiver via a network-based transfer - by using an encryption key that is delivered using a separate secure channel.


## 📌 FEATURES 📌

- 🔐 AES-level symmetric encryption with Fernet
- 🖼️ LSB-based image steganography
- 📡 Network-based transmission of stego-images
- 🧾 Secure key sharing over a separate TCP channel
- 🔧 CLI interface with intuitive commands

## 🛠️ Installation

### Requirements

- Python 3.7+
- pip packages: `Pillow`, `cryptography`, `pyfiglet`

### Install Dependencies

```bash
pip install -r requirements.txt
```
## 🚀 Usage 🚀
After making `main.py` executable(or renaming it to `covertcomm`):-

```bash
chmod +x main.py
mv main.py covertcomm
```
You can use it like a CLI tool as follows:

```bash
python3 covertcomm <command>
```

## 🔧 Available Commands 🔧

| Command       | Description                               |
| ------------- | ----------------------------------------- |
| `encode`      | Encrypt a message and hide it in an image |
| `decode`      | Extract and decrypt a hidden message      |
| `send`        | Send a stego image over the network       |
| `receive`     | Receive a stego image over the network    |
| `send-key`    | Send the encryption key to a receiver     |
| `receive-key` | Receive the encryption key from a sender  |


## 📥 Example Workflow 📥
Sender Side
```bash
python3 covertcomm encode
python3 covertcomm send-key
python3 covertcomm send
```
Receiver Side
```bash
python3 covertcomm receive-key
python3 covertcomm receive
python3 covertcomm decode
```
## 🧠 Technical Overview 🧠
- Steganography: Least Significant Bit (LSB) encoding in RGB image pixels.

- Encryption: Symmetric encryption using cryptography.Fernet.

- Key Channel: Separate TCP socket for secure key delivery.

- Transport: Standard Python socket module for image transmission.

## 🧪 Testing 🧪
To run locally between two terminals on the same machine:

- Use 127.0.0.1 as the IP.

- Use different ports for key and image transfer.

## 📁 Project Structure 📁
```graphql
CovertComm/
├── main.py               # Main CLI wrapper
├── encoder.py            # Steganography + encryption
├── decoder.py            # Decryption + extraction
├── network_sender.py     # Sends stego image
├── network_receiver.py   # Receives stego image
├── key_sender.py         # Sends encryption key
├── key_receiver.py       # Receives encryption key
└── README.md             # You're reading it!
```

## 🔐 Security Considerations 🔐
- The encryption key is never embedded in the image — it's transferred separately.

- Ensure the key is not intercepted — use TLS or secure networks for best results.

- For academic or demo use ONLY. Production-grade systems should use authenticated encryption and more robust secure channels.

## 🧑‍💻 Authors 🧑‍💻
Anupam Rajiv Lakra (A023166923085)
Akshay Kumar (A023166923082)
