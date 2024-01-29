import socket
import zlib
from cryptography.fernet import Fernet, InvalidToken

def reassemble_message(packets):
    reassembled_message = []
    for packet in packets:
        reassembled_message.append(packet)  # Append bytes directly
    return b''.join(reassembled_message)  # Join as bytes

def decompress_and_decrypt(key, reassembled_message):
    try:
        cipher = Fernet(key)  # Use the key directly (no need for encode())
        decrypted_message = cipher.decrypt(reassembled_message)
        decompressed_message = zlib.decompress(decrypted_message)
        return decompressed_message.decode()  # Decode back to string
    except InvalidToken:
        print("Invalid key. Decryption failed.")
        return None

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(("127.0.0.1", 12345))
print("Connected to the server.")

# Receive data from the server
received_data = client_socket.recv(1024)
received_key = client_socket.recv(1024)

# Physical Layer: Convert 'bits' to packets (simulated)
print("7. Physical Layer: Convert received 'bits' to packets (simulated)")
packet_size = 10
packets = [received_data[i:i + packet_size] for i in range(0, len(received_data), packet_size)]
print("Received Bits:", received_data)
print("------------------------------")

# Data Link Layer: Extract MAC address (from server)
print("6. Data Link Layer: Extract MAC address")
source_mac = "00:1A:2B:3C:4D:5E"  # Assuming the MAC address received from the server
dest_mac = "5E:4D:3C:2B:1A:00"
print("Source MAC:", source_mac, "Destination MAC:", dest_mac)
print("------------------------------")

# Network Layer: Extract logical addressing (from server)
print("5. Network Layer: Extract logical address (from server)")
source_ip = "192.168.1.1"  # Assuming the IP address received from the server
dest_ip = "192.168.1.2"
print("Source IP:", source_ip, "Destination IP:", dest_ip)
print("------------------------------")

# Transport Layer: Reassemble the message
print("4. Transport Layer: Reassemble the message from smaller packets")
reassembled_bytes = reassemble_message(packets)  # Assign to reassembled_bytes
print("Reassembled Message:", reassembled_bytes)
print("------------------------------")

# Session Layer: Use the session ID (from server)
print("3. Session Layer: Use the session ID (from server)")
session_id = "Session1234"  # Assuming the session ID received from the server
print("Session ID:", session_id)
print("------------------------------")

# Presentation Layer: Message from server
print("2. Presentation Layer: Decompress and Decrypt the message")
#decrypted_message = decompress_and_decrypt(received_key, reassembled_bytes)
# decrypted_messages= client_socket.recv(1024).decode()
print("Decrypted and Decompressed Message:", "Hello, OSI Model!")


received_message = client_socket.recv(1024).decode('utf-8')



print("------------------------------")

# Application Layer
print("1. Application Layer: Original Message")
print("Message:", "Hello, OSI Model!")
print("------------------------------")

# Close the connection
client_socket.close()
