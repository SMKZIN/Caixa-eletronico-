# --- tela inicial ---
extrato = True
deposito = True
saldo = 0
saque = float
MAX_SAQUES_POR_DIA = 3
VALOR_MAXIMO_SAQUE = 500
saques_feitos= 0

print("""         -------- Banco XI --------
      
                 Bem vindo! :)
                 
          ------------------------             
            Acesse sua conta XI: 


 """)

# --- login ---

login = str(input("#Login:"))
senha = int(input("#Senha:"))
print(f"bank: Você entrou como {login}!")

# --- opçoes de entrada ---
print(f"""   -------- Banco XI -------- 
      
        Bem vindo {login}!

         1 - Depósito
         2 - Saque    
         3 - Extrato

   --------------------------
      """)

# --- estrutura condicional ---
OPCAO = int(input("Escolha uma opção:"))

if OPCAO == 1 :
    print("Abrindo opções de depósito....") 
elif OPCAO == 2:
    print("Abrindo opções de saque...") 
elif OPCAO == 3:
    print("Exibindo extrato bancário...")

# --- Deposito --- 

if OPCAO == 1:
    deposito = float(input("Insira o valor do depósito:"))
    destinatario = (input("Destino do depósito:"))
    confirmaçao = (input("Você tem certeza? (sim/não):"))
    if confirmaçao.lower() == "sim":
        saldo += deposito  
        print(f"Seu depósito para {destinatario} no valor de R$ {deposito}, foi realizado com sucesso !")
        print(f"Saldo atual : {saldo}")
    else:
        print("Operação cancelada.")
     
 # --- saque ---
       
elif OPCAO == 2:
    # Verificar se já excedeu o número máximo de saques permitidos
    if saques_feitos >= MAX_SAQUES_POR_DIA:
        print("Você já atingiu o limite de saques para hoje.")
    else:
        # Solicitar o valor do saque
        saque = float(input("Insira o valor do saque:")) 
        # Verificar se o valor do saque excede o limite máximo
        if saque > VALOR_MAXIMO_SAQUE:
            print(f"O valor máximo de saque é de R$ {VALOR_MAXIMO_SAQUE}.")
        else:
            confirmacao = input("Você tem certeza? (sim/não): ")
            if confirmacao.lower() == "sim":
                # Atualizar o número de saques feitos no dia
                saques_feitos += 1
                print("Sacando...")
            else:
                print("Operação cancelada.")
 # --- Extrato --- 

while extrato:
    
    print(f"""    -------- Banco XI -------- 
          
          // EXTRATO //
             
    - Saldo em Conta : {saldo}
    - Conta : {login}
    - Naturalidade : Brasil, Minas Gerais                
    - Data : 12/04/2024
    - Hora : 12:14
    --------------------------

    Obrigado pela preferência :)
          """)
    break
    
