def removeSpecialCharacters(string):
    cleanText = ""
    alphabet = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g',
        'h', 'i', 'j', 'k', 'l', 'm', 'n',
        'o', 'p', 'q', 'r', 's', 't', 'u',
        'v', 'w', 'x', 'y', 'z', ' '
    ]

    for character in string:
        if character.lower() in alphabet:
            cleanText += character
    return cleanText

def countVowels(string):
    vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
    
    for letter in string:
        if letter in vowels:
            vowels[letter] += 1
    return vowels

def countWords(string):
    return len(string.split(' '))

def countWordsThatStartByM(words):
    words = words.split(' ')
    count = 0
    for word in words:
        if word[0].lower() == 'm':
            count += 1
    return count

def handleFirstExercise():
  year = int(input("Por favor, ingrese un año: "))
  if (year % 4 == 0):
    # Solo hago esto así porque es parte de el ejercicio.
    # Pero se puede hacer fácilmente en una sola condición sin utilizar condiciones anidadas.
    if(year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
      print("Es año bisiesto")
    else:
      print("No es un año bisiesto")        
  else:
      print("No es un año bisiesto")

def handleSecondExercise():
  words = input("Por favor, ingrese el texto: ")
  words = words.split('.')[0]
  cleanString = removeSpecialCharacters(words)
  vowels = countVowels(cleanString)
  vowelMaxValue = max(vowels.values())
  vowelMinValue = min(vowels.values())
  vowelMax = [v for v, c in vowels.items() if c == vowelMaxValue][0].upper()
  vowelMin = [v for v, c in vowels.items() if c == vowelMinValue][0].upper()
  print(f"Repeticiones de Vocales; {vowels}")
  print(f"Cantidad de palabras: {countWords(cleanString)}")
  print(f"palabras con M: {countWordsThatStartByM(cleanString)}")
  print(f"Vocal más repetida: {vowelMax} ({vowelMaxValue})")
  print(f"Vocal menos repetida: {vowelMin} ({vowelMinValue})")

def handleThirdExercise():
   pass

def handleLastThreeExercises():
   pass

def main():
  print("Bienvenido al programa de Martín Ezequiel Monzón para el segundo parcial.\n")
  print("Ejercicio 1: Un programa que dado un año indique si es o no bisiesto, debe utilizar sentencias condicionales anidadas.\n")
  print("Ejercicio 2: Un programa que lea caracteres hasta el “.”, al finalizar se desea saber: \n   a) Cuantas vocales ingreso.\n   b) Cuantas palabras ingreso.\n   c) Cuantas palabras que empiezan con “M” ingreso.\n   d) Que vocal es la que se ingresó más veces\n   e) Que vocal es la que se ingresó menos veces.\n")
  
  print("Ejercicio 3: Un programa que le permite al usuario practicar sumas. \nEl programa deberá ofrecer al usuario 10 sumas con los números aleatorios, después de cada operación se le solicita al usuario que indique el resultado, si el resultado ingresado por el usuario es correcto se le suma un punto y si se equivoca no se le suma puntos. Al finalizar las 10 operaciones se le indica al usuario el puntaje acumulado y se lo felicita.\n")
  print("Ejercicio 4: Un programa que le permite al usuario practicar sumas. \nEl programa le dará a elegir al usuario el nivel de las cuentas Fácil, Intermedio o Difícil. Si eligió Fácil, los números de las operaciones, que se le ofrecerá al usuario, serán entre 0 y 25, si eligió intermedio los números serán entre 26 y 75, si eligió difícil los números serán entre 76 y 150.\n El programa deberá ofrecer al usuario 10 sumas con los números aleatorios, después de cada operación se le solicita al usuario que indique el resultado, si el resultado ingresado por el usuario es correcto se le suma un punto y si se equivoca no se le suma puntos. Al finalizar las 10 operaciones se le indica al usuario el puntaje acumulado y se lo felicita.\n")
  
  print("Ejercicio 5: Al programa del ejercicio 4, modificarlo para que el usuario pueda elegir la operación matemática que desea practicar, de modo tal que le ofrezca las 10 cuentas con la operación matemática elegida, +, -, * o /\n")
  print("Ejercicio 6: Al programa del ejercicio 5, modificarlo para que al finalizar las 10 operaciones se le indique al usuario el puntaje acumulado, se lo felicita y consulta si desea seguir practicando, en cuyo caso deberá nuevamente elegir la operación matemática y el nivel de dificultad y proceder a seguir practicando, y así sucesivamente hasta que elija no continuar practicando.")

  exercise = int(input("Escoja un ejercicio a realizar (del 1 al 6): "))
  if exercise > 0 and exercise < 7:
    exercise = exercise - 1
    # Lo que estoy haciendo acá, es crear un array que contenga todas las funciones que procesan los ejercicios
    exerciseHandler = [handleFirstExercise, handleSecondExercise]
    # Cuando le paso el index (que representa la opción que quiere realizar)
    print(f"exercise {exercise}")
    exerciseHandler[exercise]()
  else:
     print("Me parece que no ingresaste ningún ejercicio disponible...")
  restart = input("¿Reiniciar? s/n: ")
  if restart == "s":
    return main()
  else:
     print("¡Nos vemos!")

main()