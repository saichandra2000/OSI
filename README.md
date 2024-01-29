# OSI

pip install socket
pip install zlib
pip install cryptography

Note:
Run Server3.py first and then run CLient3.py

Client3.py Expected Output
Connected to the server.
7. Physical Layer: Convert received 'bits' to packets (simulated)
Received Bits: b'11110001001110001001011011101110000010000000001101001111001110000010010100000110000100010001011110111001101000011001100100100001010000001001110010011101100111000000111101001111100000110111000100101000110011001001110100011100100011110011110001001001110111111111110000111001001011000000010000101000111111110100010100101111011111001010010000000100101110010011111001000001110011011101111001010101111000011001101001111100100111000101111010001001010001101111010001111001010110000001010010001100010101000111101110011100110111011000110011110100010101001111001110001010011000001000101101010010100111111111110010100000000011000000001111011101101000110111111100010010100000101001001011001011001000001001000000111111100011101101001100110011110000001100000001111111010011111001000010101011011111111100000111010010010111101100001000110011011100010111001001011101100000100111111100101011001010110011001000000011111111110011100010000010000110101001100000011010110110000000000111100000110110010011110010011GeaNoqSjxkYkduy0g8DXvK_7L6l-9NqYRXx'
------------------------------
6. Data Link Layer: Extract MAC address
Source MAC: 00:1A:2B:3C:4D:5E Destination MAC: 5E:4D:3C:2B:1A:00
------------------------------
5. Network Layer: Extract logical address (from server)
Source IP: 192.168.1.1 Destination IP: 192.168.1.2
------------------------------
4. Transport Layer: Reassemble the message from smaller packets
Reassembled Message: b'11110001001110001001011011101110000010000000001101001111001110000010010100000110000100010001011110111001101000011001100100100001010000001001110010011101100111000000111101001111100000110111000100101000110011001001110100011100100011110011110001001001110111111111110000111001001011000000010000101000111111110100010100101111011111001010010000000100101110010011111001000001110011011101111001010101111000011001101001111100100111000101111010001001010001101111010001111001010110000001010010001100010101000111101110011100110111011000110011110100010101001111001110001010011000001000101101010010100111111111110010100000000011000000001111011101101000110111111100010010100000101001001011001011001000001001000000111111100011101101001100110011110000001100000001111111010011111001000010101011011111111100000111010010010111101100001000110011011100010111001001011101100000100111111100101011001010110011001000000011111111110011100010000010000110101001100000011010110110000000000111100000110110010011110010011GeaNoqSjxkYkduy0g8DXvK_7L6l-9NqYRXx'
------------------------------
3. Session Layer: Use the session ID (from server)
Session ID: Session1234
------------------------------
2. Presentation Layer: Decompress and Decrypt the message
Decrypted and Decompressed Message: Hello, OSI Model!
------------------------------
1. Application Layer: Original Message
Message: Hello, OSI Model!
------------------------------

Process finished with exit code 0


Server3 Expected Output

Waiting for a connection...
Connection from ('127.0.0.1', 53527)
1. Application Layer: Original Message
Message: Hello, OSI Model!
------------------------------
2. Presentation Layer: Encrypt and Compress Message
Encrypted Message: b"x\x9cKw\x04\x01\xa7\x9c\x12\x83\x08\x8b\xdc\xd0\xcc\x90P''g\x03\xd3\xe0\xdcJ3'G#\xcf\x12w?\xc3\x92\xc0B\x8f\xf4R\xf7\xca@K\x93\xe4\x1c\xddr\xaf\x0c\xd3\xe4\xe2\xf4J7\xa3\xca\xc0\xa4b\xa3\xdc\x1c\xdd\x8c\xf4T\xf3\x8a`\x8bR\x9f\xfc\xa0\x0c\x03\xdd(\xdf\xc4\xa0\xa4\xb2\xc8$\x0f\xe3\xb4\xcc\xf00\x1f\xd3\xe4*\xdf\xf0t\x97\xb0\x8c\xdc\\\x97`\x9f\xca\xca\xcc@\x7f\xe7\x10CS\x03[\x00<\x1b'\x93"
Encryption Key: b'GeaNoqSjxkYkduy0g8DXvK_7L6l-9NqYRXxr0O7DCPo='
------------------------------
3. Session Layer: Establish a session (simulated)
Session ID: Session1234
------------------------------
4. Transport Layer: Break into smaller packets with sequence numbers
Packet 1: b'x\x9cKw\x04\x01\xa7\x9c\x12\x83\x08\x8b\xdc\xd0\xcc\x90'
Packet 2: b"P''g\x03\xd3\xe0\xdcJ3'G#\xcf\x12w"
Packet 3: b'?\xc3\x92\xc0B\x8f\xf4R\xf7\xca@K\x93\xe4\x1c\xdd'
Packet 4: b'r\xaf\x0c\xd3\xe4\xe2\xf4J7\xa3\xca\xc0\xa4b\xa3\xdc'
Packet 5: b'\x1c\xdd\x8c\xf4T\xf3\x8a`\x8bR\x9f\xfc\xa0\x0c\x03\xdd'
Packet 6: b'(\xdf\xc4\xa0\xa4\xb2\xc8$\x0f\xe3\xb4\xcc\xf00\x1f\xd3'
Packet 7: b'\xe4*\xdf\xf0t\x97\xb0\x8c\xdc\\\x97`\x9f\xca\xca\xcc'
Packet 8: b"@\x7f\xe7\x10CS\x03[\x00<\x1b'\x93"
------------------------------
5. Network Layer: Add logical address (simulated)
Source IP: 192.168.1.1 Destination IP: 192.168.1.2
------------------------------
6. Data Link Layer: Add MAC address and parity bit
Source MAC: 00:1A:2B:3C:4D:5E Destination MAC: 5E:4D:3C:2B:1A:00
Parity Bit: 1
------------------------------
7. Physical Layer: Convert to 'bits' for transmission (simulated)
Transmitting Bits: 11110001001110001001011011101110000010000000001101001111001110000010010100000110000100010001011110111001101000011001100100100001010000001001110010011101100111000000111101001111100000110111000100101000110011001001110100011100100011110011110001001001110111111111110000111001001011000000010000101000111111110100010100101111011111001010010000000100101110010011111001000001110011011101111001010101111000011001101001111100100111000101111010001001010001101111010001111001010110000001010010001100010101000111101110011100110111011000110011110100010101001111001110001010011000001000101101010010100111111111110010100000000011000000001111011101101000110111111100010010100000101001001011001011001000001001000000111111100011101101001100110011110000001100000001111111010011111001000010101011011111111100000111010010010111101100001000110011011100010111001001011101100000100111111100101011001010110011001000000011111111110011100010000010000110101001100000011010110110000000000111100000110110010011110010011
------------------------------

