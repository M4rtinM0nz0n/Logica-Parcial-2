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

# Glosario:
# Función = Código Reutilizable, se define utilizando "def"
# Parámetro = Valor que recibe una función. Este valor se convierte en una variable que almacena ese valor, y se puede ir llamando dentro de la función
# Diccionario = Tipo de dato de una variable, donde el contenido es una lista de pares clave-valor: {estudiante:"Ezequiel"}. Cuando llamás a "estudiante": miVariable['estudiante'] te devuelve "Ezequiel".
# Esta función, recibe una cadena de caracteres como parámetro. A lo largo de este ejemplo, se irá tomando el inicio del quijote como parámetro que irá recibiendo (en esta función, así como en el resto):
"""
  En un lugar de la Mancha, de cuyo nombre no quiero acordarme.
  No ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.
"""
def removeSpecialCharacters(string):
  # Se inicializa una variable con una cadena de caracteres vacía. Esto, se va ir llenando a medida que se vaya procesando la función
  cleanText = ""
  """
    Esto es una lista, hay que recordar que los valores dentro de las listas se acceden a través de un "índice", y el "índice", la posición, siempre se empieza a contar desde el cero, tal que el primer elemento de la lista siempre tendrá "posición 0".
    Por ejemplo:
    alphabet[0] devolverá "a"
    alphabet[1] devolverá "b",
    alphabet[2] devolverá "c"
    Y así consecutivamente.
    Si tratamos de acceder a un índice que no existe, ocurre un error.
  """
  alphabet = [
      'a', 'b', 'c', 'd', 'e', 'f', 'g',
      'h', 'i', 'j', 'k', 'l', 'm', 'n',
      'ñ', 'o', 'p', 'q', 'r', 's', 't',
      'u', 'v', 'w', 'x', 'y', 'z', ' '
  ]
  # La misma lógica detrás de este diccionario, si llamamos a accets['á'] nos devolverá 'a'
  accents = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}
  """
    Esto recorre cada elemento dentro de la variable "string" que recibe la función, y por cada elemento ejecuta la siguiente lógica:
    crea una variable "character" que va a ir cambiando a medida que vaya recorriendo el string.
    Por ejemplo, la primera vez que se ejecute este Loop, será:
      character = "E"
    La segunda vez:
      character = "n"
    La tercera vez:
      character = " "
    La cuarta vez: 
      character = "u"
    y así sucesivamente hasta que se termine de recorrer todo el string que se le pasó a esta función.
  """
  for character in string:
    """
    Luego, la letra a minúscula con "lower()", si le pasamos la primera "E" que es la que está en mayúscula, se convertirá en "e", duh.
    Y luego, pregunta si esa "e" en minúscula está dentro de la lista que creamos antes: alphabet.
    "e" está dentro de alphabet, por lo que ejecutará la siguiente lógica:
    """
    if character.lower() in alphabet:
      """
        A la variable que creamos en un inicio: "cleanText", le agregará la letra que contiene "character", en este caso "E"
        (no la añade en minúscula, porque nunca cambiamos el valor de la variable "character", simplemente preguntamos si el valor de esa variable en minúscula estaba en alphabet)
      """
      if character.lower() in alphabet:
        cleanText += character
      elif character.lower() in accents:
          cleanText += accents[character]
  """
    Al final, devuelve el string cambiado (Esta función solo se llama luego de que se obtiene todo el texto hasta el primer punto).
    Pasa de:
    "En un lugar de la mancha, de cuyo nombre no quiero acordarme"
    A:
    "En un lugar de la mancha de cuyo nombre no quiero acordarme"
    Removió la coma básicamente, lol. Toda esa explicación para remover una coma.
  """
  return cleanText

"""
  Esta función recibe un string, una cadena de texto, como parámetro. La idea es que retorne algo como esto:
  {"a":6, "e":5, "i":1, "o":5, "u":4}
"""
def countVowels(string):
  """
    Un diccionario, donde cada clave es una vocal, y el valor es la cantidad de veces que se repitió, siempre se inicializa en cero porque obviamente se empieza a contar desde cero, duh.
  """
  vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
  
  """
    Esto lo añadí a último momento, lol.
    Convierte el string en minúscula que recibió en.
  """
  string = string.lower()

  """
    Al igual que en la función anterior, toma el string que recibe y crea una variable, en este caso: "letter", que irá cambiando a medida que vaya recorriendo el string.
    Primero será: "e", luego "n", luego " ", y luego "u", y así consecutivamente.  """
  for letter in string:
      """
      Luego, pregunta si esa letra existe en nuestro diccionario de vocales:
        "e" = sí
        "n" = no
        " " = no
        "u" = sí
        "n" = no
      Y así consecutivamente.
      """
      if letter in vowels:
          """
            Si existe dentro de la lista, lo que hará será:
            Actualizar el diccionario, incrementando el conteo de esa lista, con el ejemplo previo será:
              {"a":0, "e":1, "i":0, "o":0, "u":1}
          """
          vowels[letter] += 1
  """
    Al final, con el inicio del quijote debería devolver lo que mencionamos antes:
    {"a":6, "e":5, "i":1, "o":5, "u":4}  
  """
  return vowels

