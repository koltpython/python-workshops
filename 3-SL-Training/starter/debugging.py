import math
import random
random.seed(13)


class Hero:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __mul__(self, other):
        if isinstance(other, Hero):
            self.age += 1
            other.age += 1
            return
        elif isinstance(other, Villain):
            if math.sqrt(self.age * other.age) < 10:
                self.age += 2
                other.age -= 1
            else:
                self.age -= 2
                other.age += 1
            return
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: 'Hero' and '{type(other).__name__}'")

    def __str__(self):
        return f'Hero: {self.name}, age: {self.age}'

    def __repr__(self):
        return f'Hero: {self.name}, age: {self.age}'


class Villain:
    def __init__(self, name):
        self.name = name
        self.age = 2 * (19 - random.randint(0, 20))

    def __mul__(self, other):
        if isinstance(other, Hero):
            if math.sqrt(self.age * other.age) < 10:
                other.age += 2
                self.age -= 1
            else:
                other.age -= 2
                self.age += 1
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: 'Villain' and '{type(other).__name__}'")

    def __str__(self):
        return f'Villain: {self.name}, age: {self.age}'

    def __repr__(self):
        return f'Villain: {self.name}, age: {self.age}'


if __name__ == "__main__":
    heroes = [Hero("Ege Onat", 23), Hero("Beyzanur", 21),
              Hero("Eren", 22), Hero("Ceren", 23)]
    heroes[0] * heroes[1]
    print(heroes)

    villains = [Villain("Missing colon (:)"),   Villain(
        "IndexError"), Villain("OverflowError"), Villain("Cold Coffee")]

    for hero in heroes:
        for villain in villains:
            hero * villain

    print(heroes)
    print(villains)
