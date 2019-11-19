import string, random

class Robot(object):

    def __init__(self):
        self.reset()

    def reset(self):
        names = []
        a = ''.join([random.choice(string.ascii_uppercase) for i in range(2)])
        b = ''.join([random.choice(string.digits) for i in range(3)])
        name = a+b
        if name not in names:
            return name
        else:
            self.reset()

    def __del__(self):
        self.reset()