"""
  Esto es muy simple, esta función recibe una cadena de caracteres (string)
  Lo que hace es, agarra y parte ese string por todos los espacios que hay en el string y lo convierte a una lista con todos los elementos que no sean un espacio, obteniendo:
  ["En" "un", "lugar", "de", "la", "mancha", "de", "cuyo", "nombre", "no", "quiero", "acordarme"]
  Luego, se cuenta cuántos elementos hay, en este caso: 12.
  Luego, devuelve ese conteo.
"""
def countWords(string):
  return len(string.split(' '))

"""
  Esta función recibe una cadena de caracteres en un parámetro "words".
"""
def countWordsThatStartByM(words):
  """
    Al igual que con la última función, partimos el string por los espacios que hay en dicho string, obteniendo:
    ["En" "un", "lugar", "de", "la", "mancha", "de", "cuyo", "nombre", "no", "quiero", "acordarme"]
  """
  words = words.split(' ')
  # Esta variable "count" se irá incrementando a lo largo de la ejecución.
  count = 0
  """
    Ahora, lo que hace es, al igual que con varias funciones anteriores, crea una variable:
    "word", esa variable "word" irá cambiando a medida que se vaya recorriendo la lista "words"
    "word" primero será:
      word = "En"
    Luego "word" será:
      word = "un"
    Luego "word" será:
      word = "lugar"
    Y así sucesivamente hasta llegar al final de la lista.
  """
  for word in words:
      """
        Al igual que con las listas, si ponemos un "índice" podemos obtener su valor en las cadenas de caracteres.
        Si en la primera ejecución de este bucle, le pasamos "0", será:
          word[0] = "E"
        Si en la SEGUNDA ejecución de este bucle, le pasamos "0", será:
          word[0] = "u"
        Si en la TERCERA ejecución de este bucle, le pasamos "0", será:
          word[0] = "l"
        Y así consecutivamente hasta llegar al final de la lista.
        Entonces, preguntamos si ese valor CONVERTIDO A MINÚSCULA (con .lower()) es igual a una "m"
      """
      if word[0].lower() == 'm':
          """
            Si es igual a una M, entonces se incrementa el contador.
          """
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

