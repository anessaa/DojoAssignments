class MathDojo(object):
    def __init__(self):
        self.total = 0

    def add(self, *args):
        for a in range(0,len(args)):
            if type(args[a]) is list or type(args[a]) is tuple:
                for j in args[a]:
                    self.total += j
            else:
                self.total += args[a]
        return self

    def subtract(self, *args):
        for a in range(0,len(args)):
            if type(args[a]) is list or type(args[a]) is tuple:
                for j in args[a]:
                    self.total -= j
            else:
                self.total -= args[a]
        return self

    def result(self):
        print self.total

md = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result()
print md

