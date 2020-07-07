class RangeFloatIterator:
    counter = 0

    def __iter__(self):
        return self

    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0.0
            self.end = args[0]
            self.step = 1.0
            self.counter = self.start
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1.0
            self.counter = self.start

        elif len(args) == 3:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]
            self.counter = self.start

    def __next__(self):
        if self.counter <= self.end:
            self.counter += self.step
            return self.counter
        else:
            raise StopIteration


frange = RangeFloatIterator(3, 50, 0.7)

for i in frange:
    print(i)
