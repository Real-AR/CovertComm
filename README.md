## 🕵️ CovertComm 🕵️

CovertComm is a Python-based, CLI tool that uses Steganography to hide encrypted messages in lossless format (PNG) images and then transmits the images to the receiver via a network-based transfer - by using an encryption key that is delivered using a separate secure channel.


## 📌 FEATURES 📌

- 🔐 AES-128 encrypted message handling using Fernet
- 🖼️ LSB-based steganography in images (currently only functional in RGB .png files)
- 📡 Secure TCP-based transmission via Python sockets
- 🌐 Seamless internet exposure using `ngrok` TCP tunnels
- 🧾 Separate key transmission module for confidentiality
- 🧑‍💻 Easy-to-use CLI interface

## 🛠️ Installation

### Requirements

- Python 3.7+
- pip packages: `Pillow`, `cryptography`, `pyfiglet`
- Ngrok or a similar TCP tunneling application
### Install Dependencies

```bash
pip install -r requirements.txt
```
Additionally, download and authenticate Ngrok from https://ngrok.com/download

## 🚀 Usage

After cloning the repository and installing the dependencies from `requirements.txt`, you can run the tool from the terminal using:

```bash
python3 main.py
```

You'll be greeted with the ASCII banner and a list of available options.

---

### 🔐 Encode a Message

To embed an encrypted message inside an image:

```bash
python3 main.py encode
```

You will be prompted to:

* Enter the message to hide
* Provide the path to a PNG image (cover image)
* Choose a destination for the stego-image (output)
* Automatically generate and store the encryption key

The result will be a `.png` file that visually looks the same but contains the hidden, encrypted message.

---

### 🧩 Decode a Message

To extract and decrypt a message from a stego-image:

```bash
python3 main.py decode
```

You will be prompted to:

* Provide the path to the stego-image
* Enter the corresponding Fernet key
* The original plaintext message will be displayed if the key is valid.

---

### 📤 Send Image to Receiver

To send the stego-image to another device:

```bash
python3 main.py send-image
```

You will be prompted to:

* Enter the ngrok forwarding address of the receiver
* Select the stego-image file to send

Make sure the receiver is running the `receive-image` command and listening on the correct endpoint.

---

### 📥 Receive Image from Sender

To receive an image:

```bash
python3 main.py receive-image
```

This opens a TCP socket listener (ngrok tunnel recommended). The received image is saved to disk.

---

### 🔑 Send/Receive Encryption Key

Use the following to share the encryption key securely over a **separate ngrok tunnel**:

```bash
python3 main.py send-key
```

```bash
python3 main.py receive-key
```

Ensure both sender and receiver are running their respective modules concurrently.



## 📥 Example Workflow 📥
- Sender Side
```bash
python3 main.py encode
python3 main.py send-key
python3 main.py send
```
Use the Ngrok TCP Address (4.tcp.ngrok.io) and the corresponding port wherever prompted.

Remember to always specify the filetype for the images (.PNG), or else you will have errors when encoding messages into them.
- Receiver Side
```bash
python3 main.py receive-key
ngrok tcp <port number> (in a different terminal)
python3 main.py receive
python3 main.py decode
```
The port used to make the ngrok tunnel must match the port used for receiving the files, or else you will have errors.

🧠 Example Use Case
| Role     | Action            | Command                    |
| -------- | ----------------- | -------------------------- |
| Receiver | Receive key       | `main.py receive-key` |
| Receiver | Expose key port   | `ngrok tcp 9998`      |
| Receiver | Receive image     | `main.py receive`     |
| Receiver | Expose image port | `ngrok tcp 9999`      |
| Sender   | Encode message    | `main.py encode`      |
| Sender   | Send image        | `main.py send`        |
| Sender   | Send key          | `main.py send-key`    |
| Receiver | Decode message    | `main.py decode`      |


## 🧠 Technical Overview 🧠
- Steganography: Least Significant Bit (LSB) encoding in RGB image pixels.

- Encryption: Symmetric encryption using cryptography.Fernet.

- Key Channel: Separate TCP socket for secure key delivery, done using Ngrok via TCP Tunneling.

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

- For academic or demo use ONLY. Production-grade systems should use authenticated encryption and more robust secure channels.

## 🧑‍💻 Authors 🧑‍💻
Anupam Rajiv Lakra (rea1ar)
