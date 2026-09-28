import socket
import threading

PORT = 5000

clients = {}


# =========================
# FOR SERVER
# =========================

def broadcast(message):
    data = (message + "\n").encode("utf-8")

    for client in list(clients):
        try:
            client.sendall(data)
        except:
            clients.pop(client, None)


def handle_client(conn, addr):
    name = "Unknown"

    try:
        name = conn.recv(1024).decode("utf-8").strip()

        clients[conn] = name

        print(f"{name} đã kết nối từ {addr}")

        while True:
            data = conn.recv(4096)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if message:
                full_message = f"{name}: {message}"

                print(full_message)

                broadcast(full_message)

    except Exception as e:
        print("Lỗi:", e)

    finally:
        clients.pop(conn, None)
        conn.close()
        print(f"{name} đã thoát")


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind(("0.0.0.0", PORT))
    server.listen(5)

    print(f"Server đang chạy tại port {PORT}")
    print("Đang chờ A và B kết nối...")

    while True:
        conn, addr = server.accept()

        thread = threading.Thread(
            target=handle_client,
            args=(conn, addr),
            daemon=True
        )

        thread.start()


def start_client(name, server_ip):

    client = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    client.connect((server_ip, PORT))

    client.sendall(
        (name + "\n").encode("utf-8")
    )

    print(f"{name} đã kết nối Server.")
    print("Gõ tin nhắn rồi Enter.")
    print("Gõ /quit để thoát.")
    print("-" * 40)

    def receive_messages():

        buffer = ""

        while True:

            try:
                data = client.recv(4096)

                if not data:
                    break

                buffer += data.decode("utf-8")

                while "\n" in buffer:

                    message, buffer = buffer.split("\n", 1)

                    if message:
                        print("\n" + message)
                        print(f"{name}: ",
                              end="",
                              flush=True)

            except:
                break

    threading.Thread(
        target=receive_messages,
        daemon=True
    ).start()

    while True:

        message = input(f"{name}: ")

        if message == "/quit":
            break

        if message.strip():

            client.sendall(
                (message + "\n").encode("utf-8")
            )

    client.close()


# =========================
# MÁY 1 = SERVER + A
# =========================

print("=" * 40)
print("MÁY 1 - SERVER + A")
print("=" * 40)

# Chạy Server bằng thread
server_thread = threading.Thread(
    target=start_server,
    daemon=True
)

server_thread.start()

# Chờ Server khởi động
import time
time.sleep(1)

# A kết nối vào chính Server trên máy 1
start_client("A", "127.0.0.1")