class box:
    def __init__(self):
    	self.__apple = 0

    @property
    def apple(self):
        return self.__apple

    @apple.setter
    def apple(self, Ap):
        self.__apple = Ap

Box = box()
Box.apple = 5
print(f'사과가 상자에 {Box.apple}개 들어있다.')
