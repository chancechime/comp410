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
        return "({} {} {})".format(str(self.left), self.op_string, str(self.right))

    def __eq__(self, other):
        return (
            isinstance(other, Binop)
            and self.op_string == other.op_string
            and self.left == other.left
            and self.right == other.right
        )

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

# Start of code

# makeTest: Bound
# Returns an Expression.  Should work the same as with assignment 6, only
# with Python.  You can use `yield` in Python to return a value from a generator,
# which additionally pauses execution until the next element is requested from
# the generator.
def makeTest(bound):
    if bound == 0:
        yield Number(0)
    else:
        yield Number(0)
        for subexpression in makeTest(bound - 1):
            yield Plus(Number(0), subexpression)
            yield Minus(Number(0), subexpression)
            yield Mult(Number(0), subexpression)
            yield Negate(subexpression)
            yield Plus(subexpression, Number(0))
            yield Minus(subexpression, Number(0))
            yield Mult(subexpression, Number(0))
            yield Negate(subexpression)
            for subexpression2 in makeTest(bound - 1):
                yield Plus(subexpression, subexpression2)
                yield Minus(subexpression, subexpression2)
                yield Mult(subexpression, subexpression2)
                yield Negate(subexpression)
                yield Plus(subexpression2, subexpression)
                yield Minus(subexpression2, subexpression)
                yield Mult(subexpression2, subexpression)
                yield Negate(subexpression2)


# makeTestWithNums: Bound, ListOfIntegers
# Returns an Expression.  Should work the same as with assignment 6.
def makeTestWithNums(bound, input_list):
    if bound == 0:
        for num in input_list:
            yield Number(num)
    else:
        for num in input_list:
            yield Number(num)
        for subexpression in makeTestWithNums(bound - 1, input_list):
            for num in input_list:
                yield Plus(Number(num), subexpression)
                yield Minus(Number(num), subexpression)
                yield Mult(Number(num), subexpression)
                yield Plus(subexpression, Number(num))
                yield Minus(subexpression, Number(num))
                yield Mult(subexpression, Number(num))
            yield Negate(subexpression)
        for subexpression1 in makeTestWithNums(bound - 1, input_list):
            for subexpression2 in makeTestWithNums(bound - 1, input_list):
                yield Plus(subexpression1, subexpression2)
                yield Minus(subexpression1, subexpression2)
                yield Mult(subexpression1, subexpression2)
                yield Plus(subexpression2, subexpression1)
                yield Minus(subexpression2, subexpression1)
                yield Mult(subexpression2, subexpression1)
            yield Negate(subexpression1)
            
