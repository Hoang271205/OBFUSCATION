import base64
import zlib
from itertools import cycle

def xor_cipher(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, cycle(key)))

def obfuscate_payload(payload_str: str, key: bytes) -> bytes:
    # 1. Encoding (Base64)
    b64_data = base64.b64encode(payload_str.encode('utf-8'))
    # 2. Encryption (XOR)
    encrypted_data = xor_cipher(b64_data, key)
    # 3. Packing (Zlib)
    packed_data = zlib.compress(encrypted_data)
    return packed_data