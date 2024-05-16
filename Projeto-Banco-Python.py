# --- tela inicial ---
deposito = float
saldo = float
SAQUE_MAXIMO = 500
LIMITE_DE_SAQUES = 3

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

# --- Saque,deposito e extrato --- 
destinatario = str
if OPCAO == 1:
    float(input("Insira o valor do depósito:"))
    destinatario = (input("Destino do depósito:"))
    str(input("Você tem certeza?"))
    print(f"Seu depósito para {destinatario}, foi realizado com sucesso !")
    while deposito :
        
elif OPCAO == 2:
    float(input("Insira o valor do saque:")) 
    input("Voce tem certeza?")
    print("Sacando...")
    while SAQUE_MAXIMO >= 500:
       print("ERROR : Infelizmente, so podemos sacar ate R$ 500 diariamente. ")
       break



  

