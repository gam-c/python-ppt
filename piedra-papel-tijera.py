nombre1 = input("Como se llama el Jugador 1?: ")
nombre2 = input("Como se llama el Jugador 2?: ")

jugador1 = input("Hola Jugador1! Que eliges? Piedra, Papel o Tijeras?: ")
jugador2 = input("Hola Jugador2! Que eliges? Piedra, Papel o Tijeras?: ")

condicion1 = jugador1 == "piedra" and jugador2 == "tijera"
condicion2 = jugador1 == "papel" and jugador2 == "piedra"
condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

if jugador1 == jugador2:
    print("Empate!!")
elif condicion1 or condicion2 or condicion3:
    print('Ha ganado:', nombre1)
else:
    print('Ha ganado:', nombre2)