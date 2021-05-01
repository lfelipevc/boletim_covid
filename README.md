# Extrator de casos de COVID 19 dos Boletins Epidemiológicos de Belo Horizonte - MG

Para conseguir as ocorrências de casos de COVID-19 no muncípio de Belo Horizonte/MG é necessário extrair do boletim em PDF divulgado pela prefeitura, já que os dados não nestão disponíveis no portal da transparência municipal.

## Exemplo : 

[PDF Boletim 240 - 19/04/201921](https://prefeitura.pbh.gov.br/sites/default/files/estrutura-de-governo/saude/2021/boletim_epidemiologico_assistencial_240_covid-19_01-04-2021.pdf)

### Parte da tabela de origem do boletim em PDF divultado pela PBH
![Tabela ilustrativa de casos de COVID por bairro em belo horizonte](/assets/tabela_covid.png "PTabela ilustrativa de casos de COVID por bairro em belo horizonte")

### Resultado da tabela extraída automaticamente pelo script
|      |bairro                  |sg |srag|obitos|
|------|------------------------|---|----|------|
|1     |Aarão Reis              |76 |5   |2     |
|2     |Acaba Mundo             |6  |0   |0     |
|3     |Acaiaca                 |30 |2   |0     |
|4     |Ademar Maldonado        |47 |5   |3     |
|5     |Aeroporto               |55 |5   |1     |
|6     |Águas Claras            |10 |0   |0     |
|7     |Alípio de Melo          |325|17  |5     |
|8     |Alpes                   |25 |2   |0     |
|9     |Alta Tensão             |7  |0   |0     |
|10    |Alta Tensão I           |18 |1   |0     |
|11    |Alto Barroca            |114|2   |0     |
|12    |Alto Caiçaras           |190|11  |0     |
|13    |Alto dos Pinheiros      |62 |4   |1     |
|14    |Alto Vera Cruz          |225|40  |9     |
|15    |Álvaro Camargos         |33 |1   |0     |
|16    |Ambrosina               |7  |0   |0     |
|17    |Anchieta                |353|15  |6     |
|18    |Andiroba                |8  |1   |1     |
|19    |Antônio Ribeiro de Abreu|4  |0   |0     |

### Colunas e Campos  Extraídos
- **bairro**: campo om nome dos bairros
- **sg**: campo com a quantidade aos casos de Síndrome Gripal
- **srag**: campo com quantidade total de casos de Sindrome Gripal Aguda Grave (inclui também os óbitos)
- **obitos**: campo com a quantidade total obitos 

> **(srag - obitos)** = casos de srag não registraram óbitos

## Ambiente
 - Python 3.5
 - [Tabula Py 2.2.0](https://pypi.org/project/tabula-py/)
## Instruções
### Instalação:
### Executar:
### Utilizar em como biblioteca:
