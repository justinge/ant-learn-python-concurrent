class Animal():
    def say(self):
        pass


class Dog(Animal):
    def say(self):
        print("i am a dog")


animal = Dog()
animal.say()
