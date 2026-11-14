# Auditoria lote 6: as duas revisões do esquema (A = Vitinho/Inovance 19061867-ZL, B = VerticalParts 19060918-ZL)

Escopo: testar a hipótese "a lista de 125 fios foi feita a partir do esquema B" e listar as diferenças A x B que mudam a fiação ou a segurança do quadro. Nenhum arquivo existente foi alterado.

## 0. Base e convenções

| Item | A (Vitinho/Inovance) | B (VerticalParts) |
|---|---|---|
| Número do desenho | 19061867-ZL | 19060918-ZL |
| Data do carimbo | 2023-07-18 | 2022-10-11 |
| Folhas no carimbo | 51 (PDF completo, 51 págs.) | 58 (o PDF tem só 37 págs.; faltam folhas, por exemplo as folhas 1 a 7, 9, 10 e outras) |
| Como citar página | folha /N do carimbo = PDF N+2 | número de página do PDF, com a folha do carimbo entre parênteses |

Mapa B (PDF -> folha do carimbo) das páginas usadas: 2 (f.8 alimentação), 3 (f.11 inversor), 4 (f.12 comando, trafo, QFB1, QFB2), 5 (f.13 freio), 6 (f.14 resgate e inspeção, KY4), 8 (f.16 bypass), 10 (f.18 cadeia na casa de máquinas), 11 (f.20 cadeia geral), 12 e 13 (legendas), 15 (f.23 limitador), 16 (f.24 resgate elétrico ERB), 22 (f.41 ventilador e luz do carro), 32 (f.52 limites ULS/DLS).

Mapa A das páginas usadas: PDF 10 (/8), 11 (/9), 12 (/10), 13 (/11), 15 (/13), 16 (/14), 21 (/19), 24 (/22).

Vocabulário do veredito de cada fio:
- B CONFIRMA A LISTA: o desenho B mostra a ligação como a lista.
- B CONFIRMA A (O ESQUEMA VITINHO): o desenho B mostra o mesmo que A, e a lista diverge dos dois.
- B NÃO MOSTRA: o ponto não existe nas páginas B disponíveis (37 de 58 folhas; a ausência não prova que a folha faltante também não mostre).
- B DIFERE DOS DOIS: B mostra uma terceira coisa.

Limite geral: leitura visual dos desenhos (imagens rasterizadas em B). Confiança dada por linha.

## 1. Tarefa 1: as 22 divergências contra B

