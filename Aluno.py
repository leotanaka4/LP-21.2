class Aluno:
    def __init__(self, nome, dre):
        self.nome = nome
        self.dre = dre

class Aluno_grad(Aluno):
    def __init__(self, nome, dre, nota1, nota2, nota3, nota4, nota5, nota6):
        super().__init__(nome, dre)
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
        self.nota5 = nota5
        self.nota6 = nota6

    def media_grad(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4 + self.nota5 + self.nota6)/6

class Aluno_pos(Aluno):
    def __init__(self, nome, dre, nota1, nota2):
        super().__init__(nome, dre)
        self.nota1 = nota1
        self.nota2 = nota2
    
    def media_pos(self):
        somatorio = 0
        if (self.nota1 == "A"):
            somatorio += 3
        elif (self.nota1 == "B"):
            somatorio += 2
        elif (self.nota1 == "C"):
            somatorio += 1
        elif (self.nota1 == "D"):
            somatorio += 0
        else:
            print("Fez besteira!")

        if (self.nota2 == "A"):
            somatorio += 3
        elif (self.nota2 == "B"):
            somatorio += 2
        elif (self.nota2 == "C"):
            somatorio += 1
        elif (self.nota2 == "D"):
            somatorio += 0
        else:
            print("Fez besteira!")
        
        media = somatorio/2
        if (media > 0 and media <= 3):
            if (media <= 3 and media > 2.5):
                string_media = "A"
            elif (media <= 2.5 and media > 1.5):
                string_media = "B"
            elif (media <= 1.5 and media > 0.5):
                string_media = "C"
            elif (media <= 0.5):
                string_media = "D"
        else:
            print("Deu ruim!")
        return string_media 

print("Bem-vindo ao calculador de médias na UFRJ!")
teste1 = Aluno_grad( "Leonardo", 9999999, 5, 6, 7, 8, 9, 10)
teste2 = Aluno_pos("Emilly", 111111, "A", "C")
print(vars(teste1))
print(vars(teste2))