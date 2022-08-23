# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';

nome = input('insira um nome maior que 3 caracteres: ')

while len(nome) <= 3:
    print('nome invalido') 
    nome = input('insira um nome maior que 3 caracteres: ')
    
idade = int(input('insira uma idade entre 0 a 150 anos: '))

while idade < 0 or idade > 150:
    print('idade invalida')
    idade = int(input('digite uma idade valida: '))
    
salario = float(input('informe seu salario, o salario tem que ser maior que zero: '))

while salario <= 0:
    print('salario invalido')
    salario = float(input('informe um salario valido: '))
    
sexo = input('insira seu sexo de acordo com F para feminino e M para masculino. ')


while sexo.lower() != 'f' and sexo.lower() != 'm':
    print('sexo invalido')
    sexo = input('digite um sexo valido. F para feminino e M para masculino: ')
if sexo.lower() == 'm':
        sexo = 'masculino'
elif sexo.lower() == 'f':
        sexo = 'feminino'
    
estado_civil = input('insira seu estado civil. Sendo S para solteiro, C para casado, V para viuvo e D para divorciado: ')

while estado_civil.lower() != 'c' and estado_civil.lower() != 's' and estado_civil.lower() != 'd' and estado_civil.lower() != 'v':
    print('estado civil invalido')
    estado_civil = input('informe um estado civil valido:')
if estado_civil.lower() == 'c':
    estado_civil = 'casado'
elif estado_civil.lower() == 's':
    estado_civil = 'solteiro'
elif estado_civil.lower() == 'd':
    estado_civil = 'divorciado'
elif estado_civil.lower() == 'v':
    estado_civil = 'viuvo'
    
print(f'nome: {nome}')
print(f'idade: {idade}')
print(f'salario: {salario}')
print(f'seu sexo é {sexo}')
print(f'estado civil: {estado_civil}')
