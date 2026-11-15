# Apêndice D. Glossário e siglas

> RASCUNHO v0.1 de 15/11/2026. Selo aberto: `PREENCHER [Q59]`. Cada termo e cada sigla vem dos capítulos do livro; o número depois do verbete é o capítulo onde ele é explicado. Onde um capítulo ainda não tem a definição do fabricante, o verbete diz isso em vez de supor.

## D.1 Termos fixos

O livro usa só estes termos para estas coisas. A coluna "Evite" lista as palavras que **não** se usam, porque confundem peças diferentes.

| Termo | O que é | Evite | Cap. |
|---|---|---|---|
| Quadro de comando | Caixa metálica que reúne inversor, placas de interface, proteções, contatores, transformador e bornes, e comanda o elevador | painel de comando, painel | 2, 3 |
| Cabo de manobra | Cabo flexível que liga o quadro de comando à caixa de teto da cabina (conectores AA e AB no quadro, CA e CB na caixa de teto) | cabo viajante | 10 |
| Caixa de teto | Caixa integrada MCTC-CTW-B3, instalada no topo da cabina, destino do cabo de manobra | caixa de inspeção do teto, caixa de inspeção (sozinha) | 8 |
| Caixa de inspeção do poço | Caixa MBT-PIB no poço, onde ficam o botão de parada do poço e as saídas para os dispositivos do poço. É outra peça, diferente da caixa de teto | caixa do poço (sozinha, quando puder ser confundida com a caixa de corrida) | 11 |
| Caixa de corrida | Espaço vertical onde a cabina se desloca, do poço ao último pavimento | passadiço, poço (quando se quer dizer a caixa inteira) | 10 |
| Poço | Parte inferior da caixa de corrida, abaixo do nível do primeiro pavimento | fosso | 11 |
| Cadeia de segurança | Série de contatos elétricos (botões de parada, chaves de poço, de cabina e de segurança) que só deixa passar o sinal de 110 V ao controlador se todos estiverem fechados | circuito de segurança (sozinho), loop de segurança | 1 |
| Circuito de fechaduras | Série de contatos das fechaduras da porta de cabina e das portas de pavimento, que confirma ao controlador que todas as portas estão fechadas e travadas antes de a cabina se mover | circuito das portas, trinco | 1 |
| Bypass de porta | Dispositivo (plugue S2 na placa KCB-B4A) que substitui temporariamente os contatos de fechadura da porta de cabina ou das portas de pavimento | ponte nas portas, jumpear a porta | 3 |
| Resgate elétrico | Equipamento MCTC-ERB-A1 que libera o freio sem rede elétrica, com bateria interna | resgate (sozinho), ERB (sem explicar na primeira vez) | 14 |
| Resgate de passageiros | Procedimento de emergência para retirar pessoas de uma cabina parada, feito por equipe treinada | resgate (sozinho) | 14 |
| Resgate automático | Equipamento reserva (UPS de 220 V ou ARD) que leva a cabina a um pavimento quando falta a rede | | 14 |
| Operação elétrica de emergência | Modo de movimentar a cabina com a chave CIS e os botões de subir e descer; **não** é o resgate elétrico | resgate elétrico, resgate | 3, 12 |
| Operador de porta | Conjunto que abre e fecha a porta de cabina (máquina de porta com motor e encoder, mais o controlador de porta) | | 9 |
| Controlador de porta | Parte do operador de porta que recebe os comandos do quadro e comanda o motor da porta (exemplo do livro: AD30, também chamado de NICE900 no boletim do fabricante) | | 9 |
| Autoajuste | Procedimento em que o controlador mede os dados do motor ou da porta e grava os resultados. Há o autoajuste do motor de tração (capítulo 12) e os autoajustes do motor e da largura da porta (capítulo 9) | | 9, 12 |
| Zona de porta | Faixa de posição em que o sensor de zona de porta detecta a cabina junto ao pavimento | | 8, 14 |

## D.2 Siglas e abreviaturas

### Placas, módulos e equipamentos

