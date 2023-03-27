#PROGRAM DEL JUEGO PIEDRA, PAPEL O TIJERAS
import random#LIBRERIA RANDOM 
opcions=("piedra","papel","tijeras")
rondas= 1
usuario_wins=0
computer_wins=0

while True:
  print("*"*10)
  print("ROUND ", rondas)
  print("*"*10)
  print(usuario_wins, "GANADAS DEL USUARIO")
  print(computer_wins, "GANADAS DE LA COMPUTADORA\n")
  
  user_opcion=input("piedra, papel o tijeras: ")
  user_opcion=user_opcion.lower()
  rondas += 1
  #VALIDACION DE OPCIONES 
  if not user_opcion in opcions:#si la opcion del usuario no esta en opciones, se jecuta la instruccion(mensaje)
    print("esa opcion no es valida")
    continue
    
  computer_opcion=random.choice(opcions)#.CHOICE elije al azar un elemento de una lista o tupla 
  
  print("opcion de usuario:", user_opcion)
  print("opcion de computadora:",
        computer_opcion)
  print(" ")
  
  #LOGICA
  if user_opcion == computer_opcion:
    print("empate")
  elif user_opcion == "piedra":
    if computer_opcion == "tijeras":
      print("piedra gana a tijera\nel usuario gana!!!")
      usuario_wins +=1
    else:
      print("el papel gana ala piedra\nel computador gana!!!")
      computer_wins +=1
  elif user_opcion == "papel":
    if computer_opcion == "piedra":
      print("el papel le gana ala piedra\nel usuario gana!!!")
      usuario_wins +=1
    else:
      print("las tijeras le ganan al papel\nel computador gana!!!")
      computer_wins +=1
  elif user_opcion == "tijeras":
    if computer_opcion == "papel":
      print("las tijeras le ganan al papel\nel usuario gana!!!")
      usuario_wins +=1
    else:
      print("la piedra gana alas tijeras\nel computador gana!!!")
      computer_wins +=1

  if computer_wins == 2:
    print("el rotundo ganador es la computadora")
    break
  if usuario_wins == 2:
    print("el rotundo ganador es el usuario")
    break
  
    