print("Calculadora de impuestos")
print('')

sa = input("Ingrese su Salario Anual: ")
ec = input("Ingrese su Estado Civil: ")

print('')

#Verifica que el salario anual sea un numero y no un string
try:
    sa = int(sa)
except:
    print("No es un salario valido")

##Calcula el impuesto para los solteros
if ec == "Soltero" or ec == "soltero" and sa <= 30000:
    tasa = 0.1
    imp = sa * tasa
    print("Impuesto a pagar:", imp)

if ec == "Soltero" or ec == "soltero" and 30000 < sa <= 70000:
    tasa = 0.2
    imp = sa * tasa
    print("Impuesto a pagar:", imp)

if ec == "Soltero" or ec == "soltero" and 70000 < sa:
    tasa = 0.3
    imp = sa * tasa
    print("Impuesto a pagar:", imp)

##Calcula el impuesto para los casados
if ec == "Casado" or ec == "casado" and sa <= 40000:
    tasa = 0.08
    imp = sa * tasa
    print("Impuesto a pagar:", imp)

if ec == "Casado" or ec == "casado" and 40000 < sa <= 90000:
    tasa = 0.15
    imp = sa * tasa
    print("Impuesto a pagar:", imp)

if ec == "Casado" or ec == "casado" and 90000 < sa:
    tasa = 0.25
    imp = sa * tasa
    print("Impuesto a pagar:", imp)
    