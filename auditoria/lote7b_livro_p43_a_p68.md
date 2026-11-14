# Lote 7b: livro Rev. 11, páginas 43 a 68 (Parte II.3 a II.11, Parte III, Parte IV)

Auditoria somente leitura. Base de verdade: esquemas e manuais dos fabricantes. Nenhum arquivo existente foi alterado.

Abreviações: V = Diagrama Vitinho 19061867-ZL (folha /N = página PDF N+2; confirmado: /21 = PDF 23, /38 = PDF 40, /48 = PDF 50); manual A02 = MCTC-CTW-B3 19010849 A02 em inglês (páginas do livreto 1 a 11: pág. 2-3 produto e especificações, 4-6 terminais, 7-9 COB, 10-11 diagramas de fiação); manual A00 = arquivo '2018_CN' (histórico October 2018); manual NICE3000new = 368 pág. (página PDF); ERB = manual ERB-A1 EN; AD30 = boletim 'Parametrização do AD30'; BST = lista de cabos modulares BST; ESQ = esquema 19060918-ZL em português.

Método: cada conector foi lido no desenho em PNG (PyMuPDF) e conferido pino a pino; a ordem dos pinos usa a regra do próprio livro (pino 1 inferior direito nas placas da cabina, canto superior esquerdo na KCB), que foi validada contra o texto numerado de V /11, /12, /13, /9, /24 e contra a figura do manual A02.

Nota sobre o escopo: as folhas 'esquema pág. N' do 19060918-ZL não são citadas nas páginas 43 a 68 (só 'Vitinho /N' e 'manual A02 pág. N'). O livro usa o rótulo Vitinho em todas as tabelas.

## 1. Resumo

Afirmações tabeladas: 155. CONFIRMA 108, CONTRADIZ 31, NÃO VERIFICÁVEL 16.

Selos agrupados: 44 itens (cobrem os 67 [Certeza], 61 [Provável], 12 [Chute] e 51 PREENCHER das págs. 43 a 68). Resultado: CONFIRMADO 12, RESOLVIDO 16, PARCIAL 9, AINDA ABERTO 7.

Pendências P21 a P51 (31): CONFIRMADA 2, RESOLVIDA 5, PARCIAL 16, AINDA ABERTA 5, NÃO VERIFICÁVEL 3.

Citações '/página.coluna:linha': 574 endereços analisados, 492 exatos, 64 com 1 linha de diferença na mesma folha e coluna, 18 de ruído do leitor, nenhum sinal ausente da folha citada. A numeração 'folha + 2 = página PDF' está certa. Citações 'manual A02 pág. 5 e 6' (P50) e 'Vitinho /48, PDF pág. 50' estão certas.

### Achados mais importantes

- AA, AB, BA, BB, BC, BD, BE, MT, OS, HW, AC, CA, CB, MSC, CC, CD, MX, PG1, PG2, COB1, COB2, EDP1, EDP2, LC, SE, DEN, DP, MOD, DZ, RDZ, WT, LW, HK, GS, SUP1, SOS e todos os plugues do poço (DA, DB, DC, PT1 a PT4, LIH) estão CERTOS contra o desenho. Isso inclui a regra de numeração.
- ERRADOS na Parte II.4: FAN (e conector de 8 posições, pinos 1 PE, 3 508, 4 508, 5 PE, 7 509, 8 510, igual ao manual), EY3 (3 sinais, não 5) e EY4 (20 posições e 14 sinais: faltam 507/508 e a numeração dos pinos 5 a 12 está comprimida e errada). II.8 K-4 (11 vias) e K-7 (7 por conector) também erram.
- IV.2 e IV.3: '121 = 119' e FLSU/FLSD 'rede 121 e PE' estão errados. A cadeia é 119 -> FLSD -> 120 -> FLSU -> 121 (V /19 e /49). O BA entra no FLSU pelo 121; o DA leva 119 ao FLSD.
- Faltou no livro: com 1 porta é preciso fechar jumpers no quadro, AA 6 com AA 14 (133-134) e BA 8 com BA 9 (132-133) (V /19, notas 'single door'). Não há item para isso em IV.4.
- Selos resolvidos pelas fontes: S2 (CAN trançado e blindado), S4 a S6 e S13 a S17 (funções de 130 a 134, 102, L/R, GS, SGC), S8 (DZI), S30 e P40 (cotas da caixa), P25 (pinagem PG-E e encoder), P39 (curto MSC 10-12), P43 (origem da iluminação e QFB4), P45 (ERB usa FL1 do RDZ), P48 (PCB-D1), FX = contator UVW, X20 = sobretemperatura (IV.6 está errado ao tratar X20 como freio).
- P38 está errada quanto ao A00: o arquivo A00 tem ambiente, IP21, Fig. 3 e 4 e a mesma Table 4. Também 'A02 de 11/2022' é a data do arquivo; o histórico diz julho de 2022. 'COB-A1/A2/F1' é erro (é COB-A1/A2 e CCB-F1).
- III.2: CA omite o 133 e MSC omite o DC12; III.3 diz que CB já batia com o manual, mas CB do livro tem 122A e não tem SGC1/SGC2. A figura do manual divide o CB em 'CC' (301, 302, CAN+, CAN-, FL1, FL2) e 'CB' (DC12, R, L, GND); isso precisa ser decidido antes do cabo de manobra (P35).
- DEN1 do Vitinho (4P, só HX5) não é o DEN1 da CTW-B3 (8 posições, 7 sinais). O mesmo vale para MSC (123A/124 no Vitinho, 128/127 no manual nos mesmos pinos 10 e 12) e SGC (pinos 6 e 2 no Vitinho, 12 e 10 no manual). A II.4 usa o Vitinho sem avisar, embora a Parte III diga que vale o manual.
- II.11.1: critério de divergência incoerente (BC/DC 6 terminais para 3 sinais e 'OK'; BB/DB 8 para 4 e 'DIVERGE'). P32 esquece VPMP-846. BD/BE: o pino 302 não vai ao poço (V /44, /49).
- Página 51 do livro está em branco.

## 2. Tabela de afirmações (página do livro, afirmação, resultado, evidência, confiança)

