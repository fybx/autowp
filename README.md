# AutoWP 

> WhatsApp Automated Message Sender

This script is a Python-based automation tool for sending formatted messages to a list of targets using WhatsApp. It utilizes Selenium, a popular web automation framework, to interact with WhatsApp Web and send messages on your behalf.

## Features

- **Efficient Performance**: The script is designed to send messages at an average speed of 5.6 seconds per message, taking into account the overall internet connection. This performance can be further improved to align with your specific automation workflow requirements.

- **Simple and Debuggable**: With less than 100 lines of code, this script is concise and easy to understand. Its simplicity makes it highly maintainable and allows for quick debugging if any issues arise during usage.

- **Flexible Input**: The script accepts the message content and target list as input files. This enables users to easily customize and integrate the script into their existing systems without modifying the source code.

- **Secure Authentication**: Unlike other approaches that may rely on passing CSRF tokens, which can be vulnerable to theft or accidental exposure, this script utilizes the official WhatsApp Web interface. It only requires a one-time linkage using a QR code, ensuring a secure and reliable authentication process.

- **Format as you'd like**: Format your message in `message.txt` to be bold, italic or monospace according WhatsApp's styles (\*bold\*, \_italic\_, ...)

## Prerequisites

Before using this script, please ensure that you have the following dependencies installed:

- Python 3.x
- Selenium for Python
- Chrome WebDriver (compatible with your Chrome browser version)

If you already have `pip` installed on your system, go ahead and run this command to get the dependencies:

```bash
pip install selenium webdriver-manager
```

## Usage

1. Install the necessary dependencies mentioned above.
2. Clone this repository or download the `sendwp.py` script.
3. Create two input files: `message.txt` (containing the formatted message) and `targets.txt` (containing the list of target contacts).
4. Run the script by executing the following command in your terminal:
   ```bash
   python sendwp.py
   ```
5. Follow the instructions provided by the script to authenticate your WhatsApp account using the QR code.
6. Sit back and relax as the script automatically sends the formatted message to each target in the list.

Please note that this script is intended for educational and personal use only. Ensure compliance with WhatsApp's terms of service and respect the privacy of others when using this automation tool.

Feel free to customize and enhance the script according to your specific requirements. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request. Happy automating!

## Credits

Feel free to contact me for collab on anything!

Ferit Yiğit BALABAN, <fybalaban@fybx.dev>

2023