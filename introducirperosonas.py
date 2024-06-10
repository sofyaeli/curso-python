while True:
    a=input("Por favor, introduce tu nombre: ")
    b=input("Por favor, introduce tu apellido: ")
    c=input("Por favor, introduce tu direccion: ")
    
    with open("/Users/cazar/desktop/personas.txt", "a") as archivo:
      archivo.write(f"Nombre= {a}, Apellido= {b}, Direccion= {c}\n")
    

    f=input("quieres continuar? (s/n): ")
    if f =="s":
        break