| Fio | Ligação da lista | O que A mostra (lotes 2 a 4) | O que B mostra (PDF pág.) | Veredito | Conf. |
|---|---|---|---|---|---|
| 16 | DQFB2 2 (201) a KY5/1 | 201 sai do borne 3 do QFB2, vai a KY5/1 | PDF 4 (f.12): disjuntor 2P (rótulo do desenho "QF2", sobreposição em português "QFB2"), R e N entram nos bornes 1 e 2 de cima, 201 sai do borne 3 e 202 do borne 4, vão a KY5/1 e KY5/5. Não há "DQFB2" | B CONFIRMA A (numeração do desenho 3/4 na saída, lista usa 2/4) | alta |
| 18 | 501: DQFB3 2 a CZ 2 | CZ é ligada ao QFB4 | PDF 2 (f.8): CZ (tomada fêmea, pinos 1, 2 e PE) alimentada pelo QFB4 (bornes 2 e 4, com LIHS1 na fase). QFB3 só alimenta 501 e 502 | B CONFIRMA A | média |
| 20 | 501 (QFB3 2) a ERB N | 501 vai ao L da ERB | PDF 16 (f.24): setas "8.4:E 501" sobre o borne L e "8.4:E 502" sobre o borne N da MCTC-ERB-A | B CONFIRMA A (501 em L) | alta |
| 29 | ERB ZQ+ a SZ 4 | ZQ+ vai ao MT1 pino 5; SZ 4 é 302 | PDF 16: ZQ+ desce ao plugue MT1 pino 5 e ZQ- ao pino 12. SZ pino 4 = 302 | B CONFIRMA A | alta |
| 30 | ERB ZQ+ a SW 73 | ZQ+ no nó ZQ1+ (SW 53) | PDF 16 (ZQ+ ao MT1/5) e PDF 5 (f.13): MT/5 = ZQ1+ = KY8/3, que liga ao SW 53 (SW 54 vai a BK1+). SW 73 é o nó ZQ2+ (KY9/2, MT/6) | B CONFIRMA A (SW 53, não SW 73) | alta |
| 32 | KY10/9 (DC12) a SZ 33 | SZ de 9 pinos, DC12 no pino 3 | PDF 16: soquete SZ de 9 pinos, pino 3 = DC12 | B CONFIRMA A | alta |
| 36 | KY11/5 (133) a SZ 13 | SZ pino 2 = 133 | PDF 16: SZ pino 2 = 133 (KY11/5, segue a MS+) | B CONFIRMA A | alta |
| 37 | KY11/6 (131) a SZ 23 | SZ pino 7 = 131 | PDF 16: SZ pino 7 = 131 (KY11/6, segue a MS-) | B CONFIRMA A | alta |
| 62 | jumper BD/3 a BD/1 | desenho não tem | PDF 32 (f.52): BD 1=301, 2=302, 3=ULS1 (X14), 4=ULS2 (X16), cada um ao seu limite; sem jumper | B CONFIRMA A (não mostra o jumper) | alta |
| 63 | jumper BD/3 a BE/3 | desenho não tem | PDF 32: BE 1=301, 2=302, 3=DLS1 (X15), 4=DLS2 (X17); sem ligação BD a BE. Na versão "limites no carro" (lado direito) BD/3 e BE/3 vão a CD3 e CD4 da placa MCTC-CTB-H6, separados | B CONFIRMA A (não mostra) | alta |
| 64 | jumper HW/3 a AA/4 | desenho não tem | PDF 10 (f.18): HW 3=110, HW 2=111, HW 4=PE. PDF 11 (f.20): AA 4 = 130 no fim da cadeia, sem fio de 110 a 130 | B CONFIRMA A (não mostra) | alta |
| 65 | jumper AA/5 a AA/4 | desenho não tem | PDF 11: AA 5 = 131A, depois dos trincos GS1/GS2; AA 4 = 130. Sem fio entre eles | B CONFIRMA A (não mostra) | alta |
| 66 | jumper AA/5 a AA/6 | desenho não tem | PDF 11: AA 5 = 131A (passa pelo UCMP a 131 e pelos trincos 1DS a nDS até 132); AA 6 está no ramo traseiro, rede 133/134. Sem fio AA/5 a AA/6 | B CONFIRMA A (não mostra) | alta |
| 88 | 201: QFB2 2 a DQFB2 1 | 201 sai do borne 3 do QFB2 | PDF 4: igual, 201 sai do borne 3 | B CONFIRMA A | alta |
| 91 | 502: QFB3 4 a CZ 1 | CZ no QFB4 | PDF 2: igual ao fio 18 | B CONFIRMA A | média |
| 94 | 502 (QFB3 4) a ERB L | 502 vai ao N da ERB | PDF 16: 502 sobre o borne N | B CONFIRMA A (502 em N) | alta |
| 105 | SZ 2 (101) a KY5/7 | SZ pino 6 = 101 | PDF 16: SZ pino 6 = 101 (seta "12.6:C 101"); SZ pino 1 = 101B ("12.6:D +CC-101B") | B CONFIRMA A | alta |
| 106 | SZ 34 (T02) a KY10/10 | SZ pino 8 = T02 | PDF 16: SZ pino 8 = T02 (KY10/10) | B CONFIRMA A | alta |
| 107 | SZ 14 a ERB MS+ | SZ pino 2 (133) | PDF 16: MS+ da ERB na rede 133, SZ pino 2 | B CONFIRMA A | alta |
| 108 | SZ 24 a ERB MS- | SZ pino 7 (131) | PDF 16: MS- na rede 131, SZ pino 7 | B CONFIRMA A | alta |
| 109 | SZ 3 (ZQ1+) a SW 53 | SZ 3 é DC12; ZQ1+ chega por MT | PDF 16: SZ pino 3 = DC12; ZQ1+ só pelo plugue MT/MT1 pino 5. O destino SW 53 está certo, a origem SZ 3 não | B CONFIRMA A | alta |
| 118 | N: XA N a QFB2 3 | neutro entra no borne 2 do QFB2, vindo por QF 7, filtro EMC e TA N | PDF 2 e PDF 3 (f.8 e f.11): N sai do QF 7 e vai ao TA N, que dá "+CC-N 12.2:A" (sem filtro EMC em B). PDF 4: +CC-N entra no borne 2 do QFB2 | B CONFIRMA A (menos o filtro EMC, que B não tem) | alta |

