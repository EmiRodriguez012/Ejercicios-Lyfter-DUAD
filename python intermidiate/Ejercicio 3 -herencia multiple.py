class Fighter():
    def __init__(self,name,weight, height):
        self.name = name
        self.weight= weight
        self.height = height

    def show_stats(self):
        print(f"fighters name: {self.name}")
        print(f"fighters weight: {self.weight}")
        print(f"fighters height: {self.height}")

class Boxer(Fighter):

    def punch(self):
        print("Right, Left Jab!")

class KickBoxer(Fighter):

    def kick(self):
        print("Kick!")

class Grappler(Fighter):
    
    def grapple(self):
        print("Takedown!")

class MartialArtist(Boxer, KickBoxer, Grappler):
    pass

fighter = MartialArtist("Josue", "80", "1.80")

fighter.show_stats()
fighter.kick()
fighter.punch()
fighter.grapple()