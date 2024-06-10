


def es_palindromo(s):
    string_limpio = "".join(caracter.lower() for caracter in s if caracter.isalnum())
    return string_limpio == string_limpio[::-1]


print(es_palindromo("anita lava la tina"))
print(es_palindromo("Dabale arroz a la zorra el abad"))
print(es_palindromo("hola"))