class Animal:
    def __init__(self,name: str,sound: str):
        self.name = name
        self.sound =sound

    def make_food(self):
        print(f"{self.name},каже{self.sound}")

    def feed(self,food:str):
        print(f"{self.name}кушает{food}")

    def __str__(self):
        return f"{self.__class__.__name__}'{self.name}'"

class Cow(Animal):

    def __init__(self, name: str,):
        super().__init__(name,"мууууууу")

class Sheep(Animal):
    def __init__(self, name: str,):
        super().__init__(name,"БЕЕЕЕЕЕЕ")

class Chicken(Animal):
    def __init__(self, name: str,):
        super().__init__(name,"КО-ко-ко")

    def feed(self,food:str):
        print(f"{self.name},кушает{food}, та знесла яйце")


if __name__ =="__main__":
    print("ферма работает\n")
    cow =Cow("Лола")
    sheep =Sheep("Лайка")
    chicken = Chicken("Денди")

    animals =[cow,sheep.chicken]
    for animal in animals:
        print(f"тварина:{animal}")
        animal.make_sound()
        animal.feed("зерно")


