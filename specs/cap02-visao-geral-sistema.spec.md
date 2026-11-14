# Spec: Capítulo 2, Visão geral do sistema Monarch NICE3000new

Status: SPEC (nada escrito). Só começa o rascunho depois da aprovação do Capítulo 1 pelo Gelson (RULES.md, seção 7).
Parte I, Fundamentos.

## 1. Objetivo pedagógico
Ao terminar, o leitor sabe nomear cada componente do sistema do quadro à cabina, o que cada um faz, como eles se comunicam (CAN e RS-485) e onde encontrar cada um nos capítulos seguintes.

## 2. Leitor e pré-requisito
Montador de quadro e técnico de campo. Pré-requisito: Capítulo 1.

## 3. Conteúdo previsto (a confirmar com o Gelson)
1. O controlador integrado NICE3000new: modelos, potências e o que "integrado" significa (inversor e controle na mesma unidade). Base: manual cap. 1.
2. A arquitetura: MCB-C3, KCB-B4A, PCB-D1, ERB-A1, CTW-B3, botoeiras e displays, AD30/NICE900. Uma tabela "componente, função, onde fica, capítulo".
3. Comunicação: CAN entre placas e RS-485 (Modbus) para botoeiras e displays; endereçamento de botoeiras e displays.
4. Diagrama em blocos de comunicação (SVG), antes do esquema completo.
5. Mapa dos conectores e bornes de controle da MCB-C3 (CN1 a CN9 e as entradas e saídas).
6. Quadro "Se o seu elevador tiver…": porta traseira, pesagem, MR.

## 4. Fontes permitidas (páginas PDF candidatas, ainda NÃO lidas)
- Manual NICE3000new (368 pp.), cap. 1 "Product Information" (pp. 26 a 36, incluindo o diagrama de sistema da p. 36), e cap. 2 "Installation and Wiring": terminais e comunicação (pp. 60 a 70) e diagrama padrão (p. 78 em diante).
- Esquema Vitinho 19061867-ZL: /24 (topologia CAN, PDF pág. 26), /21 (KCB, PDF pág. 23), /9 a /12 (alimentação).
- Manual CTW-B3 (19010849-SC_A02) para a caixa de teto.
- Manual ERB-A (19010850-SC_B01) para o resgate elétrico.
- Apostila Villarta Monarch V5.0: só conceito.

## 5. Fora de escopo
Ligação fio a fio (capítulos 3 e 4), parâmetros (capítulo 11), falhas (capítulo 13), operador de porta em detalhe (capítulo 8).

## 6. Figuras previstas (SVG)
1. Diagrama em blocos da arquitetura.
2. Topologia de comunicação CAN e RS-485.
3. Mapa dos conectores da MCB-C3.

## 7. Alertas obrigatórios
Os que se aplicarem ao manuseio de placas (descarga eletrostática e tempo de espera), citando o manual.

## 8. Perguntas de verificação
1. Qual placa recebe os sinais da cadeia de segurança e em quais bornes?
2. Que barramento liga as botoeiras e os displays dos pavimentos?
3. Qual é a função da PCB-D1 e da ERB-A1?
4. Em que capítulo está a ligação de cada componente?

## 9. Dependências do Gelson
- Aprovar o Capítulo 1 (ou pedir ajustes) antes do rascunho deste.
- Informar se algum componente além dos citados faz parte do elevador de referência (por exemplo, módulo SCB-A4 de abertura antecipada, que o livro interno deixa como pendência).
