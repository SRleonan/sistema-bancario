menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True: 
    
   
         opcao = input(menu)
    
         if opcao == "1":
            valor = float(input("informe o valor depositado: "))
       
            if valor > 0:
               saldo += valor
               extrato += f"Deposito: R$ {valor:.2f}/n"
            else:
             print("operação falhou")   
           
         elif opcao == "2":
          valor = float(input("informe o valor a ser sacado: "))
          excedeu_saldo = valor > saldo
          excedeu_limite = valor > limite
          excedeu_saques = numero_saques >= LIMITE_SAQUE
        
          if excedeu_saldo or excedeu_limite or excedeu_saques:
               print("operação falhou")
            
          elif valor > 0 :
                  saldo -= valor
                  extrato += f"saque: R$ {valor:.2f}\n"
            
          else:
            print("operação falhou!, Valor invalido")
            
         elif opcao == "3":
            print("\n==================================EXTRATO=====================================")
            print("Não foram relizado Movimentaçoes." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("===============================================================================")
            
         elif opcao == "0":
            break
         
         else:
            print("opção invalida, por favor selecionar novamente a opção desejada ")