import math #Importa una libreria
print("ingresa tu rut sin digito verificador")
num1 = int(input(":" ))#Variables a la que se le ingresa el rut
num2 = int(input(":" ))
num3 = int(input(":" ))
num4 = int(input(":" ))
num5 = int(input(":" ))
num6 = int(input(":" ))
num7 = int(input(":" ))
num8 = int(input(":" ))
multiplicacionYSuma = num8*2 + num7*3 + num6*4 + num5*5 + num4*6 + num3*7 + num2*2 + num1*3 #La variable multiplica y suma los numeros del rut
division = multiplicacionYSuma/11 #En la variable division se divide la variable multiplicacionYSuma por 11
divMul = math.trunc(division)*11 #Acá quitamos los decimales y la aproximación de la división, y multiplica por 11
resta6 = multiplicacionYSuma - divMul #Acá se está restando las variables
resultado = 11-resta6 #Acá se da el digito verificador
if resultado == 11:
    resultado = 0
    print("su digito verificador es: 0")
elif resultado == 10:
    resultado = "k"
    print("su digito verificador es: k")
else:
    print ("su digito verificador es:" + str(resultado))

def crearTxt():
    archivo.write(str(num1) + str(num2) + str(num3) + str(num4) + str(num5) +  str(num6) + str(num7) + str(num8) +"-"+ str(resultado) + " \ " )
    archivo.close()
archivo = open("Rut.txt","a")
crearTxt()