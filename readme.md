# LÓGICA - Segundo Parcial
> Recordar que, la profesora mencionó que hay que programar este proyecto imaginando un escenario donde no ocurra ningún error con la información introducida.

```
FUNCIÓN removeSpecialCharacters(str):
  Inicializar cleanText como string vacío
  Definir una lista llamada alphabet con las letras (en lowercase) del abecedario (y el espacio)
  PARA cada carácter en el string:
    SI el carácter (pasado a lowercase) está en alphabet:
      Agregar el carácter original a cleanText
    RETORNAR cleanText

FUNCIÓN countVowels(str):
  crear un DICT llamado vowels con claves siendo las vocales, y con valores inicializados en cero.
  PARA cada letra en el string:
    SI la letra está en vowels:
      Incrementar su contador.
  RETORNAR el dict vowels

FUNCIÓN countWords(str):
  RETORNAR el conteo de los elementos (cada elemento, siendo una palabra) dentro de la división del string por los espacios

FUNCIÓN countWordsThatStartByM(str):
  Dividir el string por los espacios
  Inicializar un contador en cero
  PARA cada palabra en la lista:
    SI la primera letra de la palabra (transformada a lower de vuelta) inicia en "m":
      Incrementar el contador
    RETORNAR el contador

FUNCIÓN handleFirstExercise():
  Pedir al usuario que ingrese un año (convertirlo a entero)
  SI el año es divisible por 4:
    SI el año NO es divisible por 100 O ES divisible por 400:
      Print "Es año bisiesto"
    SINO:
      Print "No es año bisiesto"
  SINO:
    Print "No es año bisiesto"

FUNCIÓN handleSecondExercise()
  Pedirle al usuario que ingrese un texto
  Tomar SOLO la parte del texto ANTES del punto final (.), dividiendo el texto justamente tomando el punto como referencia, y usando el primer elemento del array obtenido de la división.
  Llamar a RemoveSpecialCharacters para eliminar símbolos no deseados, y almacenar este valor retornado en una variable llamada clean o cleanString
  Contar las vocales usando countVowels, y almacenar esto en una variable vowels
  Buscar la vocal con más repeticiones con max(vowels.valores()) y almacenar esto en una variable max
  Buscar la vocal con menos repeticiones con min(vowels.valores()) y almacenar esto en una variable min

  Print las repeticiones obtenidas de las vocales de vowels

  Print el resultado de pasarle a countWords la variable clean
  
  Print el resultado de pasarle a CountWordsThatStartByM la variable Clean
  
  Print la vocal más repetida con max
  
  Print la vocal menos repetida con min

FUNCIÓN startAgain():
  Preguntar si al usuario le gustaría reiniciar el programa
  SI "s":
    Volver a ejecutar main()
  SINO:
    print mensaje de despedida

FUNCIÓN exerciseHandler(int):
  crear un array con las funciones que "manejen" los ejercicios
  llamar a su respectivo buscando con el entero recibido como parámetro al array.
  preguntar si al usuario le gustaría reiniciar el ejercicio
  SI responde s:
    retornar exerciseHandler(<le pasamos el int>)
  SINO:
    print mensaje de despedida

FUNCIÓN handleLastExercises():
  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

FUNCIÓN main()
  Mostrar introducción con descripción de todos los ejercicios
  Guardar en una variable el ejercicio que el usuario quiera realizar, almacenar esto en una variable.
  SI el número es mayor a 0 pero menor que 4:
    Restarle a la variable que contiene el ejercicio: 1
    pasarle a ExerciseHandler el ejercicio a ejecutar
  SINO SI el número es mayor o igual a 4 pero menor que 7:
    llamar a handleLastExercises()
  SINO:
    print mensaje de error y volver a llamar a Main
  Llamar a StartAgain()

Al final de todo el programa, llamar a main() para que se ejecute dicho programa.
```

## Participantes
- Martín *Ezequiel Monzón*
- *Facundo Bellochi*
- *Thiago Alegre*