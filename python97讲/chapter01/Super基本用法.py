class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


b = B()
