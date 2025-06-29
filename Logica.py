_seed = 1
def getRandom(minVal, maxVal):
  global _seed
  _seed = (_seed * 9301 + 49297) % 233280
  rnd = _seed / 233280
  return int (minVal + rnd * (maxVal - minVal + 1))

def getByDifficulty(difficulty = "default"):
  levels = {
    "default":[0, 150],
    "facil":[0, 25],
    "medio":[26, 75],
    "dificil":[76, 150]
  }

  return levels[difficulty]

def calc(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  elif operator == "-":
      return num1 - num2
  elif operator == "*":
      return num1 * num2
  elif operator == "/":
      if num2 == 0:
          return None  # Prevenimos que se divida por cero (porque no se puede, duh)
      return num1 // num2
  else:
      return None

# --- FUNCIONES DE PROCESAMIENTO DE TEXTO ---

def removeSpecialCharacters(string):
  cleanText = ""
  alphabet = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g',
      'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'ñ', 'o', 'p', 'q', 'r', 's', 't',
      'u', 'v', 'w', 'x', 'y', 'z', ' '
  ]

  accents = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}

  for character in string:
    if character.lower() in alphabet:
      cleanText += character
    elif character.lower() in accents:
        cleanText += accents[character]
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

def startAgain():
  # Hago todo esto en una línea porque es más cómodo hacerlo de esta manera.
  if(input("¿Te gustaría volver al menú?\ns/n: ").lower() == "s"):
    main()
  else:
    print("¡Nos vemos!")

def exerciseHandler(exercise):
    # Lo que estoy haciendo acá, es crear un array que contenga todas las funciones que procesan los ejercicios
    exercises = [handleFirstExercise, handleSecondExercise]
    # Cuando le paso el index (que representa la opción que quiere realizar)
    exercises[exercise]()
    if input("¿Reiniciar? s/n: ") == "s":
      return exerciseHandler(exercise)
    else:
      print("¡Nos vemos!")

def handleMath(exercise):
  # Le pongo un guión bajo al inicio porque "continue" es una keyword (o sea, una palabra reservada)
  _continue = True
  while _continue:
    points = 0

    if exercise == 3:
      minVal, maxVal = 0, 100
      operator = "+"
    elif exercise >= 4:
      diff = input("Elija nivel (facil, medio, dificil): ").lower()
      minVal, maxVal = getByDifficulty(diff)

      if exercise == 4:
        operator = "+"
      elif exercise >= 5:
        operator = input("Elija operación (+, -, *, /): ")
    
    for x in range(1, 11):
      num1 = getRandom(minVal, maxVal)
      num2 = getRandom(minVal, maxVal)

      if operator == "/" and num2 == 0:
        num2 = 1

      result = calc(num1, num2, operator)
      if result is None:
        print("Error interno en el cálculo.")
        continue

      print(f"{x} ¿Cuánto es {num1} {operator} {num2}?")
      try:
        response = int(input("R => "))
        if response == result:
          print("Correcto!\n")
          points = points + 1
        else:
          print(f"Incorrecto... La respuesta era {result}")
      except:
         print("Ingresaste un valor inválido.\n")
    print(f"\n Puntaje: {points}/10")
    if exercise == 6:
       again = input("¿Desea seguir practicando? (s/n): ").lower()
       if again != "s":
          _continue = False
    else:
       _continue = False

def main():
  print("Bienvenido al programa de Martín Ezequiel Monzón, Facundo Bellochi y Thiago Alegre para el segundo parcial.\n")
  print("Ejercicio 1: Un programa que dado un año indique si es o no bisiesto, debe utilizar sentencias condicionales anidadas.\n")
  print("Ejercicio 2: Un programa que lea caracteres hasta el “.”, al finalizar se desea saber: \n   a) Cuantas vocales ingreso.\n   b) Cuantas palabras ingreso.\n   c) Cuantas palabras que empiezan con “M” ingreso.\n   d) Que vocal es la que se ingresó más veces\n   e) Que vocal es la que se ingresó menos veces.\n")
  
  print("Ejercicio 3: Un programa que le permite al usuario practicar sumas. \nEl programa deberá ofrecer al usuario 10 sumas con los números aleatorios, después de cada operación se le solicita al usuario que indique el resultado, si el resultado ingresado por el usuario es correcto se le suma un punto y si se equivoca no se le suma puntos. Al finalizar las 10 operaciones se le indica al usuario el puntaje acumulado y se lo felicita.\n")
  print("Ejercicio 4: Un programa que le permite al usuario practicar sumas. \nEl programa le dará a elegir al usuario el nivel de las cuentas Fácil, Intermedio o Difícil. Si eligió Fácil, los números de las operaciones, que se le ofrecerá al usuario, serán entre 0 y 25, si eligió intermedio los números serán entre 26 y 75, si eligió difícil los números serán entre 76 y 150.\n El programa deberá ofrecer al usuario 10 sumas con los números aleatorios, después de cada operación se le solicita al usuario que indique el resultado, si el resultado ingresado por el usuario es correcto se le suma un punto y si se equivoca no se le suma puntos. Al finalizar las 10 operaciones se le indica al usuario el puntaje acumulado y se lo felicita.\n")
  
  print("Ejercicio 5: Al programa del ejercicio 4, modificarlo para que el usuario pueda elegir la operación matemática que desea practicar, de modo tal que le ofrezca las 10 cuentas con la operación matemática elegida, +, -, * o /\n")
  print("Ejercicio 6: Al programa del ejercicio 5, modificarlo para que al finalizar las 10 operaciones se le indique al usuario el puntaje acumulado, se lo felicita y consulta si desea seguir practicando, en cuyo caso deberá nuevamente elegir la operación matemática y el nivel de dificultad y proceder a seguir practicando, y así sucesivamente hasta que elija no continuar practicando.")

  exercise = int(input("Escoja un ejercicio a realizar (del 1 al 6): "))
  if exercise > 0 and exercise < 4:
    exercise = exercise - 1
    exerciseHandler(exercise)
  elif exercise >= 4 and exercise < 7:
     handleMath(exercise)
  else:
     print("Me parece que no ingresaste ningún ejercicio disponible...")
     main()
  startAgain()

main()