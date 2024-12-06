from random import randint
import arcade

class Insects:
    #задаем атрибуты насекомого (имя, еда, чувство сытости)
    def __init__(self):
        self.name = "кузнечик"
        self.food = randint(50, 100)
        self.hungry = randint(40, 100)
        self.days = 0

    def new_day(self):
        self.days += 1

    #после еды увеличиваем/уменьшаем нужные атрибуты
    def eat(self):
        self.hungry += 20
        self.food -= 10

    #после поиска еды уменьшаем/увеличиваем нужные атрибуты
    def find_food(self):
        self.hungry -= 20
        self.food += 20

#унаследуем класс пчелы от класса насекомых
class Bee(Insects):

    #задаем атрибуты пчелы (количество меда, помимо остальных атрибутов)
    def __init__(self, name):
        super().__init__()
        self.honey = randint(50, 90)
        self.name = name

    #после сбора меда увеличиваем/уменьшаем нужные атрибуты
    def collecting_honey(self):
        self.hungry -= 20
        self.food += 20

    #основной цикл
    def live(self):
        living = True
        if self.hungry <= 0:
            print(f'{self.name} died :('f"  live {self.days} days")
            living = False
            return living
        self.new_day()
        action = randint(1, 3)
        if self.hungry < 4:
            if self.food == 0:
                self.find_food()
            else:
                self.eat()
        else:
            if action == 1:
                self.collecting_honey()
            elif action == 2:
                self.eat()
            else:
                self.find_food()
        return living

    def __str__(self):
        return (f"{self.name},{self.honey},{self.hungry},{self.food},{self.days}")


bee = Bee(name="Июль")
for i in range(30):
    if not bee.live():
        break
    print(bee)
#пчела живет 30 дней (если она погибает, то итерации заканчиваются)