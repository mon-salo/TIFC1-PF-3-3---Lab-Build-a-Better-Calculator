
# plus tout les numeros dans une liste
def addmultiplenumbers(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# multiplier tous les numeros dans une liste
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

# vérifier si un nombre est un entier
def isitaninteger(num):
    return isinstance(num, int)

# vérifier si un nombre est pair
def isiteven(num):
    if not isitaninteger(num):
        return False
        #si ce n'est pas un entier, on ne peut pas dire qu'il est pair
    return num % 2 == 0
# c'est donne pour le prof Moi
def main():
    print("Calculator ready!")

if __name__=="__main__":
  main()