class Cat(object):
    def say(self):
        print("i am a cat")


class Duck(object):
    def say(self):
        print("i am a duck")


class Dog(object):
    def say(self):
        print("i am a dog")


animal = Cat()
animal.say()

animal_list = [Cat, Duck, Dog]

for animal in animal_list:
    animal().say()