Resultado das 22: B CONFIRMA A em 22 de 22. Em nenhum caso B confirma a lista. Nos jumpers 62 a 66 os dois esquemas concordam que o desenho não prevê a ligação.

Observação sobre os jumpers 61 e 67 (que A já confirma): B tem as mesmas notas "single door, connect BA-P08 and BA-P09" (BA/8 a BA/9, rede 132 a 133) e "single door, connect AA-P06, AA-P14" (AA/6 a AA/14, rede 133 a 134), PDF 11 (f.20). B CONFIRMA A e CONFIRMA A LISTA (só para porta única).

## 2. Tarefa 1: os 14 não verificáveis contra B

| Fio | Ligação da lista | O que B mostra (PDF pág.) | Veredito | Conf. |
|---|---|---|---|---|
| 15 | DQFB1 1 a QFB1 2 | PDF 4: disjuntor 1P (rótulo "QF1", sobreposição "QFB1"), borne 1 embaixo (vem do 125V) e borne 2 em cima (vai à rede 101, KY5/7, e a +CC-101B). Não existe "DQFB1" | B NÃO MOSTRA o DQFB1; QFB1 2 existe | média |
| 28 | ERB PE a chapa da botoeira PE | PDF 16: a ERB não tem borne PE; não há chapa da botoeira | B NÃO MOSTRA | alta |
| 68 | MCB-C3 PE a KCB PE-M1 | Nenhum borne "PE-M1" em B. PDF 4: PE da KCB em AA/3 vai a "+CC-PE" (f.18 e f.50) e ao símbolo de terra | B NÃO MOSTRA | média |
| 76 | PCB-D1 PE a KCB PE | PDF 4: PCB-D1 J3/8 vai a um símbolo de terra; KCB AA/3 vai a +CC-PE. Sem fio direto entre os dois | B NÃO MOSTRA | média |
| 77 | PCB-D1 PE a MCB-C2 PE | B só tem MCB-C3 (texto das págs. 8, 11, 13 e 35 do PDF) | B NÃO MOSTRA MCB-C2 (a placa é C3) | alta |
| 90 | 202: QFB2 4 a XB 202 | PDF 15 (f.23): borne XB 202 existe (dois círculos "202" na régua XB, logo acima da casa de máquinas) e PDF 4 envia "202 / 23.4:A" do borne 4 do QFB2 | B CONFIRMA A LISTA | alta |
| 92 | 501: QFB3 2 a DQFB3 1 | PDF 2: QFB3 2 = 501; "DQFB3" não existe | B NÃO MOSTRA o DQFB3 (origem confere) | média |
| 114 | TRF 0S a XPE PE | PDF 4: linha 0S tem uma derivação para símbolo PE (e 0P também); XPE não existe | B NÃO MOSTRA o XPE | média |
| 120 | 202: XB 202 a XB 202 | PDF 15: os dois círculos XB 202 são unidos por um fio horizontal (um vem de "12.3:B 202", o outro desce à bobina RRD) | B CONFIRMA A LISTA | alta |
| 121 | XPE PE a CZ PE | PDF 2: CZ PE só com símbolo de terra | B NÃO MOSTRA o XPE | média |
| 122 | XPE PE a ERB PE | PDF 16: ERB sem borne PE | B NÃO MOSTRA | alta |
| 123 | XPE PE a MCB-C2 PE | sem MCB-C2 em B | B NÃO MOSTRA | alta |
| 124 | XPE PE a NICE3000 PE | PDF 3 (f.11): PE do inversor com símbolos de terra e seta "+EX-PE"; sem XPE | B NÃO MOSTRA o XPE | média |
| 125 | XPE PE a TRF PE | PDF 4: símbolos PE na blindagem e na linha 0S; sem XPE | B NÃO MOSTRA o XPE | média |

