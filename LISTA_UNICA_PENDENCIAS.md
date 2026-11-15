# Lista única do que depende do Gelson (15/11/2026)

Tudo o que ainda trava o livro e que só você pode resolver, numa lista só, por ordem de prioridade. Responda pelo número (por exemplo, "1: CREA 123456, Nome Completo"). Entre parênteses, o código antigo (Q ou P) e a issue, só para rastrear; o assunto está sempre escrito por extenso.

Legenda de prioridade: **Grupo A** você responde de onde estiver, em minutos; **Grupo B** precisa de um documento ou de alguém da Automação ou da Qualidade; **Grupo C** se resolve numa ida ao quadro com o `CHECKLIST_QUADRO_FISICO.md`; **Grupo D** não depende de você (eu confiro).

## Grupo A. Decisões suas, sem ir ao quadro

| Nº | O que preciso | Onde aparece | Minha recomendação |
|---|---|---|---|
| A1 | **Registro profissional:** número do CREA ou do CFT e o nome completo do responsável técnico, para o verso da folha de rosto (registro CREA, issue #25) | Capa | Sem recomendação: é dado seu. Bloqueia o lançamento |
| A2 | **Ordem de montagem:** a ordem de 12 etapas (recebimento, mecânica, componentes, terra, potência, comando, placas, cabo plano, botoeira, conferência cruzada, sem tensão, energização) é a oficial? Quem faz a conferência cruzada e quem libera, por departamento? (Q117, issue #37) | Cap. 4, seção 4.4 | Confirmar a ordem do Rev. 11; conferência por um segundo montador; liberação pela Qualidade |
| A3 | **Cartilha de resgate:** a "Manual de Resgate" VP-RES-01 Rev. 02, que está marcada "versão para validação técnica", foi aprovada? (Q114, issue #34) | Cap. 14, seção 14.9 | Se não foi, manter o resumo com a ressalva que já está no texto |
| A4 | **Operador de porta do elevador de referência:** qual fabricante e modelo, se houver um definido? O capítulo já vale para vários operadores (Q107, issue #27) | Cap. 9, seção 9.2 | Se não houver um padrão, responder "vários"; eu tiro o selo e deixo o AD30 como exemplo |
| A5 | **Resgate automático:** o elevador de referência tem UPS ou ARD além do resgate elétrico? (Q112, issue #32) | Cap. 14, seções 14.2 e 14.8 | Pelo esquema e pelas fotos, só o resgate elétrico; responder "não" se for o caso |
| A6 | **Velocidade nominal** do elevador de referência (Q102, issue #23) | Cap. 10, seção 10.6; cap. 12 | Informar o valor (por exemplo, 1,0 m/s); com ele eu calculo a distância de desaceleração |
| A7 | **Rótulo da botoeira de inspeção:** vale o rótulo amarelo de 12/11 (SUBIR, DESCER, ACIONAMENTO LIMITADOR, REARME LIMITADOR, AÇÃO/FREIO) ou o branco de 13/11 (SOBE, DESCE, RESGATE, TESTE LIMITADOR, RESET LIMITADOR, AÇÃO FREIO)? (Q87, issue #15) | Cap. 3, seção 3.7 | O de 13/11, que é o mais recente |
| A8 | **Amortecedores:** confirma que o BFS1 é o do carro e o BFS2 o do contrapeso, como diz o esquema VerticalParts? (Q56, issue #3) | Caps. 1 e 11 | Confirmar; aí o texto passa a dizer carro e contrapeso |
| A9 | **Barramento de terra cheio:** o barramento de 6 polos não tem polo livre para o terra da rede e o do motor. Qual a solução: barramento de 8 ou 10 polos, ou borne de terra no trilho? (pendência P14) | Cap. 3, seção 3.10; Apêndice C | Barramento de 10 polos |
| A10 | **Disjuntor QFB4 (iluminação do poço):** entra no quadro? Existe no esquema, mas não está na lista de fios nem na lista de materiais (pendência P9) | Cap. 3, seção 3.8; Apêndice B | Entrar, como no esquema |
| A11 | **Capítulo 6, qualidade do equipamento e dos acabamentos:** onde ele entra na numeração; o que conta como qualidade do equipamento e dos acabamentos (você já concordou: equipamento = o quadro como produto; acabamentos = mão de obra visível); de onde vêm os critérios de aceite; e fotos de peça conforme e não conforme (Q49 a Q52) | Cap. 6 (em espera) | Manter como capítulo 6; critérios definidos pela Qualidade; eu monto o capítulo quando chegarem os critérios e as fotos |
| A12 | **NR-12:** entra ou não no capítulo de normas? | Em espera | Deixar fora nesta revisão |

## Grupo B. Precisa de documento ou de outra área

| Nº | O que preciso | Quem tem | Onde aparece |
|---|---|---|---|
| B1 | **Textos das normas:** os trechos da NR-10, da ABNT NBR 16858 e da EN 81-20 sobre bloqueio e etiquetagem, cadeia de segurança, acesso ao poço e posição do botão de parada do poço (Q47, issue #1) | Você ou a Qualidade | Caps. 1, 4 e 11 |
| B2 | **Valores esperados dos testes de bancada** ainda sem critério: secundário do transformador sem carga (E5), comunicação CAN (E9), motor e freio em inspeção (E11), resgate e botoeira (E12) (Q118, issue #38) | Automação | Cap. 5, seção 5.4 |
| B3 | **Critérios do checklist da Qualidade** por item (identificação, integridade, aspecto visual, montagem, componentes, conexões, acabamento) e se o POP-ISO-PCP foi aprovado, com o código final; hoje ele está em Revisão 00, com código "xxx" e setor "Financeiro" (Q119, issue #39) | Qualidade | Cap. 5, seções 5.2 e 5.6 |
| B4 | **Critério de isolação com megôhmetro:** tensão de ensaio e valor mínimo antes de energizar (Q116, issue #36) | Automação e Qualidade | Cap. 4, seção 4.7 |
| B5 | **Torque de aperto** do QF, dos disjuntores diferenciais, dos minidisjuntores, dos contatores e dos bornes de passagem; basta a folha de dados de cada um (Q115, issue #35) | Compras ou fornecedor | Cap. 4, seções 4.2 e 4.7 |
| B6 | **Plano de manutenção periódica do quadro:** itens e periodicidade, ou a decisão de o livro não trazer plano (Q113, issue #33) | Você ou o fabricante | Cap. 14, seção 14.7 |
| B7 | **Função de cada chave da cadeia de segurança** (o que cada uma detecta e por que existe), em material do fabricante. A resposta que chegou em 15/11 tem dispositivos que não estão nas fontes (Q59, issue #4) | Fabricante (BST ou Inovance) | Caps. 1 e 11 |
| B8 | **Controlador de porta, três perguntas ao fabricante:** (a) para inverter o sentido da porta, troca-se U e V, muda-se o F215, ou os dois? (Q111, issue #31); (b) qual o tempo de espera para descarga antes de abrir o controlador? (Q110, issue #30); (c) existe diagrama da ligação da caixa de teto CTW-B3 com o AD30, fio a fio? (Q108, issue #28) | Fabricante do operador | Cap. 9, seções 9.1, 9.5 e 9.10 |
| B9 | **Origem dos 220 V de comando** nas variantes de 220 V (pendência P2) | Você | Adendo 220 V (pode esperar) |

## Grupo C. Uma ida ao quadro resolve (use o CHECKLIST_QUADRO_FISICO.md)

Leve o checklist impresso, com o quadro desligado e 10 minutos de espera. Cada linha diz o item do checklist.

| Nº | O que ler ou fotografar | Item do checklist | Resolve |
|---|---|---|---|
| C1 | Plaqueta do inversor (modelo, potência, correntes) | 1 | Só confirmação: a lista de materiais já especifica o NICE-L-C-4007 (Q79 resolvida) |
| C2 | Onde o resistor de frenagem está fixado, bitola e terminal do cabo | 2 | Fixação do resistor (P5); o valor já está na lista de materiais (Q80 resolvida) |
| C3 | Etiquetas de DQFB1 a DQFB3 e do QF, QFB3 e QFB4; foto do trilho de disjuntores inteiro | 3, 4 e 5 | Função dos DQFB (Q81) e dados das proteções (Q82) |
| C4 | Conectores S1 e S2 da placa KCB, com plugues e jumpers | 6 | Pinos do bypass de porta (Q83) |
| C5 | Parâmetros B0-00 a B0-02 no display da PCB-D1 e plaqueta do freio | 7 | Tensões do freio (Q84) |
| C6 | Placa PCB-D1, base do quadro por fileira de bornes e barramento de terra com cada fio | 8, 9 e 10 | Posição das peças e dos bornes XA, TA, XB, SZ, CZ (Q85); bornes grandes (P17) |
| C7 | A bateria dentro do resgate elétrico e a serigrafia de L e N | 11 | Bateria (P16) e L e N (P10); o modelo A1 já está confirmado pela foto (Q86 resolvida) |
| C8 | Etiquetas dos contatores SW, BY e FX e dos blocos auxiliares | 13 | Dados dos contatores (Q88); mapa dos contatos (P6); bloco BC-1 ou BC-A (P15) |
| C9 | Conectores AA, AB, BA, BD, BE e HW: há jumper instalado? | 14 | Se os jumpers 62 a 66 da lista de fios ficam só na bancada (Q71) |
| C10 | Conector HW e o circuito do limitador de velocidade; se há contrapeso com cunha | 16 | Se existem RCS, CWSG e OS-G (Q54) e o botão MES-1 (Q60) |
| C11 | Plaqueta do motor de tração e do encoder | 17 e 18 | Dados da máquina (Q95) e modelo do encoder (Q96) |
| C12 | Módulo de abertura antecipada SCB-A4 ou SCB-D4 no quadro | 21 | Se o módulo está instalado (Q92) |
| C13 | Comprimento de cada cabo de manobra e de poço | 22 | Comprimento (Q101); tipo e bitola já confirmados pela lista de fiação |
| C14 | Placa dentro da caixa de inspeção do poço e o jumper J15 | 23 | Placa do poço (Q104) |
| C15 | Etiqueta da placa de comando da cabina (MCTC-COB-A1 ou A2) | 25 | Placa COB (Q99); a caixa de teto já está resolvida (Q98) |
| C16 | Placa do operador e do controlador de porta, aviso da tampa, plaqueta do motor e do encoder da porta, e como o parâmetro de pulsos aparece no display | 26 | Notação dos parâmetros (Q106), dados do motor da porta (Q109), tempo de espera (Q110) |
| C17 | UPS, ARD ou contator de marcha da UPS no quadro | 27 | Resgate automático (Q112), se você não souber de cabeça (A5) |

## Grupo D. Conferência feita em 15/11/2026

As 12 respostas do documento de 15/11 foram conferidas contra a fonte citada. O resultado está também comentado em cada issue.

| Resultado | Assunto | O que aconteceu |
|---|---|---|
| Resolvida | Modelo do inversor (Q79) | A lista de materiais especifica o NICE-L-C-4007-KZG; selo removido do capítulo 3 |
| Resolvida | Resistor de frenagem (Q80) | A lista de materiais especifica 75 ohm e 2500 W; selo removido |
| Resolvida | Resgate elétrico A1 ou A2 (Q86) | A etiqueta MCTC-ERB-A1 aparece na foto de 12/11; selo removido dos capítulos 3 e 14 |
| Resolvida | Qual diagrama vale para a caixa de teto (Q98) | Você confirmou a CTW-B3 na revisão 8 (pendência P36); vale o manual; selo removido dos capítulos 8 e 10 |
| Parcial | Cabos de manobra e de poço (Q101) | Feitos pela VerticalParts, cabo PP de 0,75 mm², Mini-Fit e Hylok; falta só o comprimento (C13) |
| Parcial | Função dos DQFB (Q81) | Os componentes batem com a lista de materiais; o circuito de cada um vem só da lista de fios (C3) |
| Não resolve | Amortecedores (Q56) | Repete o esquema; falta a sua confirmação (A8) |
| Não resolve | Função das chaves da cadeia (Q59) | Traz itens sem fonte; precisa de material do fabricante (B7) |
| Não resolve | Jumpers 62 a 66 (Q71) | Repete a indicação já registrada; falta ver no quadro (C9) |
| Não resolve | Rótulo da botoeira (Q87) | A resposta fala de outra coisa (A7) |
| Não resolve | Placa de comando da cabina (Q99) | Confundiu os conectores COB1 e COB2 com os modelos A1 e A2 (C15) |
| Não resolve | Placa do poço (Q104) | A MBT-PIB-A12 é a caixa de parada, não a placa (C14) |

**Um ajuste num capítulo já aprovado:** no teste R3 do capítulo 5, a etiqueta do ERB-A1 fotografado diz 187 a 253 V, e o manual diz 187 a 242 V. O texto agora mostra as duas e manda usar a do manual, que é a mais estreita.

## Resumo

- Grupo A: 12 decisões (A1 bloqueia o lançamento; A2 a A8 tiram selos dos rascunhos).
- Grupo B: 9 pedidos de documento ou de outra área.
- Grupo C: 17 leituras numa só ida ao quadro.
- Grupo D: feito; 4 resolvidas, 2 parciais e 6 que voltam para os grupos A, B e C.