| Sigla | O que significa ou faz | Cap. |
|---|---|---|
| MCB-C3 (MCTC-MCB-C3) | Placa principal do controlador NICE3000new, dentro do inversor | 3 |
| KCB-B4A (MCTC-KCB-B4A) | Placa de interface do quadro. Todos os fios de campo saem dela | 3 |
| PCB-D1 (MCTC-PCB-D1) | Placa fonte do freio (alimenta o freio e fornece os 24 V) | 3 |
| ERB (MCTC-ERB-A1) | Dispositivo de liberação elétrica do freio, o resgate elétrico | 14 |
| CTW-B3 (MCTC-CTW-B3) | Caixa de teto. A B3 não inclui o controlador do operador de porta | 8 |
| CTB | Placa de controle da caixa de teto (car top board) | 8 |
| CTB-H5 (MCTC-CTB-H5) | Placa de interface do teto, segundo o manual da CTW-B3 | 8 |
| COB | Placa de comando da cabina: recebe os botões de andar e de abrir e fechar a porta | 8 |
| HCB | Placa de chamada e display dos pavimentos | 10 |
| SCB-A4 e SCB-D4 | Módulo opcional de abertura antecipada da porta ("advanced door-open module"), ligado à KCB por CAN | 2 |
| PG-E (MCTC-PG-E) | Placa de encoder indicada pelo manual do controlador para o encoder SIN/COS | 7 |
| PTB-A1 e KZ-G2 | Nomes que o esquema dá à placa do poço, em duas folhas diferentes | 11 |
| AD30 | Controlador de porta usado como exemplo no capítulo 9 | 9 |
| NICE900 | Nome que o boletim do fabricante usa para o controlador de porta | 9 |
| NICE-L-C-4007 | Inversor de 7,5 kW em 380 V, o do quadro de referência (confirmação da etiqueta: capítulo 3) | 3 |
| J4210 | Máquina de porta (motor, correia, polias) usada como exemplo no capítulo 9 | 9 |
| UPS | Fonte de alimentação reserva, de 220 V, para o resgate automático | 14 |
| ARD | Dispositivo de resgate automático por bateria para evacuação de emergência | 14 |
| AFE | Sigla da falha Err67 do controlador; o texto do manual não a desdobra no capítulo | 13 |

### Proteções e contatores

| Sigla | O que significa ou faz | Cap. |
|---|---|---|
| QF | Disjuntor geral do quadro ("Main switch"), de 4 polos | 3 |
| QFB1 a QFB4 | Disjuntores de comando e diferenciais: QFB1 do circuito de segurança, QFB2 da alimentação de comando, QFB3 da caixa de teto e QFB4 da iluminação do poço | 3 |
| DQFB | Minidisjuntores que aparecem nas fotos do quadro; a função não está confirmada | 3 |
| SW | Contator de marcha: liga e desliga as três fases entre o inversor e o motor | 3 |
| BY | Contator do freio: liga e desliga o polo negativo (BK-) do freio | 3 |
| FX | Contator de curto das fases U, V e W do motor síncrono | 3 |
| F3 | Fusível da cadeia de segurança, 250 VAC e 1 A | 1 |

### Cadeia de segurança e circuito de fechaduras

| Sigla | O que significa | Cap. |
|---|---|---|
| MES, MES-1 e MES-2 | Botões de parada de emergência (no quadro, do motor e do volante) | 1 |
| CIS | Chave de operação elétrica de emergência (no esquema também "chave de inspeção de emergência") | 1 |
| PES1 e PES2 | Botões de parada do poço (o PES1 fica na botoeira de inspeção do poço) | 11 |
| GTS | Chave elétrica da polia tensora | 11 |
| BFS1 e BFS2 | Chave do amortecedor 1 e chave do amortecedor 2 (qual é do carro e qual é do contrapeso: capítulo 11) | 11 |
| FLSD e FLSU | Fins de curso inferior e superior | 11 |
| PIT, PITU, PITD e PITB | Chave de inspeção do poço e botões de subir, descer e comum | 11 |
| TES | Botão de parada de emergência da caixa de teto | 8 |
| TCI, TCIU, TCID e TCIB | Chave e botões de inspeção da caixa de teto | 8 |
| SOS | Chave elétrica da cunha de segurança | 8 |
| SUP1 e SUP2 | Chaves de espera, fora do elevador de referência | 8 |
| MSC | Régua magnética da caixa de teto; sem ela, liga-se um curto nos terminais indicados no capítulo 8 | 8 |
| GS1 | Contato de fechadura da porta de cabina da frente | 8 |
| GS2 | Contato de fechadura da porta traseira; só com porta traseira | 8 |
| 1DS, 2DS e nDS | Contatos de fechadura das portas de pavimento, um por pavimento | 1 |
| RCS, CWSG e OS-G | Dispositivos opcionais da cadeia (a presença no elevador de referência ainda não está confirmada) | 1 |

