#Operadores Condicionais
#Condicionais Simples

#Verifique se um numero é positivo
numero = 5

if numero > 5:
  print("Numero Positivo")
else:
  print("Numeor Negativo")

#Verificar se uma palavra tem mais de 5 caracteres
palavra = "qualquer"
if len(palavra) > 5:
  print("tem mais que 5 caracteres")
else:
  print("tem menos que 5 caracteres")


#verificar se o ano é bissexto

ano = 2024
if(ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
  print("O ano é bissexto")
else:
  print("O ano nao é bissexto")
  
#2.5.2 Composta
# Verificar se um numero esta entre 10 e 20.

numero = 15
if numero >= 10 and numero <= 20:
  print("O numero esta entre 10 e 20")
else:
  print("O numero não esta entre 10 e 20")
  
#Verifique se uma string contem letras e numero.

string = "abc123"
if any(c.isalpha() for c in string) and any(c.isdigit() for c in string):
  print("A string possui letras e numeros")
else:
  print("A string nao possui letras e numeros")
  

#Verificar faixa etaria de uma pessoa pela idade
idade = 25

if idade < 13:
  print("Criança")
elif idade < 18:
  print("Adolescente")
elif idade < 60:
  print("Adulto")
else:
  print("Idoso")
  
  
# Determine a estaçao di ano baseado no mes (primavera, verao, outono, inverno)

mes = 5

if mes in [6, 7, 8]:
  print("Inverno")
elif mes in [9,10,11]:
  print("Primavera")
elif mes in [3, 4, 5]:
  print("Outono")
elif mes in [12, 1, 2]:
  print("Verao")
else:
  print("Mes Invalido")
  
for i in range(1,11):
  print(i)

#imprima os elementos de uma lista. 
lista = [1,2,3,4,5]
print(lista)

#imprima os elementos de um dicionario

dicionario = {"a":1,"b":2,"c":3}
for chave, valor in dicionario.items():
  print(f"chaves:{chave}, valor:{valor}")


#Imprima os números de 1 a 10 usando um laço while. 
i = 1
while i <= 10:
  print(i)
  i += 1
  























