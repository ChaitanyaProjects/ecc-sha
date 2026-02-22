from PIL import Image
import numpy as np

END_MARKER = "1111111111111110"

def extract_data(image_path):
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img)

    binary_data = ""

    for row in arr:
        for pixel in row:
            for i in range(3):
                binary_data += str(pixel[i] & 1)

    end_index = binary_data.find(END_MARKER)
    if end_index == -1:
        raise ValueError("End marker not found")

    binary_data = binary_data[:end_index]

    bytes_data = bytearray()
    for i in range(0, len(binary_data), 8):
        bytes_data.append(int(binary_data[i:i+8], 2))

    return bytes(bytes_data)