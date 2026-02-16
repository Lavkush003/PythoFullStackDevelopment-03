
class Dog:
    def set_name(self, name):
        self.name=name
    def bark(self):
        print(f"{self.name} says Bhoo")
dog1 = Dog()
dog1.set_name("Tomy")
dog2 = Dog()
dog2.set_name("Dogesh bhai")
dog1.bark()
dog2.bark()