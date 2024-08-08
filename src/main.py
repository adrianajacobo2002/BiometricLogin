import sys
import os

import cv2
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN
from tkinter import *
import numpy as np
import sounddevice as sd
from resemblyzer import VoiceEncoder, preprocess_wav
from scipy.io.wavfile import write


import database as db

from PyQt6.uic import load_ui
from PyQt6 import QtWidgets

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from PySide6.QtCore import Qt
from mainwindow import Ui_MainWindow
from logindesign import Ui_Login  
from registerdesign import Ui_Dialog
from homedesign import Ui_Home


encoder = VoiceEncoder()
path = "C:/Users/Adriana Jacobo/Desktop/biometriclogin/src/"
color_success = "\033[1;32;40m"
color_error = "\033[1;31;40m"
color_normal = "\033[0;37;40m"

#MAIN
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Aquí puedes conectar señales y slots, por ejemplo:
        self.btnLogin.clicked.connect(self.handle_login)
        self.txtRegister.mousePressEvent = self.handle_register  # Conectar el clic en el label de registro

    def handle_login(self):
        dialog = LoginDialog(self)
        dialog.exec()

    def handle_register(self, event):
        dialog = RegisterDialog(self)
        dialog.exec()


#PANTALLA DE REGISTRO
class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super(RegisterDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnFaceRecon.clicked.connect(self.capture_face)
        self.ui.btnVoiceRecon.clicked.connect(self.capture_voice)
        self.ui.btnRegister.clicked.connect(self.register_user)

    def capture_voice(self):
        user_name = self.ui.txtName.text()

        if not user_name:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa tu nombre.")
            return

        audio, fs = self.grabar_voz()

        if audio is not None:
            huella_voz = self.process_voice(audio, fs)
            if huella_voz is not None:
                # Puedes guardar la huella de voz en tu base de datos o procesarla según tus necesidades
                self.user_voiceprint = huella_voz


    def grabar_voz(self, duracion_segundos=5, fs=16000):
        print("Grabando...")
        try:
            audio = sd.rec(int(duracion_segundos * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            print("Grabación completada.")
            return audio.flatten(), fs
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al grabar el audio: {str(e)}")
            return None, None

    def process_voice(self, audio, fs):
        try:
            # Convertir audio a formato WAV y luego a numpy array
            wav_path = "../temp.wav"
            write(wav_path, fs, audio.astype(np.int16))
            
            # Cargar el archivo WAV y procesar
            wav = preprocess_wav(wav_path)
            huella_voz = encoder.embed_utterance(wav)
            
            return huella_voz
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al procesar el audio: {str(e)}")
            return None

    def capture_face(self):
        cap = cv2.VideoCapture(0)
        user_name = self.ui.txtName.text()

        if not user_name:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa tu nombre.")
            return

        img = f"{user_name}.jpg"

        while True:
            ret, frame = cap.read()
            cv2.imshow("Registro Facial", frame)
            if cv2.waitKey(1) == 27:
                break

        cv2.imwrite(img, frame)
        cap.release()
        cv2.destroyAllWindows()

        pixels = plt.imread(img)
        faces = MTCNN().detect_faces(pixels)
        self.process_face(img, faces)

    def process_face(self, img, faces):
        data = plt.imread(img)
        for i in range(len(faces)):
            x1, y1, ancho, alto = faces[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            plt.subplot(1, len(faces), i + 1)
            plt.axis("off")
            face = cv2.resize(data[y1:y2, x1:x2], (150, 200), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(img, face)
            plt.imshow(data[y1:y2, x1:x2])

    def register_user(self):
        user_name = self.ui.txtName.text()
        user_last_name = self.ui.txtLastName.text()
        user_email = self.ui.txtEmail.text()
        img = f"{user_name}.jpg"

        if not all([user_name, user_last_name, user_email]):
            QMessageBox.warning(self, "Advertencia", "Por favor, completa todos los campos.")
            return

        if hasattr(self, 'user_voiceprint'):
            huella_voz = self.user_voiceprint
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, completa la verificación de voz.")
            return


        res_bd = db.registerUser(user_name, user_last_name, user_email, img, huella_voz)

        if res_bd["affected"]:
            QMessageBox.information(self, "Éxito", "¡Éxito! Se ha registrado correctamente")
        else:
            QMessageBox.warning



#PANTALLA DE INICIO SESIÓN
class LoginDialog(QDialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        self.ui = Ui_Login()
        self.ui.setupUi(self)


        self.ui.btnVoice.clicked.connect(self.login_capture_voice)
        self.ui.btnFacial.clicked.connect(self.login_capture_face)

    #Reconocimiento por Voz
    def grabar_voz(self, duracion_segundos=5, fs=16000):
        print("Grabando...")
        try:
            audio = sd.rec(int(duracion_segundos * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            print("Grabación completada.")
            return audio.flatten(), fs
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al grabar el audio: {str(e)}")
            return None, None

    """ def login_capture_voice(self):
        user_email = self.ui.txtEmail.text()

        if not user_email:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa tu correo electrónico.")
            return

        audio, fs = self.grabar_voz()
        
        if audio is None:
            return

        # Convertir audio a formato WAV y luego a numpy array
        wav_path = "../temp.wav"
        write(wav_path, fs, audio.astype(np.int16))

        # Cargar el archivo WAV y procesar
        wav = preprocess_wav(wav_path)
        huella_actual = encoder.embed_utterance(wav)

        res_db = db.getUserByVoice(user_email)


        if res_db["affected"] > 0:
            huella_registrada_blob = res_db["huella_voz"]
            if isinstance(huella_registrada_blob, memoryview):
                huella_registrada_blob = huella_registrada_blob.tobytes()
            huella_registrada = np.frombuffer(huella_registrada_blob, dtype=np.float32)

            distancia = np.linalg.norm(huella_registrada - huella_actual)
            print(f"Distancia entre huellas: {distancia}")

            umbral = 0.6
            if distancia < umbral:
                QMessageBox.information(self, "Éxito", "Verificación exitosa. Identidad confirmada.")

                
            else:
                QMessageBox.warning(self, "Error", "Verificación fallida. Identidad no confirmada.")
        else:
            QMessageBox.warning(self, "Error", "Usuario no encontrado.")

 """
    
    def login_capture_voice(self):
        user_email = self.ui.txtEmail.text()

        if not user_email:
            QMessageBox.warning(self, "Advertencia", "Por favor, ingresa tu correo electrónico.")
            return

        audio, fs = self.grabar_voz()
        
        if audio is None:
            return

        # Convertir audio a formato WAV y luego a numpy array
        wav_path = "../temp.wav"
        write(wav_path, fs, audio.astype(np.int16))

        # Cargar el archivo WAV y procesar
        wav = preprocess_wav(wav_path)
        huella_actual = encoder.embed_utterance(wav)

        res_db = db.getUserByVoice(user_email)

        if res_db["affected"] > 0:
            huella_registrada_blob = res_db["huella_voz"]
            if isinstance(huella_registrada_blob, memoryview):
                huella_registrada_blob = huella_registrada_blob.tobytes()
            huella_registrada = np.frombuffer(huella_registrada_blob, dtype=np.float32)

            distancia = np.linalg.norm(huella_registrada - huella_actual)
            print(f"Distancia entre huellas: {distancia}")

            umbral = 0.6
            if distancia < umbral:
                QMessageBox.information(self, "Éxito", "Verificación exitosa. Identidad confirmada.")
                user_name = res_db["nombre"]
                user_last_name = res_db["apellido"]
                home_dialog = HomeDialog(self, user_name, user_last_name)
                home_dialog.exec()
                
            else:
                QMessageBox.warning(self, "Error", "Verificación fallida. Identidad no confirmada.")
        else:
            QMessageBox.warning(self, "Error", "Usuario no encontrado.")


    #Reconocimiento Facial
    def login_capture_face(self):
        cap = cv2.VideoCapture(0)
        user_login = self.ui.txtEmail.text()  # Usamos txtEmail como nombre de usuario
        img = f"{user_login}_login.jpg"
        img_user = f"{user_login}.jpg"

        while True:
            ret, frame = cap.read()
            cv2.imshow("Login Facial", frame)
            if cv2.waitKey(1) == 27:  # Presiona ESC para capturar la imagen
                break

        cv2.imwrite(img, frame)
        cap.release()
        cv2.destroyAllWindows()

        pixels = plt.imread(img)
        faces = MTCNN().detect_faces(pixels)

        self.face(img, faces)

        res_db = db.getUserByPhoto(user_login, path + img_user)

        if res_db["affected"]:
            my_files = os.listdir()
            if img_user in my_files:
                face_reg = cv2.imread(img_user, 0)
                face_log = cv2.imread(img, 0)

                comp = self.compatibility(face_reg, face_log)
                
                if comp >= 0.94:
                    print("{}Compatibilidad del {:.1%}{}".format(color_success, float(comp), color_normal))
                    self.printAndShow(f"Bienvenido, {user_login}", True)
                    user_name = res_db["nombre"]
                    user_last_name = res_db["apellido"]
                    home_dialog = HomeDialog(self, user_name, user_last_name)
                    home_dialog.exec()
                    
                else:
                    print("{}Compatibilidad del {:.1%}{}".format(color_error, float(comp), color_normal))
                    self.printAndShow("¡Error! Incopatibilidad de datos", False)
                os.remove(img_user)
        
            else:
                self.printAndShow("¡Error! Usuario no encontrado", False)
        else:
            self.printAndShow("¡Error! Usuario no encontrado", False)
        os.remove(img)

    def face(self, img, faces):
        data = plt.imread(img)
        for i in range(len(faces)):
            x1, y1, ancho, alto = faces[i]["box"]
            x2, y2 = x1 + ancho, y1 + alto
            plt.subplot(1, len(faces), i + 1)
            plt.axis("off")
            face = cv2.resize(data[y1:y2, x1:x2], (150, 200), interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(img, face)
            plt.imshow(data[y1:y2, x1:x2])

    def compatibility(self, img1, img2):
        orb = cv2.ORB_create()

        kpa, dac1 = orb.detectAndCompute(img1, None)
        kpa, dac2 = orb.detectAndCompute(img2, None)

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = comp.match(dac1, dac2)

        similar = [x for x in matches if x.distance < 70]
        if len(matches) == 0:
            return 0
        return len(similar) / len(matches)

    def printAndShow(self, text, flag):
        if flag:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(text)
            msg.setWindowTitle("¡Éxito!")
            msg.exec()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText(text)
            msg.setWindowTitle("Error")
            msg.exec()



class HomeDialog(QDialog, Ui_Home):
    def __init__(self, parent, user_name, user_last_name):
        super(HomeDialog, self).__init__(parent)
        self.setupUi(self)
        self.txtName.setText(user_name)
        self.txtLastName.setText(user_last_name)
        self.btnLogOut.clicked.connect(self.close)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

