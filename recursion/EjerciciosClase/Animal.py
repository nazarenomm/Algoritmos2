class Animal():
    def __init__(self):
        pass
    
    def hablar(self):
        pass
    
class Perro(Animal):
    def __init__(self):
        super().__init__()
        
    def hablar(self):
        print("guau")
        
class Gato(Animal):
    def __init__(self):
        super().__init__()
        
    def hablar(self):
        print("miau")
        
        
animal = Animal()
animal.hablar()
