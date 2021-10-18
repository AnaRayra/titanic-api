# Titanic REST API 
Essa API tem como objetivo retornar os dados de um modelo que prevê se uma pessoa sobreviveria ao naufrágio do Titanic.

## Subindo localmente

Para subir a API localmente basta ter o docker instalado em sua máquina (caso não tenha acesse esse 
[link](https://docs.docker.com/engine/install/ubuntu/)) e rodar os seguintes comandos:

_Criação a imagem docker:_

>docker build -t api-model .  
>

_Rodar o container utilizando a imagem criada na porta 5000:_
>docker run -it -d -p 5000:5000 --name api-model api-model 

Com o container rodando devidamente, você terá acesso a API em localhost:5000/.