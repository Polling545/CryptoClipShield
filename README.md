# CryptoClipShield

A lightweight Python tool designed to protect your cryptocurrency assets by monitoring the system clipboard for potential hijackers, scanning for suspicious background processes, and safely isolating potential threats.

## Features

- **Clipboard Guard**: Monitors clipboard activity to detect exposed cryptocurrency addresses (Bitcoin, Ethereum).
- **Process Scanner**: Inspects active background processes for suspicious indicators or potential stealer scripts.
- **Interactive Quarantine Zone**: Automatically isolates flagged suspicious files into a secure local directory (`quarantine_zone`), giving you full control to inspect, restore, or permanently delete them.
- **Lightweight & Open-Source**: Zero cost, easy to run, and built for crypto security enthusiasts.

## Requirements

Make sure you have Python installed on your system.

## Installation

Clone the repository and install the required dependencies:

```bash
pip install psutil pyperclip
