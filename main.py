#===[Inicio de Programa]===========================================#
print("="*60)
print("=============[Bienvenido al Cajero Automático]==============")
print("="*60)

#===[Ingreso de Datos y Validación]==========================================#
item = input("Ingresar nombre del Articulo: ")

valid = True
while valid == True:
    try:
        price = float(input("Ingresar precio del Articulo: "))
        amount = int(input("Ingresar cantidad de Articulos vendidos: "))
        
#===[Cálculo del Venta]==========================================#
        total = price * amount
        
        valid = False
        
#===[Resumen de Venta]==========================================#
        print("-"*60)
        print("Resumen de Venta.......")
        print("Articulo.......: ", item)
        print("Precio.........: ", price)
        print("Cantidad.......: ", amount)
        print("Total..........: ", total)
        print("-"*60)
    
#===[Manejo de Errores]==========================================#
    except ValueError:
        print("Error: Por favor ingrese un valor numérico válido para Precio y Cantidad")