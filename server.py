                (p1_choice == "scissors" and p2_choice == "paper"):
            result1, result2 = "win", "lose"
        else:
            result1, result2 = "lose", "win"


        player1.send(json.dumps({"action": "result", "result": result1, "opponent": p2_choice}).encode())
        player2.send(json.dumps({"action": "result", "result": result2, "opponent": p1_choice}).encode())


        play_again_count = 0
        while play_again_count < 2:
            for player in [player1, player2]:
                try:
                    data = player.recv(1024).decode()
                    if not data:
                        raise ConnectionResetError
                    msg = json.loads(data)
                    if msg["action"] == "play_again":
                        play_again_count += 1
                    elif msg["action"] == "report_result":
                        print(f"[RESULT] Client báo cáo: {msg}")

