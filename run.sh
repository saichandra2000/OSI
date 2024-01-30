#!/bin/bash

# Prompt user for message
read -p "Enter the message (default: 'Hello World'): " message
message=${message:-"Hello World"}

# Confirm message with user
read -p "Would you like to proceed with this message: '$message' [Y/n]? " confirm
confirm=${confirm:-"Y"}

# Check if the user wants to proceed
if [[ $confirm =~ ^[Yy]$ ]]; then
    # Default values for IP address and MAC address
    ip_address="192.168.0.1"
    mac_address="0E:23:AA:EF:EA"

    # Run Server.py with default values
    python3 Server3.py "$message" "$ip_address" "$mac_address" &

    


    # Run Client.py with default values
    python3 Client3.py "$ip_address" "$mac_address"

    # Exit script
    echo "Script execution complete."
else
    echo "Operation aborted by user."
fi

