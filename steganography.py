from PIL import Image

def encode_text(image_path, text, output_path):
    img = Image.open(image_path)
    encoded = img.copy()
    width, height = img.size
    index = 0

    # Add a delimiter at the end of text
    text += "%%END%%"
    binary_text = ''.join(format(ord(c), '08b') for c in text)

    for row in range(height):
        for col in range(width):
            if index < len(binary_text):
                r, g, b = img.getpixel((col, row))
                # Change LSB of red channel
                r = (r & ~1) | int(binary_text[index])
                encoded.putpixel((col, row), (r, g, b))
                index += 1
            else:
                break

    encoded.save(output_path)
    print(f"Message encoded and saved as {output_path}")


def decode_text(image_path):
    img = Image.open(image_path)
    width, height = img.size
    binary_data = ""
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            binary_data += str(r & 1)

    # Convert binary to text
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    decoded = ''.join(chr(int(c, 2)) for c in chars if len(c) == 8)

    # Stop at delimiter
    message = decoded.split("%%END%%")[0]
    return message


if __name__ == "__main__":
    print("1. Encode text")
    print("2. Decode text")
    choice = input("Choose option: ")

    if choice == "1":
        img_in = input("Enter input image path: ")
        text = input("Enter text to hide: ")
        img_out = input("Enter output image path: ")
        encode_text(img_in, text, img_out)

    elif choice == "2":
        img_in = input("Enter image path with hidden text: ")
        message = decode_text(img_in)
        print("Hidden message:", message)
