# Auditoria lote 7a: Livro do Quadro NICE3000 Rev. 11, págs. 7 a 35

Escopo: págs. PDF 7 a 35. Nenhum arquivo existente foi alterado.

## Legenda das fontes

- NICE Pn: manual NICE3000new (368 págs.), página do PDF (marcador P). Ex.: Tab. 1-1 está em P30.
- ERB Pn: manual da ERB-A em inglês (3 págs. PDF); o chinês foi consultado só para BAT/BPQ e bateria.
- VIT /n: Vitinho 19061867-ZL, folha n do carimbo (PDF = n+2).
- VP n: esquema Verticalparts 19060918-ZL, página do PDF (37 págs.; o carimbo mostra outra numeração, ex.: PDF 13 = "pág. 21 de 58"). O livro usa essa convenção e ela fecha.
- lote2, lote3: auditorias anteriores da Lista (auditoria/lote2_kcb.md, lote3_contatores_resgate.md).
- Resultados: CONFIRMA (com ressalva quando indicado), CONTRADIZ, NÃO VERIFICÁVEL.

## Tabela de afirmações

| # | Pág. livro | Afirmação | Resultado | Evidência | Conf. |
|---|---|---|---|---|---|
| 1 | 7 | Fluxo POP-ISO-PCP: Produção monta, Automação testa, Qualidade inspeciona e libera | CONFIRMA | POP-ISO-PCP rev 00 (14/09/2026): âmbito (montagem, testes pela Automação, inspeção e liberação pela Qualidade) e fluxo Produção > Testes > Qualidade > Liberação | alta |
| 2 | 7 | Cada fio da Lista aparece duas vezes nas tabelas por peça | CONFIRMA | Recontagem das págs. 16 a 31: 250 linhas = 125 fios x 2; cada nº aparece 2 vezes, com mesma cor, bitola, comprimento, terminais invertidos e bornes espelhados | alta |
| 3 | 7 | KCB girada 180° (esquema pág. 14); pino 1 do KY1 na ponta direita [Certeza: foto] | NÃO VERIFICÁVEL | VP 14 existe e é o desenho da KCB, mas a orientação real só consta em foto | - |
| 4 | 7 | Mesma regra de rotação nos demais conectores [Provável] | NÃO VERIFICÁVEL | Só o ponto de pino 1 impresso na placa decide | - |
| 5 | 7 | Numeração: 101-199 = 110 V CA; 201-299 = 220 V CA; 501-599 = 220 V CA iluminação da cabina; 801-810 = poço; 301/302 = 24 V CC | CONFIRMA | VIT /4 (PDF 6), regras de nomeação de fio | alta |
| 6 | 7 | Citação "Vitinho p. 4-5" para essa numeração | CONTRADIZ | Numeração e tabela de cores estão só na folha /4 (PDF 6). A /5 (PDF 7) é lista de parâmetros; PDF 4-5 é lista de peças. Erro de citação | alta |
| 7 | 7 | ERB e KCB POW1 usam 501/502 | CONFIRMA | VIT /11 (PDF 13) POW1/1 = 501, POW1/2 = 502; VIT /23 (PDF 25) ERB em 501/502 | alta |
| 8 | 7 | CAN+/CAN- = KCB e PCB-D1; MOD+/MOD- = botoeiras de andar | CONFIRMA | VIT /24 (PDF 26) KY12/1-2 para J4/2,5 (o CAN também vai ao AB, SCB e MSC); VIT /12 (PDF 14) BB/3-4 = MOD+/-; NICE P61 MOD± = RS485 de chamadas | alta |
| 9 | 7 | Tabela de cores da Inovance na folha /4 (preto, azul N, verde-amarelo PE) | CONFIRMA | VIT /4 (PDF 6) tabela de cor de cabo. Decisão de não seguir é da empresa (NV) | média |
| 10 | 7 | Conectores de campo AA, AB, BA, BB, MT têm mais pinos que a Lista usa | CONFIRMA | VIT /11 a /13 e /21 (PDF 23): AA até 16, BA 10, BB 4, MT 12 | alta |
| 11 | 7 | Esquemas 19060918-ZL (2022-10-11) e 19061867-ZL (2023-07-18) | CONFIRMA | Carimbos: VP 2022-10-11 A00; Vitinho capa 2022/10/10, folhas 2023/7/18, A00 | alta |
| 12 | 8 | Só P1, P2 e P3 bloqueiam energização | CONFIRMA | Coerente com capa, pág. 12 e pág. 32 (consistência interna) | alta |
| 13 | 9 | Corrente de entrada: 4007 = 20,5 A; 4015 = 36 A; 220-4015 = 36 A; 220-4022 = 49 A | CONFIRMA | NICE Tab. 1-1 (P29-P30) | alta |
| 14 | 9 | 7,5/380 = 4007; 15/380 = 4015; 7,5/220 = 220-4015; 15/220 = 220-4022 | CONFIRMA | NICE Tab. 1-1, tabela trifásica 220 V e 380 V (P30) | alta |
| 15 | 9 | Resistores 75 ohm/2500 W; 40/4500; 25/4500; 13/4500 | CONFIRMA | NICE Tab. 3-12 (P99-P100): 85-65 ohm 2500 W; 43-35 ohm 4500 W; 26-22 ohm 2500 W; 13,0-12,5 ohm 4500 W. Todos dentro da faixa | alta |
| 16 | 9 | Contatores CWB25 / CWB40 / CWB40 / CWB50 | CONFIRMA | NICE Tab. 3-2 (P87-P88) contator recomendado 25, 38, 38, 50 A (compatível). Marca WEG sem datasheet | média |
| 17 | 9 | Disjuntor QF C50 / C50 / C50 / C70 | CONTRADIZ | NICE Tab. 3-2: recomendado 32 A (4007), 50, 50 e 80 A (220-4022). C70 em 15 kW/220 V fica abaixo do recomendado; C50 em 7,5/380 fica acima | média |
| 18 | 9 | Cabo de potência 6 mm² e 10 mm² (15/220) | CONFIRMA | NICE Tab. 3-2: 4 mm² (4007), 6 mm² (4015 e 220-4015), 10 mm² (220-4022) | alta |
| 19 | 9 | Cabo terra 6 e/ou 10 mm² por variante | CONFIRMA | NICE Tab. 3-2 terra 4/6/6/10 mm² e Tab. 2-8 (P54). Erro interno: Compilado lista 6 e 10 mm² juntos em 7,5/380 e 7,5/220, a Lista usa um PE de potência só (6*, 160 cm) | média |
| 20 | 9 | PCB-D1 48 a 207 Vcc | CONFIRMA | VP 5 e VIT /13 | alta |
| 21 | 9 | VPB-383 flat de 40 pinos | CONFIRMA | VP 13 (40 rótulos) e VP 14 (J10, 40 vias) | alta |
| 22 | 9 | Trafo VPMP-898 220 para 110 V, 150 VA | CONTRADIZ | VIT /10 (PDF 12): TRF 63 VA (3,7 a 22 kW), primário 220V/0P, secundário 125V/0S. 150 VA cobre; "110 V" x "125 V" ver P3 | média |
| 23 | 9 | DR 2P RDWS-AC-30-25-2 x3 e minidisjuntor 1P C6 x3 como QFB/DQFB | NÃO VERIFICÁVEL | Sem catálogo. VIT /8 e /10: QFB3 e QFB4 = DR 2P 6 A 30 mA tipo D; QFB1 = 1P+N 10 A C; QFB2 = 2P 6 A C; DQFB não existe | média |
| 24 | 9 | Bornes BTWP-35: 7/7/6/6; cabo azul: nenhum/1/1/1 | CONFIRMA | Interno: consistente com P2 e com o quadro de corte (2 fios azuis na Lista) | alta |
| 25 | 9 | Blocos de contato NA x13 / NF x4 | NÃO VERIFICÁVEL | Erro interno provável: setas 4 NA + vermelhos 2 NA + comutadores 4 NA e 4 NF + cogumelo 1 NF = 10 NA e 4-5 NF. Conferir no Compilado | baixa |
| 26 | 9 | VPMP-867 aparece como "BC-A" (págs. 9 e 27) e como "BC-1" (págs. 7, 8, 10) | CONTRADIZ | Erro interno de código/tag; o esquema não tem esse bloco (VIT lista de peças) | média |
| 27 | 9 | Cabos (parêntesis) provavelmente em metros | CONFIRMA | Indireto: 1,5 e 1,6 só fazem sentido em metros; 1,6 = PE de 160 cm (#124); 6 mm² Lista 11,0 m x Compilado 14 | média |
| 28 | 10 | Caixa ~1350 x 450 x 350 mm | CONTRADIZ | DES-FURACAO_QDC-1350x350x240-R04 (citado pelo livro): "Painel elétrico 1350x350x240" | média |
| 29 | 10 | CN2: XCM X25 X26 X27 X28 XCM | CONFIRMA | NICE Tab. 2-15 (P61); VIT /16 (PDF 18) | alta |
| 30 | 10 | CN3: X23 X24 N AI+ MOD- MCM CAN | CONTRADIZ | NICE P60-P61: X23, X24, AI-M, AI+ são do CN9; CN3 = +12V, MCM, M24, MCM, MOD+, MOD-, CAN1+, CAN1-. Transcrição de foto | baixa |
| 31 | 10 | Bornes do inversor PE R S T (+) PB U V W | CONFIRMA | NICE P52, P55 (Fig. 2-15); VIT /9 | alta |
| 32 | 10 | Potência XA > QF > inversor > SW > TA | CONFIRMA | VIT /8 e /9 (PDF 10-11) | alta |
| 33 | 10 | Primário do trafo vem dos 207/208 (KY8/1, KY8/2) | CONFIRMA | VIT /10 (PDF 12) | alta |
| 34 | 10 | Botoeira para KY4: 10 fios | CONFIRMA | KY4 usa 10 pinos (págs. 17 e 19); VIT /14 (PDF 16) | alta |
| 35 | 10 | ERB: 501/502 de QFB3/DQFB3; "ERB para SZ e SW" | CONTRADIZ | 501/502 correto. ZQ vai ao plugue MT1 (pinos 5, 6, 11, 12), não ao SZ/SW: VIT /23 e VP 16 (ver lote3) | média |
| 36 | 10 | Ref. "ver «Conectores da KCB»" | CONTRADIZ | Seção com esse título não existe; o real é "Conectores de MCTC-KCB-B4A e pinos usados" (pág. 17) | alta |
| 37 | 10 | Ordem Z1 a Z6 fotografada [Certeza]; posições aproximadas [Provável] | NÃO VERIFICÁVEL | Só fotos | - |
| 38 | 11 | Torques 0,565 / 2,5 / 4,0 N·m "tab. 2-9" | CONFIRMA | 2,5 N·m (4007/4015) e 4,0 N·m (10 mm²): NICE Tab. 2-9 (P56). 0,565: Tab. 2-17 (P63), não 2-9 (citação errada) | alta |
| 39 | 11 | Descasque de 6 mm nos bornes de controle | CONFIRMA | NICE Fig. 2-22 (P63) | alta |
| 40 | 11 | Pulseira antiestática [Provável: não consta nos documentos] | CONTRADIZ | Consta: NICE P20 e P83 (procedimento ESD e pulseira); ERB P3 (Wiring, CAUTION) | alta |
| 41 | 11 | Megôhmetro: critério PREENCHER (POP não define) | CONFIRMA | POP sem critério de isolamento; NICE sem valor de megôhmetro | média |
| 42 | 11 | Parâmetros B0-00, B0-01, B0-02 da PCB-D1 | CONFIRMA | VP 5, VIT /13. Lacuna: B0-03 (fonte de 24 V: 1 = 24 V, 2 = 26 V, 3 = 28 V, 4 = 30 V; VIT /10) | alta |
| 43 | 11 | Esquema elétrico com 37 págs. | CONFIRMA | PDF 19060918-ZL tem 37 páginas (carimbo diz 58) | alta |
| 44 | 11 | Lista de tags existentes | CONTRADIZ | Omite +CC-FL1, +CC-DC12, +CC-133 e +CC-131 (fios #35, #32, #36, #37, pág. 19) | alta |
| 45 | 11 | 10% de reserva [Chute]; P13 manda recalcular "com 10% (P13 do PCP)" | NÃO VERIFICÁVEL | POP não contém "10%" nem "P13". Um [Chute] virou instrução em P13 | média |
| 46 | 11 | Mini-Fit 4,2 mm, abraçadeiras 160x2,5 (30), MA4x16 (11), MA5x8 (22), rebites 12x4 (16), Allen 4 mm | NÃO VERIFICÁVEL | Itens de BOM/catálogo sem fonte de fabricante na pasta | - |
| 47 | 12 | Chapas VPMP-895 (botoeira) e VPMP-896 (KCB, M4) | CONFIRMA | PRT-BOTOEIRA: VPMP-895, 8x Ø22. PRT-CHAPA_PCB_B4A: VPMP-896, 7x M4x0,7. Comprimento 10 mm do espaçador NV | média |
| 48 | 12 | Potência, FX e resistor (+/PB) | CONFIRMA | VIT /9 (PDF 11); NICE P52-P53 | alta |
| 49 | 12 | Sem curto 207-208, 201-202, 501-502, 301-302: "sem continuidade" | CONTRADIZ | VIT /10: primário do trafo (220V/0P) está entre 207/208 e 201/202 chegam a 207/208 por OVP/F1: com tudo aberto ainda há enrolamento (não é circuito aberto). 301-302 liga a PS-24V da PCB-D1 | média |
| 50 | 12 | Resistência de PE: PREENCHER (p.12) x "abaixo de 4 ohm" (p.34) | CONTRADIZ | Páginas divergem; NICE P54: aterramento do circuito principal < 10 ohm | média |
| 51 | 12 | Jumper no S1 e nenhum no S2 [Certeza: esquema pág. 8] | CONFIRMA | VP 8 e VIT /16 (PDF 18): normal = S1 ON, S2 OFF | alta |
| 52 | 12 | Trafo 220V/OP e 125V/0S | CONTRADIZ | VIT /10 grafa 0P (zero P). "OP" é transcrição; a ref. "/42.6:E" (pág. 31) é a folha de inspeção do poço, onde há outro rótulo OP | média |
| 53 | 13 | 125 fios: 108 de 0,75, 4 de 2,5, 13 de 6 mm² | CONFIRMA | Soma das 48 linhas: 97+2+9 = 108; 4; 12+1 = 13 | alta |
| 54 | 13 | Σ comprimentos por grupo (1,18; 63,65; 5,21; 0,96; 9,39; 1,60 m) | CONFIRMA | Recalculado do quadro de corte: bate nos 6 grupos | alta |
| 55 | 14 | Σ 11,0 m (6 mm²) e 70,0 m (0,75); Compilado 14 e 80 | CONFIRMA | 9,39+1,60 = 10,99; 1,18+63,65+5,21 = 70,04; 75+4+1 = 80 | alta |
| 56 | 8/13 | Pontas: Faston 1, Forquilha 16, Mini fit 65, Olhal 1, Tubular 142, Tubular duplo 25 | CONFIRMA | Somadas do quadro de corte; cada linha tem pontas = 2 x fios | alta |
| 57 | 8/9 | P13 omite: tubular 6 mm² | CONTRADIZ | Lista usa 19 pontas tubulares de 6 mm² (3+3+12+1); BOM VPMP-393 = 16 (faltam 3). Tubular duplo 6 mm²: 3 no Compilado, 0 na Lista | alta |
| 58 | 8/13 | Dois fios >= 150 cm (P18) | CONFIRMA | 160 cm (#124) e 157 cm (#123) | alta |
| 59 | 15 | Flat 1:1 da MCB-C3 para a KCB, X1...MOD1- | CONFIRMA | VP 13 (linhas 1:1) e VP 14 (J10 na KCB); VIT /20 (PDF 22) | alta |
| 60 | 15 | 22 X + 7 W + 11 = 40 pinos; M24+MCM+MCM+MCM+12V = 5 pinos em 9 linhas | CONFIRMA | VP 13: 22 X, W1 W2 W2A W3 W4 W5 W6, +24V W7 M24 MCM x3 +12V CAN- CAN+ MOD1+ MOD1- = 40 | alta |
| 61 | 15 | X1-X11, X14, X18, X20-X22 conforme tabela do esquema | CONFIRMA | VP 13 (tabela PT e rótulos EN), VIT /20 e /21 | alta |
| 62 | 15 | X15 = "subida 2"; X16 = "descida 1"; X17 = "descida 2" | CONTRADIZ | VIT /44 (PDF 46): BD/3 = ULS1 (X14), BE/3 = DLS1 (X15), BD/4 = ULS2 (X16), BE/4 = DLS2 (X17); VIT /20, /21 e F5-14 a F5-17 (VIT /5) idem. A ordem do livro (copiada da tabela PT do VP 13) troca X15 e X16 | alta |
| 63 | 15 | X12 e X13 "Limite de parada superior/inferior (Não usado)" | CONTRADIZ | VIT /20 e /21: X12 = Emergency leveling signal, X13 = Reserved; F5-12/13 = 0. "Não usado" confere, o nome não | média |
| 64 | 15 | W1 = Brake contactor output; W2 = brake 1; W3 = UVW short | CONTRADIZ | Legenda EN do VP 13/VIT /20 diz isso, mas VIT /21 e VP 14 dizem Y1 = Run contactor (SW), Y2 = brake 1 (BY), Y3 = UVW short (FX), e a KCB liga Y1 ao SW (VIT /17). Legenda de W1 não bate com o uso | média |
| 65 | 15 | X4 = KCB S1/5 (esquema pág. 6) | CONFIRMA | VP 6 e VIT /14: S1/4 = 301, S1/5 = X4 | alta |
| 66 | 15 | X9, X10, X11 = KY4/4, KY4/3, KY4/2 = CIS 2, CIU 4, CID 4 | CONFIRMA | VP 6; VIT /14 | alta |
| 67 | 15 | X18 = MT/1; X22 = MT/2 | CONFIRMA | VP 5; VIT /13 | alta |
| 68 | 15 | CAN- = KY12/2 = J4/5; CAN+ = KY12/1 = J4/2; MOD1± = BB | CONFIRMA | VIT /24; VIT /12 | alta |
| 69 | 15 | W1..W6 passam pelos blocos Y1..Y7 | CONFIRMA | VP 13: W1, W2, W2A, W3, W4, W5, W6 por Y1, Y2, Y2A, Y3, Y4, Y5, Y6; W7 por Y7 (Y7 "Reservado") | alta |
| 70 | 15 | LEDs acesos X4, X6, X7, X12, X14, X15 em inspeção fora da zona de porta | CONFIRMA | VP 13 (texto do desenho) | alta |
| 71 | 16 | FX nos terminais 2,4,6 do SW (FX 22, 32, 21), curto das fases | CONFIRMA | VIT /9 (PDF 11) e lista de peças "U.V.W short contactor" | alta |
| 72 | 16 | Resistor em (+) e PB, modelos < 37 kW [Certeza: manual] | CONFIRMA | NICE P52-P53 (cabo < 5 m; nunca no barramento CC); VIT /9 | alta |
| 73 | 16 | QFB3 ligado antes do QF | CONFIRMA | VIT /8 (PDF 10): derivação acima do QF e aviso "after disconnecting QF voltage remains in QFB3/4" | alta |
| 74 | 16 | 4007: 4 mm², 2,5 N·m, GTNR4-5; 4015: 6 mm², 2,5, GTNR6-5 | CONFIRMA | NICE Tab. 2-9 (P56) | alta |
| 75 | 16 | Linhas 220 V por corrente (6/2,5/GTNR6-5 e 10/4,0/GTNR16-6) [Provável] | CONFIRMA | Cabo confirmado: NICE Tab. 3-2 (P87-P88) 220-4015 = 6 mm², 220-4022 = 10 mm². Torque e terminal só existem para linhas 380 V (NV). 220-4022 é estrutura metálica 554,5x289,6x207,7 mm, 14,5 kg (Tab. 2-3, P43) | média |
| 76 | 16 | Controle: 0,2-0,75 mm², 0,565 N·m, descasque 6 mm | CONFIRMA | NICE Tab. 2-17 e Fig. 2-22 (P63) | alta |
| 77 | 8/16 | P1 cita NICE "tab. 1, linhas 1811-1815" | CONTRADIZ | Nº de linha não reproduzível: no texto extraído a Tab. 1-1 trifásica 220 V está nas linhas 1394-1405 (PDF P30). Citar tabela e página | média |
| 78 | 16 | CN2: XCM1>KY1/6[102]; X25>KY1/1[130]; X26>KY1/4[131]; X28>KY1/3[133]; X27>KY1/2[134]; XCM2>SW A2[102] | CONFIRMA | VIT /16 (PDF 18) e /19 (PDF 21); VP 8 | alta |
| 79 | 16 | CN2 = entradas de tensão alta "do circuito de bypass de portas" | CONTRADIZ | NICE P61: 110 VAC do circuito de segurança e de fechaduras. VIT /5: X25 = segurança, X26 = curto porta 1, X27 = fechaduras, X28 = curto porta 2. Não é só bypass | alta |
| 80 | 16 | Encoder PG-E fora da Lista (esquema pág. 3) | CONFIRMA | VP 3 e VIT /9 | alta |
| 81 | 17 | PCB-D1 = freio 48-207 Vcc; CAN por KY12/J4 | CONFIRMA | VP 5, VIT /13. Lacuna: a PCB-D1 também gera os 24 V (PS-24V 7 A, VIT /10) | alta |
| 82 | 17 | Pinos usados por conector (17 na KCB, 3 na PCB-D1) | CONFIRMA | Recontagem págs. 18 a 21: todos batem (59 pinos na KCB) | alta |
| 83 | 17 | Carcaças do BOM 2, 4, 6, 8, 10, 12, 16 vias (14 vias: 0) | CONFIRMA | Consistente com pág. 9 | alta |
| 84 | 18 | Sete jumpers de 9 cm "fecham a cadeia de segurança onde não há cabo" [Provável] | CONTRADIZ | Só #61 (BA/8-9) e #67 (AA/6-14) existem no desenho (VIT /19, notas single door). HW/3 = rede 110 e AA/4 = 130: #64 curto-circuita a cadeia entre MES e X25; #65 anula GS1/GS2; #66 une 131A e 133; #62/#63 ligam X14/X15 (ULS1/DLS1, VIT /44) à 301. Ver lote2 | alta |
| 85 | 21 | POW1 1 = 501, 2 = 502; BB = 301, 302, MOD+, MOD- | CONFIRMA | VIT /11, /12 | alta |
| 86 | 21 | MT: 1 X18; 2 X22; 5 ZQ1+; 6 ZQ2+; 7 e 8 = 301; 11 ZQ1-; 12 ZQ2- | CONFIRMA | VP 5; VIT /13 | alta |
| 87 | 21 | S1/S2: S1 normal; embaixo do S2 cabina; em cima pavimento | CONFIRMA | VP 8 (texto). Mapa top/bottom x pinos 1-5/2-6 do VIT /16 não verificado | média |
| 88 | 21 | KY11/5 = 133 > SZ 13; KY11/6 = 131 > SZ 23 (esquema pág. 10) | CONFIRMA | Redes: VIT /23 e VP 16 (SZ 2 e 7). Citação errada: VP 10 só tem KY11/1-2 (122/122A). Numeração SZ do esquema (1-9) difere da da Lista | média |
| 89 | 21 | AA/AB cabo de manobra pág. 25; BA poço pág. 30 | CONFIRMA | VP 25 = segurança do carro; VP 30 = segurança no poço | alta |
| 90 | 21 | PCB-D1: 48-207 Vcc, padrão 110; 6 A impacto, 4 A manutenção; B0-01 <= B0-00; B0-02 0-5 s padrão 3 s; ajuste por celular ou botão 5 s | CONFIRMA | VP 5 e VIT /13 | alta |
| 91 | 21 | J4 = "24 V e CAN" | CONFIRMA | VIT /10: J4/1 (301) e J4/4 (302) são saídas da PS-24V; CAN em J4/2 e J4/5 | alta |
| 92 | 22 | Bateria dentro da ERB-A1, 12 V, >= 7 Ah | CONFIRMA | ERB P1 (A1 = com bateria) e P2 (chumbo-ácido 12 V >= 7 AH) | alta |
| 93 | 22 | Entrada 187-253 V (coluna "manual ERB / Vitinho /23"); R3 usa 187-253 | CONTRADIZ | ERB P1 Tab. 1: 220 VAC (-15% a +10%) = 187 a 242 V. 253 V só pode ser da etiqueta (foto) | alta |
| 94 | 22 | Etiqueta: saída 110 V CC 4,0 A | CONFIRMA | ERB P1: 110 V partida, 80 V mantida, 4 A máx | alta |
| 95 | 22 | Avisos: 10 min, disjuntor, vermelho +, lado direito para baixo, 12 h, testar a cada 6 meses | NÃO VERIFICÁVEL | Manual confirma 12 h, recarga semestral, vermelho + preto -, troca a cada 2 anos (ERB P2). "10 min", "lado direito" e "testar" só na etiqueta | média |
| 96 | 22 | Bornes MS, MQ, COM, 24V, ZQ, L, N | CONFIRMA | ERB P1-P2. O manual usa ZQ1+ e ZQ2-; MQ+ é entrada de nível alto e MQ- de nível baixo (sinal ao COM), não um par +/- | média |
| 97 | 22 | MS+/MS- curto se não usado; sem trava fechada a ERB não libera | CONFIRMA | ERB P2 | alta |
| 98 | 22 | 24V/COM só para o sensor da ERB, <= 300 mA | CONFIRMA | ERB P1 Tab. 1 e tabela de bornes | alta |
| 99 | 22 | MQ+ vem de FL1 pela KY10/8 | CONFIRMA | VIT /23 | alta |
| 100 | 22 | BPQ+/BPQ- não consta no manual [Chute: bateria] | CONFIRMA | Manuais EN e CN: bateria = BAT+/BAT-; sem BPQ. O chute segue sem prova | média |
| 101 | 22 | LEDs verde, vermelho, amarelo, azul | CONFIRMA | ERB P2 | alta |
| 102 | 22 | 110 V por 2 s, 80 V por 120 s, 3 vezes, espera 10 min | CONFIRMA | ERB P2 (80 V "até 120 s") | alta |
| 103 | 22 | 4 A = bobina >= 27,5 ohm | CONFIRMA | Derivado: 110/4 = 27,5; manual só dá 110 V e 4 A | alta |
| 104 | 22 | Sobrecarga >= 4,5 A bloqueia 1 min; curto >= 6 A 5 min; < 10,2 V | CONFIRMA | ERB P1: valores de partida (sobrecarga com >= 200 ms). Omite 3,5 A (sobrecarga) e 4,5 A (curto) na tensão mantida. Abaixo de 10,2 V não libera o freio | alta |
| 105 | 22 | Partida 1 s liga bateria 3 min; Partida+Comum fora da zona; Forçado+Comum na zona; carga 12 h; recarga 6 meses; troca 2 anos | CONFIRMA | ERB P2 | alta |
| 106 | 22 | Operação: tirar SZ1, pôr SZ2; MT no MT1; voltar ao final | CONFIRMA | VP 16 (passos 1, 2, 6) | alta |
| 107 | 22 | ERB: L = 502 e N = 501 (Lista) | CONTRADIZ | VIT /23 e VP 16: 501 no borne L, 502 no N | alta |
| 108 | 23 | Chapa VPMP-895 com 8 furos Ø22, passo 50 x 30 mm | CONFIRMA | PRT-BOTOEIRA: 8x Ø22, 4 colunas a 50 mm, 2 linhas (cotas 30 e 60) | alta |
| 109 | 23 | KY4/1 301>CIS 1; /4 X9>CIS 2; /3 X10>CIU 4; /2 X11>CID 4; /12 101A>MES 2; /9 110>MES 1; /8 118>CIS 14; /10 122B>CIS 12; /11 123>CIS 11; /7 125>CIU 13 | CONFIRMA | VIT /14 (PDF 16). Cadeia flui 101A > MES > 110: "entrada/saída" do MES depende do ponto de vista | alta |
| 110 | 23 | Ponte CIS 4 > CIU 3 > CID 3; CIS 3 em 301 | CONFIRMA | VIT /14; VP 6 | alta |
| 111 | 23 | Contatos 13/14 de CIS/CIU/CID e 11/12 do CIS na cadeia 125/118 e 122B/123 | CONFIRMA | Só VIT /14 mostra. VP 6 NÃO mostra (125/118 só por CIS 13/14; 122B e 123 ligados direto): prova que as revisões diferem (P20) e que a Lista segue o Vitinho | alta |
| 112 | 24 | CIU/CID 3/4 e 13/14 NA; MES NF | CONFIRMA | VIT /14 simbologia; MES 1NF no BOM. NA/NF dos 13/14 sem ficha | média |
| 113 | 24 | Chapa da botoeira PE ligada à ERB PE | NÃO VERIFICÁVEL | Esquema não mostra PE na ERB; ERB não documenta borne PE | média |
| 114 | 25 | QF 3P | CONTRADIZ | VIT /8 desenha QF com 4 polos (1 a 8; N pelo 7/8). BOM é 3P | média |
| 115 | 25 | QFB3: 501 = fase (1P), 502 = neutro | CONFIRMA | VIT /8: pino 1 na linha R, pino 3 na linha N; saídas 2 = 501, 4 = 502 | alta |
| 116 | 25 | QFB2 > 201/202 > KY5/1, KY5/5, TIS 13, XB 202 | CONFIRMA | VIT /10 e /22 (PDF 24) | alta |
| 117 | 25 | TRF 125V/0S > QFB1 > 101B/102 > KY5/8 | CONFIRMA | VIT /10 | alta |
| 118 | 25 | QFB1-3 = DR e DQFB = mini [Provável] | CONTRADIZ | VIT lista de peças: QFB1 breaker 10 A, QFB2 breaker 6 A, QFB3 e QFB4 RCD; DQFB não existe no esquema | média |
| 119 | 27 | SW = contatora do motor (Run), 53/54 e 73/74 em BK1+/BK2+ [Certeza] | CONFIRMA | VP 5; VIT /13, /17 | alta |
| 120 | 27 | BY = contatora do freio; 1-2, 3-4, 5-6 em série no BK-; jumpers 2>4 e 3>5 | CONFIRMA | VP 5; VIT /13 | alta |
| 121 | 27 | FX = contator de curto U,V,W [Provável]; 21,22,31,32; X8 = feedback | CONFIRMA | VIT lista de peças (/17.4:D), VIT /9, /17; VP 3. Bitola 2,5 mm² NV | alta |
| 122 | 27 | Bobinas SW KY2/1, BY KY2/2, FX KY2/3; A2 em 102; X6 NC, X7 NC, X8 NA | CONFIRMA | VIT /17 (PDF 19); F5-06 = 38 NC, F5-07 = 39 NC, F5-08 = 30 NA (VIT /5) | alta |
| 123 | 27 | Candidatos impressos [Chute]; BFB-22 (53/54, 61/62, 71/72, 83/84) | NÃO VERIFICÁVEL | Sem datasheet WEG/Frotal. O esquema exige NA em 73/74 (VP 5; VIT /13), logo o par escolhido deve ser NA | - |
| 124 | 29 | XA R,S,T,N; TA U,V,W; XB 202/203/205 (202 duplo); S1 14/24 > 203/205 | CONFIRMA | VIT /8, /9, /22 | alta |
| 125 | 29 | S1 (Lista) e TIS "Provável bypass/chave" | CONTRADIZ | VIT /22 (PDF 24) e lista de peças: TIS e S1 = chaves de acionamento e liberação remota do limitador de velocidade. A tag S1 do bypass é conector da KCB | alta |
| 126 | 30 | S1 13<TIS 14; S1 14>XB 203; S1 23<TIS 14; S1 24>XB 205; TIS 13<201 | CONFIRMA | VIT /22 | alta |
| 127 | 29 | SZ 1,2,3,4,13,14,23,24,33,34 (redes) | CONFIRMA | VIT /23: SZ 1 = 101B, 6 = 101, 4 e 9 = 302, 5 = FL1, 3 = DC12, 8 = T02, 2 = 133, 7 = 131; DC12 e T02 unidos pelo SZ2 (3-8), coerente com SZ 33/34. A Lista liga COM, MQ-, MQ+ direto na KY10, o esquema passa pelo SZ2. Numeração física NV | média |
| 128 | 31 | Trafo classe F; PE por faston | NÃO VERIFICÁVEL | Sem fonte | - |
| 129 | 32 | E1 rede 380 V ou 220 V | CONFIRMA | NICE Tab. 1-1: 380-440 V e 220-240 V | média |
| 130 | 32 | E3 201-202 e E4 207-208 = 220 V [Provável] | CONFIRMA | VIT /4 (201-299 AC220V); VIT /10: 207/208 vêm de 201/202 por OVP e F1 | alta |
| 131 | 32 | E6 301-302 = 24 Vcc, KCB > PCB-D1 J4 | CONTRADIZ | Valor certo, sentido errado: a PS-24V está na PCB-D1 e J4/1, J4/4 alimentam KY3 da KCB (VIT /10). Ajustável 24-30 V (B0-03) | alta |
| 132 | 32 | E7 BK1+/BK2+/BK-: 110 Vcc padrão, 48-207 [Certeza] | CONFIRMA | VP 5; VIT /13 | alta |
| 133 | 32 | E8 501-502 = 220 V [Provável; P2] | CONFIRMA | ERB P1 (220 VAC); VIT /8, /11 | média |
| 134 | 32 | E10 LEDs X4 X6 X7 X12 X14 X15 [Certeza] | CONFIRMA | VP 13 | alta |
| 135 | 33 | R1 12 h; LED amarelo fixo = cheia; pisca lento = carregando | CONFIRMA | ERB P2 | alta |
| 136 | 33 | R3 187-253 V | CONTRADIZ | ERB P1: 187-242 V | alta |
| 137 | 33 | R4 azul "conforme zona de porta" | NÃO VERIFICÁVEL | ERB P2 só define o azul como posição quando faltou a rede | média |
| 138 | 33 | R5/R6 ZQ ≈ 110 V por 2 s e 80 V; SZ1>SZ2; MT>MT1 | CONFIRMA | ERB P2; VP 16 | alta |
| 139 | 33 | Vitinho PDF p. 7-8 = parâmetros e ajuste | CONFIRMA | VIT PDF 7 = /5 parâmetros; PDF 8 = /6 ajuste | alta |
| 140 | 34 | CAN+ a CAN- ≈ 60 ohm (120 ohm x2) [Certeza] | CONFIRMA | NICE P73 (valor normal ~60 ohm); P71 terminadores de 120 ohm | alta |
| 141 | 34 | MOD+ a MOD- ≈ 60 ohm [Provável] | CONFIRMA | NICE P71: RS485 normal ~60 ohm; < 50 ohm revisar as pontas | alta |
| 142 | 34 | CAN/MOD contra terra próxima de infinito [Provável] | CONFIRMA | Parcial: NICE P73 diz COMs ligados entre si e não ao aterramento do sistema | média |
| 143 | 34 | Continuidade à terra < 4 ohm [Provável] | CONTRADIZ | NICE P54: < 10 ohm | média |
| 144 | 34 | Isolação à terra próxima de infinito [Provável] | NÃO VERIFICÁVEL | NICE sem valor de megôhmetro | - |
| 145 | 34 | Trafo 380 V +-15%; saídas 110 VCA, 220 VCA e 110 VCC +-5% | CONTRADIZ | Neste quadro: trafo só 125V/0S > QFB1 > 101/102; 220 V vem de QFB2 (R-N); 110 VCC vem da PS-110V da PCB-D1 (VIT /10). NICE: 380-440 V | alta |
| 146 | 34 | Relé de fase PFR, contator da cadeia e das fechaduras | CONTRADIZ | Não existem no Vitinho; a cadeia chega por X25-X27 (NICE P61, VIT /19). O livro já avisa | alta |
| 147 | 35 | Desaceleração = v²/(2 x 0,9) | CONFIRMA | NICE P76: L > V²/(2 x F3-08), F3-08 padrão 0,9 m/s² | alta |
| 148 | 35 | 0,75 m/s = 0,31 m; 1,0 = 0,56; 1,5 = 1,25 | CONFIRMA | Aritmética correta; NICE Tab. 2-19 (P76) recomenda 0,4; 0,7; 1,5 m (>= fórmula) | alta |
| 149 | 35 | Chave de limite a 100 mm [Provável] | CONTRADIZ | NICE P77: 30 a 50 mm. VIT /5 nota: limites por software (F6-40 Bit1), chaves de limite dispensáveis | alta |
| 150 | 35 | Fim de curso final a 100-150 mm [Provável] | CONFIRMA | Parcial: NICE P77 "normalmente 150 mm" | alta |
| 151 | 35 | Chave 2 a partir de 1,5 m/s (3,2 m); chave 3 a partir de 2,4 m/s (8,0 m) [Provável] | CONTRADIZ | NICE Tab. 2-19: chave 2 a partir de 2 m/s (2,5 m), chave 3 a partir de 3 m/s (6 m); até 1,75 m/s só a chave 1 | alta |
| 152 | 35 | Posição da chave 1: "1,3 m - L/2" inválido; vale a fórmula como mínimo [Chute] | CONFIRMA | NICE Tab. 2-19: 0,4 m (0,75 m/s), 0,7 m (1,0), 1,5 m (1,5); tolerância +-0,1 m (1 a 2 m/s) | alta |
| 153 | 35 | Bandeiras 80-200 mm, mesmo comprimento, na vertical [Provável] | CONFIRMA | NICE P74 (80 <= D <= 200), P75, P174 (mesmo comprimento, desvio < 5 mm) | alta |
| 154 | 35 | "Aceita de 1 a 3 sensores de nível" | CONTRADIZ | NICE P75: suporta 4 chaves de nivelamento (Tab. 2-18) | alta |
| 155 | 35 | Abertura antecipada: duas chaves e bandeira maior [Certeza] | CONFIRMA | NICE P317-P318: duas chaves de zona de porta, placa <= 300 mm (300 recomendada), H1 <= 20 mm, H2 = 60 mm; MCTC-SCB (P11); VIT /15 (PDF 17) SCB-A4 porta única síncrona, SCB-D4 portas opostas ou assíncrona | alta |
| 156 | 35 | FX: NA em série na bobina da marcha; "Confirma o Vitinho /17 [Certeza]" | CONTRADIZ | VIT /17 (PDF 19): o NA 13/14 do FX só realimenta X8; A1 do SW vem de Y1 sem contato do FX. A lógica em série existe no esquema da placa de atraso do NICE (P322), não no Vitinho | média |
| 157 | 35 | F5-18, F5-28 e FE-33 "não entram" | CONTRADIZ | VIT /5: F5-28 (Y3) = 12 está configurado e F5-08 (X8) = 30 dá o retorno; F5-18 = 58 (freio). NICE P322 usa F5-18, F5-28 e FE-33 no esquema com contator de curto independente | média |
| 158 | 35 | UPS: 1 kVA até 5,5 kW; 2 kVA acima de 5,5 até 11; 3 kVA para 15 kW; 7,5 kW = 2 kVA; 15 kW = 3 kVA [Provável] | CONFIRMA | NICE Tab. 9-5 (P326): 1 kVA P <= 5,5; 2 kVA 5,5 < P <= 11; 3 kVA 15 <= P <= 22 kW | alta |

## Pendências P1 a P20

| P | O que as fontes dizem | Situação |
|---|---|---|
| P1 | NICE Tab. 1-1 (P30): 7,5 kW/220 V trifásico = 220-NICE-L-C-4015 (36 A); 15 kW/220 V = 220-NICE-L-C-4022 (49 A); "2015" não existe no manual. O 220-4022 é estrutura metálica 554,5x289,6x207,7 mm, 14,5 kg (Tab. 2-3, P43): conferir espaço na caixa. | RESOLVIDO quanto ao modelo. ABERTO: ler etiqueta do inversor recebido e corrigir Compilado/ERP |
| P2 | ERB P1: entrada 220 VAC -15% a +10% = 187 a 242 V. 220/127 V = 127 V fase-neutro. Vitinho /4 e /8 pressupõem rede 380 V com N; 201/202 e 501/502 saem de fase e N. Contagem lógica: XA (R,S,T,N) + TA (U,V,W) = 7 bornes de potência, igual ao BOM 380 V; sem N dá 6, igual ao BOM 220 V. | ABERTO (decisão por variante); corrigir faixa da ERB para 187-242 V |
| P3 | VIT /10 (PDF 12): TRF 63 VA, primário 220V e 0P, secundário 125V e 0S; 125V/0S alimenta QFB1 > 101/102, que o VIT /4 chama de AC110V. A Lista segue o esquema. "OP" do livro é 0P (zero). 150 VA do BOM cobre os 63 VA. | RESOLVIDO quanto aos bornes. ABERTO: etiqueta e medição sem carga |
| P4 | NICE Tab. 3-2 (P87-P88): cabo 6 mm² (220-4015) e 10 mm² (220-4022); Tab. 2-9: GTNR-5 a 2,5 N·m (até 6 mm²), GTNR-6 a 4,0 N·m; Fig. 2-15: parafusos M4/M5/M6 por estrutura. Torque e terminal dos 220 V não constam. | Cabo RESOLVIDO. ABERTO: medir parafuso e torque dos 220-xxxx |
| P5 | NICE P52-P53: resistor em (+) e PB (< 37 kW), cabo < 5 m, nunca no barramento CC. Os 4 resistores do BOM cabem nas faixas da Tab. 3-12. Bitola do cabo e fixação não constam. | ABERTO (bitola, terminal, fixação); resistores CONFIRMADOS |
| P6 | Esquema define o esperado: SW 1-6 potência, 11/12 NC, 53/54 e 73/74 NA; BY 1-2, 3-4, 5-6 NA em série e 11/12 NC; FX 21/22, 31/32 e 13/14 NA (VIT /17). Sem datasheet WEG/Frotal o mapa impresso não se resolve. | ABERTO (multímetro); 73/74 deve cair em par NA |
| P7 | PRT-BOTOEIRA: 8x Ø22, passo 50 x 30 (confirma). VIT /14: a botoeira é o handle KKB4-1C-02 com CIS (1/2, 3/4, 11/12, 13/14), CIU, CID (3/4 e 13/14) e MES; não há botões vermelhos extras. CIS tem 4 elementos, igual ao 2NA+2NF em número. | ABERTO: mapa furo/botão e destino dos 2 vermelhos (nenhum esquema os usa); tipo do VPMP-857 sem ficha |
| P8 | VP 8 e VIT /16: S1 normal, S2 bypass (confirmado). VIT /14 e VP 6: S1/4 = 301, S1/5 = X4; VIT /19: S1/1-2 na cadeia 122B/122A; VP 14 e VIT /21 rotulam S1 = X4, 301, 122A, 122B e S2 = 134, 133, 131A, 130. A tag S1 da Lista é o limitador de velocidade (VIT /22): RESOLVIDO. Jumpers: só #61 e #67 existem no desenho; #62 a #66 não (lote2). | ABERTO: conferir pinos na placa; decidir jumpers #62 a #66 (risco: curto da cadeia de segurança) |
| P9 | QFB4 e LIHS1 existem no esquema (VIT /8, lista de peças; VP 2) e não na Lista/BOM: CONFIRMADO. QFB3 e QFB4 são RCD; QFB1 (1P+N 10 A) e QFB2 (2P 6 A) são breakers; DQFB não existe. | ABERTO: etiquetas físicas e decisão sobre QFB4 |
| P10 | VIT /23 (PDF 25) e VP 16: ERB L = 501 (fase, polo 1-2 do QFB3) e N = 502. A Lista (#20 e #94) está invertida. | RESOLVIDO no esquema. ABERTO: serigrafia da ERB e correção da Lista |
| P11 | Ambos os esquemas só têm MCTC-MCB-C3 (VIT lista de peças, /9, /20; VP 13). | RESOLVIDO; corrigir Lista (#77 e #123) |
| P12 | VIT /15: SCB-A4 (síncrona, porta única) ou SCB-D4; F6-52 Bit1 = 1. VIT /22 traz limitador AC 220 V ou DC 24 V; a Lista usa a versão AC 220 V (201, 202, 203, 205). Cabos de campo não auditados aqui. | Informativo, parcialmente RESOLVIDO |
| P13 | Contagens do livro conferem (pontas, 125 fios). Falta: tubular 6 mm² 19 na Lista x 16 no BOM. O "10%" é [Chute] e não consta no POP. | ABERTO: recalcular compra |
| P14 | XPE recebe 6 PE (#114, #121 a #125): cheio, confirmado pela Lista. Sem dado de projeto do barramento. | ABERTO (decisão) |
| P15 | Nenhum esquema mostra bloco auxiliar de QFB; BC-1 x BC-A é inconsistência interna. | ABERTO |
| P16 | ERB EN/CN: bateria = BAT+/BAT- (sem BPQ); a troca de bateria mostra dois cabos (vermelho +, preto -) entre bateria e placa; sem rede a bateria fica desligada da carga até apertar Partida. Estado de fábrica não declarado. | ABERTO (abrir tampa >= 10 min sem rede); BPQ = bateria sem prova |
| P17 | XA 4 + TA 3 = 7 bornes de potência = BOM 380 V. As 14 posições das fotos podem ser 7 bornes de dois níveis ou outros bornes. | ABERTO (contar na montagem) |
| P18 | Caixa real 1350x350x240 (DES-FURACAO), não 1350x450x350. Nada sobre folga e canaleta no comprimento. | ABERTO (PCP) |
| P19 | VIT /23 nota 2: a alimentação de emergência do topo da cabina alimenta os sensores de zona de porta. CTW-B3: FL1/FL2 com 24 V normal e 12 V de emergência. Mas ERB P2 especifica sensor de 24 V e não dá o limiar de MQ+ com 12 V. | Parcialmente RESOLVIDO. ABERTO: teste R5/R6 ou consulta à Inovance |
| P20 | Revisões diferem: VP 6 não tem 13/14 de CIU/CID nem 11/12 do CIS, VIT /14 tem; datas 2022-10-11 e 2023-07-18; a Lista da botoeira segue o Vitinho. | Diferença CONFIRMADA. ABERTO: decidir qual vale |

## Selos [Certeza], [Provável], [Chute] e PREENCHER (págs. 7 a 35)

Contagem no escopo: 30 [Certeza], 40 [Provável], 8 [Chute], 45 PREENCHER (21 são a coluna "Carcaça Mini-Fit" da pág. 17).

| Pág. | Selo e tema | Resultado | Evidência / o que falta |
|---|---|---|---|
| 7 | [Certeza] KY1 pino 1 à direita; [Provável] demais conectores | ABERTO | Só foto e ponto de pino 1 |
| 7 | [Certeza] numeração do esquema | CONFIRMADO | VIT /4; citar só /4 |
| 8 | [Certeza] 220/127 V | CONFIRMADO | 220/raiz de 3 = 127 V |
| 8 | [Provável 2NA+2NF] CIS | ABERTO | VIT /14: CIS com 4 elementos; falta ficha do VPMP-857 |
| 8 | [Provável] QFB1-3 = DR | CONTRADITO em parte | QFB1/QFB2 são breakers no esquema |
| 10 | [Provável] posições; [Certeza] ordem Z1-Z6 | ABERTO | Fotos |
| 11 | [Provável] antiestático | RESOLVIDO | NICE P20, P83; ERB P3 |
| 11 | [Chute] Allen 4 mm, CAT III, 10% de reserva | ABERTO | Sem fonte |
| 12 | [Certeza: esquema pág. 8] S1/S2 | CONFIRMADO | VP 8, VIT /16 |
| 15 | [Certeza] flat 1:1, BOM | CONFIRMADO | VP 13 |
| 15 | [Provável] +24V e Y7 | ABERTO | VP 14: Y7 "Não usado"; +24V e W7 dividem a legenda |
| 15 | [Provável] W7 em Y7 | RESOLVIDO | VP 13 |
| 15 | [Provável] M24>301; MCM x3>302; +12V>T02 | RESOLVIDO | VP 13 e VIT /20 imprimem 301, 302 x3 e T02 no lado da KCB; NICE P340: +12V/MCM = entrada de 12 V de emergência |
| 16 | [Provável] FX = curto U,V,W | RESOLVIDO | VIT lista de peças e /9; VP 3 |
| 16 | [Certeza: manual] resistor em (+)/PB | CONFIRMADO | NICE P52-P53 |
| 16 | [Provável] cabo das linhas 220 V | RESOLVIDO | NICE Tab. 3-2 |
| 16 | [Provável] torque e terminal das linhas 220 V | ABERTO | Falta etiqueta/manual do 220-xxxx |
| 16 | [Certeza] CN2 "bypass" | CONFIRMADO o mapa; descrição imprecisa | VIT /16, NICE P61 |
| 18 | [Certeza: foto] KY1 real | ABERTO | Foto |
| 18 | [Provável] jumpers fecham cadeia | CONTRADITO (5 de 7) | VIT /19, /44; lote2 |
| 21 | [Certeza] POW1, BB, MT, S1/S2 | CONFIRMADO | VIT /11, /12, /13; VP 5, 8 |
| 21 | [Certeza] KY11/5-6 (esquema pág. 10) | CONFIRMADO a rede; citação errada | Página certa: VP 16 |
| 22 | [Certeza] bateria dentro; LEDs | CONFIRMADO | ERB P1-P2 |
| 22 | [Chute] BPQ = bateria | ABERTO | Manuais usam BAT+/BAT- |
| 23 | [Certeza] KY4 e topologia; [Provável] 301 = +24 V | CONFIRMADO / RESOLVIDO | VIT /14, /4, /10 |
| 25 | [Provável] QFB = DR, DQFB = mini | CONTRADITO em parte | VIT lista de peças |
| 27 | [Certeza] SW, BY; [Provável] FX | CONFIRMADO / RESOLVIDO | VP 5, VIT /13, /17 |
| 27 | [Chute] candidatos impressos | ABERTO | Datasheet; 73/74 deve ser NA |
| 32 | [Provável] E3, E4, E8 = 220 V; E6 = 24 Vcc | RESOLVIDO | VIT /4, /10; ERB P1 (E6 com sentido corrigido) |
| 32 | [Certeza] E7, E10 | CONFIRMADO | VP 5, 13 |
| 33 | [Certeza] valores da ERB | CONFIRMADO exceto 187-253 V (manual: 242 V) | ERB P1 |
| 34 | [Certeza] CAN 60 ohm | CONFIRMADO | NICE P73 |
| 34 | [Provável] MOD 60 ohm | RESOLVIDO | NICE P71 |
| 34 | [Provável] CAN/MOD contra terra e demais cabos; isolação | ABERTO / parcial | NICE P73 só diz COM isolado do aterramento |
| 34 | [Provável] terra < 4 ohm | CONTRADITO | NICE P54: < 10 ohm |
| 34 | [Provável] trafo 380 V e relés do quadro antigo | CONTRADITO para este quadro | VIT /10, /19 |
| 35 | [Certeza na fórmula; 0,9 a conferir] | RESOLVIDO | NICE P76: F3-08 = 0,9 |
| 35 | [Provável] limite a 100 mm; chaves 2 e 3 | CONTRADITO | NICE P77 (30-50 mm), Tab. 2-19 |
| 35 | [Provável] fim de curso 100-150 mm | CONFIRMADO em parte | NICE P77: 150 mm |
| 35 | [Chute] posição da chave 1 | RESOLVIDO | NICE Tab. 2-19 |
| 35 | [Provável] bandeiras 80-200 mm | RESOLVIDO | NICE P74, P174 |
| 35 | [Provável] 1 a 3 sensores | CONTRADITO | NICE P75: 4 |
| 35 | [Certeza] abertura antecipada | CONFIRMADO | NICE P317-P318; VIT /15 |
| 35 | [Certeza] FX em série, "Confirma Vitinho /17" | CONTRADITO em parte | VIT /17 |
| 35 | [Provável] UPS 7,5 kW = 2 kVA; 15 kW = 3 kVA | RESOLVIDO | NICE Tab. 9-5 (P326) |

### PREENCHER

- Carcaça Mini-Fit por conector (pág. 17, 21 campos): VIT /21 (PDF 23) desenha cada conector com os pinos; leitura segura aqui só para KY3, KY12 e POW1 (2 vias) e HW (4). Os demais não foram transcritos: resolvível no desenho, não feito.
- Resistor (cabo/fixação), botões vermelhos, furos, bornes grandes, entradas de cabo, folga de corte, torque de QF/DR/contatores/BTWP, megôhmetro, etiquetas de trafo e freio: sem fonte de fabricante na pasta (ABERTO). Parcial: resistência de PE < 10 ohm (NICE P54).

## Resumo

- Linhas da tabela: 158. CONFIRMA: 110. CONTRADIZ: 35. NÃO VERIFICÁVEL: 13.
- Selos (grupos da seção acima, 45 linhas): 13 com algum RESOLVIDO; contraditos 10; abertos por falta de foto ou ficha de componente.
- Achados mais importantes:
  1. ERB: L e N invertidos na Lista (VIT /23, VP 16); entrada é 187-242 V, não 187-253 V (ERB P1).
  2. Jumpers #62 a #66 não existem no desenho e curto-circuitam cadeia de segurança, trincos e sinais ULS1/DLS1; só #61 e #67 são previstos.
  3. Flat: X15 e X16 trocados (X15 = descida 1, X16 = subida 2); legenda de W1 conflita com Y1 = SW.
  4. Págs. 34 e 35 trazem valores do manual antigo que o NICE3000new contradiz: limite 30-50 mm, chaves 2 e 3 a 2 e 3 m/s, 4 sensores de nível, terra < 10 ohm. Confirma 60 ohm CAN e MOD, UPS 2 e 3 kVA, 0,9 m/s².
  5. E6: os 24 V saem da PCB-D1 para a KCB; "sem continuidade" em 207-208 e 201-202 é falso com o trafo no circuito; trafo/relés do quadro antigo não valem.
  6. S1/TIS da pág. 29 são do limitador de velocidade, não bypass; FX em série com a bobina não está no Vitinho.
  7. Caixa é 1350x350x240 (DES-FURACAO); tubular 6 mm² falta 3 no BOM; citações erradas: "p. 4-5", "tab. 2-9" (0,565 é Tab. 2-17), "linhas 1811-1815", KY11 na pág. 10.
  8. QF: BOM C70 abaixo dos 80 A recomendados em 15 kW/220 V; esquema desenha QF de 4 polos.