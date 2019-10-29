class Robot(object):
    def __init__(self):
        self.reset()
    def reset(self):
        import string, random
        a = ''.join([random.choice(string.ascii_uppercase) for i in range(2)])
        b = ''.join([random.choice(string.digits) for i in range(3)])
        return a+b