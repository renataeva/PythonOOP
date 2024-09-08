class Money:
    def __init__(self, dollars, cents):
        self._dollars = dollars
        self._cents = cents
        self._total_cents = self._dollars * 100 + self._cents

    @property
    def dollars(self):
        return self._dollars

    @property
    def cents(self):
        return self._cents

    @property
    def total_cents(self):
        return self._total_cents

    @total_cents.setter
    def total_cents(self, new_cents):
        if new_cents < 0:
            raise ValueError("Total cents cannot be negative")
        self._total_cents = new_cents
        self._dollars, self._cents = divmod(new_cents, 100)

# Example usage
cash = Money(2, 80)
print(cash.total_cents)  # Should print 280
