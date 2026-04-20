# 📱 QR Payment Fixer

## A simple Python project that:

Decodes an existing QR code
Extracts the payment link (UPI-based)
Generates a corrected / custom QR code

### 🚀 How It Works
Step 1: Decode QR Code
Uses OpenCV to scan an image
Extracts the embedded data (usually a UPI payment link)
Step 2: Generate New QR Code
Constructs a new UPI payment URL
Allows customization (like amount, currency, etc.)
Generates a fresh QR using the qrcode library

### ⚠️ Notes
Ensure the input QR image is clear and readable
Incorrect formatting of UPI URL may result in invalid QR
This project is for learning/testing purposes

### 👨‍💻 Author

Atharva Shinde

# ⭐ If you found this useful, consider giving it a star!
