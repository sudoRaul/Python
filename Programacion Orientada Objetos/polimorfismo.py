
class gato():
    def hablar(self):
        print("MIAU")
        
class perro():
    def hablar(self):
        print("GUAU")
        
def escucharMascots(animal):
    animal.hablar()
    
if __name__ == "__main__":
    g = gato()
    p = perro()
    escucharMascots(g)
    escucharMascots(p)