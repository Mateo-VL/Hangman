from es_ES import words
from random import choice
from es_ES import reglas
from typing import List, Tuple
#%% Entrada humano
def entrada (diccionario : List)->str:
    '''
    Función que pide al usuario para ingresar una letra o palabra. Si ingresa una palabra llama a la función palabra_valida para corroborar si está incluida en el diccionario.

    Parameters
    ----------
    diccionario : List
    Contiene todas las palabras validas para jugar 

    Returns
    -------
    str
    Es la letra o palabra que ingreso el usuario.

    '''
    ingreso_valido = False
    while not ingreso_valido:
        ingreso_valido= True
        ingreso = input('Ingrese su suposicion:\n')
        if ingreso.isalpha():
            ingreso = ingreso.lower()
            if len(ingreso) > 1:
                ingreso_valido=palabra_valida(ingreso, diccionario)
                if ingreso_valido== False:
                    print ('palabra no conocida')
        else:
            print('Ingrese solo letras o palabras')
            ingreso_valido = False
    return ingreso
#%% Palabra Random
def palabra_a_adivinar(diccionario : List)-> str:
    '''
    Función que selecciona al azar una palabra del diccionario en español, palabra la cual el usuario debe adivinar.

    Parameters
    ----------
    diccionario : List
        Contiene todas las palabras validas para jugar

    Returns
    -------
    str
        Una palabra elegida al azar del diccionario

    '''
    palabra = choice(diccionario)
    return palabra
