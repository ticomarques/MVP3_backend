from pydantic import BaseModel
from typing import Optional, List
from model.loan import Loan
import json
import numpy as np

class LoanSchema(BaseModel):
    """ Define como um novo Loan a ser inserido deve ser representado
    """
    ## Colunas
    # id,
    # Age,
    # Experience,
    # Income,
    # ZIP,
    # Family,
    # CCAvg,
    # Education,
    # Mortgage,
    # pLoan,
    # SecuritiesAccount,
    # CdAccount,
    # Online,
    # CreditCard (outcome) não entra no esquema

    ### Valores para teste
    ## 16,60,30,22,95054,1,1.5,3,0,0,0,0,1,1

    id: int = 1
    Age: int = 20
    Experience: int = 150
    Income: int = 22
    zip: int = 95054
    Family: int = 1
    CCAvg: float = 1.5
    Education: int = 3
    Mortgage: int = 0
    pLoan: int = 0
    SecuritiesAccount: int = 0
    CdAccount: int = 0
    Online: int = 1

    
    
class LoanViewSchema(BaseModel):
    id: int = 1
    Age: int = 20
    Experience: int = 150
    Income: int = 22
    zip: int = 95054
    Family: int = 1
    CCAvg: float = 1.5
    Education: int = 3
    Mortgage: int = 0
    pLoan: int = 0
    SecuritiesAccount: int = 0
    CdAccount: int = 0
    Online: int = 1
    CreditCard: int = None #outcome
    
class LoanBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no id do loan.
    """
    id: int = 1

class ListaLoansSchema(BaseModel):
    """Define como uma lista de loans será representada
    """
    loans: List[LoanSchema]

    
class LoanDelSchema(BaseModel):
    """Define como um loan para deleção será representado
    """
    id: int = 1
    
# Apresenta apenas os dados de um loan    
def apresenta_loan(loan: Loan):
    """ Retorna uma representação do loan seguindo o schema definido em
        LoanViewSchema.
    """
    return {
        "id": loan.id,
        "Age": loan.age,
        "Experience": loan.experience,
        "Income": loan.income,
        "zip": loan.zip,
        "Family": loan.family,
        "CCAvg": loan.ccavg,
        "Education": loan.education,
        "Mortgage": loan.mortgage,
        "pLoan": loan.ploan,
        "SecuritiesAccount": loan.securitiesAccount,
        "CdAccount": loan.cdAccount,
        "Online": loan.online,
        "outcome": loan.outcome
    }
    
# Apresenta uma lista de loans
def apresenta_loans(loans: List[Loan]):
    """ Retorna uma representação do loan seguindo o schema definido em
        LoanViewSchema.
    """
    result = []
    for loan in loans:
        result.append({
            "id": loan.id,
            "Age": loan.age,
            "Experience": loan.experience,
            "Income": loan.income,
            "zip": loan.zip,
            "Family": loan.family,
            "CCAvg": loan.ccavg,
            "Education": loan.education,
            "Mortgage": loan.mortgage,
            "pLoan": loan.ploan,
            "SecuritiesAccount": loan.securitiesAccount,
            "CdAccount": loan.cdAccount,
            "Online": loan.online,
            "outcome": loan.outcome
        })

    return {"loans": result}

