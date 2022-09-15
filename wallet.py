class Purse:
    def __init__(self, valuta, name="Unknown"):
        self.money=0.00
        self.valuta=valuta
        self.name=name

    def top_up_balance(self,howmoney):
        self.money=self.money+howmoney

    def top_down_balance(self, howmoney):
        if self.money-howmoney<0:
            print("pietrukst naudas maka")
            raise ValueError ("pietrukst naudas")
        self.money=self.money-howmoney

    def info(self):
        print("makā, kura ipasnieks ir ",self.name, "atrodas ",self.money, self.valuta,)

    def __del__(self):
        print("maks izdzests")
        #return self.money

y=Purse("USD")
x=Purse("EUR", "Bill")
x.money=int(input("ievadiet cik daudz naudas ir maka "))
money1=int(input("ievadiet cik nopelnijat "))
money2=int(input("ievadiet cik iznemat  "))
x.top_up_balance(money1)
x.top_down_balance(money2)

y.top_up_balance(300)
x.info()
y.info()
#x.money=100
#print(y.info())
#print(x.info())