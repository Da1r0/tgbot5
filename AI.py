from random import choice

otvets = [
    'Точно да',
    'Возможно',
    'Может быть',
    'Скорее всего нет',
    'Точно нет'
]


def generate_answer():
    return choice(otvets)
