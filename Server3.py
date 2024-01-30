import socket
import time
import zlib
import sys

def encrypt_and_compress(message):
    encrypted_message = ''.join([chr(ord(char) + 1) for char in message])
    compressed_message = zlib.compress(encrypted_message.encode())
    return compressed_message

def segment_data(data):
    packet_size = 15
    segments = [data[i:i + packet_size] for i in range(0, len(data), packet_size)]
    return segments

def send_packet(client_socket, packet, delay=2):
    time.sleep(delay)
    client_socket.send(packet)

def server(original_message, destination_ip, destination_mac):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 8081))
        server_socket.listen(1)

        print("Waiting for a connection...")
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Use provided input
        original_message = original_message
        destination_ip = destination_ip
        destination_mac = destination_mac

        # Application Layer
        print("1. Application Layer: Original Message\nMessage:", original_message)
        print("------------------------------")

        # Presentation Layer
        encrypted_message = encrypt_and_compress(original_message)
        print("2. Presentation Layer: Encrypt and Compress Message\nEncrypted Message:", encrypted_message)
        print("------------------------------")

        # Session Layer (simulated)
        print("3. Session Layer: Establish a session (simulated)")
        print("------------------------------")

        # Transport Layer
        segments = segment_data(encrypted_message)
        sequence_number = 1
        for segment in segments:
            print(f"4. Transport Layer: Packet {sequence_number}: {segment}")
            send_packet(client_socket, segment)
            sequence_number += 1

        # Network Layer (user input)
        source_ip = "127.0.0.1"
        print(f"5. Network Layer: Add logical address (simulated)\nSource IP: {source_ip} Destination IP: {destination_ip}")
        print("------------------------------")

        # Data Link Layer (user input)
        source_mac = "00:1A:2B:3C:4D:5E"
        print(f"6. Data Link Layer: Add MAC address and parity bit\nSource MAC: {source_mac} Destination MAC: {destination_mac}")
        print("------------------------------")

        # Physical Layer (simulated)
        print("7. Physical Layer: Convert to 'bits' for transmission (simulated)")
        print("Transmitting Bits:", ' '.join(format(byte, '08b') for byte in encrypted_message))
        print("------------------------------")

        print("Sending to the CLient _________________")

        client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        print("Check the port number and change it in the code manually")
        print("----------------------------------------------------------------")


if __name__ == "__main__":
    # Use command-line arguments
    if len(sys.argv) == 4:
        message_arg, ip_arg, mac_arg = sys.argv[1:4]
        server(message_arg, ip_arg, mac_arg)
    else:
        print("Usage: python3 Server.py <message> <destination_ip> <destination_mac>")