"""
  Esta función NO recibe parámetros, será llamada cuando el usuario escoja qué quiere hacer.
"""
def handleSecondExercise():
  """
    Primero, se ingresa el texto:
    "En un lugar de la Mancha, de cuyo nombre no quiero acordarme. No ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor."
  """
  words = input("Por favor, ingrese el texto: ")
  """
    Esta parte de acá, al igual que en muchas funciones de antes que lo partían por un espacio, ahora lo separa por un punto:
    ["En un lugar de la Mancha, de cuyo nombre no quiero acordarme", "No ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor"]
    Y si obtenemos el elemento en la posición 0 (porque, recordemos que en la programación se empieza a contar desde 0), se obtiene:
    "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"
  """
  words = words.split('.')[0]

  """
    Se crea una variable "cleanString", la cual posee como valor el resultado de pasarle:
      "En un lugar de la Mancha, de cuyo nombre no quiero acordarme"
    A "removeSpecialCharacters()"
    recordemos que removeSpecialCharacters nos devuelve:
      "En un lugar de la Mancha de cuyo nombre no quiero acordarme" (remueve la coma, lol)
    Ese será el valor de cleanString
  """
  cleanString = removeSpecialCharacters(words)

  """
    Se crea una variable llamada "vowels", la cual obtiene el valor de contar todas las vocales en:
      "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
    con countVowels
    Esto nos devolverá:
      {"a":6, "e":5, "i":1, "o":5, "u":4}
    Entonces ese será el valor de vowels.
  """
  vowels = countVowels(cleanString)
  """
    se crea una variable vowelMaxValue, la cual solo obtiene CUÁNTAS VECES se repitió la vocal que más veces se repitió.
    En este caso, la "a" se repitió 6 veces, y es la que más se repitió. Entonces, el valor de vowelMaxValue será 6.
    
    Esto funciona así:
      .values() obtiene una lista con los valores de vowels = [6, 5, 1, 5, 4]
    Entonces, se busca cuál es el valor más grande dentro de esa lista, en este caso el 6, ese será el valor de vowelMaxValue.

    Después, se crea una variable vowelMinValue la cual ejecuta el caso contrario, vowels.values obtiene la lista ([6, 5, 1, 5, 4]) y luego busca el valor MÁS PEQUEÑO.
    En este caso, la i se repitió 1 vez y ese será el valor que tendrá: 1.
  """
  vowelMaxValue = max(vowels.values())
  vowelMinValue = min(vowels.values())
  """
    Luego, se crean dos variables: vowelMax y vowelMin, que buscan LA CLAVE de la variable que más se repitió, recordemos que las claves son con lo que accedemos a los valores
    En este caso, a, e, i, o y u.
    
    Esto funciona así:
    ".items" hace lo mismo que ".values" solo que en lugar de obtener solo los valores, obtiene también las claves.
    {"a": 6, "e": 5, "i": 1, "o": 5, "u": 4}.items() -> [('a', 6), ('e', 5), ('i', 1), ('o', 5), ('u', 4)]

    Dentro de [('a', 6), ('e', 5), ('i', 1), ('o', 5), ('u', 4)] lo que hace es:
      crea unas variable "v" y "c" (con v de vocal y con c de cantidad), y por cada par (v y c) pregunta si el valor de "c" (el conteo) es igual a vowelMaxValue o vowelMinValue respectivamente.
      Si lo es, obtiene una lista tipo:
        ["a", 6]
      cuando hacemos una declaración múltiple con coma de variables:
        x, y = 1, 2
      Python sabe cómo asignarlas, por lo que es lo mismo que:
        x = 1
        y = 2
      En este caso:
        v, c = "a", 6
      entonces:
        v = "a"
        c = 6
      Y eso es lo que hace:
        v for v, c in vowels.items()
      Cuando obtenemos el par clave-valor que más se repitió, se asignan v y c
      Entonces, se pregunta si "c" es igual a vowelMaxValue (6 en este caso)
      Entonces lo que hace es obtener la primera de esos dos valores dentro de la lista, pero esto es importante:
      se hace con la primera v
        v = a
        c = c
      entonces vos solo guardás en una lista de un solo elemento, la v:
        [v] que es lo mismo que ["a"]
      Entonces, con indexación (llamar al índice) 0, se obtiene la "a":
        ["a"][0] nos devuelve "a"
      Entonces la línea, "despejada" quedaría tipo:
        vowelMax = ["a"][0].upper() -> porque v es el valor que se guarda en la lista.
      Entonces, se convierte esa letra obtenida en mayúscula con ".upper()"
      Esto es un ejemplo en pseudo-código:
      vowelMax = [obtener "a" por cada par "a", 6 en [('a', 6)] si 6 es igual a vowelMaxValue]
                                                                                    (6)
      La mismoa lógica se ejecuta para vowelMinValue
  """
  vowelMax = [v for v, c in vowels.items() if c == vowelMaxValue][0].upper()
  vowelMin = [v for v, c in vowels.items() if c == vowelMinValue][0].upper()
  
  """
    Finalmente, se imprime en la pantalla el mensaje que queremos mostrar:
  """
  print(f"Repeticiones de Vocales; {vowels}")
  """
    repeticiones de vocales: {"a":6, "e":5, "i":1, "o":5, "u":4}  
  """
  print(f"Cantidad de palabras: {countWords(cleanString)}")
  """
    Cantidad de palabras: 12
  """
  print(f"palabras con M: {countWordsThatStartByM(cleanString)}")
  """
    Palabras con M: 1
  """
  print(f"Vocal más repetida: {vowelMax} ({vowelMaxValue})")
  """
    Vocal más repetida: A (6)
  """
  print(f"Vocal menos repetida: {vowelMin} ({vowelMinValue})")
  """
    Vocal menos repetida: I (1)
  """

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
  if exercise > 0 and exercise < 3:
    exercise = exercise - 1
    exerciseHandler(exercise)
  elif exercise >= 3 and exercise < 7:
     handleMath(exercise)
  else:
     print("Me parece que no ingresaste ningún ejercicio disponible...")
     main()
  startAgain()

main()