class Ice:
    def getName(self):
        return self.name

    def __str__(self):
        return self.name+", "+self.taste+", "+self.wafer


class Choco(Ice):
    def __init__(self):
        self.name = "SuperChoco"
        self.taste = "chocolate"
        self.wafer ="danish"

class Vanilla(Ice):
    def __init__(self):
        self.name = "Standard"
        self.taste = "vanilla"
        self.wafer ="classic"

class Nut(Choco):
    def __init__(self):
        Choco.__init__(self)
        self.name='ChocoNut'
        self.taste = "nut+chocolate"


class Factory:
    def makeIce(self, kind):
        if kind=='choco':
            return Choco()
        elif kind=='vanil':
            return Vanilla()

f=Factory()
print(f.makeIce('choco'))
print(f.makeIce('vanil'))