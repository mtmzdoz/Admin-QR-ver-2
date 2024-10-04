nombre = input("Nombre: ")
mascota = input("Nombre de su mascota: ")
continuar = True
while continuar:
    contraseña = input("Contraseña propuesta (FIN para terminar): ")
    if contraseña.upper() == "FIN":
        continuar = False
    else:
        tinene_espacio = " "
        len_ok = len(contraseña) >= 10
        tiene_minusculas = False
        tiene_mayusculas = False
        tiene_digitos = False
        tiene_caracteres_especiales = False
        esta_nombre_mascota = nombre.lower() in contraseña.lower() or mascota.lower() in contraseña.lower()
        patron_repeticion = False
        for caracter in contraseña:
            if 'a' <= caracter <= 'z':
                tiene_minusculas = True
            elif 'A' <= caracter <= 'Z':
                tiene_mayusculas = True
            elif '0' <= caracter <= '9':
               tiene_digitos = True
            elif caracter in "¡!¿?@#$%&_-+*=|{}[].,;:<>/\\~^'\"":
                tiene_caracteres_especiales = True
        i = 0
        while i < len(contraseña) - 4 and not patron_repeticion:
            if contraseña[i] == contraseña[i+1] == contraseña[i+2] == contraseña[i+3] == contraseña[i+4]:
                patron_repeticion = True
                patron_repetido = contraseña[i:i+5]
            i += 1
        no_valida = True
        while no_valida:
            if not len_ok:
                print("Contraseña muy corta, debe tener al menos 10 caracteres.")
                no_valida = False
            elif not tiene_minusculas:
                print("Debe incluir letras minúsculas.")
                no_valida = False
            elif not tiene_mayusculas:
                print("Debe incluir letras mayúsculas.")
                no_valida = False
            elif not tiene_digitos:
                print("Debe incluir dígitos numéricos.")
                no_valida = False
            elif not tiene_caracteres_especiales:
                print("Debe incluir caracteres especiales válidos.")
                no_valida = False
            elif esta_nombre_mascota:
                print("Contraseña no debe incluir su nombre ni el de su mascota.")
                no_valida = False
            elif patron_repeticion:
                print(f"Contraseña no debe contener patrones: {patron_repetido}")
                no_valida = False
            else:
                print("Contraseña válida!")
                no_valida = False