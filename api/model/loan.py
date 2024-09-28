from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base

# colunas = Age,Experience,Income,ZIP, Family, CCAvg, Education, Mortgage, pLoan, SecuritiesAccount, CdAccount, Online,
            # CreditCard (outcome) não entra no esquema

class Loan(Base):
    __tablename__ = 'loans'

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column("Age", Integer)
    experience = Column("Experience", Integer)
    income = Column("Income", Integer)
    zip = Column("Zip.Code", Integer)
    family = Column("Family", Integer)
    ccavg = Column("CCavg", Float)
    education = Column("Education", Integer)
    mortgage = Column("Mortgage", Integer)
    ploan = Column("Personal.Loan", Integer)
    securitiesAccount = Column("Securities.Account", Integer)
    cdAccount = Column("CD.Account", Integer)
    online = Column("online", Integer)
    outcome = Column("CreditCard", Integer, nullable=True)
    #data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, 
                 age:int, 
                 experience:int, 
                 income:int, 
                 zip: int,
                 family:int, 
                 ccavg:float, 
                 education:int, 
                 mortgage:int, 
                 ploan:int, 
                 securitiesAccount:int, 
                 cdAccount:int, 
                 online:int, 
                 outcome:int 
                 ):
        


        """
        Cria um Loan

        Arguments:
            Age: idade
            Experience: experiencia
            Income: salario
            ZIP.Code: CEP
            Family: numero de integrantes da familia
            CCAvg: media cartao de credito
            Education: Nivel de educacao
            Mortgage: Prestacao do imovel
            Personal.Loan: Emprestimos
            Securities.Account: contas extras
            CD.Account: Cd contas
            Online: Online
            CreditCard: resultado 

            data_insercao: data de quando o loan foi inserido à base
        """


        self.age = age
        self.experience = experience
        self.income = income
        self.zip = zip
        self.family = family
        self.ccavg = ccavg
        self.education = education
        self.mortgage = mortgage
        self.ploan = ploan
        self.securitiesAccount = securitiesAccount
        self.cdAccount = cdAccount
        self.online = online
        self.outcome = outcome

        # # se não for informada, será o data exata da inserção no banco
        # if data_insercao:
        #     self.data_insercao = data_insercao