Resultado dos 14: B CONFIRMA A LISTA em 2 (fios 90 e 120), B NÃO MOSTRA em 12.

### 2.1 Correção ao lote 4 (A)

O lote 4 disse que o borne XB 202 "não está desenhado". Ele está em A, na folha /22 (PDF 24): duas bolhas de borne XB com "202" unidas por um fio (e XB 203, 205 do lado esquerdo; 302, 302, 303 e 305 do lado 24 V), e o PDF 10 (/8) tem XB 807, 809, 802. Conferido por mim. Portanto os fios 90 e 120 passam a CONFERE contra A também, e as contagens do Rev. 11 mudam para 91 CONFERE, 22 DIVERGE e 12 NÃO VERIFICÁVEL (fios 90 e 120 saem dos 14). A nota "XB 202 não aparece" do AUDITORIA_REV11.md precisa ser corrigida.

## 3. Os pontos que você pediu em especial

| Ponto | A | B | Veredito para a lista |
|---|---|---|---|
| L e N da ERB-A1 (fios 20 e 94) | 501 em L, 502 em N | 501 em L, 502 em N (PDF 16, setas 8.4:E) | Lista invertida contra os dois. B CONFIRMA A |
| Tomada CZ (fios 18 e 91) e QFB3/QFB4 | CZ no QFB4 (com LIHS1) | CZ no QFB4 (PDF 2). QFB3 e QFB4 são "2P/6A/0,03 A tipo D" nos dois | Lista liga CZ ao QFB3; B CONFIRMA A (CZ no QFB4) |
| SZ (fios 29, 32, 36, 37, 105 a 109) | soquete de 9 pinos: 1=101B, 2=133, 3=DC12, 4=302, 5=FL1, 6=101, 7=131, 8=T02, 9=302 | idêntico (PDF 16), com os plugues SZ1 (ponte 1 a 6) e SZ2 (ponte 3 a 8) e o procedimento de resgate passo a passo | Numeração da lista (13, 14, 23, 24, 33, 34) não existe em nenhum. B CONFIRMA A |
| Fio 30 (ZQ+ para SW 73 ou SW 53) | SW 53 (nó ZQ1+) | SW 53 (ERB ZQ+ a MT1/5 = ZQ1+ = SW 53; ZQ- a MT1/12 = ZQ2-) | B CONFIRMA A. A lista (SW 73) está errada nos dois |
| Trafo (bornes e tensão) | primário 220V e 0P, secundário 125V e 0S, "63 VA (3,7 a 22 kW) / 110 VA (30 a 37 kW)", 50 Hz | idêntico (PDF 4), mesmos rótulos 220V, 0P, 125V, 0S, PE na linha 0S e em 0P | Secundário é 125 V e potência 63 VA (ou 110 VA para 30 a 37 kW) nos dois. O BOM Rev. 11 (110 V, 150 VA) não bate com nenhum |
| Jumpers 61 a 67 (BA, BD, BE, HW, AA) | 61 e 67 previstos (porta única); 62 a 66 não | idêntico (PDF 10, 11, 32) | Ver tabela 1; B não ajuda a justificar 62 a 66 |
| DQFB1/2/3 e XPE | não existem | não existem (só QFB1/QF1, QFB2/QF2, QFB3, QFB4; sem XPE) | B NÃO MOSTRA. Nome "D..." e XPE ficam sem fonte nos dois |
| MCB-C2 ou C3 | C3 | C3 (PDF 8, 11, 13, 35) | C3 nos dois |
| Bitola | nenhuma indicação | nenhuma indicação (busca de texto e leitura das folhas lidas) | NÃO VERIFICÁVEL pelo esquema (confiança alta de que nenhum dos dois indica bitola nas folhas lidas) |

## 4. Tarefa 2: diferenças A x B que mudam a fiação ou a segurança

Só entram pontos que eu li nas duas imagens. "Igual" significa que comparei as folhas e não achei diferença de ligação.