### Conectores e bornes

| Sigla | O que significa ou faz | Cap. |
|---|---|---|
| AA e AB | Conectores do quadro para o cabo de manobra | 10 |
| CA e CB | Conectores da caixa de teto para o cabo de manobra | 8 |
| BA, BB, BC | Conectores do quadro para os cabos de poço (cadeia e fechaduras, 24 V e RS-485, interfone) | 10 |
| BD e BE | Conectores das chaves de desaceleração | 10 |
| DEN1 e DEN2 | Bornes da caixa de teto para os comandos e limites do operador de porta 1 e 2 | 8, 9 |
| DC1 e DC2 | Bornes da caixa de teto para a alimentação do controlador do operador de porta | 8, 9 |
| DP | Borne da caixa de teto para a proteção térmica do operador de porta | 8 |
| EDP1 e EDP2 | Entradas da cortina de luz e da borda de segurança da porta 1 e 2 | 8 |
| DA, DB e DC | Plugues da caixa de inspeção do poço para os cabos de poço BA, BB e BC | 11 |
| PT1 a PT4 | Plugues da caixa de inspeção do poço para a caixa de parada, os dispositivos de segurança, a botoeira de inspeção e o botão de reset | 11 |
| LIH | Plugue da iluminação do poço | 11 |
| KY2 a KY12, MT e MT1 | Conectores da KCB e do freio (detalhe no capítulo 3) | 3 |
| CN1 a CN12 | Conectores da placa MCB-C3 (CN1 e CN9 entradas, CN2 detecção de tensão, CN7 saídas a relé, CN3 alimentação, CAN e RS-485) | 3, 4 |
| SZ | Soquete do resgate elétrico na KCB; o jumper SZ é marcado "Use for MRL" | 3 |
| XA, TA, XB, CZ e XPE | Bornes e tomada da base do quadro (função e posição ainda sem confirmação visual) | 3 |
| PUR1 e PUR2 | Tomadas de 220 VAC da caixa de inspeção do poço | 11 |
| PL1 | Lâmpada da caixa de inspeção do poço | 11 |
| PE | Terra de proteção | 4 |

### Sinais e redes

| Sigla | O que significa | Cap. |
|---|---|---|
| R, S, T | Entrada trifásica do inversor | 3 |
| U, V, W | Saída do inversor para o motor | 3 |
| (+), PB | Bornes do resistor de frenagem | 3 |
| BK1+, BK2+ e BK- | Saídas do freio na PCB-D1 | 3 |
| ZQ1+, ZQ2+, ZQ1- e ZQ2- | Retornos do freio na PCB-D1; ZQ+ e ZQ- também são os bornes de saída do resgate elétrico | 3, 14 |
| CAN+ e CAN- | Comunicação CAN entre a KCB, a PCB-D1 e a caixa de teto | 3 |
| MOD+ e MOD- (RS-485) | Comunicação com as placas de chamada dos pavimentos | 4 |
| 301 e 302 | Alimentação de 24 VCC e seu comum | 3 |
| 201 e 202; 207 e 208; 501 e 502 | Redes de 220 VAC: comando, cabina (operador e cortina) e iluminação da cabina e resgate elétrico | 3 |
| DZI | Sinal de zona de porta no cabo de manobra | 10 |
| FL1 e FL2 | Sinais de renivelamento | 8 |
| X1 a X28 | Entradas digitais do controlador (X25 a X28 são as de 110 V da cadeia e das fechaduras) | 3, 4 |
| Y1 a Y6 | Saídas a relé do controlador | 3 |
| MQ+, MQ-, MS+, MS- | Entrada de zona de porta e de fechadura do resgate elétrico | 14 |
| BAT+ e BAT- | Bateria do resgate elétrico | 14 |
| DI1 a DI8; TA12, TC1 a TC4 | Entradas e saídas a relé do controlador de porta AD30 | 9 |
| PGA, PGB e PGZ | Sinais de posição do encoder do motor de porta | 9 |
| LPA e LPF | Retorno do limite de porta aberta e de porta fechada | 9 |

