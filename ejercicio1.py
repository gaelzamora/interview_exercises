def add_word_to_dict(palabra: str, palabras: dict) -> None:
    if palabra in palabras:
        palabras[palabra] += 1
    else:
        palabras[palabra] = 1
 
def imprimir_palabras(texto: str, buscar: str) -> str:
    palabras = {}
    palabra = ""
    for ch in texto:
        if ch != ' ' and ch != '.' and ch != ',' and ch != '¿' and ch != '?' and ch != '(' and ch != ')':
            palabra += ch
        else:
            if palabra != "":
                add_word_to_dict(palabra, palabras) 
                palabra = ""
    
    if palabra:
        add_word_to_dict(palabra, palabras)
 
    return f"{palabras[buscar]} ocurrencias encontradas"
 
 
t = 'La logística Digital es un concepto que surge de la integración entre la logística tradicional y la era digital. Con el auge del correo electrónico y las descargas digitales reemplazando productos físicos, podríamos estar hablando de un golpe devastador para la industria de la logística, pero, de hecho, ha ocurrido algo muy diferente. El sector de la logística ha introducido las innovaciones digitales.'

print(imprimir_palabras(t, "logística"))