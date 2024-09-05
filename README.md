# QR Code Generator

This Python script, `qrcode_generator.py`, generates a QR code based on the input data provided. In this example, the QR code contains personal information like a name, phone number, and email address. The QR code is saved as an image file.

## Key Features:
- Creates a QR code using the `qrcode` library.
- Customizable QR code version, box size, and border.
- Allows customization of the QR code's fill and background colors.
- Saves the generated QR code image in `.png` format.

## Technologies Used:
- Python
- `qrcode` library for generating QR codes.
- `Pillow` library for image manipulation (handled internally by `qrcode`).

## Usage Instructions:
1. Install Python 3.x on your system.
2. Install the `qrcode` library:
   ```bash
   pip install qrcode[pil]
