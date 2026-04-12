import math

temp = float(input('Probability of Landing on Blue is _ /6 : '))

p_blue = (temp/6)
p_red = float((6 - temp) /2 )
p_yellow = p_red

num1 = ((p_blue *-1) *math.log2(p_blue))
num2 = ((p_red*-1) *math.log2(p_red))
num3 = ((p_yellow*-1) *math.log2(p_yellow))

H = num1 + num2 + num3

def printall():
    print(f"{p_red} is the probability of Landing on red or yellow")
    print('\n')
    print(f"The entropy of the spinner is {H}")

if (temp < 6):
    printall()
else:
    print('Probability must be less than 1')
