from pessoas import Pessoa
from usuarios import Usuario

class Professor(Pessoa, Usuario):

    def __init__(self):
        self.apelido = apelido
        self.disciplinas = []
        self.ra = ra
        self.nome = nome
        self.email = email  
        self.celular = celular 

    def adiciona_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)

    def disciplinas_professor(self):
        return self.disciplinas

    def remove_disciplina(self, disciplina):
        for d in self.disciplinas:
            if d.retorna_nome() == disciplina.retorna_nome():
                self.disciplinas.remove(d)
                break
        

    

