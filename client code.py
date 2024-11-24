# Python code for the client
import socket

# Основна функція для запуску клієнта
def main():
    # Створюємо сокет для клієнта
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Задаємо серверну адресу та порт
    server_ip_address = "127.0.0.1"
    server_port = 6116

    try:
        # Підключаємося до сервера
        client_socket.connect((server_ip_address, server_port))
        print(f"Підключено до сервера {server_ip_address}:{server_port}")

        # Відправляємо дані серверу
        message = "Hello, Server!"
        client_socket.send(message.encode('ascii'))

        # Отримуємо відповідь від сервера
        response = client_socket.recv(1024)
        print(f"Від сервера отримано відповідь: {response.decode('ascii')}")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        # Закриваємо з'єднання з сервером
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()

if __name__ == "__main__":
    main()
