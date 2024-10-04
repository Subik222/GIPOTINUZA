# GIPOTINUZA
Автори:
Корнєєв Маркіян,
Качмар Данило,
Шиленко Владислав.

import time
import random
def choose_social_media():
    print("Виберіть соціальну мережу для пошуку даних:")
    print("1. Telegram")
    print("2. TikTok")
    print("3. Instagram")
    while True:
        choice = input("Ваш вибір (1, 2 або 3): ")
        if choice == '1':
            return "Telegram"
        elif choice == '2':
            return "TikTok"
        elif choice == '3':
            return "Instagram"
        else:
            print("Неправильний вибір! Будь ласка, виберіть з 1, 2 або 3.")
def simulate_data_collection(social_media):
    print(f"\nШукаємо дані по {social_media}...")
    for i in range(1, 101):
        print(f"Збір даних: {i}%", end='\r')
        time.sleep(random.uniform(0.05, 0.1)) 
    print("\nІнформація зібрана!")
def mobilize_choice():
    print("\nЧи слід мобілізувати користувача?")
    while True:
        choice = input("Ваш вибір (так/ні): ").lower()
        if choice == "так":
            print("Користувач мобілізований!")
            break
        elif choice == "ні":
            print("Користувач не мобілізований!")
            break
        else:
            print("Неправильний вибір! Будь ласка, введіть 'так' або 'ні'.")
def main():
    name = input("Введіть ім'я користувача: ")
    social_media = choose_social_media()  
    simulate_data_collection(social_media)  
    mobilize_choice() 
if __name__ == "__main__":
    main()










#Хрестики нолики


import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.title("Хрестики-Нолики")
current_player = "X"
board = [""] * 9
buttons = []
game_over = False
def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        a, b, c = condition
        if board[a] == board[b] == board[c] and board[a] != "":
            return True
    return False
def check_tie():
    return all(board)
def computer_move():
    available_moves = [i for i, val in enumerate(board) if val == ""]
    if available_moves:
        move = random.choice(available_moves)
        update_board(move, "О")
def update_board(index, player):
    global current_player, game_over
    if board[index] == "" and not game_over:
        board[index] = player
        buttons[index].config(text=player)
        if check_winner():
            game_over = True
            messagebox.showinfo("Перемога!", f"Гравець {player} виграв!")
            reset_game()
        elif check_tie():
            game_over = True
            messagebox.showinfo("Нічія", "Нічія!")
            reset_game()
        else:
            current_player = "O" if player == "X" else "X"
            if current_player == "O":
                computer_move()
def player_move(index):
    if current_player == "X" and board[index] == "":
        update_board(index, "X")
def reset_game():
    global board, current_player, game_over
    board = [""] * 9
    current_player = "X"
    game_over = False
    for button in buttons:
        button.config(text="")
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                       command=lambda i=i: player_move(i))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)
root.mainloop()
