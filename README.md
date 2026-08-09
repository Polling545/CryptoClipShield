# CryptoClipShield

A lightweight open-source Python security auxiliary script designed to provide basic cryptocurrency asset protection through local process monitoring and clipboard behavior analysis.

## ⚠️ Important Notice and Limitations (Disclaimer)

Please read the following safety instructions carefully before using this tool:

* **Defense Limitations**: This tool uses basic feature-matching logic for monitoring. It can only identify processes with obvious naming characteristics (such as containing keywords like `keylog`, `stealer`, `hook`, etc.). **Do not treat it as a substitute for professional enterprise-grade firewalls or antivirus software.** If malicious programs disguise their names or run through other advanced stealth techniques, this script may fail to identify or intercept them.
* **Potential False Positive Risk**: This script has automatic process termination and file-moving functions. If any legal development debugging tools, system assistant programs, or special software running on your system have process names containing the aforementioned sensitive keywords, misjudgment may be triggered. Please ensure you understand all relevant processes running in your system before running this script.
* **For Learning and Personal Use Only**: The original intention of this project is to enhance personal defense awareness against clipboard attacks. Do not rely solely on this script for protection in production environments or critical asset devices.

## Features

* **Clipboard Guard**: Real-time monitoring of clipboard activity to accurately identify Bitcoin and Ethereum addresses, preventing clipboard tampering threats.
* **Process Audit**: Scans active background processes and issues initial warnings for programs suspected of malicious behavior.
* **Quarantine Zone Mechanism**: Automatically moves flagged suspicious files into a local `quarantine_zone`, giving you full authority to dispose of them (delete, restore, or check).

## How to Use

1. **Environment Preparation**: Ensure Python is installed on your system and environment variables are configured.
2. **Dependency Installation**:
   ```bash
   pip install psutil pyperclip
   ```
3. Run the Program:
   python shield.py