# End of code


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
    makeTestTest(
        1,
        set(
            [
                Number(0),
                Plus(Number(0), Number(0)),
                Minus(Number(0), Number(0)),
                Mult(Number(0), Number(0)),
                Negate(Number(0)),
            ]
        ),
    )
    makeTestTest(
        2,
        set(
            [
                Number(0),
                Plus(Number(0), Number(0)),
                Plus(Number(0), Plus(Number(0), Number(0))),
                Plus(Number(0), Minus(Number(0), Number(0))),
                Plus(Number(0), Mult(Number(0), Number(0))),
                Plus(Number(0), Negate(Number(0))),
                Plus(Plus(Number(0), Number(0)), Number(0)),
                Plus(Plus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Plus(Plus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Plus(Plus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Plus(Plus(Number(0), Number(0)), Negate(Number(0))),
                Plus(Minus(Number(0), Number(0)), Number(0)),
                Plus(Minus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Plus(Minus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Plus(Minus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Plus(Minus(Number(0), Number(0)), Negate(Number(0))),
                Plus(Mult(Number(0), Number(0)), Number(0)),
                Plus(Mult(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Plus(Mult(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Plus(Mult(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Plus(Mult(Number(0), Number(0)), Negate(Number(0))),
                Plus(Negate(Number(0)), Number(0)),
                Plus(Negate(Number(0)), Plus(Number(0), Number(0))),
                Plus(Negate(Number(0)), Minus(Number(0), Number(0))),
                Plus(Negate(Number(0)), Mult(Number(0), Number(0))),
                Plus(Negate(Number(0)), Negate(Number(0))),
                Minus(Number(0), Number(0)),
                Minus(Number(0), Plus(Number(0), Number(0))),
                Minus(Number(0), Minus(Number(0), Number(0))),
                Minus(Number(0), Mult(Number(0), Number(0))),
                Minus(Number(0), Negate(Number(0))),
                Minus(Plus(Number(0), Number(0)), Number(0)),
                Minus(Plus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Minus(Plus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Minus(Plus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Minus(Plus(Number(0), Number(0)), Negate(Number(0))),
                Minus(Minus(Number(0), Number(0)), Number(0)),
                Minus(Minus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Minus(Minus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Minus(Minus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Minus(Minus(Number(0), Number(0)), Negate(Number(0))),
                Minus(Mult(Number(0), Number(0)), Number(0)),
                Minus(Mult(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Minus(Mult(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Minus(Mult(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Minus(Mult(Number(0), Number(0)), Negate(Number(0))),
                Minus(Negate(Number(0)), Number(0)),
                Minus(Negate(Number(0)), Plus(Number(0), Number(0))),
                Minus(Negate(Number(0)), Minus(Number(0), Number(0))),
                Minus(Negate(Number(0)), Mult(Number(0), Number(0))),
                Minus(Negate(Number(0)), Negate(Number(0))),
                Mult(Number(0), Number(0)),
                Mult(Number(0), Plus(Number(0), Number(0))),
                Mult(Number(0), Minus(Number(0), Number(0))),
                Mult(Number(0), Mult(Number(0), Number(0))),
                Mult(Number(0), Negate(Number(0))),
                Mult(Plus(Number(0), Number(0)), Number(0)),
                Mult(Plus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Mult(Plus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Mult(Plus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Mult(Plus(Number(0), Number(0)), Negate(Number(0))),
                Mult(Minus(Number(0), Number(0)), Number(0)),
                Mult(Minus(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Mult(Minus(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Mult(Minus(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Mult(Minus(Number(0), Number(0)), Negate(Number(0))),
                Mult(Mult(Number(0), Number(0)), Number(0)),
                Mult(Mult(Number(0), Number(0)), Plus(Number(0), Number(0))),
                Mult(Mult(Number(0), Number(0)), Minus(Number(0), Number(0))),
                Mult(Mult(Number(0), Number(0)), Mult(Number(0), Number(0))),
                Mult(Mult(Number(0), Number(0)), Negate(Number(0))),
                Mult(Negate(Number(0)), Number(0)),
                Mult(Negate(Number(0)), Plus(Number(0), Number(0))),
                Mult(Negate(Number(0)), Minus(Number(0), Number(0))),
                Mult(Negate(Number(0)), Mult(Number(0), Number(0))),
                Mult(Negate(Number(0)), Negate(Number(0))),
                Negate(Number(0)),
                Negate(Plus(Number(0), Number(0))),
                Negate(Minus(Number(0), Number(0))),
                Negate(Mult(Number(0), Number(0))),
                Negate(Negate(Number(0))),
            ]
        ),
    )


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
    makeTestWithNumsTest(0, [1, 2, 3], set([Number(1), Number(2), Number(3)]))
    makeTestWithNumsTest(
        1,
        [2],
        set(
            [
                Number(2),
                Plus(Number(2), Number(2)),
                Minus(Number(2), Number(2)),
                Mult(Number(2), Number(2)),
                Negate(Number(2)),
            ]
        ),
    )
    makeTestWithNumsTest(
        1,
        [2, 3],
        set(
            [
                Number(2),
                Number(3),
                Plus(Number(2), Number(2)),
                Plus(Number(2), Number(3)),
                Plus(Number(3), Number(2)),
                Plus(Number(3), Number(3)),
                Minus(Number(2), Number(2)),
                Minus(Number(2), Number(3)),
                Minus(Number(3), Number(2)),
                Minus(Number(3), Number(3)),
                Mult(Number(2), Number(2)),
                Mult(Number(2), Number(3)),
                Mult(Number(3), Number(2)),
                Mult(Number(3), Number(3)),
                Negate(Number(2)),
                Negate(Number(3)),
            ]
        ),
    )
    makeTestWithNumsTest(
        2,
        [2],
        set(
            [
                Number(2),
                Plus(Number(2), Number(2)),
                Plus(Number(2), Plus(Number(2), Number(2))),
                Plus(Number(2), Minus(Number(2), Number(2))),
                Plus(Number(2), Mult(Number(2), Number(2))),
                Plus(Number(2), Negate(Number(2))),
                Plus(Plus(Number(2), Number(2)), Number(2)),
                Plus(Plus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Plus(Plus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Plus(Plus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Plus(Plus(Number(2), Number(2)), Negate(Number(2))),
                Plus(Minus(Number(2), Number(2)), Number(2)),
                Plus(Minus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Plus(Minus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Plus(Minus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Plus(Minus(Number(2), Number(2)), Negate(Number(2))),
                Plus(Mult(Number(2), Number(2)), Number(2)),
                Plus(Mult(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Plus(Mult(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Plus(Mult(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Plus(Mult(Number(2), Number(2)), Negate(Number(2))),
                Plus(Negate(Number(2)), Number(2)),
                Plus(Negate(Number(2)), Plus(Number(2), Number(2))),
                Plus(Negate(Number(2)), Minus(Number(2), Number(2))),
                Plus(Negate(Number(2)), Mult(Number(2), Number(2))),
                Plus(Negate(Number(2)), Negate(Number(2))),
                Minus(Number(2), Number(2)),
                Minus(Number(2), Plus(Number(2), Number(2))),
                Minus(Number(2), Minus(Number(2), Number(2))),
                Minus(Number(2), Mult(Number(2), Number(2))),
                Minus(Number(2), Negate(Number(2))),
                Minus(Plus(Number(2), Number(2)), Number(2)),
                Minus(Plus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Minus(Plus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Minus(Plus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Minus(Plus(Number(2), Number(2)), Negate(Number(2))),
                Minus(Minus(Number(2), Number(2)), Number(2)),
                Minus(Minus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Minus(Minus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Minus(Minus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Minus(Minus(Number(2), Number(2)), Negate(Number(2))),
                Minus(Mult(Number(2), Number(2)), Number(2)),
                Minus(Mult(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Minus(Mult(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Minus(Mult(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Minus(Mult(Number(2), Number(2)), Negate(Number(2))),
                Minus(Negate(Number(2)), Number(2)),
                Minus(Negate(Number(2)), Plus(Number(2), Number(2))),
                Minus(Negate(Number(2)), Minus(Number(2), Number(2))),
                Minus(Negate(Number(2)), Mult(Number(2), Number(2))),
                Minus(Negate(Number(2)), Negate(Number(2))),
                Mult(Number(2), Number(2)),
                Mult(Number(2), Plus(Number(2), Number(2))),
                Mult(Number(2), Minus(Number(2), Number(2))),
                Mult(Number(2), Mult(Number(2), Number(2))),
                Mult(Number(2), Negate(Number(2))),
                Mult(Plus(Number(2), Number(2)), Number(2)),
                Mult(Plus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Mult(Plus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Mult(Plus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Mult(Plus(Number(2), Number(2)), Negate(Number(2))),
                Mult(Minus(Number(2), Number(2)), Number(2)),
                Mult(Minus(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Mult(Minus(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Mult(Minus(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Mult(Minus(Number(2), Number(2)), Negate(Number(2))),
                Mult(Mult(Number(2), Number(2)), Number(2)),
                Mult(Mult(Number(2), Number(2)), Plus(Number(2), Number(2))),
                Mult(Mult(Number(2), Number(2)), Minus(Number(2), Number(2))),
                Mult(Mult(Number(2), Number(2)), Mult(Number(2), Number(2))),
                Mult(Mult(Number(2), Number(2)), Negate(Number(2))),
                Mult(Negate(Number(2)), Number(2)),
                Mult(Negate(Number(2)), Plus(Number(2), Number(2))),
                Mult(Negate(Number(2)), Minus(Number(2), Number(2))),
                Mult(Negate(Number(2)), Mult(Number(2), Number(2))),
                Mult(Negate(Number(2)), Negate(Number(2))),
                Negate(Number(2)),
                Negate(Plus(Number(2), Number(2))),
                Negate(Minus(Number(2), Number(2))),
                Negate(Mult(Number(2), Number(2))),
                Negate(Negate(Number(2))),
            ]
        ),
    )

# Added to run tests
if __name__ == "__main__":
    testMakeTest()
    testMakeTestWithNums()