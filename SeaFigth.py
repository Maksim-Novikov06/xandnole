from random import randint


class Board:

    def __init__(self, size=6):
        self.board = [['O'] * size for i in range(size)]
        self.size = size
        self.ships = []
        self.busy = []
        self.damaged = 0

    def draw_board(self):
        for i in self.board:
            print(*i)

    def out(self, dot):
        return not (0 <= dot.x < self.size) or not (0 <= dot.y < self.size)

    def contour(self, ship):
        pass

    def place_ship(self, ship):
        for dot in ship.dots:
            if self.out(dot) or (dot in self.busy):
                raise BoardException
        for dot in ship.dots:
            self.board[dot.x][dot.y] = '■'
            self.busy.append(dot)
        self.ships.append(ship)

    def shot(self, target):
        if self.out(target):
            raise BoardOutException
        for ship in self.ships:
            if target in ship.dots:
                ship.health -= 1
                self.board[target.x][target.y] = 'X'
            if ship.health == 0:
                self.damaged += 1


class BoardException(Exception):
    pass


class BoardShotException(BoardException):
    def __str__(self):
        return 'Выстрел по данным координатам уже был совершен до этого.'


class BoardOutException(BoardException):
    def __str__(self):
        return 'Вы пытаетесь совершить выстрел за пределами игрового поля.'


class Player:
    def __init__(self, board, enimy):
        self.board = board
        self.enimy = enimy

    def ask(self):
        raise NotImplementedError()

    def shoting(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enimy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class User(Player):
    def ask(self):
        while True:
            print('Введите координаты: ')
            d = input().split()

            if len(d) != 2:
                print('Введите 2 координаты!')
                continue
            x, y = d
            if not (x.isdigit()) or not (y.isdigit()):
                print('Координаты должны быть цифрами!')
            return Dot(x, y)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f'Ход компьютера: ({d.x + 1};{d.y + 1})')
        return d


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __repr__(self):
        return f'Dot({self.x}, {self.y})'


class Ship:

    def __init__(self, x, y, health, oren):
        self.dot = Dot(x, y)
        self.health = health
        self.oren = oren
        self.dots = []
        self.add_dots()

    def add_dots(self):
        for i in range(self.health):
            if self.oren == 0:
                self.dots.append(Dot(self.dot.x, self.dot.y + i))
            else:
                self.dots.append(Dot(self.dot.x + i, self.dot.y))
        return self.dots


class Game:
    def try_board(self):
        lens = [1, 1, 1, 1, 2, 2, 3]
        board = Board(size=self.size)
        attempts = 0
        for i in lens:
            while True:
                attempts += 1
                if attempts >= 2000:
                    return None
                ship = Ship(randint(0, self.size - 1), randint(0, self.size - 1), i, randint(0, 1))
                try:
                    board.place_ship(ship)
                except BoardException:
                    pass

        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def cycle(self):
        num = 0
        while True:
            print("Доска игрока:")
            print(self.us.board)
            print('')
            print("Доска компьютера:")
            print(self.ai.board)
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.shoting()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.shoting()
            if repeat:
                num -= 1

            if self.ai.board.damaged == 7:
                print("Пользователь выиграл!")
                break

            if self.us.board.damaged == 7:
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.cycle()


g = Game()
g.start()