| Pág. | Afirmação | Resultado | Evidência (documento e página) | Conf. |
|---|---|---|---|---|
| 43 | II.3: dois cabos de manobra, A (AA 16P no quadro <-> CA 16P na caixa) e B (AB 14P <-> CB 14P), ligação pino a pino | CONFIRMA | V /21 (layout KCB: AA 2x8, AB 2x7) e V /38 (CA 2x8, CB 2x7). Pinos de AA e CA idênticos, AB e CB idênticos | alta |
| 43 | [Certeza] conferido sinal a sinal nos 30 pinos | CONFIRMA | Releitura dos desenhos /21 e /38 e do texto de /11: AA 1=207, 3=PE, 4=130, 5=131A, 6=133, 8=507, 9=208, 12=125, 13=123, 14=134, 16=508; AB 3=301, 4=302, 7=FL1, 8=122A, 10=FL2. Tudo bate | alta |
| 43 | 12 sinais em 16 vias (AA) e 12 em 14 (AB); 4 pinos sem uso no AA/CA (2, 7, 10, 15) e 2 no AB/CB (2, 9) | CONFIRMA | Contagem nos desenhos V /21 e /38 | alta |
| 43 | 24 condutores com sinal nos dois cabos; 16+14 se forem dois cabos | CONFIRMA | Aritmética 12+12=24 e 16+14=30 vias; confere | alta |
| 43 | Regra de numeração na KCB: pino 1 no canto superior esquerdo, linha de cima E->D e depois a de baixo E->D | CONFIRMA | V /21: rótulos '1' e '7' (MT), '1' e '4' (HW, OS); texto de V /11 e /12 lista AA/AB nessa ordem | alta |
| 43 | Regra na caixa: pino 1 = quadrado do canto inferior direito; linha de baixo da direita p/ esquerda (1..n), a de cima também (n+1..2n) | CONFIRMA | V /38: rótulos '1' no canto inferior direito e '16/9', '14/7', '18/10' nas pontas de CA, CB, MSC; manual CTW-B3 A02 fig. de fiação (pág. 11 do livreto): CA 130=4, 131A=5, 133=6, 125=12, 123=13, 134=14, 207=1, 208=9, PE=3 (mesma ordem) | alta |
| 43 | A KCB está montada girada 180 graus no quadro real; conferir o pino 1 impresso na placa [Provável] | NÃO VERIFICÁVEL | Depende de fotos do quadro; o Vitinho só traz o layout desenhado | - |
| 43 | II.3.1 tabela de 16 pinos AA = CA (207, PE, 130, 131A, 133, 507, 208, 132, 125, 123, 134, 508) | CONFIRMA | V /21 (AA), V /38 (CA) e V /11 (texto 'AA n'). Manual A02 fig. pág. 11 confirma CA 4=130, 5=131A, 6=133, 12=125, 13=123, 14=134 | alta |
| 43 | 207/208 = 220 V CA de cabina (faixa 201-299); 507/508 = 220 V CA de iluminação (faixa 501-599) | CONFIRMA | V /10 (QFB2 -> KY8 207/208, fusível F1 250 V/4 A 'Door/light curtain fuse'); V /11 (POW1 501/502 -> F2 4 A 'Car fan/light curtain fuse' -> AA 8=507, AA 16=508). Manual A02 pág. 3 e 6: 507/508 'car top lighting power', 207/208 'door operator/light curtain' | alta |
| 43 | 130, 131A, 133, 134 = circuito de portas/bypass [Provável]; 132 = 'cadeia de segurança 110 V' [Provável] | CONFIRMA | Direção certa e agora com definição: manual A02 pág. 5-6: GS1 130/131A = trinco da porta frontal; GS2 133/134 = trinco da porta traseira; CA 132 = 'rear car door lock start', 134 = 'rear car door lock end', 131A = 'front car door lock end', 130 = 'safety circuit end'. V /19 mostra 130..134 em série com GS1, DS, GS2 e bypass S2 | alta |
| 43 | 125 e 123 = cadeia de segurança 110 V CA (faixa 101-199) | CONFIRMA | V /19 (123 após o contato OS/SOS, 125 após o TCI); manual A02: 123 'car top safety circuit start', 125 'car top emergency drive output point'. Tensão: manual NICE3000new pág. 61 'Safety circuit 110 VAC +-15%' (o trafo do Vitinho /10 entrega 125 V, dentro da tolerância) | alta |
| 43 | 102 = 110 V CA retorno/comum [Provável] | CONFIRMA | Manual A02 pág. 5: MSC 102 'common point of the safety circuit and door lock circuit'; manual NICE3000new pág. 65 'neutral line of the safety circuit'; V /19: LEDs de 130/132/133/134 retornam em +CC-102 | alta |
| 43 | AB 5/6 = CAN+/CAN- (par KCB <-> placa da cabina) | CONFIRMA | V /24: AB 5 CAN+, AB 6 CAN-, CB 5/6, LC1 3/4, MSC 9 e 18; manual A02 fig.: CAN+ e CAN- no grupo 24V/CAN/FL1/FL2 | alta |
| 43 | AB 7 = FL1 (subida), AB 10 = FL2 (descida); lista de peças 'Up/Down Door-area signal' | CONFIRMA | V /11 (AB 7 FL1, AB 10 FL2), V /3.a (FL1 'Up Door-area signal'), V /25 (conector chamado 'CA' no desenho: 3=301, 4=302, 7=FL1, 10=FL2; rótulo do conector parece trocado no Vitinho) | alta |
| 43 | AB 11 = DC12V (12 V do interfone), 12 = L, 13 = R [Provável]; 3 e 4 = 301/302 | CONFIRMA | Manual A02 pág. 5: CB 'R, L intercom signal', 'DC12 intercom power supply (12 V positive)'; fig. pág. 11 liga 'AB-P11 = DC12, AB-P13 = R, AB-P12 = L, AB-P04 = GND(302)', o que confirma as posições 11, 12, 13 e 4 de forma independente do Vitinho | alta |
| 43 | Pino 14 (DZI) e pino 1 (102) do AB/CB [Certeza] | CONFIRMA | V /21 e /38 concordam (DZI inferior direito da fila de cima = 14; 102 = 1) | alta |
| 44 | AB 14 / CB 14 = DZI, 'não rotulado no Vitinho' | CONFIRMA | Função confirmada: manual A02 pág. 5 (CB e MSC): 'DZI Door zone signal output by magnetic scale'. Posição 14 confirmada em V /21 e /38 | alta |
| 45 | EDP1 12P (10 com sinal): 1=208, 3=PE, 4/5/6=301, 7=207, 9=PE, 10=HX1, 11=302, 12=HX20 | CONFIRMA | V /38 (EDP1: 208 pino 1, PE 3, 301 em 4-6, 207 pino 7, PE 9, HX1 10, 302 11, HX20 12). Manual A02 fig. pág. 10: 208=1, PE=3, 301=4/5/6, 207=7, X1=10, 302=11, X15=12 (pino 9 não aparece no manual) | alta |
| 45 | HX1 = barreira da porta 1; HX20 = detecção de falha da barreira 1; HX2/HX21 na porta 2 [Certeza tabela HX] | CONFIRMA | V /38 tabela: HX1 'Light curtain of door 1', HX2 'door 2', HX20/HX21 'Light curtain fault detection 1/2' | alta |
| 45 | Rótulo EDP1 pino 12 = HX20 (falha da barreira) | CONTRADIZ | Para a CTW-B3 o manual A02 rotula o mesmo pino 12 como X15 'Safety edge signal input terminal of door 1'. Mesmo pino, duas funções (ver selos e P36) | média |
| 45 | EDP2 12P: mesma pinagem com HX2/HX21 e conector /31 | CONFIRMA | V /38 (EDP2) e manual (EDP2: X2 pino 10, X16 pino 12) | alta |
| 45 | LC1/LC2 4P: 1=301, 2=302, 3=CAN+, 4=CAN- | CONFIRMA | V /38 (LC1, LC2) e V /24 (LC1 3=CAN+, 4=CAN-) | alta |
| 46 | SE1/SE2 4P: 1=301, 4=HX15 / HX16 (painel de toque) | CONFIRMA | V /38 layout e tabela HX15/HX16 'Touch panel of door 1/2' | alta |
| 46 | DEN1/DEN2 4P (TB1/TB2): 1=301, 4=HX5/HX6 | CONFIRMA | V /38 e V /3 (TB1 'Door 1 close limit switch') | alta |
| 46 | DEN1: 'fim de curso porta 1 fechada (HX3/HX4/HX5)' | CONTRADIZ | V /38 tabela HX: HX3 e HX4 são '/' (sem função); só HX5 e 'Door 1 close limit' | alta |
| 46 | DEN1 é conector de 4 pinos com 2 sinais (301 e HX5) | CONTRADIZ | Vale só para o DEN1 da placa D1/D2-G do Vitinho. O DEN1 da CTW-B3 (manual A02 fig. pág. 10) tem 8 posições e 7 sinais: BM=2, B3=3, B2=4, B1=5, 301=6, X5=7, X3=8. O próprio livro (III.2, P37) usa o do manual; a Parte II.4 não avisa a divergência | alta |
| 46 | DP1/DP2 4P: 1=301, 2=302, 3=HX11/HX19, 4=OT1/OT2 (sobretemperatura do motor da porta) | CONFIRMA | V /38 e V /3 (MT1 'Door-machine overheat sensor 1'). Manual A02: DP 301 pino 1, X11 pino 3 (coincide nos pinos 1 e 3) | alta |
| 46 | MOD1 4P: 1=301, 2=302, 3=MOD1+, 4=MOD1- | CONFIRMA | V /38 layout | alta |
| 47 | MOD2 4P; DZ 4P: 3=HX9 (subida), 4=HX10 (descida); DZU/DZD | CONFIRMA | V /38 e V /3 (DZU 'Up-level', DZD 'Down-level'); manual A02: DZ X9 pino 3, X10 pino 4 | alta |
| 47 | RDZ 4P: 1=301 (24 V normal, 12 V emergência), 2=302, 3=FL1, 4=FL2 [Certeza manual CTW-B3] | CONFIRMA | V /38 rotula o pino 1 '301/DC12V'; manual A02 pág. 5: RDZ FL1/FL2, '301/T01 power supply positive; normal 24 V, emergency 12 V'; fig. pág. 11 RDZ 1=301, 2=302, 3=FL1, 4=FL2 | alta |
| 47 | WT1: 3=HX8 (sobrecarga), 4=HX7 (carga plena); WT2: 4=HAI1; LW: 1=301, 2=HX17, 3=301, 4=HX18; HK1 e HK2 reservados | CONFIRMA | V /38 layouts e tabela HX; manual A02 fig. pág. 11: WT1 X8 pino 3, X7 pino 4; WT2 AI pino 4 | alta |
| 48 | GS1: 1=131A, 2=130; GS2: 1=134, 2=133; SUP1: 1=130, 2=129; pino 1 é o de baixo | CONFIRMA | V /38 e manual A02 fig. pág. 11 (GS1 131A=1/130=2; GS2 134=1/133=2; SUP1 130=1/129=2). GS1/GS2 = trincos de porta de cabina frontal/traseira (manual pág. 5) | alta |
| 48 | SUP2: pino 2 = 127 | CONTRADIZ | V /38 SUP2 129 e 127. Manual A02 pág. 5 e fig.: SUP2 129 e 128. O manual diz 'sem MSC, curto entre 127 e 128', logo é o mesmo nó elétrico, rótulo diferente | média |
| 48 | SUP1 = 'Standby switch 1' [Certeza pela lista de peças] | CONFIRMA | V /3 (SUP1 'Standby switch 1', /34.4:F). Manual traduz 'Backup safety switch'; V /49 'spare safety switch' | alta |
| 48 | CC 8P (SGC): 2=SGC2, 6=SGC1 | CONFIRMA | V /38 (CC 8 posições, SGC1 pino 6, SGC2 pino 2) | alta |
| 48 | CC = SGC com numeração dos pinos igual a da CTW-B3 | CONTRADIZ | Manual A02 fig. pág. 11: SGC1 pino 12, SGC2 pino 10 (conector diferente do CC do Vitinho). Além disso o manual chama de 'CC' outro grupo (301, 302, CAN+, CAN-, FL1, FL2). Conferir o conector físico | média |
| 48 | CD 4P: 3=ULS, 4=DLS (contato seco); MX 4P: 1=301, 2=302, 3=ULS, 4=DLS | CONFIRMA | V /38 layout e V /44 (CD 3/4, MX 1/3/4) | alta |
| 48 | MSC: conector de 18 pinos, 12 com sinal | CONFIRMA | V /38 e V /24 (MSC 9=CAN+, 18=CAN-). Contagem 134,132,102,DZI,302,CAN+,123A,124,130,DC12V,301,CAN- = 12 | alta |
| 49 | MSC pinos 1..18 (134, 132, 102, DZI, 302, CAN+, 123A, 124, 130, DC12V, 301, CAN-) | CONFIRMA | V /38 leitura do desenho, todos os 12 sinais nas posições do livro | alta |
| 49 | MSC (manual): para a CTW-B3 os pinos 10 e 12 são 128 e 127 | CONTRADIZ | A Parte II.4 só traz a pinagem do Vitinho (pino 10 = 123A, pino 12 = 124); manual A02 fig.: MSC 127 pino 12, 128 pino 10. Em ambos o curto sem régua magnética e entre os pinos 10 e 12 (ver P39) | média |
| 49 | SOS 6P: pino 1 = 123A (124 no manual), pino 3 = 123 [Certeza manual] | CONFIRMA | V /38 (SOS 123A em 1, 123 em 3) e manual fig. pág. 11 (SOS 124 em 1, 123 em 3). 123A e 124 são o mesmo nó se o MSC 10-12 estiver em curto (V /19) | alta |
| 49 | FAN 6P (6 com sinal): 1=PE, 2=508, 3=508, 4=PE, 5=509, 6=510 | CONTRADIZ | V /38: o FAN é de 8 posições: 1=PE, 3=508, 4=508, 5=PE, 7=509, 8=510 (pinos 2 e 6 vazios). Manual A02 fig. pág. 11 mostra o mesmo (1 PE, 3 508, 4 508, 5 PE, 7 509, 8 510). O livro comprimiu a numeração; a lista de materiais (MiniFit 8 vias) está certa | alta |
| 49 | EY3 (luz CL2/CL3): 'sinais 507, 508, 508, PE, 507 (5 posições)' | CONTRADIZ | V /38: EY3 só tem 3 sinais: pino 1=PE, 3=508, 6=507 | alta |
| 49 | EY5 = DC12V1, E12V, 302, 302; BAT = BAT-, NTC+, BAT+, BAT-; TEL1 = EB2, EB1, PC-, PC+, 302, DC12V, R, L | CONFIRMA | V /38 (sinais corretos). Pinagem que o livro deixou em PREENCHER: EY5 1=302, 2=302, 3=E12V, 4=DC12V1; TEL1 1=L, 2=R, 3=DC12V, 4=302, 5=PC+, 6=PC-, 7=EB1, 8=EB2 (9 e 10 livres); BAT mostra BAT-, vazio, BAT-, NTC+, vazio, BAT+ (ordem do desenho) | alta |
| 49 | EY4 12P, 12 com sinal: 1=HX14, 2=HX13, 3=HX12, 4=301, 5=EB1, 6=EB2, 7=127, 8=124, 9=123, 10=125, 11=122A, 12=PE | CONTRADIZ | V /38: EY4 tem 20 posições (2x10) e 14 sinais. Pinos reais: 1 HX14, 2 HX13, 3 HX12, 4 301, 6 EB1, 7 EB2, 10 507, 11 127, 12 124, 13 123, 14 125, 15 122A, 17 PE, 20 508. Os pinos 1 a 4 do livro estão certos, os demais estão errados; faltam 507 e 508. Também diverge de II.8 (K-4: 11 vias) | alta |
| 49 | EY4 pinos 1 a 3 = HX14, HX13, HX12 [Certeza tabela HX] | CONFIRMA | V /38 tabela HX12 'Insp. signal input', HX13 'up', HX14 'down'; manual Y4 X14=1, X13=2, X12=3 | alta |
| 49 | EB1/EB2 sem função descrita | NÃO VERIFICÁVEL | Pela fig. do manual A02 (pág. 11) EB1/EB2 são os contatos do botao de alarme ALB no interfone C2; V /3 lista ALB 'Alarm button' /36.8:C. Função fica resolvida (ver selos), mas o livro não a afirma | média |
| 50 | PG1/PG2 12P: 1=5V, 2=GND, 3=CS, 4=CLK, 5=DIN, 6=DATA, 7=24V, 8=GND, 9=Z, 10=B, 11=A, 12=PE; exceção 'topo E->D = 6..1, base E->D = 12..7' | CONFIRMA | V /38 PG1/PG2: rótulos 6..1 no topo (da esq. p/ dir.) e 12..7 embaixo; sinais na ordem do livro | alta |
| 50 | COB1/COB2 10P em 1 fileira, pino 1 na extremidade direita: 1=R, 2=L, 3=302, 4=E12V, 5=DC12V, 6=302, 7=MOD-, 8=MOD+, 9=301, 10=301 | CONFIRMA | V /38 (rótulo 1 a direita, 10 a esquerda) e manual A02 fig. pág. 10 (COB1: 1 R, 2 L, 3 302, 4 Z01, 5 DC12, 6 302, 7 MOD-, 8 MOD+, 9 301, 10 301). E12V = Z01 (12 V de luz de emergência) | alta |
| 51 | Página do livro sem conteúdo | CONTRADIZ | Livro pág. 51 tem só cabecalho e rodape (defeito de diagramação; provável imagem não inserida) | alta |
| 52 | MT 12P (10 com sinal): 1=X18, 2=X22, 3=X20, 5=ZQ1+, 6=ZQ2+, 7/8/9=301, 11=ZQ1-, 12=ZQ2- | CONFIRMA | V /21 (layout), V /13 (MT 1 X18, 2 X22, 5 ZQ1+, 6 ZQ2+, 7 301, 8 301, 11 ZQ1-, 12 ZQ2-), V /9 (MT 3 X20, MT 9 301), V /49 | alta |
| 52 | Destinos de /13 e /9: BK1 /13.4:F, BK2 /13.6:F, BK1-FB /13.3:F, BK2-FB /13.6:F, PT1 /9.7:F | CONFIRMA | V /3 lista de peças traz exatamente esses endereços | alta |
| 52 | Nota de /13: freios esquerdo e direito 'completamente separados' | CONFIRMA | V /13 'Note: The left and right brakes on the host side should be completely separated and wired' | alta |
| 52 | Pares 301: X18 com 301 do pino 7, X22 com o do 8, X20 com o do 9 (inferido pelo livro) | CONFIRMA | V /13 (BK1-FB entre MT 7 e MT 1; BK2-FB entre MT 8 e MT 2) e V /9 (PT1 entre MT 9 e MT 3) | alta |
| 52 | Cabos sugeridos 'C-03a / C-03b' (II.5) | CONTRADIZ | Inconsistência interna: a lista II.8 chama os mesmos cabos de T-1 e T-2 | alta |
| 52 | Bitola/corrente do freio 'não consta no Vitinho' | CONTRADIZ | V /13: fonte de freio PCB-D1 ajustável de 48 a 207 VCC (padrao 110 VCC), corrente máxima de impacto 6 A e de manutenção 4 A. A bitola em si realmente não consta | alta |
| 52 | Encoder em /9.4:E ligado ao cartao PG MCTC-PG-E /9.4:C; motor M1 /9.2:F | CONFIRMA | V /3 e V /9 (PG-E ligado ao 'Encoder'; M1 'Traction machine') | alta |
| 52 | OS 6P (5 com sinal): 1=PE, 2=121A, 3=121, 5=122, 6=121A | CONFIRMA | V /21 (layout), V /49 (OS 3 = 121, OS 5 = 122) | alta |
| 52 | Ação remota do limitador: RTD /22.2:E, RRD /22.3:E, VDR1, VDR2, S1 /22.2:C, TIS /22.2:B | CONFIRMA | V /3 e V /3.a (RTD /22.2:E, RRD /22.3:E, VDR1/VDR2, S1 /22.2:C, TIS /22.2:B) | alta |
| 52 | HW 6P (3 com sinal): 2=111, 3=110, 4=PE | CONFIRMA | V /21 e V /49 (HW 2=111, HW 3=110, 'Handwheel') | alta |
| 52 | BA 10P: 1=PE, 2=118, 3=121, 4=131, 5=122A, 6=111, 7=132, 8=132, 9=133, 10=123 | CONFIRMA | V /21 (layout BA), V /12 (texto BA 1..10) | alta |
| 52 | No Vitinho /48 o cabo de poço liga BA a DA; BA inclui circuitos de fechadura (/43) | CONFIRMA | V /48 ('Shaft cable' BA, BB, BC); V /43 (131 -> 1DS..nDS -> 132; 132 -> 1RDS..nRDS -> 133) | alta |
| 53 | BB 4P: 1=301, 2=302, 3=MOD+, 4=MOD-; igual ao plugue DB do poço [Certeza /48] | CONFIRMA | V /21 (BB 301/302 / MOD+/MOD-) e V /48 (tabela DB) | alta |
| 53 | BC 4P: 1=R, 2=L, 3=302, 4=DC12V; DC 4P do poço: 1=R, 2=L, 3=sem uso, 4=DC12 [Certeza /48]; 302 do BC não vai ao poço | CONFIRMA | V /21 e V /48 (tabela DC) | alta |
| 53 | BD 4P (301, 302, ULS1, ULS2) e BE 4P (301, 302, DLS1, DLS2); chaves no poço ULS1 /44.2:C, ULS2 /44.3:D, DLS1 /44.4:F, DLS2 /44.5:E | CONFIRMA | V /21, V /44 e V /3.a (endereços da lista de peças) | alta |
| 53 | AC 8P (4 com sinal): 2=SGC2, 4=123, 6=SGC1, 8=122A | CONFIRMA | V /21 layout AC | alta |
| 53 | 132 (BA 7 e 8) 'cadeia de segurança 110 V' [Provável]; 133 (BA 9) 'circuito de portas' | CONFIRMA | V /19 e /43: BA 4 (131) -> fechaduras frontais 1DS..nDS -> BA 7 (132); BA 8 (132) -> fechaduras traseiras 1RDS..nRDS -> BA 9 (133). Manual A02: 132 'rear car door lock start' | alta |
| 54 | DA 6P: 119, 118, 122A, PE, 123, 111 | CONFIRMA | V /48 tabela DA(6P) | alta |
| 54 | DB 4P (301, 302, MOD+, MOD-) e DC 4P (R, L, vazio, DC12) | CONFIRMA | V /48 tabelas DB e DC | alta |
| 54 | PT1 6P (caixa do poço): 802, 805, PE, vazio, 111, 112; PT2 6P: vazio, 118B, PE, 119, 112, 113 | CONFIRMA | V /48 tabelas PT1 e PT2; icones Buffer 1/2 e Tension pulley em PT2 | alta |
| 54 | PT3 12P: 113, 118, 118B, 122A, 123, vazio, 301, PX1, PX2, PX3, EB1, EB2 | CONFIRMA | V /48 tabela PT3 (icone 'Pit inspection handle') | alta |
| 55 | PT4 3P (301, PX4, vazio); LIH 6P (802, 805, 803, 804, vazio, PE); PT1 6P caixa A12 (802, 805, PE, vazio, 111, 112) | CONFIRMA | V /48 tabelas PT4, LIH e PT1 (A12); PT4 = 'Reset box outside shaft' (V /3.a RSW /42.8:B) | alta |
| 55 | Contagem de sinais por plugue (DA 6, DB 4, DC 3, PT1 5, PT2 5, PT3 11, PT4 2, LIH 5) | CONFIRMA | V /48, contagem direta | alta |
| 56 | II.8 vias com sinal: M-A 12, M-B 12, T-1 4, T-2 6, L-1 4 (121, 121A, 122, PE), P-A 9 distintos, P-B 4, P-C 3, H-1 3, B-1 10+4, B-2 10+4 | CONFIRMA | Contagens batem com as tabelas da Parte II e com V /21, /38, /48 | alta |
| 56 | D-1: BD+BE = 6 vias (301, 302 e 4 sinais) | CONTRADIZ | V /44 (poço): BD 2 e BE 2 (302) não tem fio; cada chave leva ULSn/DLSn + 301 + PE (V /49: 'ULS1, 301, PE'). Necessário: 301 + 4 sinais (+ PE) | alta |
| 56 | K-4: EY4 = 11 vias com sinal | CONTRADIZ | Conflita com a própria pág. 49 (12 sinais) e com V /38 (14 sinais) | alta |
| 56 | K-7: COB1/COB2 = 7 por conector | CONTRADIZ | Pág. 50 diz 10 pinos com sinal (8 distintos); III.2 e IV.4 dizem 8 sinais (manual A02 fig. pág. 10) | alta |
| 56 | 'Os cabos K-x são os cabos de topo de cabina' | CONFIRMA | V /49 lista os conectores da caixa de teto (DC1, DZ, DEN1, SOS, EDP1, RDZ, FAN, WT, GS1, DP, SL, SUP1/2, DEN2, EDP2, GS2, DC2, SGC) | alta |
| 56 | Colunas 'Vitinho' (ex.: AA /12.2:D, BB /12.6:D) | CONFIRMA | Ver verificação em lote das citações abaixo | média |
| 57 | II.9 índice cruzado: sinal -> folha.coluna:linha | CONFIRMA | Parser simples sobre 574 endereços de II.3 a II.9: 492 batem exatamente (mesma folha, coluna, linha, sinal presente na celula); 64 diferem só em 1 linha (mesma folha e coluna); 18 são ruído do parser; 0 sinal ausente da folha citada. Contagens '+N pags' não testadas | média |
| 57 | P23 RESOLVIDA: RDZ pino 1 = 301 (manual); P24 RESOLVIDA: SOS pino 1 = 123A, pino 3 = 123 | CONFIRMA | Ver linhas das págs. 47 e 49 | alta |
| 57 | P26: 201 -> TIS 13-14 -> S1 -> XB 203 -> RTD (VDR1) -> 202 e 205 -> RRD (VDR2) -> 202; versão 24 V com 301, 303, 305, 302 'e diodos' | CONFIRMA | V /22 confirma o caminho 201/TIS/S1/203 e 205/RRD/202 e a versão 24 V (301, 303, 305, 302) | alta |
| 57 | P26: versão 24 V 'e diodos' | CONTRADIZ | V /22 não desenha diodos; ambas as versoes mostram só varistores VDR1/VDR2 | média |
| 58 | II.11.1 divergências OS 3x5, BD/BE 2x4, PT1 3x5, DA Hylok 4x6, AA/AB 40x48 | CONFIRMA | Coerente com as pinagens: OS 5 pinos com sinal, BD/BE 4, PT1 5, DA 6 (V /21, /48) e 24 sinais x 2 pontas = 48 | alta |
| 58 | BC/DC: terminais 6, pinos com sinal 3 = 'OK (3 fios)'; BB/DB: terminais 8, pinos com sinal 4 = 'DIVERGE' | CONTRADIZ | Critério incoerente: nos dois casos terminais = 2 x sinais (6 = 2x3; 8 = 2x4). BB/DB deveria ser OK pelo mesmo critério do BC/DC | alta |
| 58 | DC1 3 fios (208, 207, PE); EDP1 220 V usa 5 fios (208, 207, PE, 301, X1); X15 e 24 V opcionais; DEN1 7 sinais (X3, X5, 301, B1, B2, B3, BM) | CONFIRMA | Manual A02 fig. pág. 10: DC1 208/207/PE; EDP1 208 pino 1, PE 3, 301 pino 4, 207 pino 7, X1 pino 10 (5 fios); DEN1 7 sinais | alta |
| 58 | FAN MiniFit 8 vias com 6 pinos com sinal 'OK' | CONFIRMA | V /38 e manual: FAN de 8 posições, 6 usadas (confere, contra a Parte II.4 que diz 6 pinos) | alta |
| 58 | Cabo 0,75 mm2, Mini Fit 4,2 mm 'Ryndack', Hylok, códigos VPMP, VPEL-704a, CSV de estrutura, PDF de 13/11/2026 | NÃO VERIFICÁVEL | Fontes de empresa fora do escopo (lista de materiais, estrutura). Só a lista BST confirma que cabos modulares usam 0,75 mm2 | - |
| 58 | BD/BE: 'conferir se 301/302 realmente não vao ao cabo' | NÃO VERIFICÁVEL | Não é afirmação verificável, mas já respondível: V /44 e /49 (só 301 vai; 302 não) | alta |
| 59 | II.11.2/II.11.3: quantidades e percentuais (63,7 -> 77 m = +21%; 9,4 -> 14 m = +49%; forquilha 9-7 = falta 2; tubular 115-75 = falta 40) | CONFIRMA | Aritmética interna correta (+20,9% e +48,9%) | alta |
| 59 | 108 fios de 0,75, 4 de 2,5 e 13 de 6 mm2 | CONFIRMA | Contagem no extrato da lista de fios usado nas auditorias (108+4+13 = 125 linhas); fonte derivada, peso baixo | baixa |
| 59 | P32: divergências FIXO (VPMP-057, 793, 799, 853, 855, 889) e bateria VPMP-067 | CONTRADIZ | Incompleta pelos dados do próprio livro: VPMP-846 (contator, 'ausente' no PDF, 1 no CSV, FIXO) também diverge e não está na P32 | alta |
| 60 | Manual CTW-B3 19010849, rev. A02 'de 11/2022' | CONTRADIZ | Manual A02 pág. 11 (histórico): A02 = July 2022, A01 = Sep 2020, A00 = October 2018. 11/2022 é a data do nome do arquivo (20221124) | alta |
| 60 | Modelo CTW-B3 sem controladora de porta (porta dupla possível); placa MCTC-CTB-H5 | CONFIRMA | Manual A02 pág. 3 (Model Description, 'Without door operator controller (double-door)') e pág. 4 (CTB-H5). Obs.: V /44 e o esquema 19060918-ZL (pág. 29, 32) citam 'CTB-H6' | alta |
| 60 | 'COB-A1/A2/F1 e CCB-F1 são placas de cabina' | CONTRADIZ | Manual: as placas são MCTC-COB-A1, MCTC-COB-A2 e MCTC-CCB-F1. Não existe 'COB-F1' | alta |
| 60 | Entradas: CA 507/508 220 V 7 A; CA 207/208 220 V 4 A; CB 301/302 24 VDC 5 A, só 24 V | CONFIRMA | Manual A02 pág. 3 (Table 3) e NOTE pág. 6 | alta |
| 60 | Saídas: DC1 e DC2 220 V 4 A; FAN 509/510 com 508 220 V 1 A; EDP 207/208 220 V 1 A e 301/302 24 V 2 A; SL 24 V 1 A; COB 301/302 24 V 3 A, T01 12 V 0,62 A, Z01 12 V 0,48 A | CONFIRMA | Manual A02 pág. 3 (Table 3), valores idênticos | alta |
| 60 | Y3 220 V 5 A = tomada | NÃO VERIFICÁVEL | Table 3 lista 'Y3 1PH 220VAC 5A' e a Table 1 diz que a tomada tem máximo 5 A, mas o manual não rotula Y3 como tomada | média |
| 60 | Tomada 220 V máximo 5 A, sem furadeira de impacto | CONFIRMA | Manual A02 pág. 2 (Table 1) | alta |
| 60 | Ambiente: interno, -10 a +50 C, UR <95%, vibração <5,9 m/s2, IP21 vertical, resfriamento natural | CONFIRMA | Manual A02 pág. 3 (Table 3) | alta |
| 60 | Fixação na balaustrada, parede, Fig. 3 e 4 (PREENCHER) | CONFIRMA | Manual A02 pág. 3: instalada na balaustrada, montagem em parede; Fig. 3 e Fig. 4 existem (ver P40) | alta |
| 60 | 5 botoes de inspeção, luz do teto, interfone, LEDs D1-D30, porta USB | CONFIRMA | Manual A02 pág. 2 (Table 1, Table 2) | alta |
| 60 | III.2 CA: sinais 507, 508, 207, 208, PE, 134, 123, 125, 132, 131A, 130 (11) | CONTRADIZ | O 133 (CA pino 6) está no desenho do manual (fig. pág. 11) e no Vitinho, e a própria Parte II.3.1 o lista; a Table 4 do manual também o omite, mas a ligação existe. CA tem 12 sinais | alta |
| 60 | III.2 CB (13 sinais: DZI, R, L, DC12, FL1, FL2, 301, 302, CAN+, CAN-, SGC1, SGC2, 102) | CONFIRMA | Manual A02 pág. 5 (CB). Atenção: a fig. pág. 11 separa em 'CC' (301, 302, CAN+, CAN-, FL1, FL2) e 'CB' (DC12, R, L, GND) | alta |
| 60 | III.2 DEN: X3/X4 abertura, X5/X6 fechamento, 301, B1/C1 abrir, B2/C2 fechar, B3/C3 forçado, BM/CM comum; entradas 10-30 V; saídas a relé 28 V 5 A | CONFIRMA | Manual A02 pág. 6 | alta |
| 60 | III.2 EDP: até 9 fios; 5 se barreira 220 V | CONFIRMA | Manual fig. pág. 10: EDP1 usa 9 pinos (1,3,4,5,6,7,10,11,12); barreira 220 V: 208, 207, PE, 301, X1 | alta |
| 60 | III.2 DP, COB, FAN, WT, DZ, RDZ, SL, SGC, GS, SUP, SOS, Y4 (sinais) | CONFIRMA | Manual A02 pág. 5-6 e fig. pág. 10-11; SUP2 = 128/129; SOS = 123/124; Y4 = 301, X12, X13, X14, 125, 124, 127 | alta |
| 60 | III.2 MSC: CAN+, CAN-, 301, 302, DZI, 130, 102, 127, 128, 132, 134 (11 sinais) | CONTRADIZ | Manual A02 pág. 5: MSC tem também DC12 (12 sinais) | alta |
| 60 | 'Cabo sugerido': 2 fios -> VPMP-304; 3 -> VPMP-221; 4 -> VPMP-005; >4 -> VPMP-912 [Chute] | NÃO VERIFICÁVEL | Códigos internos de cadastro, sem fonte técnica | - |
| 61 | III.3 funções 130/131A porta frontal; 133/134 traseira; 132/134 inicio/fim da trava traseira; 125 saída de emergência; 123 inicio do circuito de segurança; 102 ponto comum [Certeza] | CONFIRMA | Manual A02 pág. 5-6 (tabelas CA, GS1, GS2, MSC), todas as definições batem | alta |
| 61 | III.3: 'os demais pinos já batiam com o manual (CA, CB, GS1/GS2, SUP1, WT1/WT2, DZ, COB1/COB2, EDP1)' | CONTRADIZ | CB de II.3.2 tem 122A (pino 8) e não tem SGC1/SGC2, ao contrário do manual; CA e EDP1 (pino 12) tem as ressalvas acima. GS, SUP1, WT, DZ, COB batem | média |
| 61 | P38: A00 (2018) 'não traz as exigências de instalação e de ambiente'; A01 só pequenas correções | CONTRADIZ | O arquivo A00 (Manual_Caixa_de_Teto_MCTC-CTW-B3_2018_CN.pdf, histórico 'October 2018, A00, First release') contem a Table 3 completa (ambiente, IP21, vibração), as Fig. 3 e 4 e a mesma Table 4. Única diferença encontrada no texto: o aviso 'instalar na vertical e manter a tampa fechada'. A01 'minor corrections' confere | alta |
| 61 | P37: DEN1 manual 7 sinais; lista 6 terminais | CONFIRMA | Manual: 7 sinais. A fig. pág. 10 liga 6 deles (X3, X5, 301, B2, B1, BM); B3 não tem fio no exemplo | alta |
| 62 | Elevador de referência, caixa do poço no nível do 1o pavimento | NÃO VERIFICÁVEL | Informação de projeto do Gelson; não há fonte técnica. V /48 só traz a nota 'instalar o interfone fora da caixa de inspeção do poço' | - |
| 62 | BA vai do último ao 1o pavimento, ~30 m com 3 m horizontais [Chute]; curso 24 m | NÃO VERIFICÁVEL | Nenhuma fonte traz curso ou comprimento. A lista BST traz só segmentos (ex.: 6 m 'control cabinet connection') | - |
| 62 | Cabos da caixa aos dispositivos do poço: ~4 m com poço de 1,5 m [Provável] | NÃO VERIFICÁVEL | BST: 'Safety switch plug-in cable of the shaft pit' 4,7 m (3x0,75+1x0,75), ordem de grandeza compatível, mas não é a mesma instalação | baixa |
| 62 | Valores de cota/distância do botao de parada na NBR 16858 / EN 81-20 | NÃO VERIFICÁVEL | Normas não estão entre as fontes | - |
| 62 | PT1 vira jumper curto se for uma única caixa [Provável] | NÃO VERIFICÁVEL | V /48 mostra duas caixas (PIB-XX e PIB-A12) ligadas pelo cabo PT1; com uma caixa só, a ligação interna depende do projeto | baixa |
| 62 | IV.2: caixa do poço recebe BA em DA 6P, BB em DB 4P e BC em DC 4P [Certeza] | CONFIRMA | V /48 (icones 'Shaft cable' BA, BB, BC sobre DA, DB, DC) | alta |
| 62 | IV.2 BA: 'PE, 118, 121 (=119), 122A, 111, 123 até o poço' | CONTRADIZ | 121 e 119 NÃO são o mesmo nó: V /19 mostra 119 -> FLSD -> 120 -> FLSU -> 121 -> BA 3 (V /49: limite inferior 119, 120, PE; superior 120, 121, PE). BA 3 (121) vai ao FLSU; DA 1 (119) vai ao FLSD. BA para DA direto: PE, 118, 122A, 111, 123 | alta |
| 62 | IV.2 BA: '131, 132, 132, 133 passam pelos contatos das 3 portas de pavimento' | CONTRADIZ | V /43 e /19: só 131 -> 132 passa pelas fechaduras frontais (BA 4 a BA 7). 132 -> 133 (BA 8 a BA 9) é o trecho das portas traseiras; V /19 manda ligar BA-P08 e BA-P09 em porta única | alta |
| 62 | IV.2 BA: tronco >= 10 veias + 3 ramais de 2 fios (VPB-098, 4 m) | NÃO VERIFICÁVEL | V /49: fechadura superior 131, 131B, PE e inferior 130n, 132, PE (3 condutores); BST: segmentos de 4 m com 3x0,75+1x0,75 e de 2x0,75 (6 m). Código VPB-098 fora das fontes | baixa |
| 62 | IV.2 BB 'KCB 8P?' | CONTRADIZ | BB é de 4 pinos (V /21: 301, 302, MOD+, MOD-), como a própria pág. 53 informa | alta |
| 62 | IV.2 BB: 301, 302, MOD+, MOD-; 24 V + RS-485 (V /45) | CONFIRMA | V /45: barramento 301, 302, MOD+, MOD- até as HCB (24V, COM, 485+, 485-) com blindagem desenhada | alta |
| 62 | IV.2 BC: R, L, DC12; IL: 802, 805, 803, 804, PE, 6 veias | NÃO VERIFICÁVEL | BST: cabo de iluminação do poço 4x0,75+1x0,75 (5 condutores) e V /46: do quadro seguem 807, 809, 802 e PE; 805 é interno da caixa A12 | média |
| 62 | IV.3: PT1 (802, 805, PE, 111, 112), PT2 (118B, PE, 119, 112, 113), PT3 (11 de 12), PT4 (301, PX4), LIH (5 de 6) | CONFIRMA | V /48 | alta |
| 62 | IV.3: PT2 GTS entre 112-113; BFS1->BFS2 em série 118B->119 | CONFIRMA | V /19: GTS entre PT2 5 e PT2 6; BFS1 e BFS2 em série entre PT2 2 e PT2 4 (119) | alta |
| 62 | IV.3: PT3 com PES1, PITU/PITD/PITB, placas MCTC-PTB-A1 e MCTC-KZ-G2 | CONFIRMA | V /3.a (PES1 'Handle stop button', PTB-A1 'Pit inspection board'), V /48 ('Pit extension board MCTC-KZ-G2'), V /19 | alta |
| 62 | IV.3: FLSU/FLSD 'rede 121 e PE, 2 a 3 cada' | CONTRADIZ | V /49: FLSD 119, 120, PE; FLSU 120, 121, PE (3 condutores cada, redes diferentes) | alta |
| 62 | IV.3: PL1 e PUR1/PUR2 ficam dentro da caixa, sem cabo de campo | CONFIRMA | V /48 e /46 | alta |
| 63 | IV.4: 12 cabos = 1 de manobra + 11 ramais | CONFIRMA | Contagem da tabela: manobra, DC1, DEN1, EDP1, DP, COB1, FAN, DZ, RDZ, GS1, SOS, SL = 12. Coerente com a lista de conectores da caixa em V /49 | alta |
| 63 | IV.4: 24 sinais, 301/302 em dobro -> 26 veias + 10% = >= 29 | CONFIRMA | Aritmética (24+2 = 26; x1,1 = 28,6). Manual A02: CB 301/302 24 V 5 A. Obs.: pelo manual CB tem 13 sinais (CA 12 + CB 13 = 25) | média |
| 63 | IV.4: itens excluídos (porta traseira, pesagem, SUP, SGC, Y4) | CONFIRMA | V /49: SGC 'Add when asynchronous', GS2/DC2 'Add when through door'; manual: Y4 'pronta de fábrica' | alta |
| 63 | IV.4: com 1 porta, não há item para os jumpers do quadro (BA 8-9; AA 6-14) | CONTRADIZ | V /19: notas 'single door, connect BA-P08 and BA-P09' e 'single door, connect AA-P06, AA-P14'. Sem GS2 e sem portas traseiras, 133-134 (AA 6 e 14) e 132-133 (BA 8 e 9) precisam ser fechados. O livro não cita | alta |
| 63 | IV.4: DEN1 7 sinais -> 8 veias; COB1 8 sinais; EDP1 3 veias (301, 302, X1) para cortina 24 V; DP 2; SOS 2 | CONFIRMA | Manual A02 fig. pág. 10-11 (DEN1 7 sinais; COB1 301, 302, MOD+, MOD-, DC12, Z01, L, R; DP 301 e X11; SOS 124/123) | média |
| 63 | IV.4: comprimento do manobra L ~ 15 + 14,5 = 30 m [Chute] | NÃO VERIFICÁVEL | Aritmética fecha (29,5), mas nenhum dado de curso, ponto fixo ou horizontal consta nas fontes | - |
| 63 | IV.4: terminal Mini Fit VPMP-795, corpos VPMP-796..801 (2 a 12 vias) | NÃO VERIFICÁVEL | Cadastro interno | - |
| 64 | IV.5: N2-A inversor NICE3000new + MCB-C3; N2-B KCB-B4A; N2-B' PCB-D1; N2-C ERB-A1 com bateria; N2-D botoeira de inspeção/resgate | CONFIRMA | V /3 e /3.a (NICE-L-C-40XX, MCTC-MCB-C3, KCB-B4A, PCB-D1 'Brake power board', ERB-A, CIU/CID/CIS/MES); manual ERB-A1 EN: 'Battery Provided: A1 yes, A2 no'. 'Conferida pelo rótulo' e posição na foto: não verificável | média |
| 64 | IV.5: E1 QFB1, E3 QFB2, H1 QFB3, H4 QF; G transformador TRF; F1 BY, F2 FX, F3 SW | CONFIRMA | V /3.a: QFB1 'Safety circuit breaker', QFB2 'control power', QFB3 'RCD for car top', QF 'Main switch', TRF, BY 'Brake contactor', SW 'Run contactor', FX 'U.V.W short contactor' | alta |
| 64 | IV.5: DQFB1, DQFB2, DQFB3 e H3 'BC-1?' | NÃO VERIFICÁVEL | Estes códigos não aparecem no Vitinho nem no esquema 19060918-ZL; vem das fotos | - |
| 64 | IV.5: I1-I7 = R, S, T, N, U, V, W; J tomada; K barramento PE | CONFIRMA | V /9 (bornes R, S, T, N; U, V, W; PE) e V /8 (CZ 'Female receptacle'); posição física não verificável | média |
| 64 | IV.6: PCB-D1 J3 pino 2 (BK1+) -> SW 53-54 -> KY8 3 (ZQ1+); J3 pino 3 (BK2+) -> SW 73-74 -> KY9 2 (ZQ2+); J3 pino 1 (BK-) -> BY -> KY6 4 e KY9 4 (ZQ1-, ZQ2-) | CONFIRMA | V /13 (desenho completo do circuito) | alta |
| 64 | IV.6: MT pinos 5, 6, 11, 12 = ZQ1+, ZQ2+, ZQ1-, ZQ2-; pinos 1, 2, 3, 7, 8, 9 = X18, X22, X20 e 301 x3 | CONFIRMA | V /13, /9, /21 (ver pág. 52) | alta |
| 64 | IV.6: X18, X22, X20 'sinais 24 V de fim de curso do freio'; X20 função [Chute] | CONTRADIZ | X20 não é do freio: V /9 (MT 3 X20 -> PT1 'Motor overheating detection') e V /21 tabela 'X20 Motor overheating protection'. O próprio livro (pág. 52) já diz isso | alta |
| 65 | P47: /15 manda usar SCB-A4 (síncrona, porta única) com F6-52 BIT1 = 1; /25 pede F6-52 BIT6 e F5-25 bits 9 e 10 [Certeza] | CONFIRMA | V /15: 'Synchronous machine single door, use SCB-A4 ... F6-52 BIT1=1'; V /25: 'F6-52 BIT6=1; F5-25 Bit9=1 up-level, Bit10=1 down-level' | alta |
| 66 | IV.8: AD30 tem L, N, PE; U, V, W, PE; 24V, COM, PGA, PGB, PGZ [Certeza boletim] | CONFIRMA | Boletim AD30 pág. 1-2 (texto e Figura 1) | alta |
| 66 | IV.8: motor 4 veias, 'blindagem não consta no boletim' | CONTRADIZ | A Figura 1 do boletim (pág. 2) desenha elipse (simbolo de cabo blindado) em torno dos cabos do motor e do encoder; o texto não fala | média |
| 66 | IV.8: DI1 abrir, DI2 fechar (padrao); DI3 cortina; DI4 fechamento forçado; TA12 comum; TC1 LPA; TC2 LPF; DO3 fechamento impedido; DO4 falha | CONFIRMA | Boletim AD30 pág. 2 e Figura 1: DI1 'Door open command', DI2 'Door close command', DI3 'Light curtain signal', DI4 'Forced door close signal', TA12 'control system input COM' (com TB1, TB2), DO1 TC1 'Door open limit', DO2 TC2 'Door close limit', DO3 TA3/TC3 'Door close hindered', DO4 TC4/TA4 'Fault output' | alta |
| 66 | IV.8: L, N, PE do AD30 <- DC1 207, 208, PE [Provável] | CONFIRMA | Manual A02 fig. pág. 10: DC1 208 -> N, 207 -> L, PE -> PE da controladora de porta | alta |
| 66 | IV.8: comandos B1/B2/B3 do DEN1 -> DI1/DI2/DI4; X3 -> TC1; X5 -> TC2; 301 -> TA12 [Provável] | CONFIRMA | Manual A02 fig. pág. 10 liga B1 a DI1, B2 a DI2, BM a COM e 301/X3/X5 a TA1/TC3/TC1 (controladora genérica). No AD30 valem as funções do boletim. Ligação CTW-B3 <-> AD30 só por correspondência de função | média |
| 66 | IV.8: DP (X11, 301) não é a saída de falha do AD30 | CONFIRMA | Manual A02 pág. 5: DP = 'motor overheat protection input'; boletim: DO4 'Fault output' | alta |
| 66 | IV.8: parametros F1-00 = 1 PMSM, F1-01 a F1-05, F1-06 (0 ABZ, 1 SPI, 2 ABPWM), F1-07, FP-01 = 1; autoajuste TUNE1 e TUNE2 (até 3 aberturas) | CONFIRMA | Boletim AD30 pág. 3 a 5 | alta |
| 66 | IV.8: total sobe de 12 para 14 cabos | CONFIRMA | Aritmética | alta |
| 66 | P50: manual A02 pág. 5 e 6; o manual escreve 'output' para X5/X6 | CONFIRMA | Table 4 (pág. 6): 'X5/X6 Door 1/2 close limit signal output'; DEN está na pág. 6, DP/WT/DZ/... na pág. 5 | alta |
| 66 | P51: cortina entra em EDP1 X1 (aresta X15) com 301/302 para 24 V | CONFIRMA | Manual A02 fig. pág. 10 (EDP1 X1 pino 10, X15 pino 12, 301 pinos 4/5/6, 302 pino 11) | alta |

