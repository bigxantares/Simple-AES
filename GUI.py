import sys
import typing


from encrypt import Decrypy1, Encrypy, Encrypy1
from CBC import CBCEncrypy, CBCDecrypy
from decrypt import Decrypy
from PyQt5.QtGui import QIcon, QFont, QPalette, QColor
from PyQt5.QtWidgets import  QLabel, QLineEdit, QMessageBox
from PyQt5 import QtCore
from PyQt5.QtWidgets import  QApplication,QMainWindow, QPushButton, QVBoxLayout, QWidget, QSizePolicy, QHBoxLayout
class SAESEncryptionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.mode = "binary"  # 默认模式为"binary"
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setFixedSize(500, 600)
        self.setWindowTitle("S-AES ")

        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))
        # 设置窗口样式
        self.setStyleSheet("QMainWindow { border: 2px solid red; }")
        # 设置背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(180, 180, 180))
        self.setPalette(palette)

        main_layout = QVBoxLayout()

        # 明文输入框
        plain_text_label = QLabel("输入明文/密文:")
        plain_text_label.setFont(QFont('微软雅黑', 20))
        self.plain_text_edit = QLineEdit()
        self.plain_text_edit.setFont(QFont('微软雅黑', 12))
        self.plain_text_edit.setStyleSheet("background-color: white;")

        # 密钥输入框
        key_label = QLabel("输入密钥:")
        key_label.setFont(QFont('微软雅黑', 20))
        self.key_edit = QLineEdit()
        self.key_edit.setFont(QFont('微软雅黑', 12))
        self.key_edit.setStyleSheet("background-color: white;")

       

        # 密文输出框
        cipher_text_label = QLabel("结果:")
        cipher_text_label.setFont(QFont('微软雅黑', 18))
        self.cipher_text_edit = QLineEdit()
        self.cipher_text_edit.setFont(QFont('微软雅黑', 12))
        self.cipher_text_edit.setStyleSheet("background-color: white;")
        self.cipher_text_edit.setReadOnly(True)

        # 加密按钮
        encrypt_button = QPushButton("Encrypt")
        encrypt_button.setFont(QFont('微软雅黑', 20))
        encrypt_button.setStyleSheet("background-color: #4C11CC; color: white;")
        encrypt_button.clicked.connect(self.encrypt)
        encrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

       

 
        # 解密按钮
        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.decrypt)
        decrypt_button.setFont(QFont('微软雅黑', 20))
        decrypt_button.setStyleSheet("background-color: #f44336; color: white;")
        decrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

       

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(encrypt_button)
        button_layout.addWidget(decrypt_button)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)

       

        # 模式选择布局
        mode_layout = QHBoxLayout()
        mode_label = QLabel("Mode:")
        mode_label.setFont(QFont('微软雅黑', 18))
        self.mode_button = QPushButton("binary Mode")
        self.mode_button.setFont(QFont('微软雅黑', 18))
        self.mode_button.setStyleSheet("background-color: #555555; color: white;")
        self.mode_button.setCheckable(True)
        self.mode_button.setChecked(True)
        self.mode_button.clicked.connect(self.changeMode)

        # 向模式选择布局添加控件
        mode_layout.addWidget(mode_label)
        mode_layout.addWidget(self.mode_button)
        mode_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局居中对齐

        # 向主布局添加控件
        main_layout.addWidget(plain_text_label)
        main_layout.addWidget(self.plain_text_edit)
        main_layout.addWidget(key_label)
        main_layout.addWidget(self.key_edit)
       
        main_layout.addWidget(cipher_text_label)
        main_layout.addWidget(self.cipher_text_edit)
        main_layout.addLayout(mode_layout)  # 添加模式选择布局
        main_layout.addLayout(button_layout)
        

        self.setLayout(main_layout)
        self.show()

    def changeMode(self):
        if self.mode_button.isChecked():
            self.mode = "binary"
            self.mode_button.setText("binary Mode")
            self.mode_button.setStyleSheet("background-color: #1C9B64; color: white;")
        else:
            self.mode = "ascii"
            self.mode_button.setText("ASCII Mode")
            self.mode_button.setStyleSheet("background-color: #812299; color: white;")

    def encrypt(self):
        # 获取输入的明文和密钥
        mingwen = [[0 for _ in range(8)] for _ in range(2)]
        key = [[0 for _ in range(8)] for _ in range(2)]
        binary_input = self.plain_text_edit.text()

        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return

        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(binary_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

        # 二进制
        if self.mode == "binary":
            mingwen = [[int(binary_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            # 如果选择了ASCII码模式，将输入的字符转换为对应的二进制字符串
            if all(ord(c) < 128 for c in binary_input) and len(binary_input) != 0:
                binary_input = ''.join(format(ord(char), '08b') for char in binary_input)
                mingwen = [[int(binary_input[i * 8 + j]) for j in range(8)] for i in range(2)]
            else:
                QMessageBox.warning(self, "Error", "输入的ASCII格式不正确！(分组为2 Bytes)")
                return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

            # 二进制
        if self.mode == "binary":
                key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            # 如果选择了ASCII码模式，将输入的字符转换为对应的二进制字符串
            if all(ord(c) < 128 for c in key_input) and len(binary_input) != 0:
                key_input = ''.join(format(ord(char), '08b') for char in key_input)
                key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
            else:
                QMessageBox.warning(self, "Error", "输入的ASCII格式不正确！(分组为2 Bytes)")
                return

        # 将结果显示在输出框中
        try:
            if self.mode == "binary":
                decrypted_text = Encrypy(mingwen, key)
            else:
                decrypted_text = Encrypy(mingwen, key)
                # 将二进制字符串按8位分割
                binary_chunks = [decrypted_text[i:i + 8] for i in range(0, len(decrypted_text), 8)]
                # 将每个8位二进制字符串转换为对应的整数
                integer_values = [int(chunk, 2) for chunk in binary_chunks]
                # 将整数转换为对应的ASCII字符并拼接成字符串
                decrypted_text = ''.join(chr(value) for value in integer_values)
            self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")

    def decrypt(self):
        # 获取输入的密文和密钥
        miwen = [[0 for _ in range(8)] for _ in range(2)]
        key = [[0 for _ in range(8)] for _ in range(2)]
        binary_input = self.plain_text_edit.text()

        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return

        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(binary_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

        # 二进制
        if self.mode == "binary":
            miwen = [[int(binary_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            # 如果选择了ASCII码模式，将输入的字符转换为对应的二进制字符串
            if len(binary_input) != 0:
                binary_input = ''.join(format(ord(char), '08b') for char in binary_input)
                miwen = [[int(binary_input[i * 8 + j]) for j in range(8)] for i in range(2)]
            else:
                QMessageBox.warning(self, "Error", "输入的ASCII格式不正确！(分组为2 Bytes)")
                return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

            # 二进制
        if self.mode == "binary":
            key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            # 如果选择了ASCII码模式，将输入的字符转换为对应的二进制字符串
            if all(ord(c) < 128 for c in key_input) and len(binary_input) != 0:
                key_input = ''.join(format(ord(char), '08b') for char in key_input)
                key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
            else:
                QMessageBox.warning(self, "Error", "输入的ASCII格式不正确！(分组为2 Bytes)")
                return

        # 将结果显示在输出框中
        try:
            if self.mode == "binary":
                decrypted_text = Decrypy(miwen, key)
            else:
                decrypted_text = Decrypy(miwen, key)
                # 将二进制字符串按8位分割
                binary_chunks = [decrypted_text[i:i + 8] for i in range(0, len(decrypted_text), 8)]
                # 将每个8位二进制字符串转换为对应的整数
                integer_values = [int(chunk, 2) for chunk in binary_chunks]
                # 将整数转换为对应的ASCII字符并拼接成字符串
                decrypted_text = ''.join(chr(value) for value in integer_values)
            self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"解密发生错误: {e}")

    def CBC_encrypt(self):
        # 获取输入的向量
        iv_input = self.iv_edit.text()
        iv = [[int(iv_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        # 获取输入的明文
        binary_input = self.plain_text_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC加密")
            return
        # 二进制
        if self.mode == "binary":
            num_rows = len(binary_input) // 8
            mingwen = [[0 for _ in range(8)] for _ in range(num_rows)]
            for i in range(num_rows):
                start_index = i * 8
                end_index = start_index + 8
                row_values = binary_input[start_index:end_index]
                mingwen[i] = [int(val) for val in row_values]
        else:
            QMessageBox.warning(self, "Error", "请使用二进制进行CBC加密")
            return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return
            # 二进制
        if self.mode == "binary":
            key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            QMessageBox.warning(self, "Error", "请使用二进制进行CBC加密")
            return

        # 将结果显示在输出框中
        try:
                print("成功进入CBC加密")
                decrypted_text = CBCEncrypy(mingwen, key, iv)
                self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")

    def CBC_decrypt(self):
        # 获取输入的向量
        iv_input = self.iv_edit.text()
        iv = [[int(iv_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        # 获取输入的明文
        binary_input = self.plain_text_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC解密")
            return
        # 二进制
        if self.mode == "binary":
            num_rows = len(binary_input) // 8
            mingwen = [[0 for _ in range(8)] for _ in range(num_rows)]
            for i in range(num_rows):
                start_index = i * 8
                end_index = start_index + 8
                row_values = binary_input[start_index:end_index]
                mingwen[i] = [int(val) for val in row_values]
        else:
                QMessageBox.warning(self, "Error", "请使用二进制进行CBC解密")
                return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC解密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

            # 二进制
        if self.mode == "binary":
            key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
                QMessageBox.warning(self, "Error", "请使用二进制进行CBC解密")
                return

        # 将结果显示在输出框中
        try:
                print("成功进入CBC解密")
                decrypted_text = CBCDecrypy(mingwen, key, iv)
                self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")

    def multiple(self):
        child_window=multiple_SAESEncryptionGUI()
        child_window.show()
       
#多重加密界面
class multiple_SAESEncryptionGUI(QWidget):

   
    def __init__(self):
        super().__init__()
        self.mode = "double"  # 默认模式为"double"
        self.initUI()

    def initUI(self):
        # 设置窗口标题和大小
        self.setFixedSize(500, 600)
        self.setWindowTitle("S-AES ")

        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))
        # 设置窗口样式
        self.setStyleSheet("QMainWindow { border: 2px solid red; }")
        # 设置背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(180, 180, 180))
        self.setPalette(palette)

        main_layout = QVBoxLayout()

        # 明文输入框
        plain_text_label = QLabel("输入明文/密文:")
        plain_text_label.setFont(QFont('微软雅黑', 20))
        self.plain_text_edit = QLineEdit()
        self.plain_text_edit.setFont(QFont('微软雅黑', 12))
        self.plain_text_edit.setStyleSheet("background-color: white;")

        # 密钥输入框
        key_label = QLabel("输入密钥:")
        key_label.setFont(QFont('微软雅黑', 20))
        self.key_edit = QLineEdit()
        self.key_edit.setFont(QFont('微软雅黑', 12))
        self.key_edit.setStyleSheet("background-color: white;")

        # 密文输出框
        cipher_text_label = QLabel("结果:")
        cipher_text_label.setFont(QFont('微软雅黑', 18))
        self.cipher_text_edit = QLineEdit()
        self.cipher_text_edit.setFont(QFont('微软雅黑', 12))
        self.cipher_text_edit.setStyleSheet("background-color: white;")
        self.cipher_text_edit.setReadOnly(True)

        # 加密按钮
        encrypt_button = QPushButton("Encrypt")
        encrypt_button.setFont(QFont('微软雅黑', 20))
        encrypt_button.setStyleSheet("background-color: #4C11CC; color: white;")
        encrypt_button.clicked.connect(self.encrypt)
        encrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # 解密按钮
        decrypt_button = QPushButton("Decrypt")
        decrypt_button.clicked.connect(self.decrypt)
        decrypt_button.setFont(QFont('微软雅黑', 20))
        decrypt_button.setStyleSheet("background-color: #f44336; color: white;")
        decrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # 按钮布局
        button_layout = QHBoxLayout()
        button_layout.addWidget(encrypt_button)
        button_layout.addWidget(decrypt_button)
        button_layout.setAlignment(QtCore.Qt.AlignCenter)

        # 模式选择布局
        mode_layout = QHBoxLayout()
        mode_label = QLabel("Mode:")
        mode_label.setFont(QFont('微软雅黑', 18))
        self.mode_button = QPushButton("double Mode")
        self.mode_button.setFont(QFont('微软雅黑', 18))
        self.mode_button.setStyleSheet("background-color: #555555; color: white;")
        self.mode_button.setCheckable(True)
        self.mode_button.setChecked(True)
        self.mode_button.clicked.connect(self.changeMode)

        # 向模式选择布局添加控件
        mode_layout.addWidget(mode_label)
        mode_layout.addWidget(self.mode_button)
        mode_layout.setAlignment(QtCore.Qt.AlignCenter)  # 设置布局居中对齐

        # 向主布局添加控件
        main_layout.addWidget(plain_text_label)
        main_layout.addWidget(self.plain_text_edit)
        main_layout.addWidget(key_label)
        main_layout.addWidget(self.key_edit)
        main_layout.addWidget(cipher_text_label)
        main_layout.addWidget(self.cipher_text_edit)
        main_layout.addLayout(mode_layout)  # 添加模式选择布局
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.show()

    def changeMode(self):
        if self.mode_button.isChecked():
            self.mode = "double"
            self.mode_button.setText("double Mode")
            self.mode_button.setStyleSheet("background-color: #1C9B64; color: white;")
        else:
            self.mode = "triple"
            self.mode_button.setText("triple Mode")
            self.mode_button.setStyleSheet("background-color: #812299; color: white;")

    def encrypt(self):
        # 获取输入的明文和密钥
        mingwen = [[0 for _ in range(8)] for _ in range(2)]
        key1 = [[0 for _ in range(8)] for _ in range(2)]
        key2 = [[0 for _ in range(8)] for _ in range(2)]
        double_input = self.plain_text_edit.text()

        # 判断输入的文本是否为二进制
        if self.mode == "double" and not all(c in "01" for c in double_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return

        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "double" and len(double_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

       
        mingwen = [[int(double_input[i * 8 + j]) for j in range(8)] for i in range(2)]
            

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "double" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于32，则给出错误提示
        if self.mode == "double" and len(key_input) != 32:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

        
        key_input1=key_input[:16]
        key_input2=key_input[16:]
        key1 = [[int(key_input1[i * 8 + j]) for j in range(8)] for i in range(2)]
        key2 = [[int(key_input2[i * 8 + j]) for j in range(8)] for i in range(2)]
       

        # 将结果显示在输出框中
        try:
            if self.mode == "double":
                decrypted_text = Encrypy(Encrypy1(mingwen,key1),key2)
            else:
                decrypted_text = Encrypy(Encrypy1(Encrypy1(mingwen,key1),key2),key1)   
            self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")

    def decrypt(self):
        # 获取输入的密文和密钥
        miwen = [[0 for _ in range(8)] for _ in range(2)]
        key1 = [[0 for _ in range(8)] for _ in range(2)]
        key2 = [[0 for _ in range(8)] for _ in range(2)]
        double_input = self.plain_text_edit.text()

        # 判断输入的文本是否为二进制
        if self.mode == "double" and not all(c in "01" for c in double_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return

        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "double" and len(double_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return
 
        miwen = [[int(double_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "double" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于32，则给出错误提示
        if self.mode == "double" and len(key_input) != 32:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return
        key_input1=key_input[:16]
        key_input2=key_input[16:]
        key1 = [[int(key_input1[i * 8 + j]) for j in range(8)] for i in range(2)]
        key2 = [[int(key_input2[i * 8 + j]) for j in range(8)] for i in range(2)]
        # 将结果显示在输出框中
        try:
            if self.mode == "double":
                decrypted_text = Decrypy(Decrypy1(miwen,key2),key1)

            else:
                decrypted_text = Decrypy(Decrypy1(Decrypy1(miwen,key1),key2),key1)              
            self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"解密发生错误: {e}")
#CBC加密界面
class CBC_SAESEncryptionGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.mode = "binary"  # 默认模式为"binary"
        self.initUI()

    def initUI(self):
         # 设置窗口标题和大小
        self.setFixedSize(500, 600)
        self.setWindowTitle("S-AES ")

        # 设置窗口图标
        self.setWindowIcon(QIcon('icon.png'))
        # 设置窗口样式
        self.setStyleSheet("QMainWindow { border: 2px solid red; }")
        # 设置背景颜色
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(180, 180, 180))
        self.setPalette(palette)
        main_layout = QVBoxLayout()
        # 明文输入框
        plain_text_label = QLabel("输入明文/密文:")
        plain_text_label.setFont(QFont('微软雅黑', 20))
        self.plain_text_edit = QLineEdit()
        self.plain_text_edit.setFont(QFont('微软雅黑', 12))
        self.plain_text_edit.setStyleSheet("background-color: white;")

        # 密钥输入框
        key_label = QLabel("输入密钥:")
        key_label.setFont(QFont('微软雅黑', 20))
        self.key_edit = QLineEdit()
        self.key_edit.setFont(QFont('微软雅黑', 12))
        self.key_edit.setStyleSheet("background-color: white;")

        # 向量输入框
        iv_label = QLabel("输入向量:")
        iv_label.setFont(QFont('微软雅黑', 20))
        self.iv_edit = QLineEdit()
        self.iv_edit.setFont(QFont('微软雅黑', 12))
        self.iv_edit.setStyleSheet("background-color: white;")
        # 密文输出框
        cipher_text_label = QLabel("结果:")
        cipher_text_label.setFont(QFont('微软雅黑', 18))
        self.cipher_text_edit = QLineEdit()
        self.cipher_text_edit.setFont(QFont('微软雅黑', 12))
        self.cipher_text_edit.setStyleSheet("background-color: white;")
        self.cipher_text_edit.setReadOnly(True)
        # CBC加密按钮
        CBCencrypt_button = QPushButton("CBC加密")
        CBCencrypt_button.setFont(QFont('微软雅黑', 20))
        CBCencrypt_button.setStyleSheet("background-color: #54FF9F; color: white;")
        CBCencrypt_button.clicked.connect(self.CBC_encrypt)
        CBCencrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # CBC解密按钮
        CBCdecrypt_button = QPushButton("CBC解密")
        CBCdecrypt_button.setFont(QFont('微软雅黑', 20))
        CBCdecrypt_button.setStyleSheet("background-color: #FFC125; color: white;")
        CBCdecrypt_button.clicked.connect(self.CBC_decrypt)
        CBCdecrypt_button.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        button_layout_3 = QHBoxLayout()
        button_layout_3.addWidget(CBCencrypt_button)
        button_layout_3.addWidget(CBCdecrypt_button)
        button_layout_3.setAlignment(QtCore.Qt.AlignCenter)
        # 向主布局添加控件
        main_layout.addWidget(plain_text_label)
        main_layout.addWidget(self.plain_text_edit)
        main_layout.addWidget(key_label)
        main_layout.addWidget(self.key_edit)
        main_layout.addWidget(iv_label)
        main_layout.addWidget(self.iv_edit)
        main_layout.addWidget(cipher_text_label)
        main_layout.addWidget(self.cipher_text_edit)
        main_layout.addLayout(button_layout_3)

        self.setLayout(main_layout)
        self.show()
    def CBC_encrypt(self):
        # 获取输入的向量
        iv_input = self.iv_edit.text()
        iv = [[int(iv_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        # 获取输入的明文
        binary_input = self.plain_text_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC加密")
            return
        # 二进制
        if self.mode == "binary":
            num_rows = len(binary_input) // 8
            mingwen = [[0 for _ in range(8)] for _ in range(num_rows)]
            for i in range(num_rows):
                start_index = i * 8
                end_index = start_index + 8
                row_values = binary_input[start_index:end_index]
                mingwen[i] = [int(val) for val in row_values]
        else:
            QMessageBox.warning(self, "Error", "请使用二进制进行CBC加密")
            return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC加密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return
            # 二进制
        if self.mode == "binary":
            key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
            QMessageBox.warning(self, "Error", "请使用二进制进行CBC加密")
            return

        # 将结果显示在输出框中
        try:
                print("成功进入CBC加密")
                decrypted_text = CBCEncrypy(mingwen, key, iv)
                self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")

    def CBC_decrypt(self):
        # 获取输入的向量
        iv_input = self.iv_edit.text()
        iv = [[int(iv_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        # 获取输入的明文
        binary_input = self.plain_text_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in binary_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC解密")
            return
        # 二进制
        if self.mode == "binary":
            num_rows = len(binary_input) // 8
            mingwen = [[0 for _ in range(8)] for _ in range(num_rows)]
            for i in range(num_rows):
                start_index = i * 8
                end_index = start_index + 8
                row_values = binary_input[start_index:end_index]
                mingwen[i] = [int(val) for val in row_values]
        else:
                QMessageBox.warning(self, "Error", "请使用二进制进行CBC解密")
                return

        key_input = self.key_edit.text()
        # 判断输入的文本是否为二进制
        if self.mode == "binary" and not all(c in "01" for c in key_input):
            QMessageBox.warning(self, "警告", "请使用二进制进行CBC解密")
            return
        # 如果选择了二进制模式并输入的二进制字符串长度不等于16，则给出错误提示
        if self.mode == "binary" and len(key_input) != 16:
            QMessageBox.warning(self, "Error", "输入的二进制字符串长度不正确！")
            return

            # 二进制
        if self.mode == "binary":
            key = [[int(key_input[i * 8 + j]) for j in range(8)] for i in range(2)]
        else:
                QMessageBox.warning(self, "Error", "请使用二进制进行CBC解密")
                return

        # 将结果显示在输出框中
        try:
                print("成功进入CBC解密")
                decrypted_text = CBCDecrypy(mingwen, key, iv)
                self.cipher_text_edit.setText(decrypted_text)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"加密发生错误: {e}")























#S_AES_AES主界面
class MainWindow(QMainWindow):
    def __init__(self ):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('S-AES')
        self.setFixedSize(500,600)
        self.setWindowIcon(QIcon('icon.png'))
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(180, 180, 180))
        self.setPalette(palette)
        main_layout=QVBoxLayout()
        encrypt_button1 = QPushButton("经典加密模式")
        encrypt_button1.setFont(QFont('微软雅黑', 20))
        encrypt_button1.setStyleSheet("background-color: #4C11CC; color: white;")
        encrypt_button1.clicked.connect(self.createwindow1)

        
        encrypt_button2 = QPushButton("多重加密模式")
        encrypt_button2.setFont(QFont('微软雅黑', 20))
        encrypt_button2.setStyleSheet("background-color: #5AA334; color: white;")
        encrypt_button2.clicked.connect(self.createwindow2)


        encrypt_button3 = QPushButton("CBC加密模式")
        encrypt_button3.setFont(QFont('微软雅黑', 20))
        encrypt_button3.setStyleSheet("background-color: #8F213A; color: white;")
        encrypt_button3.clicked.connect(self.createwindow3)


        main_layout.addWidget(encrypt_button1)
        main_layout.addWidget(encrypt_button2)
        main_layout.addWidget(encrypt_button3)
        
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def createwindow1(self):
        self.window1=SAESEncryptionGUI()
        self.window1.show()
    def createwindow2(self):
        self.window2=multiple_SAESEncryptionGUI()
        self.window2.show()
    def createwindow3(self):
        self.window3=CBC_SAESEncryptionGUI()
        self.window3.show()
# 创建应用程序和窗口
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

#测试数据：使用密钥           1010011100111011
# 加密二进制明文         0110111101101011
# 得出二进制密文       0000011100111000  1111000110000110

