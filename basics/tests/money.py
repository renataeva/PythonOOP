class Money:
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents
        self._total_cents = self.dollars*100 + cents

    @property
    def dollars(self):
        return self._dollars

    @dollars.setter
    def dollars(self, new_dollars):
        self._dollars = new_dollars

    @property
    def total_cents(self):
        return self._total_cents

    @total_cents.setter
    def total_cents(self, new_cents):
        if new_cents < 0:
            print("Error dollars")
            return
        self._total_cents = self._dollars * 100 + self._cents + new_cents

    def __str__(self):
        return f"{self.dollars}.{self.cents}"

    @property
    def cents(self):
        return self._cents



cash = Money(2, 80)
cash.total_cents = 8

print(cash)
