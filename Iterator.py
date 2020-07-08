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
        if self.counter < self.end:
            self.counter += self.step
            return self.counter-self.step
        else:
            raise StopIteration


assert(list(RangeFloatIterator(5)) == [0.0, 1.0, 2.0, 3.0, 4.0])
assert(list(RangeFloatIterator(5)) == [0, 1, 2, 3, 4])
assert(list(RangeFloatIterator(2, 5.5, 1.5)) == [2.0, 3.5, 5.0])
assert(list(RangeFloatIterator(0, 2, 1)) == [0.0, 1.0])
assert(list(RangeFloatIterator(1, 6)) == [1.0, 2.0, 3.0, 4.0, 5.0])
assert(list(RangeFloatIterator(0, 0)) == [])
assert(list(RangeFloatIterator(100, 0)) == [])


