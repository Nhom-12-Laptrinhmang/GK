import socket
import json
import threading

HOST = '127.0.0.1'
PORT = 12345

# Hàm gửi tin nhắn đến server
def send_message(sock, action, choice=None):
    message = {"action": action}
    if choice:
        message["choice"] = choice
    sock.send(json.dumps(message).encode())

# Hàm nhận phản hồi từ server
def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024).decode()
            if not data:
                print("Mất kết nối với server.")
                break
            msg = json.loads(data)
            if msg["action"] == "start":
                print("Trận đấu bắt đầu!")
            elif msg["action"] == "result":
                print(f"Kết quả: {msg['result']}, đối thủ chọn {msg['opponent']}")
            elif msg["action"] == "opponent_disconnected":
                print("Đối thủ đã rời trận đấu.")
                break
        except (ConnectionResetError, json.JSONDecodeError):
            print("Lỗi kết nối hoặc dữ liệu không hợp lệ.")
            break

# Hàm chính khởi tạo socket client
def main():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((HOST, PORT))
        print("Đã kết nối tới server.")

        # Luồng nhận tin nhắn
        threading.Thread(target=receive_messages, args=(sock,), daemon=True).start()

        while True:
            choice = input("Nhập lựa chọn (rock/paper/scissors hoặc 'exit' để thoát): ").strip().lower()
            if choice == "exit":
                break
            if choice in ["rock", "paper", "scissors"]:
                send_message(sock, "choose", choice)
            else:
                print("Lựa chọn không hợp lệ!")

    except Exception as e:
        print(f"Lỗi client: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
            while len(choices) < 2:
            for player in [player1, player2]:
                try:
                    data = player.recv(1024).decode()
                    if not data:
                        raise ConnectionResetError
                    msg = json.loads(data)
                    if msg["action"] == "choose":
                        choices[player] = msg["choice"]
                    elif msg["action"] == "report_result":
                        print(f"[RESULT] Client báo cáo: {msg}")
                except (ConnectionResetError, json.JSONDecodeError):
                    # Nếu một người thoát, thông báo cho người còn lại
                    other = player2 if player == player1 else player1
                    other.send(json.dumps({"action": "opponent_disconnected"}).encode())
                    return
