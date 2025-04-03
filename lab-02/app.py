from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.playfair import PlayFairCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
from cipher.transposition import TranspositionCipher
import os 
import subprocess
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '../platforms'
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
     # Đường dẫn tới file caesar_cipher.py
    file_path = os.path.abspath("../lab-03/caesar_cipher.py")
    
    # Chạy file caesar_cipher.py bằng subprocess
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Trả về kết quả đầu ra của file caesar_cipher.py
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        # Trả về lỗi nếu file caesar_cipher.py gặp vấn đề
        return f"<pre>Error: {e.stderr}</pre>", 500

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/playfair")
def playfair():
      # Đường dẫn tới file caesar_cipher.py
    file_path = os.path.abspath("../lab-03/playfair_cipher.py")
    
    # Chạy file caesar_cipher.py bằng subprocess
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Trả về kết quả đầu ra của file caesar_cipher.py
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        # Trả về lỗi nếu file caesar_cipher.py gặp vấn đề
        return f"<pre>Error: {e.stderr}</pre>", 500
@app.route("/playfair_encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    if not text or not key:
        return "Error: Missing text or key!", 400
    
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(text, matrix)
    
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"
@app.route("/playfair_decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    if not text or not key:
        return "Error: Missing text or key!", 400
    
    playfair_cipher = PlayFairCipher()
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(text, matrix)
    
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


@app.route("/vigenere")
def vigenere():
      # Đường dẫn tới file caesar_cipher.py
    file_path = os.path.abspath("../lab-03/virgenere_cipher.py")
    
    # Chạy file caesar_cipher.py bằng subprocess
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Trả về kết quả đầu ra của file caesar_cipher.py
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        # Trả về lỗi nếu file caesar_cipher.py gặp vấn đề
        return f"<pre>Error: {e.stderr}</pre>", 500
@app.route("/vigenere_encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere_decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence")
def railfence():
     # Đường dẫn tới file caesar_cipher.py
    file_path = os.path.abspath("../lab-03/railfence_cipher.py")
    
    # Chạy file caesar_cipher.py bằng subprocess
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=True
        )
        # Trả về kết quả đầu ra của file caesar_cipher.py
        return f"<pre>{result.stdout}</pre>"
    except subprocess.CalledProcessError as e:
        # Trả về lỗi nếu file caesar_cipher.py gặp vấn đề
        return f"<pre>Error: {e.stderr}</pre>", 500

@app.route("/railfence_encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    RailFence = RailFenceCipher()
    encrypted_text = RailFence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence_decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    RailFence = RailFenceCipher()
    decrypted_text = RailFence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/transposition")
def transposition():
    return render_template('transposition.html')
@app.route("/transposition_encrypt", methods=['POST'])
def transposition_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Transposition = TranspositionCipher()
    encrypted_text = Transposition.encrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/transposition_decrypt", methods=['POST'])
def transposition_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Transposition = TranspositionCipher()
    decrypted_text = Transposition.decrypt(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)