import socket

PUERTOS_CRITICOS = {
    21: "FTP",
    22: "SSH",
    25: "SMTP",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def obtener_banner(ip, puerto):
    try:
        # 1. Creamos el socket (el "teléfono")
        # AF_INET = IPv4, SOCK_STREAM = TCP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Ponemos un tiempo límite (timeout) de 1 segundos que deberia ser suficiente en este caso
        cliente.settimeout(1)
    
        # 3. Intentamos conectar
        cliente.connect((ip, puerto))
        banner = cliente.recv(1024)
        
        # 4. Recibimos la respuesta (el banner)
        return banner.decode().strip()
        
    except:
        return None
    finally:
        # 5. Cerramos la conexión
        cliente.close()

def main():
    print("--- [ Escaneo de Puertos Automatizado ] ---")
    objetivo = input("IP a escanear (ej: 127.0.0.1): ")
    
    print(f"\n[*] Iniciando auditoría en {objetivo}...")
    
    for puerto, servicio in PUERTOS_CRITICOS.items():
        banner = obtener_banner(objetivo, puerto)
        if banner:
            print(f"[+] Puerto {puerto} ({servicio}) ABIERTO: {banner}")
        else:
            print(f"[-] Puerto {puerto} ({servicio}) cerrado o sin respuesta.")

if __name__ == "__main__":
    main()