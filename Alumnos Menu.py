contacto = {
   "Nombre": input("Ingrese nombre: "),
   "Edad": int(input("Ingrese edad: ")),
   "Telefono": input("Ingrese telefono: "),
   "Email": input("Ingrese email: ")
   
 }
while True:
 print("___MENU___")
 print("1) Ver ficha")
 print("2) Editar dato")
 print("3) Salir")

 opcion=int(input("Ingrese una opción: "))

 
 if opcion == 1:
   print(contacto)

 elif opcion == 2:
    editar =input("¿Que campo deseas editar?: ")
    nuevo= input("Ingrese el nuevo dato: ")
    contacto[editar] = nuevo
    
 elif opcion == 3:
   print("Saliendo...")
   break
 
 print(contacto)