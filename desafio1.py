palindromo = str(input("palabra: "))

if palindromo == ''.join(reversed(palindromo)):
    print("Es palindromo")
else:
    print("No es palindromo")
