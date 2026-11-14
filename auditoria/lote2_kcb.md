# Auditoria lote 2: fios da placa MCTC-KCB-B4A contra o esquema

Base de verdade: esquema principal Inovance 19061867-ZL (51 pp.), arquivo "Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf". Convenção: folha /N do carimbo = página do PDF N+2. O esquema secundário (19060918-ZL) foi usado apenas para a legenda de siglas (ULS/DLS), PDF pág. 12 dele.

Nenhum arquivo existente foi alterado. Entrada: lote2_kcb.txt (48 fios).

## 1. Como os conectores da KCB foram lidos (folha /21, PDF pág. 23)

Numeração por fileira: o pino 1 fica no canto superior esquerdo e a numeração segue a fileira de cima e depois a de baixo (confirmado pelo KY1 e pelas folhas /10, /11, /13, /17, /44, que repetem os números dos pinos).

| Conector | Leitura (pino = rede) |
|---|---|
| KY2 | 1=Y1, 2=Y2, 3=Y3, 4=vazio, 5=Y2A, 6=301, 7=X6, 8=X7, 9=X8, 10=X5 (confirmado na /17) |
| KY3 | 1=301, 2=302 |
| KY5 | 1=201, 2 a 4 vazios, 5=202, 6=vazio, 7=101, 8=102 |
| KY6 | 1=207, 2=208, 3=ZQA1, 4=ZQ1- |
| KY8 | 1=207, 2=208, 3=ZQ1+, 4=ZQA1 |
| KY9 | 1=vazio, 2=ZQ2+, 3=ZQA2, 4=ZQ2- |
| KY10 | 1=vazio, 2=301, 3=302, 4=CAN1+, 5=CAN1-, 6=302, 7=301, 8=FL1, 9=DC12, 10=T02 |
| KY11 | 1=122, 2=122A, 3=SGC3, 4=SGC2, 5=133, 6=131 |
| KY12 | 1=CAN+, 2=CAN- |
| POW1 | 1=501, 2=502 |
| AA (fileira de cima 1 a 8, de baixo 9 a 16) | 1=207, 3=PE, 4=130, 5=131A, 6=133, 8=507, 9=208, 11=132, 12=125, 13=123, 14=134, 16=508 (confirmado na /11) |
| BA | 1=PE, 2=118, 3=121, 4=131, 5=122A, 6=111, 7=132, 8=132, 9=133, 10=123 (confirmado na /19: BA4=131, BA7=132, BA8 e BA9 no trecho 132/133) |
| HW | 2=111, 3=110, 4=PE (confirmado na /18) |
| BD | 1=301, 2=302, 3=ULS1 (X14), 4=ULS2 (X16) (confirmado na /44) |
| BE | 1=301, 2=302, 3=DLS1 (X15), 4=DLS2 (X17) (confirmado na /44) |

Observação: a etiqueta de numeração do BD/BE no desenho da /21 mostra "8" na fileira de baixo (provável erro de cópia do desenho); a /44 mostra BD/BE com pinos 1 a 4, e foi essa numeração usada.

## 2. Tabela fio a fio

Legenda de confiança: alta = pino e rede legíveis; média = precisou seguir traço ou interpretar nomenclatura; baixa = leitura incerta.