| # | Ponto do quadro | A (página) | B (PDF pág.) | Efeito | Conf. |
|---|---|---|---|---|---|
| 1 | QFB1 (circuito de segurança, 125 V) | 1P+N, In=10 A, tipo C, com bloco diferencial desenhado, bornes N e 1 embaixo, N e 2 em cima; 0S ao N de baixo, N de cima a KY5/8 (102). PDF 12 (/10) | 1P, In=1 A, tipo C, só bornes 1 e 2; 125V ao borne 1, borne 2 a 101 (KY5/7). 0S vai direto a KY5/8 (102), sem passar pelo disjuntor. PDF 4 (f.12) | Muda a fiação (3 e 4 bornes em A, nenhum em B) e a proteção (neutro/102 sem disjuntor em B; 1 A em B contra 10 A em A). Os fios 51 (KY5/8 a QFB1 4) e 113 (0S a QFB1 3) da lista seguem o disjuntor de A; para B esses fios não existem como estão | alta |
| 2 | QFB2 (comando) | 2P/6 A, símbolo com bloco diferencial (PDF 12) | 2P/6 A, disjuntor simples "Air breaker for control power", sem bloco diferencial (PDF 4) | Proteção diferente; topologia igual (R e N em 1 e 2, 201 e 202 em 3 e 4) | média |
| 3 | Filtro EMC na potência | caixa "EMC filter cabinet" (+H) entre QF e borne TA, com PE (PDF 10, /8) | sem filtro; QF vai direto ao TA (PDF 2 e 3) | Muda a fiação de entrada. A lista (fios 83 a 85, QF para NICE3000 R) não cita filtro nem TA, então não decide | alta |
| 4 | Resistor de frenagem | caixa separada "DBR-B" com PE (PDF 11, /9) | DBR dentro do comando, sem PE desenhado (PDF 3) | Detalhe de montagem e aterramento | média |
| 5 | Segundo par 501/502 do QFB3 | vai a "11.2:A" (POW1 da KCB, via F2 4 A para 507/508) | marcado "ERB Power 24.3:D / 24.4:D" (alimenta a ERB, PDF 16) e POW1 da KCB aparece em PDF 22 (f.41), "30.2:A" | Referências cruzadas diferentes; a topologia 501/502 em POW1 e L/N da ERB é a mesma. Sem efeito na lista | média |
| 6 | Contato CIS 11/12 no ramo 122B a 123 | CIS (11, 12) entre KY4/10 e KY4/11 (PDF 16, /14, e PDF 21, /19) | fio ponte direto de KY4/10 a KY4/11, sem contato (PDF 6, f.14; PDF 11, f.20) | Em B o ramo 122B/123 nunca é aberto pela chave da botoeira de resgate. Muda a segurança (leitura do desenho; a consequência é inferência) | alta |
| 7 | Contatos CIU 13/14 e CID 13/14 no ramo 125 | CIS 13/14 em série com CIU e CID (PDF 16 e PDF 21) | CIS 13/14 liga 118 a 125 sem CIU e CID (PDF 6, PDF 11) | Em B os botões de subida e descida de resgate não interrompem esse ramo. Muda a segurança | alta |
| 8 | Chave de inspeção do poço (PITB, PITU, PIT, PT3) | presente na cadeia, entre 118 e PT2, com CIU e CID no ramo inferior (PDF 21) | ausente: só PT1 (PES2), PT2 (GTS), PES1, 118 (PDF 11) | A cadeia de segurança do poço é diferente. Muda a fiação e a segurança | alta |
| 9 | Rótulos X27 e X28 na MCB-C3 | pinos CN2/4 = X27 (134), CN2/5 = X28 (133) | mesmos pinos (PDF 8, f.16), mas a legenda em português no PDF 11 diz "X27 porta de pavimento, X28 porta de cabina ao fundo", o oposto da fiação desenhada (133, trincos de pavimento, entra no X28) | Erro de rótulo em B (média); não muda a ligação | média |
| 10 | Freio (BK1, BK2, SW, BY, R22, R220, R21, R23, D9, D26) | PDF 15 (/13) | PDF 5 (f.13) | Igual | alta |
| 11 | Resgate elétrico (ERB, SZ, MT) | PDF 25 (/23) | PDF 16 (f.24) | Igual (L=501, N=502, SZ 9 pinos, MT1 5/6/11/12) | alta |
| 12 | Bypass de porta (S1, S2) | PDF 21 (/19), parte inferior | PDF 8 (f.16): mesmos KY1/1, 2, 3, 4 e 6 (130, 134, 133, 131, 102) e S2 pinos 1 a 6; textos em português do jumper S1 e S2 | Igual na ligação (não conferi pino a pino do S2) | média |
| 13 | Cadeia na casa de máquinas (MES-1, MES-2, OS, OS-G, CWSG, RCS) | PDF 21 | PDF 10 e 11 | Igual, inclusive "jumpear se não existir" | alta |
| 14 | Limitador remoto (TIS, S1, RTB, RRB, XB 203/205/202) | PDF 24 (/22), versão 24 V com "+CC-301" e "+CC-" | PDF 15 (f.23), versão 24 V com "301" e "302" | Igual na ligação | alta |
| 15 | Limites ULS/DLS | BD e BE, X14 a X17 (/44) | PDF 32 (f.52): iguais e com tabela de distâncias e versão "limites no carro" | Igual na ligação | alta |
| 16 | Trafo, 63 VA e 125 V | PDF 12 | PDF 4 | Igual | alta |

