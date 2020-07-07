class RangeFloatIterator:
    counter = 0

    def __iter__(self):
        return self

    def __init__(self, start, end=None, step=1.0):
        self.step = step
        self.start = start
        self.end = end
        if self.end is not None:
            self.start, self.end = start, end
        else:
            self.start, self.end = 0.0, start

        self.counter = self.start

    def __next__(self):
        if self.counter <= self.end-self.step:
            self.counter += self.step
            return self.counter-self.step
        else:
            raise StopIteration


frange = RangeFloatIterator(5, 10, 1.5)

for i in frange:
    print(i)

assert(list(RangeFloatIterator(5)) == [0.0, 1.0, 2.0, 3.0, 4.0])

