import pygame
from pyfiglet import Figlet
from time import sleep as wait
import os
pygame.init()
sample = pygame.mixer.Sound("sample.mp3")
music = pygame.mixer.Sound("music.mp3")
gate_close = pygame.mixer.Sound("gate_close.ogg")


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
    wait(0.8)
    print('\n\n')
    text = "      [0] ПРОГРАМА ДО ЗАВДАННЯ 1"
    animate_text(text)
    wait(0.8)
    print('\n')
    text = "      [1] ПРОГРАМА ДО ЗАВДАННЯ 2"
    animate_text(text)
    wait(0.8)
    print('\n')
    choose = input('  Ваш вибір: ')

    wait(0.3)
    clear()
    gate_close.play()
    if choose == '0':
        music.play()
        def program_1():
            wait(3)
            animate_text2("Спочатку. . .")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Напишіть три числа, ")
            wait(0.5)
            animate_text2("результатом яких буде їх сума і добуток.")
            wait(0.4)
            print('\n')
            int1 = int(input('  Напишіть перше число: '))
            int2 = int(input('  Напишіть друге число: '))
            int3 = int(input('  Напишіть третє число: '))
            result1 = f'{int1 + int2 + int3}'
            result2 = f'{int1 * int2 * int3}'
            wait(0.45)
            clear()
            animate_text2("Прекрасно.")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Ось сума трьох чисел:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(result1))
            gate_close.play()
            wait(0.8)
            print('\n')
            animate_text2("Ось добуток трьох чисел:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(result2))
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
        music.play()
        def program_2():
            wait(3)
            animate_text2("Напишіть три числа, ")
            wait(0.5)
            animate_text2("результатом яких буде сума, яка залишиться у вас після всіх витрат.")
            wait(0.4)
            print('\n')
            int1 = int(input('  Зарплата за місяць: '))
            int2 = int(input('  Сума місячного платежу за кредитом у банку: '))
            int3 = int(input('  Заборгованість за комунальні послуги: '))
            result1 = f'{int1 - int2 - int3}'
            wait(0.45)
            clear()
            animate_text2("Прекрасно.")
            wait(2)
            clear()
            wait(0.45)
            animate_text2("Ось сума, яка залишилась у вас після всіх виплат:")
            print('\n')
            wait(1)
            print(Figlet(font='slant').renderText(result1))
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
    else:
        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()





menu()