| Fio | Ligação listada | Evidência no esquema | Resultado | Confiança | Observação |
|---|---|---|---|---|---|
| 3 | BY 6 para KY9/4 | /13 (pág. 15): contatos BY 1-2, 4-3, 5-6 em série entre BK- (J3/1) e o nó que alimenta KY6/4 (ZQ1-) e KY9/4 (ZQ2-). | CONFERE | alta | O nó BY 6 desce e se divide para KY6/4 e KY9/4. |
| 4 | BY A1 para KY2/2 | /17 (pág. 19): KY2/2=Y2 liga à bobina BY (A1). | CONFERE | alta | |
| 5 | BY 11 para KY2/8 | /17: contato de realimentação BY 11-12; KY2/8=X7 liga ao terminal 11. | CONFERE | alta | O terminal 12 vai à 301 (KY2/6). |
| 16 | DQFB2 2 (rede 201) para KY5/1 | /10 (pág. 12): QFB2 (2P) tem entradas 1 e 2 (R e N) e saídas 3 e 4; a rede 201 sai do terminal 3 e vai a KY5/1. | DIVERGE | média | Rede 201 e pino KY5/1 batem. A divergência é só o terminal do disjuntor: o desenho diz QFB2 3, a lista diz "DQFB2 2". Não existe "DQFB2" no desenho. Hipótese: a lista usa numeração física de disjuntor 2P (1,3 entrada; 2,4 saída), igual à QFB3 da /8, e o desenho da /10 está numerado de outro jeito. Conferir no disjuntor real. |
| 19 | DQFB3 2 (rede 501) para POW1/1 | /8 (pág. 10): QFB3 (1 e 3 entrada, 2 e 4 saída); 501 sai do terminal 2. /11 (pág. 13): POW1/1=501. | CONFERE | média | O prefixo "D" de "DQFB3" não aparece no desenho (só QFB3). |
| 24 | FX A1 para KY2/3 | /17: KY2/3=Y3 liga à bobina FX (A1), bloco "Add when synchronous". | CONFERE | alta | |
| 25 | FX 13 para KY2/9 | /17: KY2/9=X8 liga ao contato FX 13; o 14 vai à 301. | CONFERE | alta | Bloco "Add when synchronous". |
| 32 | KY10/9 (DC12) para SZ 33 | /23 (pág. 25): KY10/9=DC12 liga ao soquete SZ pino 3 (DC12). | DIVERGE | média | Rede e pino KY10/9 batem. O soquete SZ do desenho tem pinos 1 a 9 (DC12=3); a lista diz "SZ 33", que não existe nessa numeração. Pode ser outra convenção de numeração do conector físico (hipótese). |
| 33 | KY10/3 (302) para ERB COM | /23: KY10/3=302 desce pelo soquete SZ pino 4 e chega ao COM do ERB. | CONFERE | média | O desenho passa o fio pelo SZ 4; a lista liga direto ao ERB. Extremos batem. |
| 34 | KY10/6 (302) para ERB MQ- | /23: KY10/6=302 pelo SZ pino 9 até MQ-. | CONFERE | média | Mesma observação do fio 33. |
| 35 | KY10/8 (FL1) para ERB MQ+ | /23: KY10/8=FL1 pelo SZ pino 5 até MQ+. | CONFERE | média | Mesma observação. |
| 36 | KY11/5 (133) para SZ 13 | /23: KY11/5=133 liga ao SZ pino 2 (133); o mesmo traço segue ao MS+ do ERB. | DIVERGE | média | Rede e KY11/5 batem; o número do pino SZ não (desenho: 2; lista: 13). Mesma ressalva do fio 32. |
| 37 | KY11/6 (131) para SZ 23 | /23: KY11/6=131 liga ao SZ pino 7 (131), segue ao MS- do ERB. | DIVERGE | média | Desenho: SZ 7; lista: SZ 23. |
| 44 | KY6/4 para KY9/4 | /13: KY6/4 (ZQ1-) e KY9/4 (ZQ2-) estão no mesmo nó, ligado ao BY 6. | CONFERE | média | O desenho mostra a união dos dois pinos no nó do BY 6; a forma física do fio não é especificada. |
| 45 | KY6/1 (207) para PCB-D1 J2/1 | /10 (pág. 12): KY6/1=207 liga a J2/1 (L) da PCB-D1. | CONFERE | alta | |
| 46 | KY6/2 (208) para PCB-D1 J2/2 | /10: KY6/2=208 liga a J2/2 (N). | CONFERE | alta | |
| 47 | KY3/1 (301) para PCB-D1 J4/1 | /10: KY3/1=301 liga a J4/1 (301). | CONFERE | alta | |
| 48 | KY3/2 (302) para PCB-D1 J4/4 | /10: KY3/2=302 liga a J4/4 (302). | CONFERE | alta | |
| 51 | KY5/8 (102) para QFB1 4 | /10: KY5/8=102 liga ao terminal N do lado de carga do QFB1 (1P+N); o 101 sai do terminal 2. | CONFERE | média | O desenho rotula esse terminal como "N", não "4". Equivale ao polo N de saída numa numeração 1/2/3/4 (hipótese). |
| 52 | KY8/4 (BK1+) para SW 54 | /13: KY8/4=ZQA1 liga ao nó BK1+ (J3/2) junto do contato SW 54. | CONFERE | alta | |
| 53 | KY8/3 para SW 53 | /13: KY8/3=ZQ1+ liga ao contato SW 53. | CONFERE | alta | |
| 54 | KY9/2 para SW 73 | /13: KY9/2=ZQ2+ liga ao contato SW 73 (lista de contatos da /17 confirma 74-73). | CONFERE | alta | |
| 55 | KY8/1 (207) para TRF 220V | /10: KY8/1=207 liga ao TRF 220V. | CONFERE | alta | |
| 56 | KY8/2 (208) para TRF OP | /10: KY8/2=208 liga ao TRF "0P" (zero P). | CONFERE | média | A lista escreve "OP" (letra O); o desenho rotula "0P" (zero). Provável erro de digitação. |
| 57 | KY9/3 para SW 74 | /13: KY9/3=ZQA2 liga ao nó BK2+ (J3/3) junto do contato SW 74. | CONFERE | alta | |
| 58 | SW 12 para KY2/6 | /17: terminal 12 do contato SW vai à 301 = KY2/6. | CONFERE | alta | |
| 59 | KY12/1 (CAN+) para PCB-D1 J4/2 | /24 (pág. 26): KY12/1 CAN+ liga a J4/2 CAN+. | CONFERE | alta | |
| 60 | KY12/2 (CAN-) para PCB-D1 J4/5 | /24: KY12/2 CAN- liga a J4/5 CAN-. | CONFERE | alta | |
| 61 | jumper BA/8 para BA/9 | /19 (pág. 21): BA/8 está na rede 132, BA/9 na 133. Nota do desenho: "single door, connect BA-P08 and BA-P09". | CONFERE | alta | Une 132 a 133. É o jumper previsto pelo desenho, só para elevador de porta única. Ver seção 4. |
| 62 | jumper BD/3 para BD/1 | /44 (pág. 46): BD/3=ULS1 (X14), BD/1=301. O desenho não mostra essa ligação; ULS1 vai ao sensor no poço. | DIVERGE | alta | Une a entrada X14 (desaceleração de subida 1) à 301. Ver seção 4. |
| 63 | jumper BD/3 para BE/3 | /44: BD/3=ULS1 (X14), BE/3=DLS1 (X15). Sem ligação no desenho. | DIVERGE | alta | Une X14 a X15. Ver seção 4. |
| 64 | jumper HW/3 para AA/4 | /18 (pág. 20) e /19: HW/3=110 (após o botão MES); AA/4=130 (fim da cadeia de segurança, vai a X25). Sem ligação no desenho. | DIVERGE | alta | Une a rede 110 à 130. Ver seção 4. |
| 65 | jumper AA/5 para AA/4 | /19: AA/5=131A, AA/4=130. Entre elas o desenho coloca os trincos da porta de cabina GS1/GS2. | DIVERGE | alta | Ver seção 4. |
| 66 | jumper AA/5 para AA/6 | /19: AA/5=131A, AA/6=133. Sem ligação no desenho. | DIVERGE | alta | Ver seção 4. |
| 67 | jumper AA/14 para AA/6 | /19: AA/14=134, AA/6=133. Nota do desenho: "single door, connect AA-P06, AA-P14". | CONFERE | alta | Une 134 a 133. É o jumper previsto pelo desenho, só para porta única. Ver seção 4. |
| 68 | MCB-C3 PE para KCB PE-M1 | Não há borne "PE-M1" nas folhas lidas, nem PE da MCB-C3 ligado à KCB. | NÃO VERIFICÁVEL | baixa | O desenho só mostra PE da KCB em AA/3 (/11) indo ao PE do armário. |
| 69 | MCB-C3 CN2/1 para KY1/6 | /19: KY1/6 (rede 102) liga a CN2/1 da MCB-C3 (traço do topo). | CONFERE | alta | |
| 70 | MCB-C3 CN2/2 para KY1/1 | /19: KY1/1 (130) liga a CN2/2 (X25). | CONFERE | alta | |
| 71 | MCB-C3 CN2/3 para KY1/4 | /19: KY1/4 (131) liga a CN2/3 (X26). | CONFERE | alta | |
| 72 | MCB-C3 CN2/5 para KY1/3 | /19: KY1/3 (133) liga a CN2/5 (X28). | CONFERE | alta | |
| 73 | MCB-C3 CN2/4 para KY1/2 | /19: KY1/2 (134) liga a CN2/4 (X27). | CONFERE | alta | |
| 76 | PCB-D1 PE para KCB PE | /10: PCB-D1 J3/8 vai ao símbolo de PE; /11: KCB AA/3 vai a +CC-PE. | NÃO VERIFICÁVEL | média | Os dois pontos estão na rede PE do armário, mas não há fio direto entre eles no desenho, e a lista não diz o pino de PE da KCB. |
| 89 | QFB2 4 (202) para KY5/5 | /10: QFB2 terminal 4 = rede 202 = KY5/5. | CONFERE | alta | |
| 93 | QFB3 4 (502) para POW1/2 | /8: QFB3 terminal 4 = 502. /11: POW1/2=502. | CONFERE | alta | |
| 103 | SW A1 para KY2/1 | /17: KY2/1=Y1 liga à bobina SW (A1). | CONFERE | alta | |
| 104 | SW 11 para KY2/7 | /17: KY2/7=X6 liga ao terminal 11 de SW. | CONFERE | alta | |
| 105 | SZ 2 (rede 101) para KY5/7 | /10: KY5/7=101 vai à seta "101 / 23.4:B"; /23: essa rede entra no SZ pino 6 (101). | DIVERGE | média | Rede 101 e KY5/7 batem; o pino SZ do desenho é 6, a lista diz 2 (no desenho o SZ 2 é a 133). Mesma ressalva do fio 32. |
| 106 | SZ 34 (T02) para KY10/10 | /23: KY10/10=T02 liga ao SZ pino 8 (T02). | DIVERGE | média | Desenho: SZ 8; lista: SZ 34. Mesma ressalva. |