## 3. Selos e pendências: o que as fontes resolvem

Legenda: CONFIRMADO = selo [Certeza] que as fontes sustentam; RESOLVIDO = selo [Provável], [Chute] ou PREENCHER fechado por fonte; PARCIAL = fonte ajuda mas falta algo; AINDA ABERTO = nenhuma fonte lida resolve.

### 3.1 Selos e campos PREENCHER por página

| Id | Pág. | Selo ou campo | Situação | Evidência ou o que falta |
|---|---|---|---|---|
| S1 | 43 | [Certeza] AA=CA e AB=CB sinal a sinal | CONFIRMADO | V /21 e /38, V /11 texto |
| S2 | 43 | [Chute] par CAN+/CAN- trançado e blindado e prática usual | RESOLVIDO | Manual NICE3000new pág. 73: 'communication cable must be twisted pair with metal shield, at least 0,75 mm2'; 'four-core cable: 24 VDC, CAN+, CAN-, COM'; pág. 116: 'shielded twisted pair'. Ressalva da pág. 73: blindado não é recomendado em alta taxa e longa distância (atraso) |
| S3 | 43 | [Provável] KCB girada 180 graus no quadro real | AINDA ABERTO | Falta foto do quadro; o Vitinho só traz o layout desenhado |
| S4 | 43 | [Provável] 130, 131A, 133, 134 circuito de portas/bypass; 132 cadeia 110 V | RESOLVIDO | Manual A02 pág. 5-6: 130 safety circuit end / porta frontal sinal 1, 131A front lock end, 133 rear lock signal 1, 134 rear lock end, 132 rear lock start; V /19 e /43 |
| S5 | 43 | [Provável] 102 retorno/comum 110 V | RESOLVIDO | Manual A02 pág. 5 (MSC 102 'common point of the safety circuit and door lock circuit'); manual NICE3000new pág. 65 'neutral line'; V /19 LEDs retornam em 102 |
| S6 | 43 | [Provável] L e R áudio de interfone | RESOLVIDO | Manual A02 pág. 5: 'R, L Intercom signal'; DC12 'intercom power supply 12 V positive'; fig. pág. 11: AB-P13 = R, AB-P12 = L, AB-P11 = DC12 |
| S7 | 43 | [Certeza] pino 14 (DZI) e pino 1 (102) concordam em /21 e /38 | CONFIRMADO | V /21 e /38 |
| S8 | 44 | DZI 'não rotulado no Vitinho' | RESOLVIDO | Manual A02 pág. 5: 'DZI door zone signal output by magnetic scale' |
| S9 | 45 | [Provável] EDP1 = HX1/HX20 (falha) (também EDP2 HX2/HX21) | PARCIAL | HX1, HX2, HX20, HX21 definidos em V /38. Mas o manual da CTW-B3 chama o pino 12 de X15 (aresta de segurança) e não de HX20. Mesmo pino, função diferente entre as duas fontes: falta decidir na montagem qual vale (P36) |
| S10 | 45 | [Certeza tabela HX/HY] HX1, HX20, HX2, HX21 | CONFIRMADO | V /38 tabela HX |
| S11 | 46 | [Certeza tabela HX/HY] HX15, HX16, HX5, HX6, HX11, HX19 | CONFIRMADO | V /38 tabela; ressalva: '(HX3/HX4/HX5)' da pág. 46: HX3 e HX4 são '/' em V /38 |
| S12 | 47 | [Certeza] HX9/HX10, HX7/HX8, HX17/HX18, HX22/HX23; DZ pela tabela; RDZ pelo manual | CONFIRMADO | V /38 tabela HX; manual A02 pág. 5 |
| S13 | 48 | [Provável] GS1 e GS2 circuito de portas (contato) | RESOLVIDO | Manual A02 pág. 5: GS1 'front car door lock signals' (130, 131A); GS2 'rear car door lock signals' (133, 134) |
| S14 | 48 | [Certeza pela lista de peças] SUP1 'Standby switch 1' | CONFIRMADO | V /3 (SUP1 /34.4:F) |
| S15 | 48 | [Provável] SUP2 chave de espera 2 (129/127) | RESOLVIDO | Manual A02: SUP2 = 129 e 128; 'sem MSC, curto entre 127 e 128' => 127 do Vitinho é o nó 127/128 curto. Inferência sustentada pelo manual; confirmar com multímetro na montagem |
| S16 | 48 | [Provável] CC = SGC1/SGC2 (porta/bypass) | RESOLVIDO | Manual A02 pág. 5: SGC1/SGC2 'auxiliary car door lock 1/2'; V /49: SGC 'auxiliary lock, add when asynchronous'. Obs.: numeração física no manual e SGC1=12, SGC2=10 (conferir conector) |
| S17 | 48 | [Provável] AC SGC1/SGC2 (pág. 53) | RESOLVIDO | Mesmo item, V /21 AC 2=SGC2, 6=SGC1; V /15 (SGC2/SGC3 só com SCB-D4) |
| S18 | 49 | [Certeza manual] SOS pino 1 = 123A (124), pino 3 = 123 | CONFIRMADO | V /38 e manual A02 fig. pág. 11; V /19 mostra 123A e 124 ligados pelo curto MSC 10-12 |
| S19 | 49 | PREENCHER pinagem final de EY3, EY5, BAT, TEL1 | PARCIAL | V /38: EY5 1=302, 2=302, 3=E12V, 4=DC12V1; TEL1 1=L, 2=R, 3=DC12V, 4=302, 5=PC+, 6=PC-, 7=EB1, 8=EB2; EY3 só tem 3 sinais (PE pino 1, 508 pino 3, 507 pino 6); BAT na ordem do desenho BAT-, vazio, BAT-, NTC+, vazio, BAT+ (numeração não rotulada) |
| S20 | 49 | [Certeza tabela HX] EY4 HX12 a HX14 | CONFIRMADO | V /38 e manual Y4 (X14=1, X13=2, X12=3) |
| S21 | 50 | [Provável] COB1/COB2 R/L áudio | RESOLVIDO | Mesmo item de S6; manual A02 fig. pág. 10: COB1 1=R, 2=L |
| S22 | 52 | PREENCHER bitola/blindagem do cabo do freio | AINDA ABERTO | V /13 da só a fonte: 48-207 VCC (110 padrao), 6 A de impacto e 4 A de manutenção. A bitola não consta em nenhuma fonte lida |
| S23 | 52 | PREENCHER pinos do cabo do limitador (OS, P26) | PARCIAL | OS já resolvido (V /21 e /49). Ação remota: não usa conector OS, usa bornes XB 203, 205, 202 (versão 220 V) ou 303, 305, 302 (versão 24 V) em V /22; cabo de 3 vias |
| S24 | 53 | [Provável] 132 (BA 7 e 8) e 133 (BA 9) | RESOLVIDO | V /19 e /43: BA 4 (131) -> BA 7 (132) frontal; BA 8 (132) -> BA 9 (133) traseira |
| S25 | 53 | PREENCHER pinagem das botoeiras e displays de andar (P28) | PARCIAL | V /45: HCB tem 24V, COM, 485+, 485-, UP:1..4, DW:1..4, ST:1/2 (fora de servico), XF:1/2 (incendio); manual NICE3000new pág. 117 (MCTC-HCB). Botoeira de fabricante BST não está nas fontes |
| S26 | 54 | [Certeza /48] todos os plugues DA, DB, DC, PT1..PT4, LIH | CONFIRMADO | V /48 tabelas (pino a pino conferido) |
| S27 | 54 | [Provável] R, L do DC | RESOLVIDO | Mesmo item S6 |
| S28 | 60 | [Certeza manual] III.1 dados técnicos | CONFIRMADO | Manual A02 pág. 2-3. Exceções: 'A02 de 11/2022' (e julho 2022) e 'COB-A1/A2/F1' |
| S29 | 60 | [Chute] cabo sugerido por número de fios (P35) | AINDA ABERTO | Convenção interna de cadastro; sem fonte técnica |
| S30 | 60 | PREENCHER cotas de furação e fixação (Fig. 3 e 4) | RESOLVIDO | Manual A02 pág. 3: Fig. 3: furo Ø8, entre-eixos 254 (horizontal) x 340 (vertical), caixa 275 x 376, profundidade 135 (80 até a face de fixação); Fig. 4: 4 parafusos M6. Leitura da figura: 254 e 340 são menores que a caixa, logo são os entre-eixos |
| S31 | 61 | [Certeza] funções de 130..134, 125, 123, 102 | CONFIRMADO | Manual A02 pág. 5-6 |
| S32 | 62 | [Chute] ~30 m do cabo BA | AINDA ABERTO | Sem fonte; depende de P41 e P42 |
| S33 | 62 | [Provável] ~4 m aos dispositivos do poço | PARCIAL | Apoio fraco: BST 'safety switch plug-in cable of the shaft pit' 4,7 m |
| S34 | 62 | [Certeza que a norma trata / Chute nos valores] botao de parada | AINDA ABERTO | NBR 16858 e EN 81-20 não estão nas fontes |
| S35 | 62 | [Provável] PT1 vira jumper curto | PARCIAL | V /48: duas caixas (PIB-XX e PIB-A12) ligadas por cabo PT1 (802, 805, PE, 111, 112); com caixa única o cabo não existe, decisão de projeto |
| S36 | 62 | [Provável] origem da iluminação não aparece em DA, DB, DC | RESOLVIDO | V /46, /7, /8: origem é o quadro: QFB4 'RCD for [hoistway] lighting' (/8.7:C) -> LIHS1 (/8.7:E) -> bornes XB 807, 809, 802 e PE; plugue LIH: 802=1, 805=2, 803=3, 804=4, PE=6; esquema 19060918-ZL pág. 2: 'QFB4 disjuntor da iluminação da caixa' |
| S37 | 62 | [Certeza] PT1 mistura iluminação e segurança (desenho do fabricante) | CONFIRMADO | V /48 |
| S38 | 63 | [Provável] DEN1 8 veias; CAN em par blindado; RS-485 em par trançado; EDP1 3 veias | PARCIAL | CAN: ver S2. RS-485 trançado: manual NICE3000new pág. 70 'twisted pair as the RS485 communication cable'. V /45 desenha blindagem no barramento 301/302/MOD+/MOD-. Contagem de veias do DEN1 e EDP1 depende do projeto |
| S39 | 63 | [Chute] ~30 m do cabo de manobra; fórmula | AINDA ABERTO | Sem fonte |
| S40 | 64 | [Certeza]/[Provável] zonas N2-A a N2-K | PARCIAL | Nomes dos itens confirmados em V /3 e /3.a; posição física na foto não verificável |
| S41 | 64 | [Chute] FX função a confirmar | RESOLVIDO | FX = contator U.V.W de curto (para motor síncrono): V /3.a (FX 'U.V.W short contactor' /17.4:D), V /21 (Y3 'U.V.W short contactor output', X8 feedback), esquema 19060918-ZL pág. 3 e 9 ('Contatora auxiliar se motor síncrono') |
| S42 | 64 | [Chute] H3 'BC-1?' | AINDA ABERTO | O código 'BC-1' não aparece em nenhuma fonte; falta foto/etiqueta |
| S43 | 64 | X20 função [Chute] (IV.6) | RESOLVIDO | V /9, /21, /49: X20 = proteção de sobretemperatura do motor (PT1), não é contato de freio. Corrigir IV.6 |
| S44 | 66 | [Provável]/[Chute] linhas 'Liga em' do AD30 (L,N,PE; DI1, DI2, DI4, DI3, TA12, TC1, TC2, TA4) | PARCIAL | Funções dos terminais do AD30 confirmadas (boletim). L,N,PE <- 207, 208, PE confirmado pelo manual A02; B1->DI1, B2->DI2, BM->COM pelo manual A02; B3->DI4 e X3->TC1, X5->TC2, 301->TA12 só por correspondência de função. DI3 'sinal da cortina de luz' está no boletim; usar ou não é decisão de projeto |

