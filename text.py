class Aoo:
    def __init__(self):
        self.value = 2


class Boo:
    def __init__(self):
        self.alpha = Aoo()


b = Boo()
print(b.alpha.value)
a = b.alpha
a.value = 3
print(b.alpha.value)