## 3. Resumo

Contagem (48 fios): 35 CONFERE, 11 DIVERGE, 2 NÃO VERIFICÁVEL.

CONFERE (35): 3, 4, 5, 19, 24, 25, 33, 34, 35, 44, 45, 46, 47, 48, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 67, 69, 70, 71, 72, 73, 89, 93, 103, 104.

DIVERGE (11):
- Jumpers 62, 63, 64, 65, 66: ligações que o esquema não mostra (seção 4). São as divergências mais importantes.
- Fio 16: terminal do disjuntor (desenho QFB2 3, lista "DQFB2 2"). Rede e KY5/1 conferem.
- Fios 32, 36, 37, 105, 106: numeração do pino SZ (desenho 3, 2, 7, 6, 8; lista 33, 13, 23, 2, 34). Em todos, a rede e o pino da KCB conferem. Pode ser só outra numeração do conector físico, o que precisa de checagem no próprio SZ.

NÃO VERIFICÁVEL (2): 68 (PE-M1 não aparece), 76 (PE sem pino da KCB e sem fio direto no desenho).

Pontos de atenção que não mudam o resultado: o prefixo "D" em DQFB2/DQFB3 não existe no desenho; "TRF OP" provavelmente é "0P"; QFB1 4 corresponde ao terminal "N" do desenho; nos fios 33 a 35 o desenho passa o traço pelo soquete SZ, que a lista omite.

