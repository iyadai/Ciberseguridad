import socket

def obtener_banner(ip, puerto):
    try:
        # 1. Creamos el socket (el "teléfono")
        # AF_INET = IPv4, SOCK_STREAM = TCP
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # 2. Ponemos un tiempo límite (timeout) de 2 segundos
        cliente.settimeout(2)
        
        # 3. Intentamos conectar
        print(f"[*] Conectando a {ip}:{puerto}...")
        cliente.connect((ip, puerto))
        
        # 4. Enviamos un pequeño saludo (opcional, para despertar al servidor)
        # cliente.send(b'Hello\r\n')
        
        # 5. Recibimos la respuesta (el banner)
        banner = cliente.recv(1024)
        return banner.decode().strip()
        
    except Exception as e:
        return f"[!] No se pudo obtener el banner: {str(e)}"
    finally:
        # 6. Cerramos la conexión
        cliente.close()

def main():
    print("--- [ Herramienta de Reconocimiento Inicial ] ---")
    objetivo = input("IP a escanear: ")
    puerto = int(input("Puerto (ej: 22, 80, 443): "))
    
    resultado = obtener_banner(objetivo, puerto)
    print(f"\n[+] Resultado del Banner:\n{resultado}")

if __name__ == "__main__":
    main()