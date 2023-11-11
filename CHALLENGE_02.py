# En el mundo del espionaje, se utiliza un lenguaje de codificación con símbolos que realizan operaciones matemáticas simples.
#
# Tu tarea es crear un mini compilador que interprete y ejecute programas escritos en este lenguaje de símbolos.
#
# Las operaciones del lenguaje son las siguientes:
#
# "#" Incrementa el valor numérico en 1.
# "@" Decrementa el valor numérico en 1.
# "*" Multiplica el valor numérico por sí mismo.
# "&" Imprime el valor numérico actual.
# El valor numérico inicial es 0 y las operaciones deben aplicarse en elorden en que aparecen en la cadena de símbolos.

script_1 = "##*&"
script_2 = "&##&*&@&"
script_test = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

def compiler(script: str) -> str:
    ans = ""
    current_number = 0
    script_char_array = list(script)

    for element in script_char_array:
        if element == '#':
            current_number += 1
        if element == '@':
            current_number -= 1
        if element == '*':
            current_number = current_number**2
        if element == '&':
            ans = ans + str(current_number)

    return ans

print(compiler(script_1))
print(compiler(script_2))
print(compiler(script_test))