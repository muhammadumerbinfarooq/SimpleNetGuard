# Simple Firewall

This is a basic firewall implemented in Python using the `scapy` library. The firewall captures network packets and filters them based on predefined rules, such as allowed IP addresses and blocked ports.

## Description

The Simple Firewall is an interactive Python script that monitors network traffic and applies filtering rules to block or allow packets. It's a great way to learn about network security and Python programming.

## Features

- Captures network packets using `scapy`.
- Filters packets based on allowed IP addresses and blocked ports.
- Logs blocked packets for review.
- Simple and easy-to-understand code.
- Great for beginners to practice Python and network security basics.

## Requirements

- Python 3.x
- `scapy` library

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/muhammadumerbinfarooq/SimpleNetGuard.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd simple-firewall
    ```

3. **Install the `scapy` library:**
    ```bash
    pip install scapy
    ```

## Implementation

The Simple Firewall is implemented in a single Python script (`simple_firewall.py`). Here's a brief overview of the main functions:

- `packet_callback(packet)`: Processes each packet and applies filtering rules.
- `sniff(prn=packet_callback, store=0)`: Starts sniffing packets and calls `packet_callback` for each packet.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please feel free to submit an issue or a pull request. Here are some ways you can contribute:

- Report bugs and issues.
- Suggest new features or enhancements.
- Improve documentation.
- Submit pull requests with improvements or fixes.

## Acknowledgments

- Inspired by various network security tools and tutorials.
- Thanks to the Python and `scapy` communities for their support and resources.
- Special thanks to everyone who has contributed to this project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Example

```plaintext
Blocked packet from 192.168.1.3
Blocked packet to port 80
