from PIL import Image
import numpy as np

END_MARKER = "1111111111111110"

def embed_data(image_path, data: bytes, output_path):
    img = Image.open(image_path).convert("RGB")
    arr = np.array(img, dtype=np.uint8)

    binary_data = "".join(format(byte, "08b") for byte in data) + END_MARKER
    data_index = 0

    for row in arr:
        for pixel in row:
            for i in range(3):
                if data_index < len(binary_data):
                    bit = int(binary_data[data_index])
                    pixel[i] = (pixel[i] & 0b11111110) | bit
                    data_index += 1

    Image.fromarray(arr).save(output_path)