import random
f = open('puntaje.txt', 'a', encoding='utf8')
for _ in range(1,4):
    user_actions = input("Seleccione (piedra-papel-tijera)")
    possible_actions = ["piedra", "papel", "tijera"]
    computer_action = random.choice(possible_actions)
    #print(computer_action)
    print("\nTú elegiste", user_actions, ", la computadora eligió", computer_action, "\n")
    if user_actions==computer_action:
        print("Empate !", user_actions, " . Ambos Ganaron !")
        f.write("Empate. \n")
    elif user_actions=="piedra" and computer_action=="papel":
        print("Ganó la computadora . \n")
        f.write("Ganó la computadora. \n")
    elif user_actions== "piedra" and computer_action == "tijera":
        print("Ganó el usuario . \n")
        f.write("Ganó el usuario. \n")
    elif user_actions=="papel" and computer_action=="piedra":
        print("Ganó el usuario . \n")
        f.write("Ganó el usuario. \n")
    elif user_actions== "papel" and computer_action == "tijera":
        print("Ganó la computadora . \n")
        f.write("Ganó la computadora. \n")
    elif user_actions=="tijera" and computer_action=="piedra":
        print("Ganó la computadora . \n")
        f.write("Ganó la computadora. \n")
    elif user_actions== "tijera" and computer_action == "papel":
        print("Ganó el usuario . \n")
        f.write("Ganó el usuario. \n")
    else:
        print("Error seleccione bien !")
        


   