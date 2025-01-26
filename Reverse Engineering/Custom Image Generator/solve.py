from PIL import Image

def parse_timg(file_path, output_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        if not data.startswith(b'TIMG'):
            raise ValueError("Invalid TIMG file header.")

]
        version_minor = data[5]
        width = int.from_bytes(data[8:12], byteorder='big')
        height = int.from_bytes(data[12:16], byteorder='big')

        red_channel = []
        green_channel = []
        blue_channel = []

        offset = 16  # Start reading after the header
        while offset < len(data):
            chunk_type = data[offset:offset + 4]
            offset += 4

            if chunk_type == b'DATR':
                red_channel.append(data[offset:offset + width])
                offset += width + 1  # +1 for the checksum
            elif chunk_type == b'DATG':
                green_channel.append(data[offset:offset + width])
                offset += width + 1  # +1 for the checksum
            elif chunk_type == b'DATB':
                blue_channel.append(data[offset:offset + width])
                offset += width + 1  # +1 for the checksum
            elif chunk_type == b'DATE':
                break
            else:
                # Log unknown chunk types and continue
                print(f"Skipping unknown chunk type: {chunk_type}")
                while offset < len(data) and data[offset:offset + 4] not in [b'DATR', b'DATG', b'DATB', b'DATE']:
                    offset += 1

        # Validate data length
        if len(red_channel) != height or len(green_channel) != height or len(blue_channel) != height:
            raise ValueError("Corrupted TIMG file. Mismatch in channel data length.")

        # Create the reconstructed image
        img = Image.new("RGB", (width, height))
        pixels = img.load()
        for y in range(height):
            for x in range(width):
                r = red_channel[y][x]
                g = green_channel[y][x]
                b = blue_channel[y][x]
                pixels[x, y] = (r, g, b)

        # Save the reconstructed image
        img.save(output_path)
        print(f"Image reconstructed and saved to {output_path}")

    except Exception as e:
        print(f"Error: {e}")

# Usage example
if __name__ == "__main__":
    timg_file_path = "flag.timg"  # Path to the TIMG file
    output_image_path = "reconstructed_flag.png"  # Path to save the reconstructed image
    parse_timg(timg_file_path, output_image_path)
