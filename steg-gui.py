import tkinter as tk
from tkinter import filedialog, messagebox
from stegano import lsb

# Encode (hide text in image)
def encode_text():
    file_path = filedialog.askopenfilename(
        title="Select Image", filetypes=[("Image Files", "*.png;*.bmp")]
    )
    if not file_path:
        return

    secret = text_entry.get("1.0", tk.END).strip()
    if not secret:
        messagebox.showerror("Error", "Please enter some text to hide")
        return

    save_path = filedialog.asksaveasfilename(
        title="Save Stego Image",
        defaultextension=".png",
        filetypes=[("PNG files", "*.png")]
    )
    if not save_path:
        return

    try:
        secret_image = lsb.hide(file_path, secret)
        secret_image.save(save_path)
        messagebox.showinfo("Success", f"Message hidden and saved as {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Encoding failed: {e}")

# Decode (extract hidden text from image)
def decode_text():
    file_path = filedialog.askopenfilename(
        title="Select Stego Image", filetypes=[("Image Files", "*.png;*.bmp")]
    )
    if not file_path:
        return

    try:
        hidden_message = lsb.reveal(file_path)
        if hidden_message:
            messagebox.showinfo("Hidden Message", hidden_message)
        else:
            messagebox.showwarning("No Message", "No hidden message found in this image!")
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed: {e}")

# GUI setup
root = tk.Tk()
root.title("Simple Steganography Tool")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter text to hide:", font=("Arial", 12)).pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack(pady=5)

tk.Button(root, text="Encode Text", command=encode_text, bg="green", fg="white", width=20).pack(pady=10)
tk.Button(root, text="Decode Text", command=decode_text, bg="blue", fg="white", width=20).pack(pady=10)

root.mainloop()

