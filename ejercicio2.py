from input import *

def cumple_filtro(elemento, filtro):
    campo, operador, valor = filtro
    valor_elemento = elemento.get(campo)
        
    if valor_elemento is None:
        return False
        
    if operador == '=':
        return valor_elemento == valor
    elif operador == '>':
        return valor_elemento > valor
    elif operador == '<':
        return valor_elemento < valor
    elif operador == '>=':
        return valor_elemento >= valor
    elif operador == '<=':
        return valor_elemento <= valor
    elif operador == '!=':
        return valor_elemento != valor
    else:
        return False

def cumple_todos_filtros(elemento, filtros):
    if not filtros:
        return True
        
    for filtro in filtros:
        if not cumple_filtro(elemento, filtro):
            return False
    return True

def load_data(filters, order_by, data):
    
    elementos_que_cumplen = []
    elementos_que_no_cumplen = []
    
    for elemento in data:
        if cumple_todos_filtros(elemento, filters):
            elementos_que_cumplen.append(elemento)
        else:
            elementos_que_no_cumplen.append(elemento)
    
    resultado = elementos_que_cumplen
    
    for i in range(0, len(resultado)):
        for j in range(0, len(resultado) - i - 1):
            prioridad_actual = resultado[j]["priority"]
            prioridad_siguiente = resultado[j + 1]["priority"]

            intercambiar = False

            if order_by == "ASC":
                if prioridad_actual > prioridad_siguiente:
                    intercambiar = True
            else:
                if prioridad_actual < prioridad_siguiente:
                    intercambiar = True
            
            if intercambiar:
                temp = resultado[j]
                resultado[j] = resultado[j + 1]
                resultado[j + 1] = temp

    return resultado + elementos_que_no_cumplen

# Ejemplo de filtros

# [
#     ('weight', '=', 3),
#     ('width', '>', 2),
# ]

# Ejemplo de order_by

# ASC | DESC

filters = [
    ('cost', '>', 130),
]

order_by = "ASC"

# Ejecutar y mostrar resultados
resultado = load_data(filters=filters, order_by=order_by, data=data)

for res in resultado:
    print(res)