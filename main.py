import pygame
from pyfiglet import Figlet
from time import sleep as wait
import os
pygame.init()
sample = pygame.mixer.Sound("res/sample.mp3")
music = pygame.mixer.Sound("res/music.mp3")
gate_close = pygame.mixer.Sound("res/gate_close.ogg")

def program_1():
    wait(3)
    animate_text2("Введіть число в діапазоні від 1 до 100:")
    wait(0.4)
    number = int(input(" "))
    wait(0.4)
    animate_text2("Результат:")
    print('\n')
    wait(0.4)
    if number < 1 or number > 100: print("Помилка: введене число не входить у діапазон від 1 до 100.")
    elif number % 3 == 0 and number % 5 == 0: print(Figlet(font="slant").renderText("Fizz Buzz"))
    elif number % 3 == 0: print(Figlet(font="slant").renderText("Fizz"))
    elif number % 5 == 0: print(Figlet(font="slant").renderText("Buzz"))
    gate_close.play()
    wait(2)
    animate_text2("Бажаєте почати знову?")
    wait(0.4)
    ans = input(' [y/n] ')
    if ans == 'y':
        wait(0.4)
        clear()
        gate_close.play()
        program_1()
    elif ans == 'Y':
        wait(0.4)
        clear()
        gate_close.play()
        program_1()

    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()

def program_2():
    wait(3)
    animate_text2("Введіть число:")
    number = int(input(" "))
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Тепер введіть степінь:")
    exp = int(input(" (0-7)"))
    wait(0.4)
    clear()
    animate_text2("Результат:")
    print('\n')
    wait(0.4)
    print(Figlet(font="slant").renderText(f"{number ** exp}")) if exp >= 0 and exp <= 7 else print('Помилка: введено неправильний степінь. Введіть значення від 0 до 7.')
    gate_close.play()
    wait(2)
    animate_text2("Бажаєте почати знову?")
    wait(0.4)
    ans = input(' [y/n] ')
    if ans == 'y':
        wait(0.4)
        clear()
        gate_close.play()
        program_2()
    elif ans == 'Y':
        wait(0.4)
        clear()
        gate_close.play()
        program_2()

    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()

def program_3():
    #init
    tariffs = {
        ("Operator1", "Operator1"): 0.05,
        ("Operator1", "Operator2"): 0.10,
        ("Operator1", "Operator3"): 0.15,
        ("Operator2", "Operator1"): 0.10,
        ("Operator2", "Operator2"): 0.05,
        ("Operator2", "Operator3"): 0.12,
        ("Operator3", "Operator1"): 0.15,
        ("Operator3", "Operator2"): 0.12,
        ("Operator3", "Operator3"): 0.05,
    }
    def get_tariff(from_operator, to_operator): return tariffs.get((from_operator, to_operator), None)
    wait(3)
    animate_text2("Це калькулятор-форма обчислення вартості дзвінка.")
    print('\n')
    wait(0.4)
    call_cost = int(input("Введіть вартість розмови (у хвилинах): "))
    from_operator = input("Введіть оператора, з якого дзвоните (Operator1, Operator2, Operator3): ")
    to_operator = input("Введіть оператора, на який дзвоните (Operator1, Operator2, Operator3): ")
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Результат:")
    print('\n')
    wait(0.4)
    tariff = get_tariff(from_operator, to_operator)

    if tariff is not None:
        total_cost = call_cost * tariff
        print(f"Вартість розмови з {from_operator} на {to_operator} дорівнює {total_cost:.2f}")
    else:
        print("Помилка: введено неправильних операторів або тариф не знайдено.")
    gate_close.play()
    wait(2)
    animate_text2("Бажаєте почати знову?")
    wait(0.4)
    ans = input(' [y/n] ')
    if ans == 'y':
        wait(0.4)
        clear()
        gate_close.play()
        program_3()
    elif ans == 'Y':
        wait(0.4)
        clear()
        gate_close.play()
        program_3()

    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()

