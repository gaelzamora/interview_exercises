class ExcelSheet:
    def __init__(self):
        """Inicializa una hoja vacia."""
        self.cells = {}
        self.max_row = 0
        self.max_col = 0
    
    def _actualizar_dimensiones(self, row, col):
        """Funcion auxiliar para mantener el rastro de las dimensiones de la hoja."""
        if row > self.max_row:
            self.max_row = row
        if col > self.max_col:
            self.max_col = col
    
    def _es_numero(self, valor):
        """Funcion auxiliar para verificiar si un valor es numerico."""
        if isinstance(valor, (int, float)):
            return True
        
        if isinstance(valor, str):
            try:
                float(valor)
                return True
            except ValueError:
                return False
        
        return False
    
    def _convertir_a_numero(self, valor):
        """Intenta convertir a un numero (ya sea int o float)."""
        if isinstance(valor, (int, float)):
            return valor
        
        if isinstance(valor, str):
            try:
                if '.' not in valor:
                    return int(valor)
                else:
                    return float(valor)
            except ValueError:
                return 0
        
        return 0
    
    def insertar_celda(self, row, col, valor):
        """Inserta informacion en una celda en especifica."""
        if row < 1 or col < 1:
            print(f"Error: Las filas y columnas deben ser mayores o iguales a 1")
            return False
        
        celda = (row, col)
        
        if celda in self.cells:
            print(f"Advertencia: La celda ({row}, {col}) ya tiene informacion. Use actualizar_celda() para modificarla.")
            return False
        
        self.cells[celda] = valor
        self._actualizar_dimensiones(row, col)
        return True
    
    def actualizar_celda(self, row, col, nuevo_valor):
        """Actualiza una celda existente"""
        if row < 1 or col < 1:
            print(f"Error: Las filas y columnas deben ser mayores o iguales a 1")
            return False
        
        celda = (row, col)
        
        if celda not in self.cells:
            print(f"Advertencia: La celda ({row}, {col}) no existe. Use insertar_celda() para crearla.")
            return False
        
        valor_anterior = self.cells[celda]
        self.cells[celda] = nuevo_valor
        print(f"Celda ({row}, {col}) actualizada: {valor_anterior} -> {nuevo_valor}")
        return True
    
    def validar_celda(self, row, col):
        "Retorna True si la celda tiene informacion, sino retorna False."
        if row < 1 or col < 1:
            return False
        
        celda = (row, col)
        return celda in self.cells
    
    def mostrar_preview(self):
        """Muestra una vista visual de toda la hoja."""
        if self.max_row == 0 or self.max_col == 0:
            print("La hoja está vacía")
            return
        
        print("     ", end="")
        for col in range(1, self.max_col + 1):
            print(f"Col{col:2d}    ", end="")
        print()
        
        print("     ", end="")
        for col in range(1, self.max_col + 1):
            print("---------", end="")
        print()
        
        for row in range(1, self.max_row + 1):
            print(f"F{row:2d} |", end="")
            
            for col in range(1, self.max_col + 1):
                celda = (row, col)
                if celda in self.cells:
                    valor = self.cells[celda]
                    valor_str = str(valor)
                    if len(valor_str) > 8:
                        valor_str = valor_str[:5] + "..."
                    print(f" {valor_str:8s}", end="")
                else:
                    print(f" {'':8s}", end="")
            print()
        print()
    
    def suma_fila(self, row):
        """Recupera todos los elementos de una fila y los suma."""
        if row < 1:
            print("Error: El numero de fila debe ser mayor o igual a 1")
            return [], 0
        
        elementos = []
        suma = 0
        
        for col in range(1, self.max_col + 1):
            celda = (row, col)
            if celda in self.cells:
                valor = self.cells[celda]
                elementos.append(valor)
                
                if self._es_numero(valor):
                    suma += self._convertir_a_numero(valor)
        
        print(f"\nFila {row}:")
        print(f"Elementos: {elementos}")
        print(f"Suma de valores numericos: {suma}")
        
        return elementos, suma
    
    def suma_columna(self, col):
        """Recupera todos los elementos de una columna y los suma."""
        if col < 1:
            print("Error: El NUMERO de columna debe ser mayor o igual a 1")
            return [], 0
        
        elementos = []
        suma = 0
        
        for row in range(1, self.max_row + 1):
            celda = (row, col)
            if celda in self.cells:
                valor = self.cells[celda]
                elementos.append(valor)
                
                if self._es_numero(valor):
                    suma += self._convertir_a_numero(valor)
        
        print(f"\nColumna {col}:")
        print(f"Elementos: {elementos}")
        print(f"Suma de valores numericos: {suma}")
        
        return elementos, suma
    
    def obtener_valor(self, row, col):
        """Obtiene el valor de una celda."""
        celda = (row, col)
        return self.cells.get(celda, None)
    
    def limpiar_celda(self, row, col):
        """Limpia el contenido de una celda."""
        celda = (row, col)
        if celda in self.cells:
            del self.cells[celda]
            print(f"Celda ({row}, {col}) limpiada")
            return True
        else:
            print(f"La celda ({row}, {col}) ya esta vacia")
            return False
    
    def contar_celdas_con_datos(self):
        """Cuenta celdas con informacion."""
        return len(self.cells)
    
    def obtener_dimensiones(self):
        """Retorna (filas, columnas) maximas."""
        return (self.max_row, self.max_col)

hoja = ExcelSheet()
    
print("\n1. INSERTAR INFORMACION EN UNA CELDA")

# Insertar algunos valores
hoja.insertar_celda(1, 1, "Producto")
hoja.insertar_celda(1, 2, "Precio")
hoja.insertar_celda(1, 3, "Cantidad")
hoja.insertar_celda(1, 4, "Total")
    
hoja.insertar_celda(2, 1, "Laptop")
hoja.insertar_celda(2, 2, 15000)
hoja.insertar_celda(2, 3, 2)
hoja.insertar_celda(2, 4, 30000)
    
hoja.insertar_celda(3, 1, "Mouse")
hoja.insertar_celda(3, 2, 250)
hoja.insertar_celda(3, 3, 5)
hoja.insertar_celda(3, 4, 1250)
    
hoja.insertar_celda(4, 1, "Teclado")
hoja.insertar_celda(4, 2, 800)
hoja.insertar_celda(4, 3, 3)
hoja.insertar_celda(4, 4, 2400)
    
print(f"Celdas con datos: {hoja.contar_celdas_con_datos()}")
    
print("\n2. ACTUALIZAR INFORMACION EN UNA CELDA")
hoja.actualizar_celda(2, 2, 14500)

print("\n3. VALIDAR CELDAS")
print(f"¿Celda (2, 2) tiene datos? {hoja.validar_celda(2, 2)}")
print(f"¿Celda (5, 5) tiene datos? {hoja.validar_celda(5, 5)}")
    
print("\n4. PREVIEW DE LA HOJA")
hoja.mostrar_preview()

# SUMAS DE FILAS Y COLUMNAS

print("\n5. SUMA DE FILA 2")
hoja.suma_fila(2)
    
print("\n6. SUMA DE COLUMNA 2 (Precio)")
hoja.suma_columna(2)
    
print("\n7. SUMA DE COLUMNA 4 (Total)")
hoja.suma_columna(4)
    
print("\n8. OBTENER VALOR ESPECIFICO")
valor = hoja.obtener_valor(3, 1)
print(f"Valor en celda (3, 1): {valor}")
    
print("\n9. DIMENSIONES DE LA HOJA")
filas, columnas = hoja.obtener_dimensiones()
print(f"Dimensiones: {filas} filas x {columnas} columnas")
    