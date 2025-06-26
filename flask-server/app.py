from flask import Flask, request, send_from_directory
import os
import uuid
import threading
import time

app = Flask(__name__)
UPLOAD_FOLDER = '/tmp/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def delete_file_later(filepath, delay=300):
    def delete_file():
        time.sleep(delay)
        if os.path.exists(filepath):
            os.remove(filepath)
    threading.Thread(target=delete_file).start()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    filename = str(uuid.uuid4())
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    delete_file_later(filepath)

    return f'File uploaded successfully with link /files/{filename}'

@app.route('/files/<filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

