class Dog:
    def sound(self):
        return "Woof"
    
class Cat:
    def sound(self):
        return "Meow"
    
class Duck:
    def sound(self):
        return "Quack"
    
def make_sound(animal):
    return animal.sound()

dog = Dog()
cat = Cat()
duck = Duck()

print(make_sound(dog))
print(make_sound(cat))
print(make_sound(duck))