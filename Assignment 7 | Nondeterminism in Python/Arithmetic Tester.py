class Expression:
    def __init__(self):
        pass

    def __repr__(self):
        return str(self)

class Number(Expression):
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return isinstance(other, Number) and self.value == other.value

    def __hash__(self):
        return self.value
    
class Binop(Expression):
    def __init__(self, left, right, op_string):
        super().__init__()
        self.left = left
        self.right = right
        self.op_string = op_string

    def __str__(self):
        return "({} {} {})".format(
            str(self.left),
            self.op_string,
            str(self.right))

    def __eq__(self, other):
        return (isinstance(other, Binop) and
                self.op_string == other.op_string and
                self.left == other.left and
                self.right == other.right)

    def __hash__(self):
        return hash(self.left) + hash(self.op_string) + hash(self.right)
    
class Plus(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "+")

class Minus(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "-")

class Mult(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "*")

class Negate(Expression):
    def __init__(self, subexpression):
        super().__init__()
        self.subexpression = subexpression

    def __str__(self):
        return "(- {})".format(str(self.subexpression))

    def __eq__(self, other):
        return isinstance(other, Negate) and self.subexpression == other.subexpression

    def __hash__(self):
        return 1 + hash(self.subexpression)
    
# makeTest: Bound
# Returns an Expression.  Should work the same as with assignment 6, only
# with Python.  You can use `yield` in Python to return a value from a generator,
# which additionally pauses execution until the next element is requested from
# the generator.
def makeTest(bound):
    # yield is here only to make the tests runnable; you'll need to remove this
    yield None

# makeTestWithNums: Bound, ListOfIntegers
# Returns an Expression.  Should work the same as with assignment 6.
def makeTestWithNums(bound, input_list):
    # yield is here only to make the tests runnable; you'll need to remove this
    yield None

def makeTestTest(bound, expected_set):
    received_set = set()
    for test in makeTest(bound):
        received_set.add(test)
    if received_set == expected_set:
        print("makeTest({}): pass".format(str(bound)))
    else:
        print("makeTest({}): FAIL".format(str(bound)))
        print("\texpected: {}".format(str(expected_set)))
        print("\treceived: {}".format(str(received_set)))
              
