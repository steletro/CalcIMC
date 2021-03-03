print('Cálculo de IMC')
#Primeira tentativa de fazer um programa realmente
print('Seja bem vinda, pessoa.')
print('Meu nome é bot.')
print('(meu criador não é muito criarivo.)')
h = float(input('Qual a sua altura?_ '))
p = float(input('Qual o seu peso?_'))
imc=(p/(h*h))
print('Seu IMC é:')
print('xxxxxxxxxx')
print(round(imc, 1))
print('xxxxxxxxxx')
if imc < 18.5:
      print('Abaixo do peso')
if imc >= 18.5 and imc <25:
   print('Abaixo do peso')
if imc >= 25:
   print('Acima do peso')
print('Fim do programa')
print('Para Susan, meu amor.')