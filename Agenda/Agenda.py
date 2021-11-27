print("Bem vindo a minha agenda!")

print("O que você deseja fazer?")

def Inserir():
    nome = input("Nome: ")
    tel = input("Telefone: ")
    end = input("Endereço: ")
    dados = nome+"/"+tel+"/"+end+"\n"
    print("Seus dados são: ", dados)
    arquivo = open("contatos.txt","a")
    arquivo.writelines(dados)

def Buscar():
    busca = input("Busca: ")
    arquivo = open("contatos.txt", "r")
    leitura = arquivo.readlines()
    linhas = len(leitura)
    for i in range(linhas):
        resultado = leitura[i].count(busca)
        if (resultado > 0):
            print(leitura[i])

def Remover():
    apagado = input("Apagado: ")
    arquivo = open("contatos.txt", "r")
    leitura = arquivo.readlines()
    linhas = len(leitura)
    for i in range(linhas):
        resultado = leitura[i].count(apagado)
        if (resultado>0):
            leitura.pop(i)
    arquivo = open("contatos.txt", "w")
    arquivo.writelines(leitura)

def Editar():
    editado = input("Editado: ")
    arquivo = open("contatos.txt", "r")
    leitura = arquivo.readlines()
    linhas = len(leitura)
    for i in range(linhas):
        resultado = leitura[i].count(editado)
        if (resultado>0):
            nome = input("Nome: ")
            tel = input("Telefone: ")
            end = input("Endereço: ")
            dados = nome+"/"+tel+"/"+end+"\n"
            print("Novos dados são: ", dados)
            leitura[i] = dados
    arquivo = open("contatos.txt", "w")
    arquivo.writelines(leitura)

comando = ""

while (comando != "FIM"):
    a = input("Digite Inserir/Buscar/Remover/Editar/FIM \n")
    if (a == "Inserir"):
        Inserir()
        pass
    elif(a == "Buscar"):
        Buscar()
        pass
    elif(a == "Remover"):
        Remover()
        pass
    elif(a == "Editar"):
        Editar()
        pass
    elif(a == "FIM"):
        comando = a
    else:
        print("Essa opção não existe")