class Pet:
    def __init__(self, name, type, lvl):
        self.name = name
        self.type = type
        self.lvl = lvl

    def attack(self):
        print("I attack you")

p = Pet("Hehe", "fight", 34)
print(p.name)
print(p.type)
print(p.lvl)
p.attack()