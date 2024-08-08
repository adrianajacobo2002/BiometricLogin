import mysql.connector as db
import json
import sounddevice as sd
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from scipy.io.wavfile import write

encoder = VoiceEncoder()


# Cargar la configuración de conexión desde el archivo JSON
with open('C:/Users/Adriana Jacobo/Desktop/biometriclogin/src/keys.json') as json_file:
    keys = json.load(json_file)

def convertToBinaryData(filename):
    try:
        with open(filename, 'rb') as file:
            binaryData = file.read()
        return binaryData
    except Exception as e:
        print(f"Error al convertir a binario: {e}")
        return None

def write_file(data, path):
    with open(path, 'wb') as file:
        file.write(data)

def conectar_db():
    """Establece una conexión a la base de datos."""
    return db.connect(host=keys["host"], user=keys["user"], password=keys["password"], database=keys["database"])

def registerUser(name, surname, email, photo, voice):
    inserted = 0
    id_usuario = 0

    try:
        con = conectar_db()
        cursor = con.cursor()
        sql = "INSERT INTO usuarios (nombre, apellido, email, rostro, huella_voz) VALUES (%s, %s, %s, %s, %s)"
        pic = convertToBinaryData(photo)
        voice_blob = voice.tobytes()

        if pic and voice_blob:
            cursor.execute(sql, (name, surname, email, pic, voice_blob))
            con.commit()
            inserted = cursor.rowcount
            id_usuario = cursor.lastrowid

    except db.Error as e:
        print(f"Error al insertar usuario: {e}")

    finally:
        if con.is_connected():
            cursor.close()
            con.close()

    return {"id_usuario": id_usuario, "affected": inserted}

""" def getUserByPhoto(email, photo_path):
    id_usuario = 0
    rows = 0

    try:
        con = conectar_db()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios WHERE email = %s"

        cursor.execute(sql, (email,))
        recuperados = cursor.fetchall()

        for row in recuperados:
            id_usuario = row[0]
            write_file(row[4], photo_path)
        rows = len(recuperados)

    except db.Error as e:
        print(f"Error al recuperar usuario: {e}")

    finally:
        if con.is_connected():
            cursor.close()
            con.close()

    return {"id_usuario": id_usuario, "affected": rows} """

def getUserByPhoto(email, photo_path):
    try:
        con = conectar_db()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios WHERE email = %s"

        cursor.execute(sql, (email,))
        recuperados = cursor.fetchall()

        if recuperados:
            id_usuario = recuperados[0][0]
            nombre = recuperados[0][1]
            apellido = recuperados[0][2]
            write_file(recuperados[0][4], photo_path)
            return {"id_usuario": id_usuario, "nombre": nombre, "apellido": apellido, "affected": len(recuperados)}
        else:
            return {"affected": 0}

    except db.Error as e:
        print(f"Error al recuperar usuario: {e}")
        return {"affected": 0}

    finally:
        if con.is_connected():
            cursor.close()
            con.close()


""" def getUserByVoice(email):
    
    try:
        con = conectar_db()
        cursor = con.cursor()
        sql = "SELECT huella_voz FROM usuarios WHERE email = %s"

        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        if result:
            huella_voz = result[0]
            print(f"huella_voz (tipo {type(huella_voz)}): {huella_voz}")
            return {"huella_voz": huella_voz, "affected": 1}
        else:
            return {"affected": 0}

    except db.Error as e:
        print(f"Error al recuperar usuario: {e}")
        return {"affected": 0}

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
 """

def getUserByVoice(email):
    try:
        con = conectar_db()
        cursor = con.cursor()
        sql = "SELECT huella_voz, nombre, apellido FROM usuarios WHERE email = %s"

        cursor.execute(sql, (email,))
        result = cursor.fetchone()

        if result:
            huella_voz = result[0]
            nombre = result[1]
            apellido = result[2]
            print(f"huella_voz (tipo {type(huella_voz)}): {huella_voz}")
            return {"huella_voz": huella_voz, "nombre": nombre, "apellido": apellido, "affected": 1}
        else:
            return {"affected": 0}

    except db.Error as e:
        print(f"Error al recuperar usuario: {e}")
        return {"affected": 0}

    finally:
        if con.is_connected():
            cursor.close()
            con.close()



