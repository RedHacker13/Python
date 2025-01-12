from cryptography.fernet import Fernet
import os

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(items, key):
    f = Fernet(key)
    for item in items:
        with open(item, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item, 'wb') as file:
            file.write(decrypted_data)
#Finalmente el archivo estara de desecriptado en el ordenador
if __name__ == '__main__':
    path_to_encrypt = 'F:\\1Proyectos-Python\\ransom\\files'
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    key = cargar_key()
    decrypt(full_path,key)