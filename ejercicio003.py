email = input("Ingrese su correo electrónico: ")

if "@" not in email:
    print("Error: El email debe contener @")
elif "." not in email:
    print("Error: El email debe contener un punto")
elif email.count("@") != 1:
    print("Error: El email debe contener solamente una @")
elif (email.find(".") - 1) != email.find("@"):
    print("Error: Debe existir un punto después de la @")
else:
    # Extraer el dominio (después del punto)
    dominio = email.split(".")[-1]
    if len(dominio) < 2 or len(dominio) > 3 or dominio not in ["com", "org", "es"]:
        print("Error: El dominio debe tener entre 2 y 3 caracteres")
    else:
        print("Email válido")