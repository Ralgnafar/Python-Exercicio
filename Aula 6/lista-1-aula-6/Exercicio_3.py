# 3.Faça um programa que receba uma string e retorne uma nova string substituindo: 
#'a' por '4' 'e' por '3' 'I' por '1' 't' por '7'
def substituir_caracteres(string):
    string = string.replace('a', '4')
    string = string.replace('e', '3')
    string = string.replace('I', '1')
    string = string.replace('t', '7')
    return string
entrada = input(" Digite uma string: ")
resultado = substituir_caracteres(entrada)
print(" String original: ", entrada)
print(" String substituída: ", resultado)
