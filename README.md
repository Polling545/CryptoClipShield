# CryptoClipShield
A lightweight Python tool to detect clipboard hijackers and suspicious processes for crypto safety.

# CryptoClipShield

A lightweight Python tool designed to protect your cryptocurrency assets by monitoring the system clipboard for potential hijackers and scanning for suspicious background processes.

## Features
- **Clipboard Guard**: Monitors clipboard activity to detect exposed cryptocurrency addresses (Bitcoin, Ethereum).
- **Process Scanner**: Inspects active background processes for suspicious indicators or potential stealer scripts.
- **Lightweight & Open-Source**: Zero cost, easy to run, and built for crypto security enthusiasts.

## Requirements
Make sure you have Python installed on your system.

## Installation
Clone the repository and install the required dependencies:
```bash
pip install psutil pyperclip
```
## Usage
Run the script locally to start monitoring:
```bash
python shield.py
