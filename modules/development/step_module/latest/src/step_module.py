class BaseClass:
    def __init__(self, context, name=None):
        self.context = context
        self.name = name


class Echo(BaseClass):
    def __init__(self, name=None):
        self.name = name

    def do(self, x):
        print("Echo:", self.name, x)
        return x+3