#%% Validar Palabra
def palabra_valida(palabra : str, diccionario : List)->bool:
    '''
    Busca a la palabra en el diccionario para saber si esta.

    Parameters
    ----------
    palabra : str
        Es la palabra que recibe 
    diccionario : List
        Es el diccionario en donde buscara si esta la palabra

    Returns
    -------
    bool
        Devuelve True si encontro a la palabra y False si no está en el diccionario

    '''
    inicio = 0
    fin = len(diccionario)
    while inicio <= fin:
        medio = ((fin + inicio) // 2)
        if diccionario[medio] == palabra:
            return True
        if diccionario[medio] > palabra:
            fin = medio -1
        if diccionario[medio] < palabra:
            inicio = medio +1
    return False
#%% Chequeo Humano
def chequeo(palabra_secreta : str, ingreso : str, oportunidades : int, comodin : List, usadas : str)->Tuple:
    '''
    La función se fija si lo que ingresa el usuario está dentro de la palabra (en caso que sea una letra). Si se ingresa palabra, verifica si es igual que la palabra secreta. En base a los aciertos devuelve las oportunidades restantes.

    Parameters
    ----------
    palabra_secreta : str
        Es la palabra a adivinar
    ingreso : str
        Es lo que el usuario ingreso en la funcion entrada
    oportunidades : int
        Es la cantidad de intentos que quedan
    comodin : List
        Tiene las letras acertadas en su posición correcta
    usadas : str
        Son las letras que el usuario ya ingreso

    Returns
    -------
    Tuple
        Es una tupla con los valores actualizados de las oportunidades, el comodin y las letras usadas

    '''
    lista_palabra = list(palabra_secreta)
    if len(ingreso) > 1:
        if palabra_secreta != ingreso:
            oportunidades = 0
        elif palabra_secreta == ingreso:
            comodin = lista_palabra
    elif len(ingreso) == 1:
        usadas += ingreso + ' '
        if ingreso not in palabra_secreta:
            oportunidades -= 1
        else:
            comodin = actualizar_comodin(palabra_secreta, ingreso, comodin)#si pongo directamente actualizar_comodin() anda igual. No se porque
    return oportunidades, comodin, usadas
#%% Actualizar Comodin
def actualizar_comodin (palabra_secreta : str, letra_correcta : str, comodin : List)->List:
    '''
    Función que modifica al comodin reemplazando con la letra elegida en la (o las) posiciones correspondientes.

    Parameters
    ----------
    palabra_secreta : str
        Es la palabra a adivinar
    letra_correcta : str
        Es la letra que se ingreso
    comodin : List
        Tiene las letras acertadas en su posición correcta

    Returns
    -------
    List
        Es el comodin luego de habersele agregado las letras.

    '''
    if len(letra_correcta) > 1:
        comodin = list(letra_correcta)
    for indice_caracter in range(len(palabra_secreta)):
        if palabra_secreta[indice_caracter] == letra_correcta:
            comodin[indice_caracter] = letra_correcta
            
    return comodin
#%% Display
def display(oportunidades : int, comodin : List, usadas : List)->None:
    '''
    Función que se encarga de imprimar el desarrollo del juego por la consola interactiva.

    Parameters
    ----------
    oportunidades : int
        Es la cantidad de oportunidades que quedan
    comodin : List
        Tiene las letras acertadas en su posición correcta
    usadas : List
        Son las letras que ya fueron usadas por el usuario

    Returns
    -------
    None

    '''
    comodin_pantalla = ''
    for letra in range(len(comodin)):
        comodin_pantalla += comodin[letra] + ' '
    print ('\n',comodin_pantalla,'(' + usadas + ')', '\nOportunidades restantes', oportunidades)
    
#%% Fin Juego
def fin_juego(palabra_secreta:str, oportunidades:int, comodin : List, jugando : bool)->bool:
    '''
    Función que revisa si el juego terminó. Dependiendo de si gana o pierde, es el mensaje que va a mostrar.

    Parameters
    ----------
    palabra_secreta : str
        Es la palabra a adivinar
    oportunidades : int
        Son las oportunidades que quedan
    comodin : List
        Tiene las letras acertadas en su posición correcta
    jugando : bool
        Señala si el juego se termino o no

    Returns
    -------
    bool
        Cuando la funcion devuelve False significa que se termino el juego

    '''
    if comodin == list(palabra_secreta):
        print (f'Felicitaciones, has ganado el juego. La palabra era {palabra_secreta}')
        jugando = False
    elif oportunidades == 0:
        print (f'Mala suerte, te has quedado sin oportunidades. La palabra era {palabra_secreta}')
        jugando = False
    return jugando
#%% Elegir Palabra
def elegir_palabra(diccionario : List)->str:
    '''
    Pregunta al usuario para que elija la palabra secreta que la computadora tratará de adivinar. LLama a función palabra_valida para chequear si está incluida en diccionario.

    Parameters
    ----------
    diccionario : List
        Contiene todas las palabras validas para jugar

    Returns
    -------
    str
        La palabra elegida para que la maquina juegue

    '''
    repetir= True
    while repetir:
        palabra_secreta= input("Elija una palabra para que la computadora adivine: \n")
        if palabra_valida(palabra_secreta, diccionario) == True:
           print("Palabra guardada")
           repetir= False
        else:
           print("Esta palabra no está incluida. Por favor ingrese otra palabra. ")
    return palabra_secreta
#%% Si o no
def siono(letra : str, palabra_secreta : str, oportunidades : int, comodin_actualizado : List)->Tuple:
    '''
    Función que pide al usuario que escriba si la letra elegida por computadora está en la palabra y verifica si es correcto.

    Parameters
    ----------
    letra : str
        Es la letra que eligio la computadora
    palabra_secreta : str
        Es la palabra a adivinar
    oportunidades : 5
        Es la cantidad de oportunidades que quedan
    comodin_actualizado : List
        Tiene las letras acertadas en su posición correcta

    Returns
    -------
    Tuple
        Devuelve una tupla que contiene las oportunidades restantes y si la computadora acerto o no.

    '''
    confirmar= input(f"La letra {letra} se encuentra en la palabra? [si/no]:").lower()
    while confirmar != "si" and confirmar != "no":
        print("Error. Confirme nuevamente")
        confirmar= input(f"La letra [{letra}] se encuentra en la palabra? [si/no]:").lower()
    if (confirmar == "si" and letra not in palabra_secreta) or (confirmar=="no" and letra in palabra_secreta) and len(palabra_secreta) < 2:
        print("Cuidado, verifique si la letra está incluida en palabra. Recuerda que hacer trampa esta mal")
        confirmar= input(f"La letra {letra} se encuentra en la palabra? [si/no]:").lower()
    if confirmar == "no":
        oportunidades -= 1
        acierto=False
    elif confirmar == "si":
        acierto=True
    return oportunidades, acierto
#%% Filtro * Largo
def filtro_largo(diccionario : List, palabra_secreta : str)-> List:
    '''
    Función que descarta todas las palabras del diccionario que no tengan la misma longitud que la palabra secreta, agregando las palabras de misma longitud a una lista vacía.

    Parameters
    ----------
    diccionario : List
        Contiene todas las palabras validas para jugar
    palabra_secreta : str
        Es la palabra a adivinar

    Returns
    -------
    List
        Es una lista con todas las letras que tienen el mismo largo que la palabra a adivinar

    '''
    diccionario_filtrado = []
    for posible_palabra in diccionario:
        if len(posible_palabra) == len(palabra_secreta):
            diccionario_filtrado.append(posible_palabra)
    return diccionario_filtrado
#%% Letra + Comun
def letra_mas_comun(diccionario_filtrado : List, abc : List, usadas : str)-> Tuple:
    '''
    Dentro de las palabras que hay en diccionario_filtrado, se fija cuál es la letra que más veces se repite. Agrega letra a string que muestra las letras usadas hasta el momento.

    Parameters
    ----------
    diccionario_filtrado : List
        Contiene todas las palabras validas para jugar ya filtradas por largo y por posición de las letras
    abc : List
        Es una lista con todas las letras del abecedario que aun no fueron usadas
    usadas : str
        Son las letras que ya fueron usadas por el usuario

    Returns
    -------
    Tuple
        Es una tupla que contiene a la letra que mas veces aparece en el diccionario filtrado, el abecedario sin las letras usadas y las letras usadas

    '''
    coincidencias = []
    for numero in range(len(abc)):
        coincidencias.append(0)
    for palabra in diccionario_filtrado:
        for letra in palabra:
            if letra in abc:
                coincidencia = abc.index(letra)
                coincidencias[coincidencia] += 1
    letra_posible = abc[coincidencias.index(max(coincidencias))]
    usadas += letra_posible
    abc.pop(abc.index(letra_posible))
    return letra_posible, abc, usadas
#%% Filtro del Comodin
def filtro(palabra : str, comodin_actualizado : List)->bool:
    '''
    Recibe una palabra y se fija si puede ser escrita con las condiciones que da el comodin (que contenga las letras que muestra, en el orden que muestra).

    Parameters
    ----------
    palabra : str
        Es la palabra que recibe la función.
    comodin_actualizado : List
        Es la condición que debe cumplir la palabra.

    Returns
    -------
    bool
        Si es True la palabra se puede escribir en el comodin, si es False es porque no se puede escribir con el comodín.

    '''
    for letra in range(len(palabra)):
        if comodin_actualizado[letra] == '_':
            continue
        elif comodin_actualizado[letra] != palabra[letra]:
            return False
    return True
#%% Filtro * Comodin
def filtro_comodin(diccionario_filtrado : List, comodin_actualizado : List)->List:
    '''
    Usa el filtro para agrupar las palabras que pasen el filtro en una nueva lista solo con las palabras que siguen siendo validas.

    Parameters
    ----------
    diccionario_filtrado : List
        Es la lista de palabras que recibe y las que le dara al filtro para que examine
    comodin_actualizado : List
        Son las condiciones que recibe el filtro para definir si la aprueba o no

    Returns
    -------
    List
        Es la lista de palabras que pasaron el filtro

    '''
    diccionario_a_actualizar = []
    for palabra in diccionario_filtrado:
        aprueba = filtro(palabra, comodin_actualizado)
        if aprueba:
            diccionario_a_actualizar.append(palabra)
    return diccionario_a_actualizar
#%% FIltro no Coincidencias
def filtro_no_coincidencia(letra_posible : str, diccionario_filtrado : List)->List:
    '''
    Esta función agrega a una lista vacia todas las palabras que no contienen a la letra_posible

    Parameters
    ----------
    letra_posible : str
        Es la letra que se va a usar para filtrar las palabras
    diccionario_filtrado : List
        Es el diccionario de donde se van a sacar las palabras para agregar al nuevo diccionario

    Returns
    -------
    List
        Una lista con todas las palabras que no contienen a letra_posible

    '''
    diccionario_actualizado = []
    for palabra in range(len(diccionario_filtrado)):
        if letra_posible not in diccionario_filtrado[palabra]:
            diccionario_actualizado.append(diccionario_filtrado[palabra])
    return diccionario_actualizado
#%% Menu
def menu(jugando : bool)->None:
    opciones_validas = ['1','2','3','4']
    while jugando:
        opciones= input("1-Jugar\n2-Ver lista de palabras \n3-Reglas\n4-Salir\nElegir una opción:")
        while opciones not in opciones_validas:
            print("\nOpción incorrecta")
            opciones= input("1-Jugar\n2-Ver lista de palabras \n3-Reglas\n4-Salir\nElegir una opción:")
        if opciones == '1':
            menu_de_juego(jugando)
        jugando = opciones_resto_menu(opciones, jugando)
#%% Menu de Juego
def menu_de_juego(jugando : bool)->None:
    usadas, oportunidades= " ", 5
    opcion_valida = ['1','2','3']
    modo_juego= input("Cómo quieres jugar?\n1-Human hangman\n2-Computer hangman\n3-Volver atrás\nElegir una opción :\n ")
    while modo_juego not in opcion_valida:
        print('Elija una opción valida')
        modo_juego= input("Cómo quieres jugar?\n1-Human hangman\n2-Computer hangman\n3-Volver atrás\nElegir una opción :\n ")
    if modo_juego == '1':
            human_hangman(usadas, oportunidades,words,jugando)
    elif modo_juego == '2':
        computer_hangman(usadas, oportunidades, words)
def opciones_resto_menu(opciones : str, jugando : bool)->bool:
    if opciones == '2':
        print (words)
    elif opciones == '3':
        print (reglas)
    elif opciones == '4':
        jugando = False
    return jugando
#%% Juego Humano
def human_hangman(usadas : str, oportunidades : int, diccionario : List, jugando : bool)->None:
    palabra_secreta = palabra_a_adivinar(diccionario)
    comodin = list('_' * len(palabra_secreta))# cambiar nombre
    display(oportunidades, comodin, usadas)
    while jugando:#ver, lo dejo por las dudas
        ingreso = entrada(diccionario)
        while ingreso in usadas:
            print('Elija una letra que no haya ingresado antes.\n Letras usadas:', usadas)
            ingreso = entrada(diccionario)
        oportunidades, comodin, usadas = chequeo(palabra_secreta, ingreso, oportunidades, comodin, usadas)
        display(oportunidades, comodin, usadas)
        jugando = fin_juego(palabra_secreta, oportunidades, comodin, jugando)
#%% Computer Hangman
def computer_hangman(usadas : str, oportunidades : int, jugando : bool)->None:
    usadas = usadas
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # agregar al modulo del diccionario
    palabra_secreta= elegir_palabra(words) 
    comodin= list("_"*len(palabra_secreta))
    display(oportunidades, comodin, usadas)
    diccionario_actualizado = filtro_largo(words, palabra_secreta)
    while jugando:#ver
        letra_posible, abc, usadas= letra_mas_comun(diccionario_actualizado, abc, usadas)
        oportunidades, acierto= siono(letra_posible, palabra_secreta, oportunidades, comodin)
        if acierto == True:
            comodin = actualizar_comodin(palabra_secreta, letra_posible, comodin)
            diccionario_actualizado = filtro_comodin(diccionario_actualizado, comodin)
        if acierto == False:
            diccionario_actualizado=filtro_no_coincidencia(letra_posible, diccionario_actualizado)
        display(oportunidades, comodin, usadas)
        jugando = fin_juego(palabra_secreta, oportunidades, comodin, jugando) #ganador, jugando)
#%% Main
def main()->None:
    jugando=True
    print("***Bienvenido al juego Ahorcado Digital***")
    menu(jugando)
