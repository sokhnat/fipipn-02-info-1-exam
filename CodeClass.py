from enum import Enum

The_Boost = {"mango": 1.5, "orange": 2, "guajana": 1}
The_Fresh = {"apples": 3, "ginger": 1, "lemon": 1}
The_Fusion = {"guava": 1, "pineaple": 0.25, "banana": 0.5}
The_Detox = {"carrots": 3, "celery stick": 1, "beetroot": 1}


class TypeJuice(Enum):
    The_Boost = 0
    The_Fresh = 1
    The_Fusion = 2
    The_Detox = 3

class TypeSize(Enum):
    Small = 0
    Medium = 1
    Large = 2

class Barmaid():
    _listJuice = list()
    _listSize = list()
    _JuiceSelected = None
    _SizeSelected = None
    _paid = False

    @property
    def bill(self):
        total = 0
        const = 0.5
        for i in range(3):
            if self._SizeSelected.value == i:
                if self._JuiceSelected == TypeJuice.The_Boost:
                        total = 5.0 + const * i

                if self._JuiceSelected == TypeJuice.The_Fresh:
                        total = 4.0 + const * i

                if self._JuiceSelected == TypeJuice.The_Fusion:
                        total = 5.0 + const * i

                if self._JuiceSelected == TypeJuice.The_Detox:
                        total = 3.5 + const * i

        return total

    @property
    def isCancelled(self):
        return self._JuiceSelected == None and self._SizeSelected == None

    @property
    def estValide(self):
        return self._seanceSelectionnee != None and len(self._billetsSelectionnes) > 0

    @property
    def paid(self):
        return self._paid


    def __init__(self):
        self._listJuice = [TypeJuice.The_Boost, TypeJuice.The_Fresh, TypeJuice.The_Fusion, TypeJuice.The_Detox]
        self._listSize = [TypeSize.Small, TypeSize.Medium, TypeSize.Large]


    def JuiceAvailable(self):
        print("Juice available : ")
        for juice in self._listJuice:
            print(juice.name)
        return self._listJuice

    def SizeAvailable(self):
        print("Size available : ")
        for size in self._listSize:
            print(size.name)
        return self._listSize


    def selectJuice(self, juice):
        print("Juice selected: ", juice)
        self._JuiceSelected = juice
        return True

    def selectSize(self, size):
        print("Size selected: ", size)
        self._SizeSelected = size
        return True


    def validate(self):
        print("Order validate, total=%d Euros" % self.bill)
        return True

    def CancelOrder(self):
        self._JuiceSelected = list()
        self._SizeSelected = list()
        print("Order cancelled")

    def pay(self, sum):
        remain = sum - self.bill
        if remain < 0:
            print("The bill is not paid, remain %d euros" % ((-1)*remain))
            return (False, remain)
        else:
            print("The order is successfully paid")
            return (True, remain)

############################test unitaire###########################################


if __name__ == '__main__':

    # init barmaid
    barmaid = Barmaid()

    # consult juices
    juices = barmaid.JuiceAvailable()

    # consult sizes
    sizes = barmaid.SizeAvailable()

    # select juice
    juice = juices.pop(2)

    # select Size
    size = sizes.pop(2)

    barmaid.selectJuice(juice)
    barmaid.selectSize(size)

    # validate
    barmaid.validate()

    # payer
    (Paid, remainder) = barmaid.pay(5)
    print(barmaid.bill)