import requests
import json

def get_ollama_move(board):
    board_str = ' '.join(['X' if x == 'X' else 'O' if x == 'O' else ' ' for x in board])
    prompt = f"Tic-Tac-Toe board is:\n{board_str}\nWhat's the best move for O?"

    ollama_url = 'http://localhost:11434/api/generate'

    data = {
        "model": "llama2",
        "prompt": prompt,
    }

    response = requests.post(ollama_url, json=data)
    if response.status_code == 200:
        response_parts = response.text.split('\n')
        full_response = ''
        for part in response_parts:
            try:
                json_part = json.loads(part)
                full_response += json_part['response']
                if json_part['done']:
                    break
            except json.JSONDecodeError:
                print("Fejl ved dekodning af JSON del")
                return None

        # Her bør du tilføje logik til at udlede den specifikke position fra 'full_response'
        # Eksempelvis kunne du søge efter en specifik tekst eller format
        print("Samlet respons:", full_response)
        # Eksempel på at finde position baseret på din egen logik
        ai_move = int()  # Opdater dette til at udlede positionen baseret på 'full_response'

        return ai_move
    else:
        print("Der opstod en fejl under kommunikationen med Ollama.")
        return None

# Initialiser spillebrættet
board = [' ' for _ in range(9)]

# Funktion til at udskrive brættet
def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

# Spillets hovedloop
player_turn = True
while True:
    print_board()
    if player_turn:
        move = int(input("Dit træk (1-9): ")) - 1
        if board[move] == ' ':
            board[move] = 'X'
            player_turn = False
        else:
            print("Feltet er allerede taget, prøv igen.")
    else:
        # Her vil du kalde Ollama for at få AI's træk
        ai_move = get_ollama_move(board)
        if ai_move is not None and 0 <= ai_move < len(board):
            board[ai_move] = 'O'  # Brug 'O' i stedet for int()
        else:
            print("Kunne ikke få et gyldigt træk fra AI.")
        player_turn = True
