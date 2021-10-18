# Titanic REST API 
Essa API tem como objetivo retornar os dados de um modelo que prevê se uma pessoa sobreviveria ao naufrágio do Titanic.

## Project Tree

```bash
├── Dockerfile
├── readme.md
├── requirements.txt
├── run.py
├── .flaskenv
└── app
    └── error_handler
        ├── error_handler.py
        ├── error_message.py
    └── model_training
        ├── model.pkg
        ├── titanic.csv
    ├── model.py
    ├── response_model.py
    ├── routes.py
    ├── service.py
    ├── validation.py
```

## Como rodar a API

Para subir a API localmente basta ter o docker instalado em sua máquina (caso não tenha acesse esse 
[link](https://docs.docker.com/engine/install/ubuntu/)) e rodar os seguintes comandos:

_Criação a imagem docker:_

>docker build -t api-model .  
>

_Rodar o container utilizando a imagem criada na porta 5000:_
>docker run -it -d -p 5000:5000 --name api-model api-model 

Com o container rodando devidamente, você terá acesso a API em localhost:5000/.

## Métodos

**GET - /**
Checar se a API está ativa

_Retorno esperado:_
<p>200 - API Ativa e disponível


**POST - /predict** 
   Consultar se as pessoas irão sobreviver. Payload esperado na chamada:

    [
        {
            "Name": "Exemplo 1",
            "Sex": "male",
            "Pclass": 1,
            "Fare": 20.0
        },
        {
            "Name": "Exemplo 2",
            "Sex": "male",
            "Pclass": 3,
            "Fare":11.5
        }
    ]

_Retorno esperado:_
<p>400 - Bad Request : Alguma informação enviada não está seguindo o que a API espera.
<p>200 - Success: Retorna uma lista com a previsão de sobrevivência.