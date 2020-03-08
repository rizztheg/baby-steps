class Point(x,y):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)
p=Point(3,1)
print(p)