## 4. Os jumpers 61 a 67

Redes unidas por cada jumper (pinos identificados nas folhas /11, /18, /19 e /44):

| Fio | Pino A (rede) | Pino B (rede) | O que o esquema espera |
|---|---|---|---|
| 61 | BA/8 (132) | BA/9 (133) | /19: entre as duas fica a cadeia dos trincos traseiros 1RDS...nRDS; caixa tracejada diz "single door, connect BA-P08 and BA-P09". |
| 62 | BD/3 (ULS1, X14) | BD/1 (301) | /44: BD/3 liga ao sensor ULS1 no poço; BD/1 é a 301. Nada liga um ao outro. |
| 63 | BD/3 (ULS1, X14) | BE/3 (DLS1, X15) | /44: cada um liga ao seu sensor (ULS1 e DLS1). Nada liga um ao outro. |
| 64 | HW/3 (110) | AA/4 (130) | /19: 110 está logo após o botão MES; 130 é o fim da cadeia de segurança, que vai a KY1/1 e CN2/2 (X25). |
| 65 | AA/5 (131A) | AA/4 (130) | /19: entre 130 e 131A ficam os trincos GS1/GS2 da porta de cabina. |
| 66 | AA/5 (131A) | AA/6 (133) | /19: 131A passa pelo UCMP até 131, depois pelos trincos de pavimento 1DS..nDS até 132. A 133 só vem depois, via BA/8 a BA/9. |
| 67 | AA/14 (134) | AA/6 (133) | /19: entre as duas fica o trinco traseiro GS2; caixa tracejada diz "single door, connect AA-P06, AA-P14". |

### 4.1 Jumpers 61 e 67