def program_4():
    #init
    tariffs = {
        ("Operator1", "Operator1"): 0.05,
        ("Operator1", "Operator2"): 0.10,
        ("Operator1", "Operator3"): 0.15,
        ("Operator2", "Operator1"): 0.10,
        ("Operator2", "Operator2"): 0.05,
        ("Operator2", "Operator3"): 0.12,
        ("Operator3", "Operator1"): 0.15,
        ("Operator3", "Operator2"): 0.12,
        ("Operator3", "Operator3"): 0.05,
    }
    def get_tariff(from_operator, to_operator): return tariffs.get((from_operator, to_operator), None)
    wait(3)
    animate_text2("Це калькулятор-форма, яка підраховує зарплату менеджерів на основі їхніх продажів, визначає кращого менеджера та нараховує йому премію.")
    print('\n')
    wait(0.4)
    def calculate_salary(sales):
        base_salary = 200
        if sales <= 500:
            bonus = sales * 0.03
        elif sales <= 1000:
            bonus = sales * 0.05
        else:
            bonus = sales * 0.08
        return base_salary + bonus

    sales1 = float(input("Введіть рівень продажів для першого менеджера: "))
    sales2 = float(input("Введіть рівень продажів для другого менеджера: "))
    sales3 = float(input("Введіть рівень продажів для третього менеджера: "))
    salary1 = calculate_salary(sales1)
    salary2 = calculate_salary(sales2)
    salary3 = calculate_salary(sales3)
    max_sales = max(sales1, sales2, sales3)
    if max_sales == sales1:
        best_salary = salary1 + 200
        best_manager = "Перший менеджер"
    elif max_sales == sales2:
        best_salary = salary2 + 200
        best_manager = "Другий менеджер"
    else:
        best_salary = salary3 + 200
        best_manager = "Третій менеджер"
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Результат:")
    print('\n')
    wait(0.4)
    print(f"Зарплата першого менеджера: {salary1:.2f} $")
    gate_close.play()
    wait(2)
    print(f"Зарплата другого менеджера: {salary2:.2f} $")
    gate_close.play()
    wait(2)
    print(f"Зарплата третього менеджера: {salary3:.2f} $")
    gate_close.play()
    wait(2)
    print(f"Кращий менеджер: {best_manager} з зарплатою {best_salary:.2f} $")
    gate_close.play()
    wait(2)
    animate_text2("Бажаєте почати знову?")
    wait(0.4)
    ans = input(' [y/n] ')
    if ans == 'y':
        wait(0.4)
        clear()
        gate_close.play()
        program_4()
    elif ans == 'Y':
        wait(0.4)
        clear()
        gate_close.play()
        program_4()

    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()

def animate_text(text):
    for char in text:
        print(char, end='', flush=True)
        sample.play()
        wait(0.03)

def animate_text2(text):
    for char in text:
        print(char, end='', flush=True)
        sample.play()
        wait(0.07)

def clear():
    if os.name == 'nt':
        _ = os.system('cls')

    else:
        _ = os.system('clear')

clear()
text = "Привіт, "
animate_text(text)
wait(0.8)
text = "як справи?"
animate_text(text)
wait(2)
clear()
wait(0.45)
def menu():
    text = "Виберіть "
    animate_text(text)
    wait(0.4)
    text = "програму:"
    animate_text(text)
    print('\n')
    wait(0.8)
    print("      [0] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 1\n")
    gate_close.play()
    wait(0.3)
    print("      [1] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 2\n")
    gate_close.play()
    wait(0.3)
    print("      [2] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 3\n")
    gate_close.play()
    wait(0.3)
    print("      [3] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 4")
    gate_close.play()
    print('\n                 (оновлено 08.06.2024)')
    wait(0.6)

    choose = input('  Ваш вибір: ')

    wait(0.3)
    clear()
    music.stop()
    gate_close.play()
    music.play()

    if choose == '0': program_1()
    elif choose == '1': program_2()
    elif choose == '2': program_3()
    elif choose == '3': program_4()
    else:

        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()





menu()
