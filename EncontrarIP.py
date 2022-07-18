#Se importa la libreria socket
import socket

#Busca el IP y nombre de la computadora
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

#Se muestran los resultados
print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es: " + ip) 