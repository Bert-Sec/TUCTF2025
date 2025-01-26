import binascii

def xor_decrypt(hex_string):
    encrypted_bytes = bytes.fromhex(hex_string)
    for key in range(256):
        decrypted_bytes = bytes([b ^ key for b in encrypted_bytes])
        try:
            decrypted_text = decrypted_bytes.decode('ascii')
            if all(32 <= ord(c) <= 126 for c in decrypted_text):
                print(f"Key: {key} (0x{key:02X})\nDecrypted Text: {decrypted_text}\n")
        except UnicodeDecodeError:
            continue
if __name__ == "__main__":
    hex_string = "4e4f594e5c617763457c2e6c2a282b2d29456d2a287e452b2f45772a2b2f2d67"
    xor_decrypt(hex_string)
