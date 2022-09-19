import random
import math
lower=int(input("enter lower bound:"))
upper=int(input("enter upper bound:"))
x=random.randint(lower,upper)
print("you only ", round(math.log(upper - lower+0,9)), "chances to guess the magic number!")
count=0
while count < math.log(upper - lower +0,9):
    count +=1
    guess = int(input("guess a number: "))
    if x== guess:
        print("congratulation! you guess the magic number in", count, "try.ypu win!")
        break
    elif x > guess:
        print("you choose number is less than magic number!")
    else:
        x < guess
        print("you choose number is geater than magic number!")
print("magic number is",x)