## 5. Resumo

Contagens:
- 22 divergências: B CONFIRMA A em 22; B CONFIRMA A LISTA em 0; B NÃO MOSTRA em 0 (os jumpers 62 a 66 são "não mostrados" nos dois, o que confirma A); B DIFERE DOS DOIS em 0.
- 14 não verificáveis: B CONFIRMA A LISTA em 2 (fios 90 e 120, que também passam a CONFERE em A, correção ao lote 4); B NÃO MOSTRA em 12 (DQFB1/3, XPE, MCB-C2, PE da ERB e da chapa, PE-M1).
- Os fios 51 e 113 (QFB1 4 e QFB1 3) conferem em A, mas B DIFERE DOS DOIS (QFB1 sem polo N).

Hipótese "a lista vem do esquema B": NÃO se sustenta, e a evidência contra é forte (confiança alta):
1. Nas 22 divergências, B desenha exatamente o que A desenha. Nenhuma "divergência" vira confirmação em B (L/N da ERB, CZ no QFB4, SZ de 9 pinos, ZQ+ em SW 53, 125 V no trafo).
2. A lista contém ligações que só existem em A: CIS 11 e 12 (fios 41 e 42, KY4/10 e KY4/11), e os contatos CIU e CID 13/14 (fios 8, 11, 12 e 13). Em B esses contatos não existem (há um fio ponte). A lista não poderia ter sido tirada de B.
3. A lista usa QFB1 com bornes 3 e 4 (fios 51 e 113, polo N). B tem QFB1 de 1 polo sem 3 e 4.
4. Único ponto em que a lista combina com B e não com A é a ausência do filtro EMC nos fios 83 a 85, mas a lista também omite o borne TA que existe nos dois, então esse ponto é fraco.

Conclusões principais:
1. Os erros da lista (L/N invertidos, CZ no QFB3, ZQ+ para SW 73, numeração do SZ, jumpers 62 a 66, DQFB e XPE) não são explicados pela revisão B. Continuam sendo erros da lista (ou ligações de campo sem desenho em nenhuma revisão). A pergunta Q70 e Q71 continuam em aberto.
2. Os dois esquemas concordam entre si nos pontos mais críticos (freio, resgate elétrico, bypass, cadeia na casa de máquinas, limitador, trafo 125 V e 63 VA). Os dois não indicam bitola.
3. Diferenças A x B com efeito de segurança: QFB1 (1 A sem N em B), ramo 122B/123 sem CIS e ramo 125 sem CIU e CID em B, ausência da chave de inspeção do poço em B, filtro EMC e diferencial no QFB2 só em A. Se o quadro de campo for fabricado pela revisão B, os fios 41, 42, 8, 11, 12, 13, 51 e 113 da lista não têm correspondente em B.
4. Correção ao lote 4: XB 202 existe em A (/22).
5. Limite: o PDF de B tem 37 das 58 folhas; "B NÃO MOSTRA" vale só para as folhas disponíveis.
