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
<img width="1102" height="545" alt="stegano" src="https://github.com/user-attachments/assets/5ab45bb6-66a5-4848-990e-70de6c1fb994" />

   Run the script in VS Code or any Python IDE.

## 🖥️ Usage
Encode: Select an image, enter secret text, and save the modified image.
Decode: Select the modified image to reveal the hidden message.

## CLI OUTPUT
- <img width="1083" height="418" alt="output for cli" src="https://github.com/user-attachments/assets/e8109a3b-9865-4df9-ab5e-0fe2353db09d" />

## 📂 Example
Original Image → Encoded Image (with hidden message).
Extract hidden text using the decode option.
<img width="1152" height="716" alt="Screenshot 2025-09-14 172312" src="https://github.com/user-attachments/assets/1caa5bd9-48f2-43b4-b1f2-4a7dca138c4a" />


## ⚠️ Limitations
Only works with PNG and BMP images (JPEG is not supported).
Currently supports hiding text only, not files.

## 🔮 Future Improvements
Add support for hiding files (PDF, DOCX, etc.).
Add password protection with encryption.
Improve GUI with drag-and-drop support.

## 👨‍💻 Author
Developed as a Python mini-project demonstration.
