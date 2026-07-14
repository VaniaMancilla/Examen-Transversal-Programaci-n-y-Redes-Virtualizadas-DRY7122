# Solicitar número de AS
as_number = int(input("Ingrese el número de AS: "))

# Validación
if (64512 <= as_number <= 65534) or (4200000000 <= as_number <= 4294967294):
    print("El AS es PRIVADO")
else:
    print("El AS es PÚBLICO")
