# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

def generate_troll_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,10)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class GayTroll(Troll):
    def __init__(self):
        self._healf = 100
        self._attack = 10
        self._character = 'весёлый'
    def question(self):
        x = randint(1,5)
        self._quest = 'Угадай число'
        self.set_answer(x)
        return self._quest

class SadTroll(Troll):
    def __init__(self):
        self._healf = 100
        self._attack = 10
        self._character = 'грустный'
    def question(self):
        x = randint(1,10)
        for i in range (x//2+1):
            if x%i == 0 and x/i != 1:
                y = '-'
            else:
                y = '+'
        self._quest = 'Число', x, 'простое?'
        self.set_answer(y)
        return self._quest

enemy_types = [GreenDragon, RedDragon, BlackDragon]