São os dois jumpers que o próprio desenho prevê, e só para elevador de porta única (sem segunda porta/porta traseira). Eles fecham o trecho dos trincos traseiros: 132 com 133 (fio 61) e 133 com 134 (fio 67). Se o elevador tiver segunda porta, esses jumpers anulam a supervisão dos trincos dessa porta, porque a rede 133 (X28) e a 134 (X27) passam a ver a rede vizinha sem passar pelos contatos traseiros. Em porta única, é o esperado pelo desenho.

### 4.2 Jumpers 64, 65 e 66 (cadeia de segurança e trincos)

O desenho não prevê nenhum deles. O que cada um faz eletricamente, olhando só para o desenho da /19:

- Fio 64 (110 com 130): liga o início da cadeia (110, após o MES) ao fim dela (130). Todos os dispositivos desenhados entre esses dois pontos ficam em curto: MES-1 e MES-2 da máquina, botões de poço PES1/PES2, tensor GTS, chaves PIT, para-choques BFS1/BFS2, fins de curso FLSU/FLSD, chaves de inspeção do topo da cabina (TCI, TES, CIS), SOS, S1, OS/OS-G/CWSG/RCS, entre outros desenhados nesse trecho. A entrada X25 (detecção do circuito de segurança) passa a receber a rede 110 mesmo com qualquer um deles aberto. A rede 130 também alimenta o início da cadeia de trincos (GS1 até 131A), então essa cadeia também fica energizada direto da 110.
- Fio 65 (131A com 130): curto-circuita os trincos GS1/GS2 da porta de cabina. A rede 131A (e, pelo contato UCMP desenhado, a 131 que vai a X26) fica igual à 130 com a porta de cabina aberta.
- Fio 66 (131A com 133): liga a rede de antes dos trincos de pavimento à rede de depois deles, curto-circuitando 1DS até nDS (e RDS). X28 passa a ver a mesma tensão que X26.
- Com os fios 61, 64, 65, 66 e 67 todos instalados, as redes 110, 130, 131A, 131, 132, 133 e 134 ficam no mesmo potencial. Isso inclui as entradas X25, X26, X27 e X28 da MCB-C3, que o desenho usa para "Safety circuit detection", "Door lock adhesion detection" e "Door detection" (tabela da /21). O que sobra de proteção upstream é só o MES e o fusível F3.
- Consequência provável (hipótese, não está no desenho): o controlador passaria a ler "cadeia de segurança fechada" e "portas travadas" mesmo com dispositivos abertos ou portas abertas, e os testes de aderência de trinco (X26, X28) perderiam sentido. Isso derrotaria a função de segurança dessas entradas. Como os jumpers 64, 65 e 66 não existem no desenho, a hipótese mais plausível é que sejam jumpers de bancada/teste que não deveriam seguir para campo; essa hipótese não foi verificada.

### 4.3 Jumpers 62 e 63 (desaceleração)

- Fio 62 (BD/3 com BD/1): X14 (desaceleração de subida 1) fica ligada à 301 o tempo todo, como se o sensor ULS1 estivesse sempre acionado.
- Fio 63 (BD/3 com BE/3): X14 e X15 (desaceleração de descida 1) ficam unidas; com o fio 62, as duas ficam ligadas à 301 em permanência. Os sensores ULS1/DLS1 do poço (desenhados na /44) e a legenda do esquema secundário (ULS = limite de corte de alta na subida, DLS = na descida) indicam que são sinais de desaceleração de fim de curso.
- Consequência provável (hipótese): o controlador veria os dois sinais de desaceleração de 1 nível sempre acionados, o que pode gerar falha de posição ou impedir a autoaprendizagem do poço. Não está no desenho; é só dedução do nome dos sinais.

Recomendação de leitura: se a lista for de um quadro de campo, os fios 62 a 66 devem ser removidos ou justificados. Os fios 61 e 67 só se justificam em elevador de porta única.

## 5. O que não deu para ler ou ficou incerto

- Fios 68 e 76 (PE): sem evidência de ligação direta no desenho.
- A numeração do SZ da lista (33, 13, 23, 2, 34) não aparece no desenho; só a numeração 1 a 9 aparece. Se o SZ físico usa outra numeração, os fios 32, 36, 37, 105 e 106 passariam a CONFERE.
- O número "8" que a /21 mostra na fileira de baixo do BD (e BC/BB) foi tratado como erro de cópia; a /44 manda no BD/BE.
