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
    for i in range(1, 101):  # Процес від 1% до 100%
        print(f"Збір даних: {i}%", end='\r')
        time.sleep(random.uniform(0.05, 0.1)) 
    print("\nІнформація зібрана!")
# Функція для вибору мобілізації
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
# Основна програма
def main():
    name = input("Введіть ім'я користувача: ")
    social_media = choose_social_media()  
    simulate_data_collection(social_media)  
    mobilize_choice() 
if __name__ == "__main__":
    main()
