class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    def getNome(self):
        return self.__nome

    def getMatricula(self):
        return self.__matricula


class Professor:
    def __init__(self, nome, id):
        self.__nome = nome
        self.__id = id

    def getNome(self):
        return self.__nome

    def getId(self):
        return self.__id


class Curso:
    def __init__(self, nome, professores=[], alunos=[]):
        self.__nome = nome
        self.__professores = professores
        self.__alunos = alunos

    def getNome(self):
        return self.__nome

    def getProfessores(self):
        return [professor.getNome() for professor in self.__professores]

    def getAlunos(self):
        return [aluno.getNome() for aluno in self.__alunos]

    def addProfessor(self, professor):
        if professor not in self.__professores:
            self.__professores.append(professor)

    def remProfessor(self, professor):
        if professor in self.__professores:
            self.__professores.remove(professor)

    def addAluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)

    def remAluno(self, aluno):
        if aluno in self.__alunos:
            self.__alunos.remove(aluno)

    def listarAlunos(self):
        return [f"Nome: {aluno.getNome()}, Matrícula: {aluno.getMatricula()}" for aluno in self.__alunos]


aluno1 = Aluno("Andreas Gabriel Nascimento Lázaro", "1881")
aluno2 = Aluno("Daniel Pinheiro de França", "2424")

professor1 = Professor("Luciano", "001")

curso = Curso("Eng. de software")

curso.addProfessor(professor1)

curso.addAluno(aluno1)
curso.addAluno(aluno2)

print("Curso: ", curso.getNome())
print("Professores:", curso.getProfessores())
print("Alunos:", curso.getAlunos())
print("Lista detalhada de alunos:")
for aluno in curso.listarAlunos():
    print(aluno)