Os 23 campos PREENCHER da lista II.8 (pág. 56) herdam as respostas de S22, S23, S29 e P22: o número de vias que o livro deixou em branco pode ser preenchido assim: T-3 (encoder) 12 condutores; L-2 (ação remota do limitador) 3 vias; D-1 (BD/BE) 5 condutores (301 + ULS1, ULS2, DLS1, DLS2) mais PE; K-5 FAN 6 pinos em conector de 8 posições. Bitola, blindagem, comprimento e carcaças continuam abertos.

### 3.2 Pendências P21 a P51 (escopo das págs. 43 a 68)

| Pend. | Situação | Evidência ou o que falta |
|---|---|---|
| P21 | PARCIAL | Lidos em V: /22 (limitador), /43 (fechaduras), /44 (desaceleração: poço BD/BE ou cabina CD/MX), /45 (chamadas externas), /46 (iluminação). /35 (inspeção de teto) não foi lido em detalhe. Fechar as tabelas N3 a N5 e C1 a C3 ainda exige a pinagem física das botoeiras |
| P22 | PARCIAL | Parcial. Fontes dao: 0,75 mm2 mínimo para CAN (manual NICE3000new pág. 73), lista BST (cabos 3x0,75+1x0,75, 2x0,75, (2x2)P x0,75, 4x0,75+1x0,75), veias por segmento em V /49 (3 condutores por chave de poço). Faltam: bitola do freio, blindagem, comprimentos, carcaças |
| P23 | CONFIRMADO | RDZ pino 1 = 301: V /38 (301/DC12V) e manual A02 pág. 5 |
| P24 | CONFIRMADO | SOS pino 1 = 123A (124 no manual), pino 3 = 123: V /38 e manual A02 fig. pág. 11. Ressalva: 123A = 124 só com o curto do MSC 10-12 (V /19) |
| P25 | RESOLVIDO | Cartao MCTC-PG-E (V /9 e manual NICE3000new pág. 131-132, Table 3-33): CN1 1=B-, 3=Z+, 4=Z-, 5=A+, 6=A-, 7=COM, 8=B+, 9=VCC, 10=C+, 11=C-, 12=D+, 13=D-. Ligação ao encoder (V /9, idêntica ao manual): B- 5a, Z+ 4b, Z- 4a, A+ 6b, A- 2a, COM 5b, B+ 3b, VCC 1b, C+ 7b, C- 1a, D+ 2b, D- 6a. Cabo T-3: 12 condutores, blindado com malha no PE do lado do controlador (manual pág. 133). Vale para encoder tipo seno/cosseno ERN1387; para outro encoder (ex.: EI53C9.25 no acervo) a pinagem do lado do encoder muda |
| P26 | PARCIAL | Circuito confirmado em V /22; faltava a pinagem e está em V /22: bornes XB 203, 205, 202 (220 V) ou 303, 305, 302 (24 V); OS 6P é só o contato de sobrevelocidade (V /21, /49). Falta definir se o limitador e 220 V ou 24 V. 'Diodos' do texto não aparecem no desenho |
| P27 | PARCIAL | Mapa BA -> DA: PE 1->4, 118 2->2, 122A 5->3, 111 6->6, 123 10->5. BA 3 (121) vai ao FLSU e DA 1 (119) ao FLSD, com 120 entre eles (V /19, /49). BA 4 (131), 7 (132), 8 (132), 9 (133) vao as fechaduras de pavimento (V /43); ramais com 3 condutores nas pontas (V /49). Falta só o número total de veias do cabo, que é escolha de projeto |
| P28 | PARCIAL | V /45 e manual NICE3000new pág. 117: bornes da HCB 24V, COM, 485+, 485-, UP1..4, DW1..4, ST1/2, XF1/2. O modelo exato da botoeira BST não está nas fontes |
| P29 | AINDA ABERTO | Decisão de projeto. Dado das fontes: 24 sinais (CA 12 + CB 12) pelo Vitinho ou 25 (CA 12 + CB 13) pelo manual, 301/302 em dobro; manual NICE3000new pág. 73 pede quatro veias para CAN (24 V, CAN+, CAN-, COM) |
| P30 | PARCIAL | OS 3x5: pinos 2 e 6 são o mesmo nó 121A (V /21, /19), logo 3 terminais (121, 122, PE) bastam se 121A estiver em ponte e houver um só contato; BD/BE 2x4: RESOLVIDO, V /44 e /49 mostram que só 301 + sinal + PE são usados (302 sem fio), a lista precisa de pelo menos 3 por conector; PT1 3x5: os 3 pinos cobrem só a luz (802, 805, PE, V /46), os pinos 111 e 112 pertencem a cadeia (PES2); DA 4x6: DA tem 6 sinais, mas 119 vai ao FLSD, então 5 pinos vem do BA |
| P31 | NÃO VERIFICÁVEL | Códigos de cadastro, fora das fontes |
| P32 | NÃO VERIFICÁVEL | Cadastro, fora das fontes. Incluir VPMP-846 na lista (ver tabela) |
| P33 | PARCIAL | Blindagem do par CAN: recomendada, manual NICE3000new pág. 73. Comprimento real: ABERTO (sem fonte) |
| P34 | NÃO VERIFICÁVEL | Cadastro de terminais, fora das fontes |
| P35 | AINDA ABERTO | Desenho e cadastro dos cabos: precisa decidir CB (14P único no Vitinho) contra CC (301, 302, CAN+, CAN-, FL1, FL2) e CB (DC12, R, L, GND) separados na figura do manual |
| P36 | PARCIAL | Rótulos explicados: EDP pino 12 = HX20 (V) ou X15 (manual); 'CC' do Vitinho = SGC (pino 6 e 2) enquanto o 'CC' do manual = grupo 24V/CAN/FL e o SGC dele está nos pinos 12 e 10; SUP2 pino 2 = 127 (V) ou 128 (manual), mesmo nó pelo curto 127-128. Falta conferir o conector físico na montagem |
| P37 | PARCIAL | Manual A02 fig. pág. 10 liga 6 dos 7 sinais do DEN1 (X3, X5, 301, B2, B1, BM). B3 fica sem fio no exemplo. Se o AD30 usar DI4 para fechamento forçado (boletim), B3 é necessário; senao, 6 terminais bastam |
| P38 | PARCIAL | A02 como referência: correto. Mas a afirmação sobre a A00 está errada: o arquivo A00 tem a Table 3 de ambiente, as Fig. 3 e 4 e a mesma Table 4; só falta o aviso de instalação vertical |
| P39 | RESOLVIDO | Sem régua magnética, curto entre os pinos 10 e 12 do MSC: manual A02 (127 no pino 12, 128 no pino 10) e V /19 (123A no pino 10, 124 no pino 12, em série na cadeia) |
| P40 | RESOLVIDO | Manual A02 pág. 3, Fig. 3 e 4: furos Ø8, entre-eixos 254 x 340 mm, 4 parafusos M6, caixa 275 x 376 x 135 mm |
| P41 | AINDA ABERTO | Nenhuma fonte tem o curso |
| P42 | AINDA ABERTO | Medidas de campo, sem fonte |
| P43 | RESOLVIDO | Origem: QFB4 (RCD de iluminação do poço, 2P 6 A 30 mA; V /3.a: /8.7:C na versão MRL) -> LIHS1 -> XB 807, 809, 802 + PE (V /8, /46). 'History lighting' do Vitinho = iluminação da caixa de corrida (esquema 19060918-ZL pág. 2: 'QFB4 disjuntor da iluminação da caixa'). Cabo de campo do quadro a caixa A12: 4 condutores (807, 809, 802, PE) |
| P44 | PARCIAL | BB tem 4 pinos (V /21): RESOLVIDO. V /45: o barramento segue por ramais até cada HCB. BC não tem ramais por pavimento: V /48 só liga o interfone do poço (DC); esquema 19060918-ZL pág. 27 lista interfones de comando, portaria, topo, poço e cabina. Falta o trajeto físico |
| P45 | RESOLVIDO | V /23: ERB-A MQ+ <- FL1 (do RDZ, sensor normal de zona de porta) e MQ- <- 302; 'o fornecimento de emergência do teto alimenta os sensores de zona de porta'. Manual ERB-A1 EN: entrada MQ+ exige sensor ativo em nível alto; 24 V do ERB só para o sensor dele. Logo usa o FL1 do RDZ, não o DZ de nivelamento (HX9/HX10) |
| P46 | PARCIAL | F2 do KCB é de 4 A / 250 V 'Car fan/light curtain fuse' em série com 501/502 -> 507/508 (V /11), portanto o circuito não passa de 4 A no quadro (o manual da caixa aceita até 7 A, tomada 5 A). Bitola 0,75 contra 1,5 mm2: ampacidade não está nas fontes |
| P47 | PARCIAL | V /15: SCB-A4 (síncrona, porta única) com F6-52 BIT1 = 1; V /25 e manual CTW-B3 Nota 1 (pág. 11): F6-52 BIT6 = 1 para re-nivelamento/pre-abertura, FL1/FL2 chegam ao MCB pelo cabo de manobra. Nenhuma fonte diz se a CTW-B3 dispensa a SCB-A4: continua aberto |
| P48 | PARCIAL | PCB-D1 resolvido pelo Vitinho: J2 1 = L, 2 = N (207/208 via KY6, V /10); J3 1 = BK-, 2 = BK1+, 3 = BK2+, 8 = PE (V /13, /10); J4 1 = 301, 4 = 302, 2/5 = CAN+/CAN- (V /10, /24). FX = contator UVW (RESOLVIDO), X20 = sobretemperatura (RESOLVIDO). H3 'BC-1?' continua aberto |
| P49 | AINDA ABERTO | Sem fonte (depende do operador de porta comprado) |
| P50 | PARCIAL | Lado da caixa: confirmado pelo manual A02 pág. 5-6. Lado AD30: B1->DI1, B2->DI2, BM->COM (manual A02 fig. pág. 10 e padrao do boletim), B3->DI4 (boletim: DI4 'Forced door close signal'); X3->TC1, X5->TC2, 301->TA12 por função. Nenhuma fonte documenta a ligação CTW-B3 <-> AD30, então fica como correspondência de função |
| P51 | PARCIAL | Caixa: confirmado (manual A02 fig. pág. 10). AD30: DI3 e 'Light curtain signal' (boletim). Usar ou não é decisão de projeto |

