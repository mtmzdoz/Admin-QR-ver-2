nombre=input("Nombre: ")
mascota=input("Nombre de su mascota: ")

flag=True
while flag:
    contraseña=input("Contraseña propuesta (FIN para terminar): ")
    if contraseña.upper()=="FIN":
        flag=False
    else:        
        if len(contraseña)<10:
            print("Contraseña muy corta, debe tener al menos 10 caracteres.")
        elif mascota.lower() in contraseña.lower():
            print("Contraseña no debe incluir el nombre de su mascota.")
        elif nombre.lower() in contraseña.lower():
            print("Contraseña no debe incluir su nombre.")
        else:
        #Para saber si hay algun patrón en la contraseña
            reps=""
            pos=0
            i=0
            repeticiones=True
            repetido=False
            #En este caso se imprimira el patron completo que se haya localizado, pero si solo se quiere imprimir el patron de 5 añadir "and repeticiones: y repeticiones=False" 
            while pos<len(contraseña) :#and repeticiones:
                if pos>0: 
                    
                    if contraseña[pos]==contraseña[pos-1]:
                        i+=1
                        reps+=contraseña[pos-1]
                        N=reps+contraseña[pos]
                    else:
                        reps=""
                        i=0
                    if i>=4:
                        repetido=True
                        #repeticiones=False

                pos+=1      
        #Para saber si hay cierto caracter dentro de la contraseña
            minusculas=False
            mayusculas=False
            especiales=False
            digitos=False
            otros_caracteres=False #Otros caracteres serian los no validos como el espacio, ( ), Ç, etc.
            
            for caracteres in contraseña :
                if caracteres in ("abcdefghijklmnñopqrstuvwxyzáéíóú"):
                    minusculas=True
                elif caracteres in ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚ"):
                    mayusculas=True
                elif caracteres in ("¡!¿?@#$%&_-+*=|{}[].,;:<>/\\~^'"""):
                    especiales=True
                elif caracteres in ("1234567890"):
                    digitos=True
                else:
                    otros_caracteres=True 
           #Para que la condicion no cumplida se imprima 1 sola vez 
            prints=True
            while prints:
                if not mayusculas:
                    print("Debe incluir letras mayúsculas.")
                    prints=False
                elif not minusculas:
                    print("Debe incluir letras minúsculas.")
                    prints=False
                elif not digitos:
                    print("Debe incluir dígitos numéricos.")
                    prints=False
                elif otros_caracteres:
                    print("La contraseña contiene caracteres inválidos.")
                    prints=False
                elif not especiales:
                    print("Debe incluir caracteres especiales válidos.")
                    prints=False
                elif  repetido:
                    print("Contraseña no debe contener patrones:",N)
                    prints=False
                else:
                    print("Contraseña válida!")
                    prints=False      
        
    
    
    
            
    
    
        

    
    

        
        