def testMakeTest():
    makeTestTest(0, set([Number(0)]))
    makeTestTest(1, set([Number(0),
                         Plus(Number(0),Number(0)),
                         Minus(Number(0),Number(0)),
                         Mult(Number(0),Number(0)),
                         Negate(Number(0))]))
    makeTestTest(2, set([Number(0),
                         Plus(Number(0),Number(0)),
                         Plus(Number(0),Plus(Number(0),Number(0))),
                         Plus(Number(0),Minus(Number(0),Number(0))),
                         Plus(Number(0),Mult(Number(0),Number(0))),
                         Plus(Number(0),Negate(Number(0))),
                         Plus(Plus(Number(0),Number(0)),Number(0)),
                         Plus(Plus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Plus(Plus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Plus(Plus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Plus(Plus(Number(0),Number(0)),Negate(Number(0))),
                         Plus(Minus(Number(0),Number(0)),Number(0)),
                         Plus(Minus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Plus(Minus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Plus(Minus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Plus(Minus(Number(0),Number(0)),Negate(Number(0))),
                         Plus(Mult(Number(0),Number(0)),Number(0)),
                         Plus(Mult(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Plus(Mult(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Plus(Mult(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Plus(Mult(Number(0),Number(0)),Negate(Number(0))),
                         Plus(Negate(Number(0)),Number(0)),
                         Plus(Negate(Number(0)),Plus(Number(0),Number(0))),
                         Plus(Negate(Number(0)),Minus(Number(0),Number(0))),
                         Plus(Negate(Number(0)),Mult(Number(0),Number(0))),
                         Plus(Negate(Number(0)),Negate(Number(0))),
                         Minus(Number(0),Number(0)),
                         Minus(Number(0),Plus(Number(0),Number(0))),
                         Minus(Number(0),Minus(Number(0),Number(0))),
                         Minus(Number(0),Mult(Number(0),Number(0))),
                         Minus(Number(0),Negate(Number(0))),
                         Minus(Plus(Number(0),Number(0)),Number(0)),
                         Minus(Plus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Minus(Plus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Minus(Plus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Minus(Plus(Number(0),Number(0)),Negate(Number(0))),
                         Minus(Minus(Number(0),Number(0)),Number(0)),
                         Minus(Minus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Minus(Minus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Minus(Minus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Minus(Minus(Number(0),Number(0)),Negate(Number(0))),
                         Minus(Mult(Number(0),Number(0)),Number(0)),
                         Minus(Mult(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Minus(Mult(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Minus(Mult(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Minus(Mult(Number(0),Number(0)),Negate(Number(0))),
                         Minus(Negate(Number(0)),Number(0)),
                         Minus(Negate(Number(0)),Plus(Number(0),Number(0))),
                         Minus(Negate(Number(0)),Minus(Number(0),Number(0))),
                         Minus(Negate(Number(0)),Mult(Number(0),Number(0))),
                         Minus(Negate(Number(0)),Negate(Number(0))),
                         Mult(Number(0),Number(0)),
                         Mult(Number(0),Plus(Number(0),Number(0))),
                         Mult(Number(0),Minus(Number(0),Number(0))),
                         Mult(Number(0),Mult(Number(0),Number(0))),
                         Mult(Number(0),Negate(Number(0))),
                         Mult(Plus(Number(0),Number(0)),Number(0)),
                         Mult(Plus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Mult(Plus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Mult(Plus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Mult(Plus(Number(0),Number(0)),Negate(Number(0))),
                         Mult(Minus(Number(0),Number(0)),Number(0)),
                         Mult(Minus(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Mult(Minus(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Mult(Minus(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Mult(Minus(Number(0),Number(0)),Negate(Number(0))),
                         Mult(Mult(Number(0),Number(0)),Number(0)),
                         Mult(Mult(Number(0),Number(0)),Plus(Number(0),Number(0))),
                         Mult(Mult(Number(0),Number(0)),Minus(Number(0),Number(0))),
                         Mult(Mult(Number(0),Number(0)),Mult(Number(0),Number(0))),
                         Mult(Mult(Number(0),Number(0)),Negate(Number(0))),
                         Mult(Negate(Number(0)),Number(0)),
                         Mult(Negate(Number(0)),Plus(Number(0),Number(0))),
                         Mult(Negate(Number(0)),Minus(Number(0),Number(0))),
                         Mult(Negate(Number(0)),Mult(Number(0),Number(0))),
                         Mult(Negate(Number(0)),Negate(Number(0))),
                         Negate(Number(0)),
                         Negate(Plus(Number(0),Number(0))),
                         Negate(Minus(Number(0),Number(0))),
                         Negate(Mult(Number(0),Number(0))),
                         Negate(Negate(Number(0)))]))

def makeTestWithNumsTest(bound, nums, expected_set):
    received_set = set()
    for test in makeTestWithNums(bound, nums):
        received_set.add(test)
    if received_set == expected_set:
        print("makeTestWithNums({}, {}): pass".format(str(bound), str(nums)))
    else:
        print("makeTestWithNums({}, {}): FAIL".format(str(bound), str(nums)))
        print("\texpected: {}".format(str(expected_set)))
        print("\treceived: {}".format(str(received_set)))

def testMakeTestWithNums():
    makeTestWithNumsTest(0, [1], set([Number(1)]))
    makeTestWithNumsTest(0, [1, 2, 3], set([Number(1),
                                            Number(2),
                                            Number(3)]))
    makeTestWithNumsTest(1, [2], set([Number(2),
                                      Plus(Number(2),Number(2)),
                                      Minus(Number(2),Number(2)),
                                      Mult(Number(2),Number(2)),
                                      Negate(Number(2))]))
    makeTestWithNumsTest(1, [2, 3], set([Number(2),
                                         Number(3),
                                         Plus(Number(2),Number(2)),
                                         Plus(Number(2),Number(3)),
                                         Plus(Number(3),Number(2)),
                                         Plus(Number(3),Number(3)),
                                         Minus(Number(2),Number(2)),
                                         Minus(Number(2),Number(3)),
                                         Minus(Number(3),Number(2)),
                                         Minus(Number(3),Number(3)),
                                         Mult(Number(2),Number(2)),
                                         Mult(Number(2),Number(3)),
                                         Mult(Number(3),Number(2)),
                                         Mult(Number(3),Number(3)),
                                         Negate(Number(2)),
                                         Negate(Number(3))]))
    makeTestWithNumsTest(2, [2], set([Number(2),
                                      Plus(Number(2),Number(2)),
                                      Plus(Number(2),Plus(Number(2),Number(2))),
                                      Plus(Number(2),Minus(Number(2),Number(2))),
                                      Plus(Number(2),Mult(Number(2),Number(2))),
                                      Plus(Number(2),Negate(Number(2))),
                                      Plus(Plus(Number(2),Number(2)),Number(2)),
                                      Plus(Plus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Plus(Plus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Plus(Plus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Plus(Plus(Number(2),Number(2)),Negate(Number(2))),
                                      Plus(Minus(Number(2),Number(2)),Number(2)),
                                      Plus(Minus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Plus(Minus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Plus(Minus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Plus(Minus(Number(2),Number(2)),Negate(Number(2))),
                                      Plus(Mult(Number(2),Number(2)),Number(2)),
                                      Plus(Mult(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Plus(Mult(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Plus(Mult(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Plus(Mult(Number(2),Number(2)),Negate(Number(2))),
                                      Plus(Negate(Number(2)),Number(2)),
                                      Plus(Negate(Number(2)),Plus(Number(2),Number(2))),
                                      Plus(Negate(Number(2)),Minus(Number(2),Number(2))),
                                      Plus(Negate(Number(2)),Mult(Number(2),Number(2))),
                                      Plus(Negate(Number(2)),Negate(Number(2))),
                                      Minus(Number(2),Number(2)),
                                      Minus(Number(2),Plus(Number(2),Number(2))),
                                      Minus(Number(2),Minus(Number(2),Number(2))),
                                      Minus(Number(2),Mult(Number(2),Number(2))),
                                      Minus(Number(2),Negate(Number(2))),
                                      Minus(Plus(Number(2),Number(2)),Number(2)),
                                      Minus(Plus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Minus(Plus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Minus(Plus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Minus(Plus(Number(2),Number(2)),Negate(Number(2))),
                                      Minus(Minus(Number(2),Number(2)),Number(2)),
                                      Minus(Minus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Minus(Minus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Minus(Minus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Minus(Minus(Number(2),Number(2)),Negate(Number(2))),
                                      Minus(Mult(Number(2),Number(2)),Number(2)),
                                      Minus(Mult(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Minus(Mult(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Minus(Mult(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Minus(Mult(Number(2),Number(2)),Negate(Number(2))),
                                      Minus(Negate(Number(2)),Number(2)),
                                      Minus(Negate(Number(2)),Plus(Number(2),Number(2))),
                                      Minus(Negate(Number(2)),Minus(Number(2),Number(2))),
                                      Minus(Negate(Number(2)),Mult(Number(2),Number(2))),
                                      Minus(Negate(Number(2)),Negate(Number(2))),
                                      Mult(Number(2),Number(2)),
                                      Mult(Number(2),Plus(Number(2),Number(2))),
                                      Mult(Number(2),Minus(Number(2),Number(2))),
                                      Mult(Number(2),Mult(Number(2),Number(2))),
                                      Mult(Number(2),Negate(Number(2))),
                                      Mult(Plus(Number(2),Number(2)),Number(2)),
                                      Mult(Plus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Mult(Plus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Mult(Plus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Mult(Plus(Number(2),Number(2)),Negate(Number(2))),
                                      Mult(Minus(Number(2),Number(2)),Number(2)),
                                      Mult(Minus(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Mult(Minus(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Mult(Minus(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Mult(Minus(Number(2),Number(2)),Negate(Number(2))),
                                      Mult(Mult(Number(2),Number(2)),Number(2)),
                                      Mult(Mult(Number(2),Number(2)),Plus(Number(2),Number(2))),
                                      Mult(Mult(Number(2),Number(2)),Minus(Number(2),Number(2))),
                                      Mult(Mult(Number(2),Number(2)),Mult(Number(2),Number(2))),
                                      Mult(Mult(Number(2),Number(2)),Negate(Number(2))),
                                      Mult(Negate(Number(2)),Number(2)),
                                      Mult(Negate(Number(2)),Plus(Number(2),Number(2))),
                                      Mult(Negate(Number(2)),Minus(Number(2),Number(2))),
                                      Mult(Negate(Number(2)),Mult(Number(2),Number(2))),
                                      Mult(Negate(Number(2)),Negate(Number(2))),
                                      Negate(Number(2)),
                                      Negate(Plus(Number(2),Number(2))),
                                      Negate(Minus(Number(2),Number(2))),
                                      Negate(Mult(Number(2),Number(2))),
                                      Negate(Negate(Number(2)))]))
