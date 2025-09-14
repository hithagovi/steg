# 🖼️ Steganography Tool

## 📌 Overview
This is a simple **Steganography Tool** built with Python.  
It allows users to hide (encode) secret text inside an image and later extract (decode) it back using a graphical user interface (GUI).

## ✨ Features
- Encode (hide) text inside PNG or BMP images using LSB (Least Significant Bit) technique.
- Decode hidden text from stego-images.
- Simple GUI built with Tkinter for ease of use.
- Error handling for missing files or empty messages.

## 🛠️ Tools & Libraries
- **Python 3**
- **Tkinter** – GUI framework
- **Stegano** – for steganography (lsb module)
- **Pillow** – image handling

## 🚀 How It Works
1. **Encoding**: User selects an image, enters secret text, and saves the stego-image with hidden data.
2. **Decoding**: User selects the stego-image, and the tool reveals the hidden text.

## 🔧 Installation
1. Make sure Python 3 is installed.
2. Install required libraries:
   ```bash
   pip install stegano pillow
