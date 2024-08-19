def win(i=0):
    return (p[i][i] == p[i + 1][i + 1] == p[i + 2][i + 2] == (0 or 'x') or (
            p[i + 2][i] == p[i + 1][i + 1] == p[i][i + 2] == (0 or 'x'))
            or (p[i][i] == p[i][i + 1] == p[i][i + 2] == (0 or 'x')) or (
                    p[i][i] == p[i + 1][i] == p[i + 2][i] == (0 or 'x')))


def igrok(i):
    if i % 2 == 0:
        return 'Нолика'
    else:
        return 'Крестика'


def ogranich(i, j):
    return p[i - 1][j - 1] == '-'


print('Приветствую вас в игре "Крестики-нолики"!')
print('Правила игры простые - первым ход делает крестик, после него нолик. Ходы чередуются до момента, \
пока на поле не выстроится диагональ или прямая, состоящая из трех одинаковых символов.')
print('Чтобы выбрать клетку, вам нужно ввести два значения: столбец и строку клетки через пробел.')
print('Удачной игры!!! Победит СИЛЬНЕЙШИЙ!!!')
print('')

p = [['-'] * 3 for i in range(3)]
hod = 0
while True:
    hod += 1
    for i in p:
        print(*i)
    print('Ход ' + igrok(hod))
    i, j = map(int, input('Введите позицию (строку, столбец): ').split())
    if ogranich(i, j):
        if (hod) % 2 == 0:
            p[i - 1][j - 1] = 0
        else:
            p[i - 1][j - 1] = 'x'
    else:
        print('Данные не корректны, введите заново ')
        hod -= 1
        pass
    if win():
        for i in p:
            print(*i)
        p = [['-'] * 3 for i in range(3)]
        hod = 0
        print('Игра закончена, поздравляю с победой!')
