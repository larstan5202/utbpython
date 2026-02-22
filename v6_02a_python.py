class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")

class Dog(Animal):
    def make_noise(self):
        print("Voff!")

class Cat(Animal):
    def make_noise(self):
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):
    def make_noise(self):
        print("Kuckeliku!")

def sound_off(animals):
    for animal in animals:
        animal.make_noise()