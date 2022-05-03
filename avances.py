from es_ES import words
from random import choice
from es_ES import reglas
#%%
def entrada (palabra_secreta, diccionario):
    ingreso_valido = False
    while not ingreso_valido:
        ingreso = input('Ingrese su suposicion:\n')
        if ingreso.isalpha():
            ingreso = ingreso.lower()
            ingreso_valido = palabra_valida(palabra_secreta, diccionario)
            if not ingreso_valido:
                print ('palabra no conocida')
        else:
            print('Ingrese solo letras o palabras')
    return ingreso
# buscar si la palabra esta en el diccionario (busca por biyeccion). Preguntar confirmación
# fijarse de reducir el largo de la funcion.
#%%
def palabra_a_adivinar(diccionario):
    palabra = choice(diccionario)
    return palabra
#%%
def palabra_valida(palabra, lista3):
    inicio = 0
    fin = len(lista3)
    while inicio <= fin:
        medio = ((fin + inicio) // 2)
        if lista3[medio] == palabra:
            return True
        if lista3[medio] > palabra:
            fin = medio -1
        if lista3[medio] < palabra:
            inicio = medio +1
    return False
#%%
def chequeo(palabra_secreta, ingreso, oportunidades, ganador, comodin, usadas):
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
            for i in range(len(lista_palabra)):
                if lista_palabra[i] == ingreso:
                    comodin[i] = ingreso
    return oportunidades, comodin, usadas
# hacer revision de si la letra ya esta usada
#%%
def display(oportunidades : int, comodin, usadas)->None:
    #solucionar problema de imprimir la lista al principio
    comodin_pantalla = ''
    for letra in range(len(comodin)):
        comodin_pantalla += comodin[letra] + ' '
    print ('\n',comodin_pantalla,'(' + usadas + ')', '\nOportunidades restantes', oportunidades)
    
#%%
def fin_juego(palabra_secreta:str, oportunidades:int, comodin, jugando):
    if comodin == list(palabra_secreta):
        print (f'Felicitaciones, has ganado el juego. La palabra era {palabra_secreta}')
        jugando = False
    elif oportunidades == 0:
        print (f'Mala suerte, te has quedado sin oportunidades. La palabra era {palabra_secreta}')
        jugando = False
    return jugando
#%%
def elegir_palabra(diccionario):
    repetir= True
    while repetir:
        palabra_secreta= input("Elija una palabra para que la computadora adivine: \n")
        if palabra_valida(palabra_secreta, diccionario) == True:
           print("Palabra guardada")
           repetir= False
        else:
           print("Esta palabra no está incluida. Por favor ingrese otra palabra. ")
    return palabra_secreta
#%%
def siono(letra, palabra_secreta, oportunidades,comodin_actualizado):
    confirmacion= True
    while confirmacion:
        confirmacion= False
        confirmar= input(f"La letra {letra} se encuentra en la palabra? [si/no]:").lower()
        if (confirmar == "si" and letra not in palabra_secreta) or (confirmar=="no" and letra in palabra_secreta):
            print("Cuidado, verifique si la letra está incluida en palabra")
            confirmacion= True
        elif confirmar != "si" and confirmar != "no":
            print("Error. Confirme nuevamente")
            confirmacion= True
        elif confirmar == "no" and letra not in palabra_secreta:
            oportunidades -= 1
            acierto=False
        elif confirmar == "si" and letra in palabra_secreta:
            acierto=True
    return oportunidades, acierto
#%%
def filtro_largo(diccionario : list, palabra_secreta : str)-> list:
    diccionario_filtrado = []
    for posible_palabra in diccionario:
        if len(posible_palabra) == len(palabra_secreta):
            diccionario_filtrado.append(posible_palabra)
    return diccionario_filtrado
#%%
def letra_mas_comun(diccionario_filtrado : list, abc : list, usadas)-> list:
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
#%%
def actualizar_comodin (palabra_secreta : str, letra_correcta : str, comodin : list) ->list:
    for indice_caracter in range(len(palabra_secreta)):
        if palabra_secreta[indice_caracter] == letra_correcta:
            comodin[indice_caracter] = letra_correcta
    return comodin
#%%
def filtro(palabra : str, comodin_actualizado : str)->bool:
    for letra in range(len(palabra)):
        if comodin_actualizado[letra] == '_':
            continue
        elif comodin_actualizado[letra] != palabra[letra]:
            return False
    return True
#%%
def filtro_comodin(diccionario_filtrado : list, comodin_actualizado : list)->list:
    diccionario_a_actualizar = []
    for palabra in diccionario_filtrado:
        aprueba = filtro(palabra, comodin_actualizado)
        if aprueba:
            diccionario_a_actualizar.append(palabra)
    return diccionario_a_actualizar
#%%
def filtro_no_coincidencia(letra_posible, diccionario_filtrado):
    diccionario_actualizado = []
    for palabra in range(len(diccionario_filtrado)):
        if letra_posible not in diccionario_filtrado[palabra]:
            diccionario_actualizado.append(diccionario_filtrado[palabra])
    return diccionario_actualizado
#%%
def main():
    diccionario=words
    print("***Bienvenido al juego Ahorcado Digital***")  
    repetir_opciones= True
    while repetir_opciones:
        repetir_opciones=False
        opciones= input("1-Jugar\n2-Ver lista de palabras \n3-Reglas\n4-Salir\nElegir una opción:")
        if opciones != '1' and opciones != '2' and opciones != '3' and opciones != '4':
            print("\nOpción incorrecta")
            repetir_opciones=True 
        
        if opciones == '1': #jugar
            repetir_modo_juego = True
            while repetir_modo_juego:
                modo_juego= input("Cómo quieres jugar?\n1-Human hangman\n2-Computer hangman\n3-Volver atrás\nElejir una opción :\n ")
                repetir_modo_juego = False
                if modo_juego== '1':
                    jugando = True
                    palabra_secreta = palabra_a_adivinar(diccionario)
                    usadas = ''
                    oportunidades = 5
                    ganador = False
                    comodin = list('_' * len(palabra_secreta))# cambiar nombre
                    display(oportunidades, comodin, usadas)
                    while jugando:
                        ingreso = entrada(palabra_secreta, diccionario)
                        while ingreso in usadas and len(ingreso) == 1:
                            print('Elija una letra que no haya ingresado antes.\n Letras usadas:', usadas)
                            ingreso = entrada(palabra_secreta, diccionario)
                        oportunidades, comodin, usadas = chequeo(palabra_secreta, ingreso, oportunidades, ganador, comodin, usadas)
                        display(oportunidades, comodin, usadas)
                        jugando = fin_juego(palabra_secreta, oportunidades, comodin, jugando)
                    else:
                        repetir_modo_juego = True
                elif modo_juego == '2':
                    usadas = ''#creac funcion para condiciones iniciales
                    oportunidades = 5
                    diccionario_actualizado = diccionario
                    jugando= True
                    abc = ["a","b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
                    palabra_secreta= elegir_palabra(diccionario_actualizado) 
                    diccionario_actualizado = filtro_largo(diccionario_actualizado, palabra_secreta)
                    comodin= list("_"*len(palabra_secreta))
                    display(oportunidades, comodin, usadas)
                    while jugando:
                        letra_posible, abc, usadas= letra_mas_comun(diccionario_actualizado, abc, usadas)
                        oportunidades, acierto= siono(letra_posible, palabra_secreta, oportunidades, comodin)
                        if acierto == True:
                            comodin = actualizar_comodin(palabra_secreta, letra_posible, comodin)
                            diccionario_actualizado = filtro_comodin(diccionario_actualizado, comodin)
                        if acierto == False:
                            diccionario_actualizado=filtro_no_coincidencia(letra_posible, diccionario_actualizado)
                        display(oportunidades, comodin, usadas)
                        jugando= fin_juego(palabra_secreta, oportunidades, comodin, jugando)
#juego con computadora
                elif modo_juego == '3':
                    repetir_opciones = True
                else:
                    print("Opción incorrecta")
                    repetir_modo_juego=True 
        if opciones == '2':
            # menu de todas las palabras
            print (words)
            repetir_opciones = True
        if opciones == '3':
            print (reglas)
            repetir_opciones = True
        if opciones == '4':
            repetir_opciones == False
#%%
main()