from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect
from urllib.parse import unquote

from sqlalchemy.exc import IntegrityError

from model import *
from logger import logger
from schemas import *
from flask_cors import CORS


# Instanciando o objeto OpenAPI
info = Info(title="Loan API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
loan_tag = Tag(name="Loan", description="Adição, visualização, remoção e predição de empréstimos.")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, permite a escolha da ferramenta de documentação.
    """
    return redirect('/openapi')


# Rota de listagem de loans
@app.get('/loans', tags=[loan_tag],
         responses={"200": LoanViewSchema, "404": ErrorSchema})
def get_loans():
    """Lista todos os loans cadastrados na base
    Args:
       none
        
    Returns:
        list: lista de loans cadastrados na base
    """
    logger.debug("Coletando dados sobre todos os loans")
    # Criando conexão com a base
    session = Session()
    # Buscando todos os loans
    loans = session.query(Loan).all()
    
    if not loans:
        # Se não houver loan
        return {"loans": []}, 200
    else:
        logger.debug(f"%d loans econtrados" % len(loans))
        print(loans)
        return apresenta_loans(loans), 200


# Rota de adição de loan
@app.post('/loan', tags=[loan_tag],
          responses={"200": LoanViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: LoanSchema):
    """Adiciona um novo loan à base de dados
    Retorna uma representação dos loans e resultados associados.
    
    Args:
        Age (int): Idade
        Experience (int): experiencia
        Income (int): income - salario
        ZIP.Code (int): zip - CEP
        Family (int): numero de integrantes da familia
        CCAvg (int): media gasto cartao de credito
        Education (int): nivel de educacao
        Personal.Loan (int): se tem emprestimos
        Securities (int): poupancas
        CD.Account (int): CD conta
        Online (int): Online
        
    Returns:
        dict: representação do loan e resultado associado
 
    """

    # TODO: Instanciar classes

    # Recuperando os dados do formulário
    
    age = form.Age
    experience = form.Experience
    income = form.Income
    zip = form.zip
    family = form.Family
    ccavg = form.CCAvg
    education = form.Education
    mortgage = form.Mortgage
    ploan = form.pLoan
    securitiesAccount = form.SecuritiesAccount
    cdAccount = form.CdAccount
    online = form.Online

    print("data: ")
    print(form)
    
        
    # Preparando os dados para o modelo
    X_input = PreProcessador.preparar_form(form)
    # Carregando modelo
    model_path = './MachineLearning/pipelines/bankloan_id.pkl'
    # modelo = Model.carrega_modelo(ml_path)
    modelo = Pipeline.carrega_pipeline(model_path)
    #carrega_modelo
    # Realizando a predição
    outcome = int(Model.preditor(modelo, X_input)[0])

    print("Outcome abaixo: ")
    print(outcome)
    
    loan = Loan(
        age=age,
        experience=experience,
        income=income,
        zip=zip,
        family=family,
        ccavg=ccavg,
        education=education,
        mortgage=mortgage,
        ploan=ploan,
        securitiesAccount=securitiesAccount,
        cdAccount=cdAccount,
        online=online,
        outcome=outcome
    )
    logger.debug(f"Adicionando loan: '{loan.age}'")
    
    try:
        # Criando conexão com a base
        session = Session()
        
        # Adicionando loan
        session.add(loan)
        # Efetivando o comando de adição
        session.commit()
        # Concluindo a transação
        logger.debug(f"Adicionado loan de nome: '{loan.age}'")
        return apresenta_loan(loan), 200
    
    # Caso ocorra algum erro na adição
    except Exception as e:
        error_msg = "Não foi possível salvar novo item :/"
        logger.warning(f"Erro ao adicionar loan '{loan.age}', {error_msg}, {e}")
        return {"message": error_msg}, 400
    

# Métodos baseados em nome
# Rota de busca de loan por nome
@app.get('/loan', tags=[loan_tag],
         responses={"200": LoanViewSchema, "404": ErrorSchema})
def get_loan(query: LoanBuscaSchema):    
    """Faz a busca por um loan cadastrado na base a partir do id

    Args:
        id (str): id do loan
        
    Returns:
        dict: representação do loan e resultado associado
    """
    
    loan_nome = query.id
    logger.debug(f"Coletando dados sobre loan #{loan_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a busca
    loan = session.query(Loan).filter(Loan.id == loan_nome).first()
    
    if not loan:
        # se o Loan não foi encontrado
        error_msg = f"Loan {loan_nome} não encontrado na base :/"
        logger.warning(f"Erro ao buscar Loan '{loan_nome}', {error_msg}")
        return {"mesage": error_msg}, 404
    else:
        logger.debug(f"Loan econtrado: '{loan.income}'")
        # retorna a representação do loan
        return apresenta_loan(loan), 200
   
    
# Rota de remoção de loan por id
@app.delete('/loan', tags=[loan_tag],
            responses={"200": LoanViewSchema, "404": ErrorSchema})
def delete_loan(query: LoanBuscaSchema):
    """Remove um loan cadastrado na base a partir do id

    Args:
        id (int): id do loan
        
    Returns:
        msg: Mensagem de sucesso ou erro
    """
    loan_nome = query.id
    logger.debug(f"Deletando dados sobre loan: #{loan_nome}")
    
    # Criando conexão com a base
    session = Session()
    
    # Buscando Loan
    loan = session.query(Loan).filter(Loan.id == loan_nome).first()
    
    if not loan:
        error_msg = "Loan não encontrado na base :/"
        logger.warning(f"Erro ao deletar Loan '{loan_nome}', {error_msg}")
        return {"message": error_msg}, 404
    else:
        session.delete(loan)
        session.commit()
        logger.debug(f"Deletado loan #{loan_nome}")
        return {"message": f"Loan {loan_nome} removido com sucesso!"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)