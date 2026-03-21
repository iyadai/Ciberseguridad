import socket
from datetime import datetime

# Tu lista de objetivos
PUERTOS_CRITICOS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

def guardar_hallazgo(ip, puerto, servicio, banner):
    # La 'a' significa 'Append' (añadir sin borrar lo anterior)
    with open("auditoria_red.txt", "a") as archivo:
        tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"[{tiempo}] IP: {ip} | Puerto: {puerto} ({servicio}) | Banner: {banner}\n"
        archivo.write(linea)

def obtener_banner(ip, puerto):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip, puerto))
        banner = sock.recv(1024).decode().strip()
        return banner
    except:
        return None
    finally:
        sock.close()

# En tu bucle 'for' dentro de main(), solo tienes que llamar a la función:
# if banner:
#     guardar_hallazgo(objetivo, puerto, servicio, banner)