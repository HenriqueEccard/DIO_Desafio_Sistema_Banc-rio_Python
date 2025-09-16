# Sistema Bancário Simples
# Autor - Henrique Leite
#Última alteração: Incluído data e hora e limite de 10 transações

from datetime import datetime



# VARIÁVEIS
saldo =0
limite = 500
# extrato=""
numero_saque=0
LIMITE_SAQUES = 3
LIMITE_TRANSACOES = 10

#Depósito
''' - Depositar apenas valores positivos e inteiros;
    - Apenas um usuário;
    - Depósitos devem ser armazenados em uma variável e exibida em extrato;
    - '''
depositos = []
transacoes = []
saques=[]


def contador_transacoes_hoje():
   #Contar quantas transações foram feitas hoje
    hoje = datetime.now().date()
    return sum(1 for t in transacoes if t["data"].date() == hoje)

def depositar(valor):
    print('---------- OPERAÇÃO DE DEPÓSITO ----------')
    global saldo 

    if contador_transacoes_hoje()>= LIMITE_TRANSACOES:
       print ('Limite de 10 transações diárias atingido. Operação não permitida.')
       return
    
    if valor>0:
        print (f"Depósito realizado com Sucesso - Valor R$ {valor:.2f}")
        depositos.append(f'Depósito = R$ {valor:.2f}')
        saldo+=valor
        transacoes.append({
           "tipo": "Depósito",
           "valor": valor,
           "data": datetime.now()
        })      

        print (f"-- Saldo Atualizado Após Depósito: R$ {saldo}")

    else:
        print ("Você não digitou um número inteiro, refaça a operação")

    return (valor)


 #Saque 

''' - 03 Saques diários
    - Limite de R$ 500,00 por saque
    - Se não tiver saldo: Não será possível sacar o dinheiro por falta de saldo
    - Todos os saques devem ser armazenados em uma variável e exibidas em extrato
    - '''


def sacar(valor):
    print('---------- OPERAÇÃO DE SAQUE ----------')
    global saldo 
    
    if contador_transacoes_hoje()>= LIMITE_TRANSACOES:
       print ('Limite de 10 transações diárias atingido. Operação não permitida.')
       return


    if saldo > 0: 
        print (f"Saque realizado com Sucesso - Valor R$ {valor:.2f}")
        saldo-=valor
        saques.append(f'Saque = R$ {valor:.2f}')
        print (f"-- Saldo Atualizado Após Saque: R$ {saldo}")
        transacoes.append({
           "tipo": "Saque",
           "valor": valor,
           "data": datetime.now()
        })    


    else:
        print(f"Saldo insuficiente para saque: Saldo Atual = R$ {saldo:.2f}")
        
    return (valor)

#Extrato
''' - Listar todos os depósitos
    - Listar todos os saques
    - Fim da listagem exibir saldo atual da conta
    - formato que deve ser exibido: R$ xxx.xx'''

def extrato():
    print('---------- EXTRATO BANCÁRIO ----------')
    if not transacoes:
       print ("Nenhuma transação realizada")
    else:
           
        for t in transacoes:
            data_formatada = t["data"].strftime('%d/%m/%Y %H:%M')
            print (f'{t['tipo']} = R$ {t['valor']:.2f} | {data_formatada}')
    print (f'Saldo Atual: R$ {saldo:.2f}')
    print (f'Número transaçoes hoje: {contador_transacoes_hoje()}/{LIMITE_TRANSACOES}')
   
menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor_depositar =input("Digite um valor para depositar: ") 
        valor_depositar_int = int(valor_depositar)
        if valor_depositar_int:
         depositar(valor_depositar_int)
        else:
           print("Digite um valor inteiro para depositar")
        
   
    elif opcao == "s":
        print("Saque")
        valor_sacar =input("Digite um valor para sacar: ") 
        valor_sacar_int = int(valor_sacar)
        if valor_sacar_int:
         sacar(valor_sacar_int)
        else:
           print("Digite um valor inteiro para sacar")
   
    elif opcao == "e":
        print("Extrato")
        extrato()
   
    elif opcao == "q":
        print("Sair")
        break
    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada")
        