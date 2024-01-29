import socket
import zlib
from cryptography.fernet import Fernet

def encrypt_and_compress(message):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    compressed_message = zlib.compress(encrypted_message)
    return key, compressed_message

def simulate_osi_layers(message):
    # Application Layer
    print("1. Application Layer: Original Message")
    print("Message:", message)
    print("------------------------------")

    # Presentation Layer
    key, compressed_message = encrypt_and_compress(message)
    print("2. Presentation Layer: Encrypt and Compress Message")
    print("Encrypted Message:", compressed_message)
    print("Encryption Key:", key)

    print("------------------------------")

    # Session Layer: Establishing a session (simulated)
    print("3. Session Layer: Establish a session (simulated)")
    session_id = "Session1234"
    print("Session ID:", session_id)
    print("------------------------------")

    # Transport Layer: Break the message into smaller packets and add sequence numbers
    print("4. Transport Layer: Break into smaller packets with sequence numbers")
    packets = [compressed_message[i:i + 16] for i in range(0, len(compressed_message), 16)]
    for i, packet in enumerate(packets):
        print(f"Packet {i + 1}: {packet}")
    print("------------------------------")

    # Network Layer: Add logical addressing (simulated)
    print("5. Network Layer: Add logical address (simulated)")
    source_ip = "192.168.1.1"
    dest_ip = "192.168.1.2"
    print("Source IP:", source_ip, "Destination IP:", dest_ip)
    print("------------------------------")

    # Data Link Layer: Add physical address (MAC) and parity bit (error detection)
    print("6. Data Link Layer: Add MAC address and parity bit")
    source_mac = "00:1A:2B:3C:4D:5E"
    dest_mac = "5E:4D:3C:2B:1A:00"
    print("Source MAC:", source_mac, "Destination MAC:", dest_mac)
    parity_bit = '1' if compressed_message.count(b'1') % 2 == 0 else '0'
    print("Parity Bit:", parity_bit)
    print("------------------------------")

    # Physical Layer: Convert packets to 'bits' (simulated)
    print("7. Physical Layer: Convert to 'bits' for transmission (simulated)")
    physical_layer_data = ''.join(format(int.from_bytes(packet, byteorder='big'), '016b') for packet in packets)
    print("Transmitting Bits:", physical_layer_data)
    print("------------------------------")

    return physical_layer_data, key

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 12345))
server_socket.listen()

print("Waiting for a connection...")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")

# Simulate OSI layers and send data to the client
message = "Hello, OSI Model!"
transmit_data, encryption_key = simulate_osi_layers(message)
#client_socket.send(message.encode())
# Send encrypted data and key to the client
client_socket.sendall(transmit_data.encode())
client_socket.sendall(encryption_key)

# Close the connection
client_socket.close()
server_socket.close()