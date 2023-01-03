palindromo = str(input("palabra: "))
palindromo = palindromo.lower()
palindromo = palindromo.replace(" ", "")
palindromo = palindromo.replace("á", "a")
palindromo = palindromo.replace("é", "e")
palindromo = palindromo.replace("í", "i")
palindromo = palindromo.replace("ó", "o")
palindromo = palindromo.replace("ú", "u")
if palindromo == palindromo[::-1]:
    print("Es palindromo")
else:
    print("No es palindromo")
