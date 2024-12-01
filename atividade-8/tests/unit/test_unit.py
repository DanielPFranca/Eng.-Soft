import pytest
from app.main import Aluno, Professor, Curso

# Fixtures
@pytest.fixture
def aluno1():
    return Aluno("Andreas Gabriel Nascimento Lázaro", "1881")

@pytest.fixture
def aluno2():
    return Aluno("Daniel Pinheiro de França", "2424")

@pytest.fixture
def professor1():
    return Professor("Luciano", "001")

@pytest.fixture
def curso(professor1, aluno1, aluno2):
    curso = Curso("Eng. de software")
    curso.addProfessor(professor1)
    curso.addAluno(aluno1)
    curso.addAluno(aluno2)
    return curso

# Testes para Aluno
def test_aluno_nome(aluno1):
    assert aluno1.getNome() == "Andreas Gabriel Nascimento Lázaro"

def test_aluno_matricula(aluno1):
    assert aluno1.getMatricula() == "1881"

# Testes para Professor
def test_professor_nome(professor1):
    assert professor1.getNome() == "Luciano"

def test_professor_id(professor1):
    assert professor1.getId() == "001"

# Testes para Curso
def test_curso_nome(curso):
    assert curso.getNome() == "Eng. de software"

def test_add_professor(curso, professor1):
    professor2 = Professor("Ana", "002")
    curso.addProfessor(professor2)
    assert "Ana" in curso.getProfessores()

def test_rem_professor(curso, professor1):
    curso.remProfessor(professor1)
    assert professor1.getNome() not in curso.getProfessores()

def test_add_aluno(curso, aluno1):
    aluno3 = Aluno("João Silva", "5678")
    curso.addAluno(aluno3)
    assert "João Silva" in curso.getAlunos()

def test_rem_aluno(curso, aluno1):
    curso.remAluno(aluno1)
    assert aluno1.getNome() not in curso.getAlunos()

@pytest.mark.parametrize("aluno, expected_nome, expected_matricula", [
    (Aluno("Carlos Souza", "3333"), "Carlos Souza", "3333"),
    (Aluno("Julia Ferreira", "4444"), "Julia Ferreira", "4444"),
])
def test_aluno_parametrizado(aluno, expected_nome, expected_matricula):
    assert aluno.getNome() == expected_nome
    assert aluno.getMatricula() == expected_matricula

def test_listar_alunos(curso):
    alunos = curso.listarAlunos()
    assert len(alunos) == 2
    assert "Andreas Gabriel Nascimento Lázaro" in alunos[0]
    assert "Daniel Pinheiro de França" in alunos[1]

# Testes com marcadores
@pytest.mark.smoke
def test_smoke(curso):
    assert curso.getNome() == "Eng. de software"
