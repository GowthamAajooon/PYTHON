class TTF:
    def __init__(self,total):
        self._total = total
    @property
    def total(self):
        return self._total
    @total.setter
    def total(self,t):
        self._total = t
d = TTF(250)
print(d.total)
d.total = 500
print(d.total)
