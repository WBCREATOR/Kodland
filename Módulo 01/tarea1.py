dict = {
    "LOL":"una respuesta a algo gracioso",
    "CRINGE": "algo raro o embarazoso",
    "ROFL" :"una respuesta a una broma",
    "SHEESH": "ligera desaprobación",
    "CREEPY": "aterrador, siniestro",
    "AGGRO": "ponerse agresivo/enojado"
}

word = input("Escriba una palabra que no entienda: ")

if word.upper() in dict.keys():
    print(dict[word.upper()])
else:
    print("[ERROR:] Esta palabra no se encuentra en el diccionario, inténtelo de nuevo.")
