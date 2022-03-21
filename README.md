# Sistema para análises a partir de sequencia de DNA

## Funcionamento
 Após informada uma sequencia genética (dna) de referenciar uma proteína base para a análise, o sistema:
  - gera a cadeia de dna complementar (completa a dupla fita com a base nitrogenada correspondente) A-T T-A G-C C-G;
  - realiza a conversão da sequencia informada para RNA (substituição da base Timina por Uracila);
  - cria a estrutura de proteína com base nos codons;
  - compara a proteína criada a partir da sequencia genética pré informada e compara com a proteína base informada, retornando variações de códons entre as proteínas;
  - calcula a massa de ambas as proteínas e retorna caso exista divergências entre elas. 
