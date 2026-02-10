
# plus tout les numeros dans une liste
from ast import operator
from py_compile import main


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
# calculatrice fountionnelle alternative pour les utilisateurs
def main():
    print("Calculator ready!")
    print("1. Additionner des nombres")  
    print("2. Multiplier des nombres")
    print("3. Vérifier si un nombre est pair")
    print("4. Vérifier si cest un entier")
    print("0. Quitter")


    operator = input("Choisissez une option : ")
    if operator == "1":
        nombres = input("Entrez des nombres separes par des espaces : ")
        liste = [float(n) for n in nombres.split()]
        print("Resultat :", addmultiplenumbers(liste))
    elif operator == "2":
        nombres = input("Entrez des nombres separes par des espaces : ")
        liste = [float(n) for n in nombres.split()]
        print("Resultat :", multiplymultiplenumbers(liste))

    elif operator == "3":
        num = float(input("Entrez un nombre : "))
        print("Est-ce pair ?", isiteven(num))

    elif operator == "4":
        num = float(input("Entrez un nombre : "))
        print("Est ce un entier ?", isitaninteger(num))

    elif operator == "0":
        print("Sortie du programme...")

    else:
        print("surement une option invalide, essayez a nouveau.")
        
if __name__ == "__main__":
    main()