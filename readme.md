# MVP3 - Qualidade, segurança e sistemas inteligentes.
## PUC-Rio - Engenharia de sistemas

Projeto de predição de empréstimo/cartão de credito, modelo preparado e treinado no google colab, importado para um sistema backend em python, e com frontend usando javascript.

Notebook (.ipynb) anexo no projeto (/api/machineLearning/notebooks).
Link do notebook: https://colab.research.google.com/drive/1B9eP0_Cv-T4IPHaB-qMwky1NfVZjl7UX?usp=sharing

#### Existe um projeto separado com um frontend desenvolvido em React para rodar junto com esse backend (link compartilhado na postagem do projeto, ou pode ser acessar na listagem de repositorios do usuário).

Para rodar o projeto:

1 - Como criar um virtal env:
```
python3 -m venv env 
```

2 - Como ativar um virtal env:
```
source env/bin/activate 
```

Como desativar um virtal env:
```
deactivate 
```

3 - Instalar dependencias
```
(env)$ pip install -r requirements.txt
```

Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`.

4 - Para executar a API  basta executar:

```
(env)$ flask --app app run --debug
```


Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.