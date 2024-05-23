import pygame
from pyfiglet import Figlet
from time import sleep as wait
import os
pygame.init()
sample = pygame.mixer.Sound("res/sample.mp3")
music = pygame.mixer.Sound("res/music.mp3")
gate_close = pygame.mixer.Sound("res/gate_close.ogg")


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
    print("      [0] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 1")
    gate_close.play()
    wait(0.6)
    print('\n')
    print("      [1] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 2")
    gate_close.play()
    wait(0.6)
    print('\n')
    print("      [2] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 3")
    gate_close.play()
    wait(0.6)
    print('\n')
    print("      [3] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 4")
    gate_close.play()
    wait(0.6)
    print('\n')
    print("      [4] *NEW* ПРОГРАМА ДО ЗАВДАННЯ 5")
    gate_close.play()
    print('\n                 (оновлено 23.05.2024)')
    wait(0.6)

    choose = input('  Ваш вибір: ')

    wait(0.3)
    clear()
    if choose == '0':
        music.stop()
        gate_close.play()
        music.play()
        def program_1():
            wait(3)
            animate_text2("Спочатку. . .")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Напишіть три цифри через пробіл, ")
            wait(0.5)
            animate_text2("результатом яких буде число, складене з цих цифр.")
            wait(0.4)
            print('\n')
            int1 = input('  Введіть значення: ').split()
            result = int(' '.join(int1))
            wait(0.45)
            clear()
            animate_text2("Окей.")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Ось результат:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(f'{result}'))
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
        program_1()

    elif choose == '1':
        music.stop()
        gate_close.play()
        music.play()
        def program_2():
            wait(3)
            animate_text2("Введіть число з чотирьох цифр, ")
            wait(0.5)
            animate_text2("результатом якого буде їх добуток.")
            wait(0.4)
            print('\n')
            int1 = input('  Введіть значення: ')
            result = 1
            for digit in int1:
                result *= int(digit)
            wait(0.45)
            clear()
            animate_text2("Окей.")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Ось результат:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(f'{result}'))
            gate_close.play()
            wait(2)
            print('\n')
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
        program_2()
    elif choose == '2':
        music.stop()
        gate_close.play()
        music.play()
        def program_3():
            wait(3)
            animate_text2("Введіть значення у метрах, ")
            wait(0.5)
            animate_text2("і отримайте конвертоване значення у см, мм, дм і милях.")
            wait(0.4)
            print('\n')
            int1 = int(input('  Введіть значення (м): '))
            result_cm = f'{int(int1 * 100)} cm'
            result_dm = f'{int(int1 * 10)} dm'
            result_mm = f'{int(int1 * 1000)} mm'
            result_mile = f'{int1 * 0.000621371} mi'
            wait(0.45)
            clear()
            animate_text2("Значення отримано.")
            wait(2)
            clear()
            wait(0.45)
            animate_text2(f"{int1} м - це:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(result_cm))
            gate_close.play()
            wait(1)
            print(Figlet(font='slant').renderText(result_dm))
            gate_close.play()
            wait(1)
            print(Figlet(font='slant').renderText(result_mm))
            gate_close.play()
            wait(1)
            print(Figlet(font='slant').renderText(result_mile))
            gate_close.play()
            wait(1)
            print('\n')
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
        program_3()

    elif choose == '3':
        music.stop()
        gate_close.play()
        music.play()
        def program_4():
            wait(3)
            animate_text2("Це калькулятор площі трикутника. ")
            wait(0.5)
            animate_text2("Введіть довжини його основи і висоти.")
            wait(0.4)
            print('\n')
            base = float(input('Введіть довжину основи трикутника: '))
            height = float(input('Введіть довжину висоти трикутника: '))
            wait(0.45)
            result = 0.5 * base * height
            clear()
            animate_text2("Гаразд.")
            wait(0.8)
            clear()
            wait(0.3)
            animate_text2("Ось площа трикутника:")
            print('\n')
            wait(0.45)
            print(Figlet(font='slant').renderText(f'S = {int(result)}'))
            gate_close.play()
            wait(1)
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
        program_4()
    elif choose == '4':
        music.stop()
        gate_close.play()
        music.play()
        def program_5():
            wait(3)
            animate_text2("Введіть число, ")
            wait(0.5)
            animate_text2("і отримайте його в перевернутому вигляді.")
            wait(0.4)
            print('\n')
            int1 = input('Введіть число: ')
            wait(0.45)
            result = int1[::-1]
            clear()
            animate_text2("Базару нуль.")
            wait(0.8)
            clear()
            wait(0.3)
            animate_text2("Ось відповідь:")
            print('\n')
            wait(0.45)
            print(Figlet(font='slant').renderText(f'{int(result)}'))
            gate_close.play()
            wait(1)
            animate_text2("Бажаєте почати знову?")
            wait(0.4)
            ans = input(' [y/n] ')
            if ans == 'y':
                wait(0.4)
                clear()
                gate_close.play()
                program_5()
            elif ans == 'Y':
                wait(0.4)
                clear()
                gate_close.play()
                program_5()

            else:
                clear()
                music.stop()
                gate_close.play()
                wait(1)
                menu()
        program_5()
    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()





menu()






menu()
