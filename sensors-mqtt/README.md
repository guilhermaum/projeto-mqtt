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

(Em desenvolvimento)

## Ferramentas utilizadas ##

O projeto utiliza:
- Java JDK 21.1
- Apache Maven 3.9.11 como ferramenta para gerenciar as dependências
- MQTTX 1.12 como broker gratuito da EMQX
- Eclipse Paho MQTT para comunicação MQTT
- Gson para serialização JSON