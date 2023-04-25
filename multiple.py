class Organism:
    def __init__(self):
        print("Hello Organism")

    def method(self):
        print("Hello method in organism")

class Animal(Organism):
    def __init__(self):
        print("Hello animal")

class Herbivore(Animal):
    def __init__(self):
        print("Hello Herbivore")

    def method(self):
        print("Hello method in Herbivore")

class Carnivore(Animal):
    pass

class Sheep(Herbivore):
    def __init__(self):
        print("Hello sheep")
        #Animal.__init__(self)
        super().__init__()

    def method(self):
        print("Hello method in Sheep")
        super().method()
        # hvis du vil ha organism method then
        Organism.method(self)

class Wolf(Carnivore):
    pass

if __name__ == "__main__":
    sheep = Sheep()
    sheep.method()
    #sprint(isinstance(sheep, Animal))