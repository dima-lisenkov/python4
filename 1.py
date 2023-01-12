import math
p = list(str(math.pi))
print(p)

def CalculatePi(roundVal):
    somepi = round(math.pi,roundVal)
    pi = str(somepi)
    someList = list(pi)
    return somepi
roundTo = input("Введите число: ")
try:
    roundint = int(roundTo)
    print(CalculatePi(roundint))
except:
    print("это не число")
