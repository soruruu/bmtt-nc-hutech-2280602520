import sys
from PIL import Image
def decode_image(image_path):
    image = Image.open(image_path)
    width, height = image.size
    binary_message = ''

    for row in range(height):
        for col in range(width):
            pixel = list(image.getpixel((col, row)))
            for color_channel in range(3):
                binary_message += format(pixel[color_channel], '08b')[-1]  # Lấy bit thấp nhất

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == '00000000':  # Dấu kết thúc (null terminator)
            break
        ascii_code = int(byte, 2)
        message += chr(ascii_code)

    return message

def main():
    if len(sys.argv) != 2:
        print("Usage: python decrypt.py <encoded_image_path>")
        return
    
    encoded_image_path = sys.argv[1]
    decoded_message = decode_image(encoded_image_path)
    print("Decoded message:", decoded_message)

if __name__ == "__main__":
    main()

    