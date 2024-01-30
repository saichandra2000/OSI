import socket
import zlib
import time


def receive_packets(server_socket):
    packets = []
    while True:
        packet = server_socket.recv(1024)
        if not packet:
            break
        packets.append(packet)
    return b''.join(packets)


def decrypt_and_decompress(data):
    # Simple decryption and decompression (for demonstration purposes)
    decompressed_data = zlib.decompress(data)
    decrypted_data = ''.join([chr(byte - 1) for byte in decompressed_data])
    return decrypted_data

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8081))
  
    # Physical Layer
    transmitted_bits = receive_packets(client_socket)
    print("Client is Connected Successfully!")
    print("1. Physical Layer: Convert to 'bits' for transmission (simulated)")
    print("Transmitting Bits:", ' '.join(format(byte, '08b') for byte in transmitted_bits))
    print("------------------------------")

    # Data Link Layer
    print("2. Data Link Layer: Add MAC address and parity bit")
    print("------------------------------")

    # Network Layer (simulated)
    network_details = receive_packets(client_socket).decode()
    print("3. Network Layer: Received network details from server\n", network_details)
    print("4. Transport Layer:", transmitted_bits)
    print("5. Session Layer: Establish a session (simulated)")

    # Presentation Layer
    decrypted_message = decrypt_and_decompress(transmitted_bits)
    print("6. Presentation Layer: Decrypt and Decompress Message\nDecrypted Message:", decrypted_message)
    print("------------------------------")

    # Application Layer
    print("7. Application Layer: Orginal Message", decrypted_message)
    print("\nSuccessfully message received")

    client_socket.close()

if __name__ == "__main__":
    client()
