import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.playfair import Ui_MainWindow
import requests

class RailFenceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        
    def call_api_encrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/encrypt"
        payload = {
            "plain_text": self.ui.txt_plain_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_cipher_text.setPlainText(data['encrypted_text'])
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Encryption Successful")
                msg.exec()
            else:
                print("Error while calling API, Status Code:", response.status_code)
        except requests.exceptions.RequestException as e:
            print("Error:", str(e))

    
    def call_api_decrypt(self):
        url = "http://127.0.0.1:5000/api/playfair/decrypt"
        payload = {
            "cipher_text": self.ui.txt_cipher_text.toPlainText(),
            "key": self.ui.txt_key.toPlainText()
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.txt_plain_text.setPlainText(data["decrypted_text"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decryption Successful")
                msg.exec()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % str(e))
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RailFenceApp()
    window.show()
    sys.exit(app.exec_())
