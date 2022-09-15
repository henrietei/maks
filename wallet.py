class Purse:
    def __init__(self, valuta, name="Unknown"):
        self.money=0.00
        self.valuta=valuta
        self.name=name

    def top_up_balance(self, howmoney):
        self.money=self.money+howmoney

    def info(self):
        return self.money

y=Purse("USD")
x=Purse("EUR")
x.top_up_balance(100)

#x.money=100
print(y.info())
print(x.info())