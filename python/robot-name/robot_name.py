import string, random

class Robot:

    def __init__(self):
        self.name = self.reset()

    def reset(self):
        random.seed()
        names = []
        a = ''.join(random.choices(string.ascii_uppercase, k=2))
        b = ''.join(random.choices(string.digits, k=3))
        self.name = a+b
        if self.name not in names:
            names.append(self.name)
            return self.name
        else:
            self.reset()
