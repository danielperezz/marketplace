
def standalone_handler(x):
    print(f"I'm a stand-alone handler and my output is: {x+4}")
    return x+4

class DummyStep:
    """ this is a dummy test for testing purpose"""
    def __init__(self, name=None, bool_param=False):
        self.name = name
        self.bool_param = bool_param

    def do(self, x):
        print(f"My name is {self.name} and my output is: {x+3}")
        class_args_ok = "yes" if self.bool_param else "no"
        print(f"Successfully accessed bool_param: {class_args_ok}")
        return x+3

    def another_do(self, x):
        print(f"I'm another class handler and my another output is: {x+5}")
        class_args_ok = "yes" if self.bool_param else "no"
        print(f"Successfully accessed bool_param: {class_args_ok}")
        return x+5