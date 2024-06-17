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
    animate_text2("Введіть початок діапазону:")
    start = int(input(" "))
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Тепер введіть кінець діапазону:")
    end = int(input(" "))
    wait(0.4)
    clear()
    animate_text2("Числа, кратні 7:")
    print('\n')
    wait(0.4)
    for num in range(start, end + 1):
        if num % 7 == 0:
            print(Figlet(font="slant").renderText(f"{num}"))
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
    animate_text2("Введіть початок діапазону:")
    start = int(input(" "))
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Тепер введіть кінець діапазону:")
    end = int(input(" "))
    wait(0.4)
    clear()
    animate_text2("Діапазон:")
    print('\n')
    wait(0.4)
    for num in range(start, end + 1):
        print(Figlet(font="slant").renderText(f"{num}"))
    gate_close.play()
    wait(2)
    input('Натисніть ANY KEY...')
    clear()
    gate_close.play()
    wait(0.4)
    animate_text2("Діапазон (в спадному порядку):")
    print('\n')
    wait(0.4)
    for num in sorted(list(range(start, end + 1)), reverse=True):
        print(Figlet(font="slant").renderText(f"{num}"))
    gate_close.play()
    wait(2)
    input('Натисніть ANY KEY...')
    clear()
    gate_close.play()
    wait(0.4)
    animate_text2("Числа кратні 7:")
    print('\n')
    wait(0.4)
    for num in range(start, end + 1):
        if num % 7 == 0:
            print(Figlet(font="slant").renderText(f"{num}"))
    gate_close.play()
    wait(2)
    input('Натисніть ANY KEY...')
    clear()
    gate_close.play()
    wait(0.4)
    animate_text2("Числа кратні 5:")
    print('\n')
    wait(0.4)
    for num in range(start, end + 1):
        if num % 5 == 0:
            print(Figlet(font="slant").renderText(f"{num}"))
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
    wait(3)
    animate_text2("Введіть початок діапазону:")
    start = int(input(" "))
    wait(0.4)
    clear()
    wait(0.4)
    animate_text2("Тепер введіть кінець діапазону:")
    end = int(input(" "))
    wait(0.4)
    clear()
    animate_text2("Результат:")
    print('\n')
    wait(0.4)
    for num in range(start, end + 1):
        if num % 3 != 0 and num % 5 != 0: print(Figlet(font="slant").renderText(f"{num}"))
        elif num % 3 == 0: print(Figlet(font="slant").renderText(f"{num} Fizz"))
        elif num % 5 == 0: print(Figlet(font="slant").renderText(f"{num} Buzz"))
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
    print('\n                 (оновлено 17.06.2024)')
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
    else:

        clear()
        music.stop()
        gate_close.play()
        wait(1)
        menu()





menu()
