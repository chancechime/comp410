#!/usr/bin/env python3
#
# ---AST Definition---
#
# There are four kinds of expressions:
#
# 1.) True, represented with `True` (Python Boolean literal)
#
# 2.) False, represented with `False` (Python Boolean literal)
#
# 3.) Logical and, which represents an AND operation between
#     two subexpressions.  This is represented with the `And`
#     class, which has `left` and `right` fields for subexpressions.
#
# 4.) Logical or, which represents an OR operation between
#     two subexpressions.  This is represented with the `Or`
#     class, which has `left` and `right` fields for subexpressions.
#
# A more compact representation of all the above information is shown
# below in a variant of a BNF grammar:
#
# e ∈ Expression ::= True | False | And(e1, e2) | Or(e1, e2)

class Binop:
    def __init__(self, left, right, op_string):
        self.left = left
        self.right = right
        self.op_string = op_string

    def __str__(self):
        return "({} {} {})".format(
            str(self.left),
            self.op_string,
            str(self.right))

class And(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "&&")

class Or(Binop):
    def __init__(self, left, right):
        super().__init__(left, right, "||")

# eval_expr
#
# Takes the following:
# 1.) An expression, according to the AST definition above
#
# Returns:
# A Boolean value (either True or False), corresponding to the result of
# evaluating the expression
#
# Purpose:
# Evaluates a Boolean expression down to a Python Boolean value (either True or False)
#
# You need to implement eval_expr.  To this end, the following hints may be helpful:
# 1.) eval_expr needs to be recursive
# 2.) You can use `expression == True` or `expression == False` to see if the expression
#     is directly `True` or `False`
# 3.) You can use `isinstance(expression, And)` or `isinstance(expression, Or)` to see
#     if the expression is an `And` or `Or` AST node.
# 4.) `True` and `False` act as base cases, and these should produce `True` and
#     `False`, respectively
# 5.) For `And` and `Or`, you can use the built-in `and` and `or` operations.
#     These operate on Python Boolean values (either `True` or `False`)
# 6.) You do not need to write a lot of code; my reference solution is 7 lines long.
#     If you start needing a lot more code than that, ask for help to make sure
#     you're still on-track.
def eval_expr(expression):
    pass

# tests that evaluate to true
true_tests = [And(True, True),
              Or(True, True),
              Or(True, False),
              Or(False, True),
              Or(And(False, True),
                 And(True, True))]

# tests that evaluate to false
false_tests = [And(True, False),
               And(False, True),
               And(False, False),
               Or(False, False),
               And(Or(True, False),
                   Or(False, False))]

def run_tests():
    tests_failed = False
    for test in true_tests:
        if not eval_expr(test):
            print("Failed: {}".format(test))
            print("\tWas false, should have been true")
            tests_failed = True

    for test in false_tests:
        if eval_expr(test):
            print("Failed: {}".format(test))
            print("\tWas true, should have been false")
            tests_failed = True

    if not tests_failed:
        print("All tests passed")

if __name__ == "__main__":
    run_tests()
