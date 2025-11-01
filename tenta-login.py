entrada = input().strip()  

# Divide a string em uma lista, removendo espaços e mantendo tudo minúsculo por segurança
tentativas = [item.strip().lower() for item in entrada.split(',')]

# Inicializa o contador de falhas consecutivas
falhas_consecutivas = 0

# TODO: Percorra cada tentativa da lista:
for tentativa in tentativas:
  # Verifica se a tentativa foi uma falha
  
  if tentativa == "falha":
    # TODO: Incremente se for uma falha:
    falhas_consecutivas += 1
    # Imprime e encerra se houver 3 ou mais falhas seguidas
    if falhas_consecutivas >= 3:
      print("Conta Bloqueada")
      break
  else:
    falhas_consecutivas = 0  
else:
  # TODO: Se o loop NÃO for interrompido por um break, retorne, Acesso Normal:
  print("Acesso Normal")