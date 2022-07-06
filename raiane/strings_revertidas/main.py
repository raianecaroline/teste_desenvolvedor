# coding=utf-8

digitar_string = str(raw_input("Digite aqui a string que deverá ser invertida!\n"))

new_string = ''
index = len(digitar_string)
while index:
    index -= 1
    new_string += digitar_string[index]

print('\033[92m' + new_string)
