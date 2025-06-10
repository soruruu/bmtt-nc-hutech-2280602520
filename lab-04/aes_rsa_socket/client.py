from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import socket
import threading
import hashlib

#Initialize
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect (('localhost', 12345))

#Generate
client_key = RSA.generate(2048)

#Recaive
server_public_key = RSA.import_key(client_socket.recv(2048))

#Send
client_socket.send (client_key.publickey().export_key(format='PEM'))

#Receive
encrypted_aes_key = client_socket.recv(2048)

#Decrypt
ciphet_rsa = PKCS1_OAEP.new (client_key)
aes_key = ciphet_rsa.decrypt(encrypted_aes_key)

#Function encrypt
def encrypt_message (key, message):
    cipher = AES.new (key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

#Function decrypt    
def decrypt_messsage (key, encrypted_message):
    iv = encrypted_message [:AES.block_size]
    ciphertext = encrypted_message [AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_messsage = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_messsage.decode()

#Function receive
def receive_message ():
    while True:
        encrypted_message = client_socket.recv (1024)
        decrypted_messsage = decrypt_messsage(aes_key, encrypted_message)
        print("Received:", decrypted_messsage)

# Start
receive_thread = threading.Thread(target= receive_message)
receive_thread.start()

#Send
while True:
    message = input ("Enter messgae ('exit' to quit): ")
    encrypted_message = encrypt_message (aes_key, message)
    client_socket.send(encrypted_message)
    if message == "exit":
        break

# Close
client_socket.close()
    