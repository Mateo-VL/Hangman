from es_ES import words
from random import choice
from es_ES import reglas
#%% Entrada para modo 
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
#%%
def palabra_a_adivinar(diccionario):
    palabra = choice(diccionario)
    return palabra
#%%
def palabra_valida(palabra, diccionario):
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
#%%
def display(oportunidades : int, comodin, usadas)->None:
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