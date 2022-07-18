#Se importa las librerias socket y sys
import socket
import sys

#Se insertar la dirección IP objetivo
objetivo = socket.gethostbyname(input("Inserte la dirección IP: "))
print("Escaneando objetivo: " + objetivo)

#Se realiza la busqueda de los puertos abiertos del equipo
try:
    for port in range(1,65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultado = s.connect_ex((objetivo, port))
        if resultado == 0:
            print("El puerto {} esta abierto".format(port))
        s.close()
except:
    print("\n Saliendo...")
    sys.exit(0)
