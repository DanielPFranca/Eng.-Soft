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
def aluno3():
    return Aluno("João Silva", "5678")

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

# Teste de criação de um professor
def test_criar_professor():
    professor = Professor("Ana", "002")
    assert professor.getNome() == "Ana"
    assert professor.getId() == "002"

# Teste de criação de alunos
def test_criar_alunos():
    aluno1 = Aluno("Carlos Souza", "3333")
    aluno2 = Aluno("Julia Ferreira", "4444")
    assert aluno1.getNome() == "Carlos Souza"
    assert aluno1.getMatricula() == "3333"
    assert aluno2.getNome() == "Julia Ferreira"
    assert aluno2.getMatricula() == "4444"

# Teste de criação do curso e associação de professor
def test_criar_curso_associar_professor(professor1):
    curso = Curso("Eng. de software")
    curso.addProfessor(professor1)
    assert curso.getNome() == "Eng. de software"
    assert professor1.getNome() in curso.getProfessores()

# Teste de adição de alunos ao curso
def test_adicionar_alunos_ao_curso(curso, aluno3):
    curso.addAluno(aluno3)
    assert aluno3.getNome() in curso.getAlunos()

# Teste de listagem de alunos e professor responsável pelo curso
def test_listagem_alunos_professor(curso):
    alunos = curso.listarAlunos()
    assert len(alunos) == 2
    assert "Andreas Gabriel Nascimento Lázaro" in alunos[0]
    assert "Daniel Pinheiro de França" in alunos[1]
    assert "Luciano" in curso.getProfessores()

# Teste completo: criar professor, alunos e curso, adicionar alunos e verificar listagem
def test_fluxo_completo():
    # Criação de um professor
    professor = Professor("Carlos", "003")
    
    # Criação de alunos
    aluno1 = Aluno("Ana Costa", "5555")
    aluno2 = Aluno("Roberta Lima", "6666")
    
    # Criação de curso e associação
    curso = Curso("Engenharia de Sistemas")
    curso.addProfessor(professor)
    
    # Adicionando alunos ao curso
    curso.addAluno(aluno1)
    curso.addAluno(aluno2)
    
    # Verificando a listagem de alunos e o professor
    assert "Ana Costa" in curso.getAlunos()
    assert "Roberta Lima" in curso.getAlunos()
    assert "Carlos" in curso.getProfessores()
    
    # Verificando a listagem detalhada de alunos
    alunos = curso.listarAlunos()
    assert "Nome: Ana Costa, Matrícula: 5555" in alunos
    assert "Nome: Roberta Lima, Matrícula: 6666" in alunos
