class SquareIterator:
    def __init__(self, max_number):
        self.n = 0
        self.max = max_number
 def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = self.n ** 2
            self.n += 1
            return result
            else:
            raise StopIteration

# Usage
for num in SquareIterator(5):
    print(num)  # Output: 0, 1, 4, 9, 16, 25
  