#!python3
"""
Create a function that finds the missing side in a right triangle.
3 input parameters:
float: one side
float: another side
boolean: indicates whether one of the sides is the hypotenuse

return: float length of the missing side

Sample assertions:
assert hypotenuse(12,5,False) == 13
assert hypotenuse(5,3,True) == 4
(2 points)
"""
def hypotenuse(a, b, values):
    if values == True:
        if a > b:
            hyp = (a ** 2 - b ** 2) ** 0.5
        elif b > a:
            hyp = (b ** 2 - a ** 2) ** 0.5
    elif values == False:
        hyp = (a ** 2 + b ** 2) **0.5
    return hyp

assert hypotenuse(5,3,True) == 4