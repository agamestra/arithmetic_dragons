# coding: utf-8
# license: GPLv3
from enemies import *
from hero import *

def annoying_input_int(message =''):
    answer = None
    while answer == None:
        try:
            answer = int(input(message))
        except ValueError:
            print('Вы ввели недопустимые символы')
    return answer


def game_tournament(hero, dragon_list, troll_list):
    for dragon in dragon_list:
        print('Вышел', dragon._color, 'дракон!')
        while dragon.is_alive() and hero.is_alive():
            print('Вопрос:', dragon.question())
            answer = annoying_input_int('Ответ:')

            if dragon.check_answer(answer):
                hero.attack(dragon)
                hero.experience()
                print('Верно! \n** дракон кричит от боли ** \nЗдоровье дракона:', dragon._health, '\nОпыт', hero._name, ':', hero._experience)
            else:
                dragon.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \nЗдоровье', hero._name, ':', hero._health)
        if dragon.is_alive():
            break
        print('Дракон', dragon._color, 'повержен!\n')

    for troll in troll_list:
        print('Вышел', troll._character, 'тролль!')
        while troll.is_alive() and hero.is_alive():
            print('Вопрос:', troll.question())
            answer = annoying_input_int('Ответ:')

            if troll.check_answer(answer):
                hero.attack(troll)
                hero.experience()
                print('Верно! \n** тролль кричит от боли ** \nЗдоровье тролля:', troll._health, '\nОпыт', hero._name, ':', hero._experience)
            else:
                troll.attack(hero)
                print('Ошибка! \n** вам нанесён удар... ** \nЗдоровье', hero._name, ':', hero._health)
        if troll.is_alive():
            break
        print('Тролль', troll._color, 'повержен!\n')

    if hero.is_alive():
        print('Поздравляем! Вы победили!')
        print('Ваш накопленный опыт:', hero._experience)
    else:
        print('К сожалению, Вы проиграли...')

def start_game():

    try:
        print('Добро пожаловать в арифметико-ролевую игру с драконами!')
        print('Представьтесь, пожалуйста: ', end = '')
        Hero._name = Hero(input())

        dragon_number = 3
        troll_number = 3
        dragon_list = generate_dragon_list(dragon_number)
        troll_list = generate_troll_list(troll_number)
        assert(len(dragon_list) == 3)
        assert(len(troll_list) == 3)
        print('У Вас на пути', dragon_number, 'драконов и', troll_number, 'троллей!')
        game_tournament(Hero._name, dragon_list)
        game_tournament(Hero._name, troll_list)

    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')
