class Human:
    default_name = 'Popo'
    default_age = 99

    def __init__(self, name=default_name, age=default_age):
        self.name, self.age, = name, age
        self.__money = 0
        self.__house = None

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, num):
        self.__money = num

    @property
    def house(self):
        return self.__house

    @house.setter
    def house(self, num):
        self.__house = num

    def info(self):
        return f"Имя {self.name}, возраст {self.age}, деньги {self.money}, дом {self.house}"

    @staticmethod
    def default_info():
        return Human.default_name, Human.default_age

    def __make_deal(self, house, price):
        self.house = house
        self.money -= price

    def get_makedeal(self, house, price):
        return self.__make_deal(house, price)

    def earn_money(self, quantity):
        self.money += quantity

    def buy_house(self, house, discount=0):
        if self.money > house.final_price(discount):
            self.get_makedeal(house, house.final_price(discount))
            return "Покупка совершена"
        return "Недостатчно средств"


class House:
    def __init__(self, area, price):
        self._area, self._price = area, price

    def final_price(self, discount=0):
        return self._price - discount


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        self.price = price
        super().__init__(SmallHouse.default_area, price)


print(Human.default_info())
Peter = Human("Peter", 20)
print(Peter.info())
Dom = SmallHouse(100)
print(Peter.buy_house(Dom, 20))
Peter.earn_money(5000)
print(Peter.info())
print(Peter.buy_house(Dom))
print(Peter.info())
