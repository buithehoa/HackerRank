class Difference:
    def __init__(self, elements):
        self.__elements = elements
        self.maximumDifference = 0

    def computeDifference(self):
        self.__elements.sort()

        self.maximumDifference = self.__elements[len(self.__elements) - 1] - self.__elements[0]

if __name__ == "__main__":
    _ = input()
    a = [int(e) for e in input().split(' ')]

    d = Difference(a)
    d.computeDifference()

    print(d.maximumDifference)
