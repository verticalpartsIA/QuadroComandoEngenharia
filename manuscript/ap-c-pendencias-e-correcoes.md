# Apêndice C. Pendências abertas e correções ao Rev. 11

> RASCUNHO v0.1 de 14/11/2026.

Este apêndice mostra o que a auditoria do Rev. 11 (14/11/2026) resolveu e o que continua aberto. Cada pendência aberta tem a ação que a fecha. Quando uma pendência é resolvida, ela sai deste apêndice. Fonte: `AUDITORIA_REV11.md` e os arquivos em `auditoria/`.

## C.1 Pendências do Rev. 11 (P1 a P20)

| P | Assunto | Situação | O que fecha |
|---|---|---|---|
| P1 | Inversor de 220 V | Modelo resolvido: 220-NICE-L-C-4015 (7,5 kW) e 220-NICE-L-C-4022 (15 kW); "2015" não existe no manual | Ler a etiqueta do inversor recebido e corrigir o cadastro |
| P2 | Origem dos 220 V de comando nas variantes 220 V | Aberto | Decisão do responsável técnico, por variante |
| P3 | Trafo | Bornes resolvidos: primário 220V e 0P, secundário 125V e 0S, 63 VA nos dois esquemas | Etiqueta do trafo e medição da saída sem carga |
| P4 | Bitola e terminais de potência | Cabo resolvido (6 mm² e 10 mm²); torque e terminal das variantes 220 V não constam | Medir o parafuso dos bornes do inversor recebido |
| P5 | Resistor de frenagem | Resistores confirmados; bitola, terminal e fixação abertos | Definir os três itens |
| P6 | Mapa dos contatores | Aberto | Multímetro nos contatores reais |
| P7 | Botoeira de inspeção | Esquema mostra o handle KKB4-1C-02 (CIS, CIU E, CID E e MES) e nenhum botão extra | Mapa furo a botão |
| P8 | Plugues S1 e S2 da KCB | Tag "S1" da lista é o limitador de velocidade (resolvido) | Conferir os pinos na placa |
| P9 | QFB4 | Existe no esquema; não está na lista nem no BOM | Decidir se entra |
| P10 | L e N da ERB-A1 | Esquema: 501 em L e 502 em N; a lista está invertida | Conferir a serigrafia da ERB e corrigir a lista |
| P11 | MCB-C2 ou C3 | Só existe a C3 | Corrigir a lista |
| P13 | Terminais no BOM | Tubular de 6 mm²: 19 na lista e 16 no BOM | Recalcular a compra |
| P14 | Barramento de terra de 6 polos | Cheio | Decisão de projeto |
| P15 | BC-1 | Inconsistência (BC-1 ou BC-A) | Confirmar o bloco |
| P16 | Bateria da ERB | Aberto | Abrir a tampa, com 10 minutos ou mais sem rede |
| P17 | Bornes grandes 2 x 7 | Aberto | Contar na montagem |
| P18 | Comprimento dos fios | A caixa real é 1350 x 350 x 240 mm | Base do comprimento (PCP) |
| P19 | Zona de porta da ERB | Parcial | Teste R5 e R6 ou consulta à Inovance |
| P20 | Duas revisões de esquema | Decidido: vale o Vitinho 19061867-ZL | Fechada |

## C.2 Pendências novas deste livro

| Selo | Assunto | O que fecha |
|---|---|---|
| `PREENCHER [Q47]` | Bloqueio e etiquetagem (LOTO) e exigências de norma sobre segurança do trabalho | Texto da NR-10 e das normas de elevadores |
| `PREENCHER [Q59]` | Função de cada chave da cadeia de segurança | Material do fabricante ou explicação do responsável técnico |
| Q56 | BFS1 e BFS2: qual é do carro e qual é do contrapeso | O esquema VerticalParts diz BFS1 = carro e BFS2 = contrapeso; falta confirmação |
| Jumpers 62 a 66 | Só de bancada ou também em campo? | Confirmação em campo (ver Apêndice A) |

Decisão de 15/11/2026: o "elevador de referência" é um modelo, não uma instalação. O que muda de um elevador para outro (RCS, CWSG, OS-G, MES-1, módulo SCB, máquina de tração, encoder, velocidade, comprimento dos cabos, placa de comando da cabina, operador de porta, UPS ou ARD) deixou de ser selo: o livro manda conferir no seu elevador e usa o pedido QC-2026-0014 (elevador EL21) como exemplo. A lista completa dos selos que restam está no Apêndice F, seção F.3.

## C.3 Correções ao Rev. 11

| Onde no Rev. 11 | Correção | Fonte |
|---|---|---|
| Conferências (págs. 34 e 35) | Chave de limite: 30 a 50 mm, e não 100 mm. Chaves de desaceleração 2 e 3: a partir de 2 e 3 m/s. Sensores de nível: 4, e não 1 a 3. Terra: abaixo de 10 ohm | Manual NICE3000new; o terra confirmado na pág. PDF 54 |
| Flat de 40 vias | X15 e X16 aparecem trocados | Esquema Vitinho /21 |
| Trafo | Secundário de 125 V e 63 VA (110 VA para 30 a 37 kW); o BOM diz 110 V e 150 VA | Esquema Vitinho /10 (PDF pág. 12) |
| Conector FAN | 8 posições, e não 6 | Esquema Vitinho |
| Conector EY3 | 3 sinais, e não 5 | Esquema Vitinho |
| Conector EY4 | 20 posições e 14 sinais (faltam 507 e 508); a numeração dos pinos 5 a 12 estava errada | Esquema Vitinho |
| Redes da cadeia (IV.2 e IV.3) | "121 = 119" e "FLSU e FLSD na rede 121" estão errados: a ordem é 119, FLSD, 120, FLSU, 121 | Esquema Vitinho /19 |
| Seção IV.4 (porta única) | Faltam os jumpers AA 6 com 14 e BA 8 com 9 | Esquema Vitinho /19 |
| X20 | É sobretemperatura do motor, e não freio | Esquema Vitinho /21 |
| E6 | Os 24 V saem da PCB-D1 para a KCB | Esquema Vitinho |
| S1 e TIS (pág. 29) | São do limitador de velocidade, e não do bypass | Esquema Vitinho /22 |
| Caixa do quadro | 1350 x 350 x 240 mm, e não 1350 x 450 x 350 mm | Desenho de furação do quadro (DES-FURACAO) |
| Tabela mestre | A tabela é a lista de fios reformatada; a conferência contra o esquema está no Apêndice A | Auditoria |

Fonte: `AUDITORIA_REV11.md` (lotes 7a e 7b), conferido contra o manual NICE3000new e os esquemas. As correções vindas do lote 7 foram feitas por agentes e ainda não conferidas ponto a ponto por mim; cada uma será verificada quando o capítulo correspondente migrar.
