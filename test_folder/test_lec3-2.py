import pytest
import lec3_strings_algos as lec
import math

####################
## EXAMPLE: while loops and strings
## CHALLENGE: rewrite while loop with a for loop
####################
def while_to_for():
    an_letters = "aefhilmnorsxAEFHILMNORSX"
    word = input("I will cheer for you! Enter a word: ")
    times = int(input("Enthusiasm level (1-10): "))

    i = 0
    for i in range(len(word)):
        char = word[i]
        if char in an_letters:
            print("Give me an " + char + "! " + char)
        else:
            print("Give me a  " + char + "! " + char)
    print("What does that spell?")
    for i in range(times):
        print(word, "!!!")

#test for approximate_root()
def approximate_root_tests():
    assert abs(lec.approximate_root(27, 0.01)[1] - 3) < 0.01
    assert abs(lec.approximate_root(8, 0.001)[1] - 2) < 0.001
    assert lec.approximate_root(10000, 1e-10)[1] == -1
    print("tests passed!!")

approximate_root_tests()