### Parâmetros e falhas

| Sigla | O que significa | Cap. |
|---|---|---|
| F0 a FP e B0 | Grupos de parâmetros do controlador NICE3000new e da PCB-D1 (o capítulo 12 traz os de uso do projeto) | 12 |
| FA-01, FA-02, FA-33 e FA-63 | Parâmetros do grupo FA citados no capítulo 12 (a função de cada um está lá) | 12 |
| EEO | "Emergency electric RUN": operação elétrica de emergência (parâmetro F3-25 é a velocidade dela) | 12 |
| SVC, CLVC e V/F | Valores do modo de controle F0-00: 0 = SVC, 1 = CLVC (vetorial em malha fechada) e 2 = V/F | 12 |
| Err e E | Formato do código de falha: Err22 no painel; E22-101 no teclado da MCB | 13 |
| RTC | Relógio de tempo real; a falha Err24 trata dele | 13 |
| TUNE, TUNE1 e TUNE2 | Indicações do display durante o autoajuste do controlador de porta | 9 |

### Motor, encoder e unidades

| Sigla | O que significa | Cap. |
|---|---|---|
| PMSM | Motor síncrono de ímã permanente | 7, 9 |
| ABZ | Encoder incremental com canais A, B e Z | 7, 9 |
| SIN/COS | Encoder de sinais senoidais | 7 |
| SPI | Encoder absoluto por comunicação (opção do controlador de porta) | 9 |
| PPR | Pulsos por rotação do encoder | 7 |
| UVW | Fases do motor (também o tipo de encoder com canais U, V e W) | 7 |
| LED | Diodo emissor de luz (indicadores das placas) | 3 |
| VCA, VCC | Volts em corrente alternada e em corrente contínua | todos |
| MR e MRL | Elevador com casa de máquinas e elevador sem casa de máquinas | 1 |

### Documentos e controle

| Sigla | O que significa | Cap. |
|---|---|---|
| POP-ISO-PCP | Procedimento da empresa para planejamento, produção e controle de quadros de comando | 5 |
| CQ | Controle de qualidade; o relatório de CQ acompanha a Ordem de Produção | 5 |
| ZL | Sufixo do código dos esquemas elétricos (19061867-ZL e 19060918-ZL) | 1 |
| VP-RES-01 | Código da cartilha "Manual de Resgate" da VerticalParts | 14 |
| PDF | Página do arquivo PDF (a numeração das citações do livro) | todos |

## D.3 Como os alertas aparecem

O livro usa quatro níveis de alerta, sempre **antes** do passo a que se referem.

| Nível | Quando usar |
|---|---|
| PERIGO | Risco de morte ou lesão grave |
| ATENÇÃO | Risco de lesão ou de dano grave ao equipamento |
| CUIDADO | Risco de dano ao equipamento ou de resultado errado |
| NOTA | Informação que evita um erro |

## D.4 Pontos de atenção do glossário

1. **Resgate elétrico não é operação elétrica de emergência.** O primeiro é o equipamento que libera o freio; a segunda é o modo de mover a cabina pela botoeira, com a chave CIS.
2. **Caixa de teto, caixa de inspeção do poço e caixa de corrida** são três coisas diferentes (D.1).
3. **Siglas com função ainda sem confirmação.** A função de cada chave da cadeia (o que detecta e por que existe) não está nos documentos lidos: `PREENCHER [Q59]`. A função de DQFB, XA, TA, XB, CZ e XPE também não está confirmada.

## Fontes do apêndice

- `GLOSSARY.md` do projeto, para os termos fixos.
- Capítulos 1 a 5 e 7 a 14 deste livro, para as siglas, com as fontes citadas em cada um.