## 4. Verificações de consistência interna

- Contagens que fecham: 12+12 = 24 sinais (II.3); 16+14 = 30 pinos; 12 cabos = 1 + 11 (IV.4); 12 -> 14 com AD30 (IV.8); 24+2 = 26 e +10% = 28,6 (IV.4); 48 = 24 x 2 (P29); +21% e +49% (II.11.3); I1 a I7 = 7 bornes; 108+4+13 = 125 fios.
- Contagens que não fecham: EY4 (12 sinais em II.4, 11 em II.8 K-4, 14 no Vitinho); COB (10 pinos, 7 em K-7, 8 em III.2/IV.4); AC/CC 'SGC' ok; FAN '6 pinos' (8 reais); EY3 '5 posições' (3 reais); CA 11 sinais em III.2 contra 12 em II.3.1.
- Códigos trocados ou duplicados: C-03a/C-03b (II.5) contra T-1/T-2 (II.8); 'COB-F1' em III.1; 'KCB 8P?' para BB (BB e 4P); 'Parte II.4' escrito 'Part II.4' em III.2; plugue DC12 em DC 4P e 'DC12V' no BC (mesmo sinal).
- Nomes diferentes entre revisões dos esquemas: caixa do poço 'MBT-PIB-A12/PIB-XX' no 19061867-ZL contra 'MBT-PIB-A22/A24/PSB-A12' no 19060918-ZL (págs. 27, 30, 34, 36); placa do teto 'CTB-H5' (manual) contra 'CTB-H6' (V /44, ESQ págs. 29 e 32). O livro segue o 19061867-ZL e o manual; não é erro, mas convem anotar.
- Sheet /25 do Vitinho rotula como 'CA' o conector que tem os pinos 3, 4, 7, 10 (301, 302, FL1, FL2), que são pinos do CB. O livro usa CB corretamente (confere com /21 e /38).

## 5. Fontes que não puderam ser usadas

- Catalogo_Cabos_e_Chicotes_BST_2020.pdf e Desenho_Explodido_Cabos_Modulares_2024.pdf: PDFs escaneados sem texto; precisariam de OCR para resolver P22, P29 e P35.
- Manual do encoder seno/cosseno EI53C9.25 e catálogos de botoeiras BST: não abertos neste lote (P25 lado do encoder, P28).
- Lista de materiais, Estrutura VPEL-704a, CSV de estrutura e NBR 16858 / EN 81-20: fora das fontes do lote.
