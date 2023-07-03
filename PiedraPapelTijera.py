'''
Juego de Piedra, PAPEL O TIJERA, donde se le pregunta al usuraio la cantidad de rondas que se desea jugar y funcion como
los tie break de tennis donde si por ejemplo, se juega al mejor de 7 y van empatando 6-6 automaticamente se juagara al mejor
de 8. Para ganar siempre debe haber una diferencia de 2 puntos. Hay 2 programa, uno para logica con strings (palabras) y 
otra con logica numerica (enteros) 
'''
import random

print("Juego de Piedra, Papel o Tijera")

Options = ("Piedra", "Papel", "Tijera")
round = 1
user_wins = 0
computer_wins = 0
total_rounds = int(input("Escoja la cantidad de rondas que quiere jugar: "))


while True:
    print("*" * 10)
    print("Round: ", round)
    print("*" * 10)
    print("Se jugara al mejor de ",total_rounds," rondas")
    
    pc = random.choice(Options)
    
    Usuario = input("Elija una opcion: \nPiedra, Papel, Tijera => ")
    Usuario = Usuario.capitalize()

    def Resultados():
        print(f"Escogiste: {Usuario}")
        print(f"La PC escogio: {pc}")

    if Usuario not in Options:
        print("Escoja una Opcion Valida")
        continue

    if Usuario in Options:
        Resultados()
        if Usuario == pc:
            print("Empataron")
        elif (Usuario == "Piedra" and pc == "Tijera") or (Usuario == "Papel" and pc == "Piedra") or (Usuario == "Tijera" and pc == "Papel"):
            print("Ganaste")
            user_wins += 1
        else:
            print("Perdiste")
            computer_wins += 1
    
    if (user_wins == total_rounds -1) and computer_wins == total_rounds - 1:
        total_rounds += 1
    

    print("User wins => ", user_wins)
    print("Computer wins => ", computer_wins)


    if computer_wins == total_rounds:
        print("\nLa Computadora GANO")
        break

    if user_wins == total_rounds:
        print("\nEl Usuario GANO")
        break

    round += 1


print("*" * 50)

def Opciones(Respuesta):
    if Respuesta == 1:
        return "Piedra"
    elif Respuesta == 2:
        return "Papel"
    elif Respuesta == 3:
        return "Tijera"
    else:
        return "Escriba una de las opciones correctas"

def Resultados():
    print(f"Escogiste: {Opciones(Usuario)}")
    print(f"La PC escogio: {Opciones(pc)}")

total_rounds = int(input("Escoja la cantidad de rondas que quiere jugar: "))
user_wins = 0
computer_wins = 0
round = 1


while True:

    print("*" * 10)
    print("Round: ", round)
    print("*" * 10)
    print("Se jugara al mejor de ",total_rounds," rondas")

    Usuario = int(input("Escoja una de las opciones: \n1 Piedra \n2 Papel \n3 Tijera \n=>"))
    pc = random.randint(1,3)


    if Usuario == pc:
        Resultados()
        print("Empataron")
    elif Usuario > pc or (Usuario == 1 and pc == 3):
        Resultados()
        print("Ganaste")
        user_wins += 1
    else:
        Resultados()
        print("Perdiste")
        computer_wins += 1
    
    print("User wins => ", user_wins)
    print("Computer wins => ", computer_wins)


    if computer_wins == total_rounds:
        print("\nLa Computadora GANO")
        break

    if user_wins == total_rounds:
        print("\nEl Usuario GANO")
        break

    if (user_wins == total_rounds -1) and computer_wins == total_rounds - 1:
        total_rounds += 1

    round += 1