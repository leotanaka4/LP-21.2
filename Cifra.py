global alfabeto
alfabeto = "abcdefghijklmnopqrstuvwxyz"

def cifra(n,salto):
    j = ""
    #para cada letra na minha palavra
    for i in n:
        # para cada carctere na minha lista de caracteres
        if i in alfabeto:
            #acha a posição da letra na string
            num = alfabeto.find(i)
            if (num+salto >=len(alfabeto)):
                #% é a função módulo ex: 28%26 == 2
                num = (num+salto)%len(alfabeto)
                j +=alfabeto[num]
            else:
                j +=alfabeto[num+salto]
        else:
            j += 1
            print("Caractere não encontrado")
    return j
    


def decifra(n, salto):
    j = ""
    for i in n:
        # para cada carctere na minha lista de caracteres
        if i in alfabeto:
            #acha a posição da letra na string
            num = alfabeto.find(i)
            if (num+salto >=len(alfabeto)):
                #% é a função módulo ex: 28%26 == 2
                num = (num-salto)%len(alfabeto)
                j +=alfabeto[num]
            else:
                j +=alfabeto[num-salto]
        else:
            j += 1
            print("Caractere não encontrado")
    return j

c = " "
while(1):
    c = input("Digite a mensagem a ser cifrada: ")
    if (c=="FIM"): break
    n = c.lower()
    d = cifra(n,4)
    cd = decifra(d,4)
    print ("A mensagem cifrada é: "+d+"\n")
    print("A mensagem decifrada é: "+cd+"\n")