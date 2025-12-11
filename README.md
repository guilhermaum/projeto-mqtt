# Projeto sobre MQTT #

Este projeto consiste em simular um sistema de agricultura inteligente com comunicação indireta MQTT para a disciplina de Sistemas Distribuídos. A arquitetura é baseada em um programa que executa simuladores de sensores de forma independente e em um arquivo que consome os dados publicados para executar determinada ações.

## Arquitetura do produtor ##

É dito produtor o programa que envia os dados emitidos dos sensores simulados para o broker MQTT, esse programa é composto pelas seguintes pastas:

    └───java
        └───com
            └───sistemasdistribuidos
                ├───client
                ├───model
                ├───mqtt
                └───sensors

### Descrição das pastas ### 

| Pasta   | Descrição |
|---------|-----------|
| client | Cria instâncias dos sensores e publica suas informações no intervalo configurado. |
| model   | Estrutura a classe usada pelos sensores; todos compartilham uma interface comum (tipo, valor e timestamp). |
| mqtt    | Implementa os métodos responsáveis por publicar mensagens no broker MQTT. |
| sensors | Contém os mocks que simulam o funcionamento dos sensores. |


Além disso, o `src/main/App.java` realiza as execuções de todos os programas que publicam sensores.

## Arquitetura do consumidor ##

Formada por microsserviços desenvolvidos com Python. O microsserviço de visão retorna operações que serão exibidas para o usuário, atualmente, o programa só retorna a média dos últimos registros

    ├───mqtt
    │   └───__pycache__
    ├───services
    │   └───__pycache__
    └───topics
        └───__pycache__

Já o serviço de alertas recebe as médias publicadas e verifica situações de risco, publicando mensagens no broker que são recebidas pelo usuário em forma de notificação

    ├───mqtt
    │   └───__pycache__
    └───services
        └───__pycache__

## Ferramentas utilizadas ##

O projeto utiliza:
- Java JDK 21.1
- Python 3.11.9
- Apache Maven 3.9.11 como ferramenta para gerenciar as dependências
- EMQX Cloud Service como broken
- Eclipse Paho MQTT para comunicação MQTT
- Gson para serialização JSON

## Execução ##

É necessário que o usuário execute todas as funções principais das pastas apresentadas, o broker conectado é de uso pessoal com uma conexão TLS certificada mas pode ser alterada para qualquer broker.

## Equipe ##

Luís Guilherme, Letícia Maria, Maria Eduarda, Maria Luiza e João Pedro Jacomé. Todos fazem parte do curso de bacharelado de ciência da computação, pelo IFCE Campus Tianguá.