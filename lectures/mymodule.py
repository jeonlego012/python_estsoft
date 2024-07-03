def test():
    print("Hello world")


class ParentMyUtil:
    val1 = 123
    __val2 = 456

    def __init__(self, default_val):
        self.default_val = default_val

    def __del__(self):
        print('''class 'PMyUtil' deleted''')

    def Test(self):
        print('PC`Hello World')


class ChildMyUtil(ParentMyUtil):
    def __init__(self, default_val):
        super().__init__(default_val)
        self.default_val = default_val

    def __del__(self):
        print('''class 'CMyUtil' deleted''')

    def Test(self):
        print('CC`Hello World')
