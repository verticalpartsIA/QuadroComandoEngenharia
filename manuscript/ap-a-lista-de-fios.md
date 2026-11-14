# Apêndice A. Lista de fios conferida contra o esquema

> RASCUNHO v0.1 de 14/11/2026.

Esta lista vem do arquivo `Lista de fios.xlsx` da produção (125 ligações internas do quadro de comando). Ela não é a base do livro: cada ligação foi conferida contra o esquema Vitinho 19061867-ZL, que é a revisão de esquema válida para produção (decisão do Gelson em 14/11/2026). A coluna "Esquema" diz o que o desenho mostra.

Resultado: **91 conferem**, **22 divergem** e **12 não são verificáveis** (terras que o esquema só mostra como símbolo, e componentes que o esquema não desenha). Divergência não quer dizer erro de fiação: em vários casos é só diferença de numeração entre o desenho e a peça física.

Legenda das cores de fio da lista: PT = preto, AZ = azul, VD+AM = verde e amarelo. A bitola vem da lista; nenhum esquema lido indica bitola.

| # | Rede | Origem | Destino | Cor | mm² | cm | Esquema | Confiança | Observação |
|---|---|---|---|---|---|---|---|---|---|
| 1 |  | BY 2 | BY 4 | PT | 0,75 | 16 | Confere | alta | Confirmado também pela legenda de bornes da /17 (1-2, 4-3, 5-6) |
| 2 |  | BY 3 | BY 5 | PT | 0,75 | 16 | Confere | alta | Idem |
| 3 |  | BY 6 | MCTC-KCB-B4A KY9/4 | PT | 0,75 | 112 | Confere | alta | O nó BY 6 desce e se divide para KY6/4 e KY9/4. |
| 4 |  | BY A1 | MCTC-KCB-B4A KY2/2 | PT | 0,75 | 86 | Confere | alta |  |
| 5 |  | BY 11 | MCTC-KCB-B4A KY2/8 | PT | 0,75 | 86 | Confere | alta | O terminal 12 vai à 301 (KY2/6). |
| 6 |  | CID E 3 | CIU E 3 | PT | 0,75 | 7 | Confere | alta/média |  |
| 7 | X11 | CID E 4 | MCTC-KCB-B4A KY4/2 | PT | 0,75 | 100 | Confere | alta/média |  |
| 8 |  | CIS 13 | CID E 14 | PT | 0,75 | 7 | Confere | alta/média |  |
| 9 | 301 | CIS 3 | CIS 1 | PT | 0,75 | 7 | Confere | alta/média |  |
| 10 |  | CIS 4 | CIU E 3 | PT | 0,75 | 7 | Confere | alta/média |  |
| 11 |  | CIS 13 | CIU E 14 | PT | 0,75 | 7 | Confere | alta/média |  |
| 12 |  | CIU E 13 | CID E 13 | PT | 0,75 | 7 | Confere | alta/média |  |
| 13 | 125 | CIU E 13 | MCTC-KCB-B4A KY4/7 | PT | 0,75 | 100 | Confere | alta/média |  |
| 14 | 101B | DQFB1 2 | SZ 1 | PT | 0,75 | 70 | Confere | média | Precisou seguir traço na /10. O disjuntor aparece como QFB1, sem o "D" |
| 15 |  | DQFB1 1 | QFB1 2 | PT | 0,75 | 45 | Não verificável | média | O lado QFB1 2 existe, mas o DQFB1 não está no esquema. |
| 16 | 201 | DQFB2 2 | MCTC-KCB-B4A KY5/1 | PT | 0,75 | 84 | Diverge | média | Rede 201 e pino KY5/1 batem. A divergência é só o terminal do disjuntor: o desenho diz QFB2 3, a lista diz "DQFB2 2". Não existe "DQFB2" no desenho. Hipótese: a lista usa numeração física de disjuntor 2P (1,3 entrada; 2,4 saída), igual à QFB3 da /8, e o desenho da /10 está numerado de outro jeito. Conferir no disjuntor real. |
| 17 | 201 | DQFB2 2 | TIS 13 | PT | 0,75 | 73 | Confere | alta/média |  |
| 18 | 501 | DQFB3 2 | CZ 2 | PT | 0,75 | 30 | Diverge | média | O esquema não liga a tomada CZ à rede 501 nem ao QFB3; liga ao QFB4. |
| 19 | 501 | DQFB3 2 | MCTC-KCB-B4A POW1/1 | PT | 0,75 | 125 | Confere | média | O prefixo "D" de "DQFB3" não aparece no desenho (só QFB3). |
| 20 | 501 | DQFB3 2 | MCTC-ERB-A1 N | PT | 0,75 | 85 | Diverge | alta | Desenho: 501 vai a L. Lista: 501 vai a N. Ligação trocada com o fio 94. O secundário (PDF 16) mostra o mesmo (501 em L) |
| 21 |  | FX A2 | BY A2 | PT | 0,75 | 25 | Confere | média | Rede comum, sem fio direto desenhado entre os dois A2 |
| 22 |  | FX 31 | FX 21 | PT | 2,5 | 15 | Confere | alta | Confirmado em ampliação |
| 23 | 102 | FX A2 | SW A2 | PT | 0,75 | 25 | Confere | média | Rede comum |
| 24 |  | FX A1 | MCTC-KCB-B4A KY2/3 | PT | 0,75 | 86 | Confere | alta |  |
| 25 |  | FX 13 | MCTC-KCB-B4A KY2/9 | PT | 0,75 | 86 | Confere | alta | Bloco "Add when synchronous". |
| 26 |  | FX 14 | SW 12 | PT | 0,75 | 30 | Confere | média | Mesma rede 301, sem fio direto desenhado |
| 27 |  | FX 14 | BY 12 | PT | 0,75 | 24 | Confere | média | Idem |
| 28 |  | MCTC-ERB-A1 PE | CHAPA BOTOEIRA PE | VD+AM | 0,75 | 10 | Não verificável | baixa | Chapa da botoeira não aparece no desenho |
| 29 |  | MCTC-ERB-A1 ZQ+ | SZ 4 | PT | 0,75 | 85 | Diverge | alta | Desenho: ZQ+ não passa pelo SZ. SZ 4 é 302. Secundário (PDF 16) igual |
| 30 |  | MCTC-ERB-A1 ZQ+ | SW 73 | PT | 0,75 | 65 | Diverge | média | Desenho leva ERB ZQ+ ao lado de SW 53, não de SW 73. Precisou seguir traço (MT1 5 e 12) |
| 31 |  | MCTC-ERB-A1 ZQ- | BY 6 | PT | 0,75 | 88 | Confere | média | Mesma rede ZQ-, passando pela KCB |
| 32 | +CC-DC12 | MCTC-KCB-B4A KY10/9 | SZ 33 | PT | 0,75 | 100 | Diverge | média | Rede e pino KY10/9 batem. O soquete SZ do desenho tem pinos 1 a 9 (DC12=3); a lista diz "SZ 33", que não existe nessa numeração. Pode ser outra convenção de numeração do conector físico (hipótese). |
| 33 | +CC-302 | MCTC-KCB-B4A KY10/3 | MCTC-ERB-A1 COM | PT | 0,75 | 80 | Confere | média | O desenho passa o fio pelo SZ 4; a lista liga direto ao ERB. Extremos batem. |
| 34 | +CC-302 | MCTC-KCB-B4A KY10/6 | MCTC-ERB-A1 MQ- | PT | 0,75 | 80 | Confere | média | Mesma observação do fio 33. |
| 35 | +CC-FL1 | MCTC-KCB-B4A KY10/8 | MCTC-ERB-A1 MQ+ | PT | 0,75 | 80 | Confere | média | Mesma observação. |
| 36 | +CC-133 | MCTC-KCB-B4A KY11/5 | SZ 13 | PT | 0,75 | 100 | Diverge | média | Rede e KY11/5 batem; o número do pino SZ não (desenho: 2; lista: 13). Mesma ressalva do fio 32. |
| 37 | +CC-131 | MCTC-KCB-B4A KY11/6 | SZ 23 | PT | 0,75 | 100 | Diverge | média | Desenho: SZ 7; lista: SZ 23. |
| 38 | 301 | MCTC-KCB-B4A KY4/1 | CIS 1 | PT | 0,75 | 105 | Confere | alta/média |  |
| 39 | X9 | MCTC-KCB-B4A KY4/4 | CIS 2 | PT | 0,75 | 105 | Confere | alta/média |  |
| 40 | 118 | MCTC-KCB-B4A KY4/8 | CIS 14 | PT | 0,75 | 105 | Confere | alta/média |  |
| 41 | 122B | MCTC-KCB-B4A KY4/10 | CIS 12 | PT | 0,75 | 105 | Confere | alta/média |  |
| 42 | 123 | MCTC-KCB-B4A KY4/11 | CIS 11 | PT | 0,75 | 105 | Confere | alta/média |  |
| 43 | X10 | MCTC-KCB-B4A KY4/3 | CIU E 4 | PT | 0,75 | 100 | Confere | alta/média |  |
| 44 |  | MCTC-KCB-B4A KY6/4 | MCTC-KCB-B4A KY9/4 | PT | 0,75 | 20 | Confere | média | O desenho mostra a união dos dois pinos no nó do BY 6; a forma física do fio não é especificada. |
| 45 | 207 | MCTC-KCB-B4A KY6/1 | MCTC-PCB-D1 J2/1 | PT | 0,75 | 67 | Confere | alta |  |
| 46 | 208 | MCTC-KCB-B4A KY6/2 | MCTC-PCB-D1 J2/2 | PT | 0,75 | 67 | Confere | alta |  |
| 47 | 301 | MCTC-KCB-B4A KY3/1 | MCTC-PCB-D1 J4/1 | PT | 0,75 | 54 | Confere | alta |  |
| 48 | 302 | MCTC-KCB-B4A KY3/2 | MCTC-PCB-D1 J4/4 | PT | 0,75 | 54 | Confere | alta |  |
| 49 | 101A | MCTC-KCB-B4A KY4/12 | MES 2 | PT | 0,75 | 105 | Confere | alta/média |  |
| 50 | 110 | MCTC-KCB-B4A KY4/9 | MES 1 | PT | 0,75 | 105 | Confere | alta/média |  |
| 51 | 102 | MCTC-KCB-B4A KY5/8 | QFB1 4 | PT | 0,75 | 80 | Confere | média | O desenho rotula esse terminal como "N", não "4". Equivale ao polo N de saída numa numeração 1/2/3/4 (hipótese). |
| 52 | BK1+ | MCTC-KCB-B4A KY8/4 | SW 54 | PT | 0,75 | 105 | Confere | alta |  |
| 53 |  | MCTC-KCB-B4A KY8/3 | SW 53 | PT | 0,75 | 85 | Confere | alta |  |
| 54 |  | MCTC-KCB-B4A KY9/2 | SW 73 | PT | 0,75 | 85 | Confere | alta |  |
| 55 | 207 | MCTC-KCB-B4A KY8/1 | TRF 220V | PT | 0,75 | 140 | Confere | alta |  |
| 56 | 208 | MCTC-KCB-B4A KY8/2 | TRF OP | PT | 0,75 | 140 | Confere | média | A lista escreve "OP" (letra O); o desenho rotula "0P" (zero). Provável erro de digitação. |
| 57 |  | MCTC-KCB-B4A KY9/3 | SW 74 | PT | 0,75 | 88 | Confere | alta |  |
| 58 |  | MCTC-KCB-B4A KY2/6 | SW 12 | PT | 0,75 | 100 | Confere | alta |  |
| 59 | CAN+ | MCTC-KCB-B4A KY12/1 | MCTC-PCB-D1 J4/2 | PT | 0,75 | 54 | Confere | alta |  |
| 60 | CAN- | MCTC-KCB-B4A KY12/2 | MCTC-PCB-D1 J4/5 | PT | 0,75 | 54 | Confere | alta |  |
| 61 | jumper | MCTC-KCB-B4A BA/8 | MCTC-KCB-B4A BA/9 | PT | 0,75 | 9 | Confere | alta | Une 132 a 133. É o jumper previsto pelo desenho, só para elevador de porta única. Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 62 | jumper | MCTC-KCB-B4A BD/3 | MCTC-KCB-B4A BD/1 | PT | 0,75 | 9 | Diverge | alta | Une a entrada X14 (desaceleração de subida 1) à 301. Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 63 | jumper | MCTC-KCB-B4A BD/3 | MCTC-KCB-B4A BE/3 | PT | 0,75 | 9 | Diverge | alta | Une X14 a X15. Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 64 | jumper | MCTC-KCB-B4A HW/3 | MCTC-KCB-B4A AA/4 | PT | 0,75 | 9 | Diverge | alta | Une a rede 110 à 130. Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 65 | jumper | MCTC-KCB-B4A AA/5 | MCTC-KCB-B4A AA/4 | PT | 0,75 | 9 | Diverge | alta | Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 66 | jumper | MCTC-KCB-B4A AA/5 | MCTC-KCB-B4A AA/6 | PT | 0,75 | 9 | Diverge | alta | Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 67 | jumper | MCTC-KCB-B4A AA/14 | MCTC-KCB-B4A AA/6 | PT | 0,75 | 9 | Confere | alta | Une 134 a 133. É o jumper previsto pelo desenho, só para porta única. Ver o aviso sobre os jumpers 62 a 66 abaixo da tabela. |
| 68 |  | MCTC-MCB-C3 PE | MCTC-KCB-B4A PE-M1 | VD+AM | 0,75 | 63 | Não verificável | baixa | O desenho só mostra PE da KCB em AA/3 (/11) indo ao PE do armário. |
| 69 |  | MCTC-MCB-C3 CN2/1 | MCTC-KCB-B4A KY1/6 | PT | 0,75 | 55 | Confere | alta |  |
| 70 |  | MCTC-MCB-C3 CN2/2 | MCTC-KCB-B4A KY1/1 | PT | 0,75 | 55 | Confere | alta |  |
| 71 |  | MCTC-MCB-C3 CN2/3 | MCTC-KCB-B4A KY1/4 | PT | 0,75 | 55 | Confere | alta |  |
| 72 |  | MCTC-MCB-C3 CN2/5 | MCTC-KCB-B4A KY1/3 | PT | 0,75 | 55 | Confere | alta |  |
| 73 |  | MCTC-MCB-C3 CN2/4 | MCTC-KCB-B4A KY1/2 | PT | 0,75 | 55 | Confere | alta |  |
| 74 | 102 | MCTC-MCB-C3 CN2/6 | SW A2 | PT | 0,75 | 123 | Confere | alta |  |
| 75 | BK- | MCTC-PCB-D1 J3/1 | BY 1 | PT | 0,75 | 64 | Confere | alta |  |
| 76 |  | MCTC-PCB-D1 PE | MCTC-KCB-B4A PE | VD+AM | 0,75 | 20 | Não verificável | média | Os dois pontos estão na rede PE do armário, mas não há fio direto entre eles no desenho, e a lista não diz o pino de PE da KCB. |
| 77 |  | MCTC-PCB-D1 PE | MCTC-MCB-C2 PE | VD+AM | 0,75 | 75 | Não verificável | baixa | Só símbolo de terra |
| 78 | BK1+ | MCTC-PCB-D1 J3/2 | SW 54 | PT | 0,75 | 98 | Confere | alta |  |
| 79 | BK2+ | MCTC-PCB-D1 J3/3 | SW 74 | PT | 0,75 | 98 | Confere | alta |  |
| 80 |  | NICE3000 U | SW 1 | PT | 6 | 88 | Confere | alta | Desenho não informa bitola (lista: 6 mm2) |
| 81 |  | NICE3000 V | SW 3 | PT | 6 | 88 | Confere | alta | Idem |
| 82 |  | NICE3000 W | SW 5 | PT | 6 | 88 | Confere | alta | Idem |
| 83 |  | QF 2 | NICE3000 R | PT | 6 | 125 | Confere | média | O desenho passa pelo filtro EMC e pelo borne TA; seguiu-se o traço. A lista não cita o filtro. |
| 84 |  | QF 4 | NICE3000 S | PT | 6 | 125 | Confere | média | Mesmo comentário do fio 83. |
| 85 |  | QF 6 | NICE3000 T | PT | 6 | 125 | Confere | média | Mesmo comentário do fio 83. |
| 86 | R | QF 2 | QFB2 1 | PT | 0,75 | 100 | Confere | média | Origem real é QF 2 via filtro EMC e TA R. Borne 1 de QFB2 confere. |
| 87 |  | QF 1 | QFB3 1 | PT | 0,75 | 18 | Confere | alta | Ligação a montante do QF no mesmo nó do QF 1. |
| 88 | 201 | QFB2 2 | DQFB2 1 | PT | 0,75 | 45 | Diverge | média | Rede 201 confere, mas no desenho o borne de saída é 3 (o borne 2 de QFB2 é a entrada N). DQFB2 não existe. |
| 89 | 202 | QFB2 4 | MCTC-KCB-B4A KY5/5 | PT | 0,75 | 84 | Confere | alta |  |
| 90 | 202 | QFB2 4 | XB 202 | PT | 0,75 | 66 | Confere | média | XB 202 aparece nos dois esquemas (Vitinho /22; VerticalParts pág. 15) |
| 91 | 502 | QFB3 4 | CZ 1 | PT | 0,75 | 30 | Diverge | média | QFB3 4 = 502 confere; o destino CZ 1 não bate. |
| 92 | 501 | QFB3 2 | DQFB3 1 | PT | 0,75 | 45 | Não verificável | média | Origem confere; o DQFB3 não está no esquema. |
| 93 | 502 | QFB3 4 | MCTC-KCB-B4A POW1/2 | PT | 0,75 | 125 | Confere | alta |  |
| 94 | 502 | QFB3 4 | MCTC-ERB-A1 L | PT | 0,75 | 85 | Diverge | alta | Desenho: 502 vai a N. Lista: 502 vai a L. Troca com o fio 20. Secundário igual ao principal |
| 95 |  | S1 14 | XB 203 | PT | 0,75 | 88 | Confere | alta/média |  |
| 96 |  | S1 24 | XB 205 | PT | 0,75 | 88 | Confere | alta/média |  |
| 97 |  | SW 2 | FX 22 | PT | 2,5 | 17 | Confere | alta | Desenho não informa bitola (lista: 2,5 mm2) |
| 98 |  | SW 4 | FX 32 | PT | 2,5 | 17 | Confere | alta | Idem |
| 99 |  | SW 6 | FX 21 | PT | 2,5 | 47 | Confere | alta | Idem |
| 100 |  | SW 2 | TA U | PT | 6 | 50 | Confere | alta | Lista: 6 mm2, sem indicação no desenho |
| 101 |  | SW 4 | TA V | PT | 6 | 50 | Confere | alta | Idem |
| 102 |  | SW 6 | TA W | PT | 6 | 50 | Confere | alta | Idem |
| 103 |  | SW A1 | MCTC-KCB-B4A KY2/1 | PT | 0,75 | 86 | Confere | alta |  |
| 104 |  | SW 11 | MCTC-KCB-B4A KY2/7 | PT | 0,75 | 86 | Confere | alta |  |
| 105 | 101 | SZ 2 | MCTC-KCB-B4A KY5/7 | PT | 0,75 | 65 | Diverge | média | Rede 101 e KY5/7 batem; o pino SZ do desenho é 6, a lista diz 2 (no desenho o SZ 2 é a 133). Mesma ressalva do fio 32. |
| 106 | T02 | SZ 34 | MCTC-KCB-B4A KY10/10 | PT | 0,75 | 100 | Diverge | média | Desenho: SZ 8; lista: SZ 34. Mesma ressalva. |
| 107 |  | SZ 14 | MCTC-ERB-A1 MS+ | PT | 0,75 | 85 | Diverge | média | Desenho: MS+ em SZ 2. Lista: "SZ 14", pino que não existe. Pode ser notação de outro conector, mas não bate com o esquema |
| 108 |  | SZ 24 | MCTC-ERB-A1 MS- | PT | 0,75 | 85 | Diverge | média | Desenho: MS- em SZ 7. Lista: "SZ 24", inexistente |
| 109 | ZQ1+ | SZ 3 | SW 53 | PT | 0,75 | 65 | Diverge | alta | Desenho: ZQ1+ chega por MT, não pelo SZ. O destino SW 53 está correto, a origem SZ 3 não |
| 110 |  | TIS 14 | S1 13 | PT | 0,75 | 7 | Confere | alta/média |  |
| 111 |  | TIS 14 | S1 23 | PT | 0,75 | 7 | Confere | alta/média |  |
| 112 |  | TRF 125V | QFB1 1 | PT | 0,75 | 56 | Confere | média | Seguiu-se o traço. Secundário rotulado 125V (BOM diz 110 V). |
| 113 |  | TRF 0S | QFB1 3 | PT | 0,75 | 56 | Confere | média | Ligação a N confere; o rótulo do desenho é N e não 3. Se "3" for a numeração do componente real, não dá para conferir pelo desenho. |
| 114 |  | TRF 0S | XPE PE | VD+AM | 0,75 | 30 | Não verificável | baixa | O desenho aterra o 0S só como símbolo; não há ponto explícito. |
| 115 |  | XA R | QF 1 | PT | 6 | 50 | Confere | alta | Só na folha /8 (MRL). |
| 116 |  | XA S | QF 3 | PT | 6 | 50 | Confere | alta |  |
| 117 |  | XA T | QF 5 | PT | 6 | 50 | Confere | alta |  |
| 118 | N | XA N | QFB2 3 | AZ | 0,75 | 100 | Diverge | média | O neutro de QFB2 entra no borne 2, não no 3; além disso passa por QF 7, EMC e TA N, e não direto de XA N. |
| 119 | N | XA N | QFB3 3 | AZ | 0,75 | 18 | Confere | alta |  |
| 120 | 202 | XB 202 | XB 202 | PT | 0,75 | 20 | Confere | média | XB 202 aparece nos dois esquemas (Vitinho /22; VerticalParts pág. 15) |
| 121 |  | XPE PE | CZ PE | VD+AM | 0,75 | 50 | Não verificável | baixa | Só símbolo de terra; XPE ausente. |
| 122 |  | XPE PE | MCTC-ERB-A1 PE | VD+AM | 0,75 | 70 | Não verificável | baixa | Sem ponto de ligação explícito na ERB |
| 123 |  | XPE PE | MCTC-MCB-C2 PE | VD+AM | 0,75 | 157 | Não verificável | baixa |  |
| 124 |  | XPE PE | NICE3000 PE | VD+AM | 6 | 160 | Não verificável | baixa |  |
| 125 |  | XPE PE | TRF PE | VD+AM | 0,75 | 46 | Não verificável | baixa |  |

> **PERIGO.** Os fios 62 a 66 (jumpers) não existem no esquema Vitinho nem no esquema VerticalParts. Pelas redes do desenho, o fio 64 liga o início da cadeia de segurança (rede 110) ao fim dela (rede 130, entrada X25), e os fios 65 e 66 fazem o mesmo com as fechaduras das portas. Instalados num quadro de campo, eles anulam essas proteções. O responsável técnico indicou que são jumpers só de bancada, sem confirmação em campo. Remova-os antes de ligar os cabos de campo. Os fios 61 e 67 são diferentes: o esquema os prevê para elevador de porta única.

> **NOTA.** Nos fios 29, 32, 36, 37 e 105 a 109 o SZ aparece numerado em pares (1-2, 3-4, 13-14, 23-24 e 33-34). Segundo o responsável técnico, é assim que o quadro real implementa a tomada de 9 pinos do esquema, com bornes pequenos em pares. A divergência desses fios é de numeração, e a rede e o pino da KCB conferem. O mapa entre os pares e os pinos da tomada ainda precisa de confirmação visual no quadro.

Fonte: `Lista de fios.xlsx` (produção); conferência contra o esquema Vitinho 19061867-ZL, lotes 1 a 6 da auditoria (arquivos em `auditoria/`).
