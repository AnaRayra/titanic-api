# Titanic REST API 
Essa API tem como objetivo retornar os dados de um modelo que prevê se uma pessoa sobreviveria ao naufrágio do Titanic.

## Métodos

**GET - /**
Checar se a API está ativa

_Retorno esperado:_
<p>200 - API Ativa e disponível


**POST - /**
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
        },
    ]

_Retorno esperado:_
<p>400 - Bad Request : Alguma informação enviada não está seguindo o que a API espera.
<p>200 - Success: Retorna uma lista com a previsão de sobrevivência.