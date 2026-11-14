# Capítulo 3: fichas de componente (placas de controle e resgate)

Levantamento de fatos verificados para o Capítulo 3 ("Componentes do quadro de comando"). Não é texto de capítulo. Elevador de referência: 7,5 kW, 380 V, MRL, 3 paradas, 1 porta. Quadro de comando NICE3000new MRL (Inovance, BST, VerticalParts).

## Convenções e fontes

- **Esquema (base de verdade):** `Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf`, desenho 19061867-ZL, versão A00, 51 páginas PDF. Citado como "Esquema /N (PDF M)". Para as folhas /3 em diante vale PDF = folha + 2, exceto a lista de peças (folhas /3 e /3.a estão nos PDF 4 e 5). Folhas usadas: /5 (PDF 7), /9 (PDF 11), /10 (PDF 12), /11 (PDF 13), /13 (PDF 15), /14 (PDF 16), /15 (PDF 17), /16 (PDF 18), /19 (PDF 21), /20 (PDF 22), /21 (PDF 23), /22 (PDF 24), /23 (PDF 25), /24 (PDF 26), /47 (PDF 49).
- **Manual do resgate:** `Manual_Dispositivo_Resgate_Eletrico_ERB-A1_EN.pdf` (folheto de 3 páginas PDF; os painéis têm numeração impressa 1 a 12). Citado como "ERB EN, PDF M (painel impresso P)". O `_CN.pdf` foi consultado só para procurar dados de resistência da bobina (não há).
- **Manual NICE3000new:** `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`. A numeração impressa é a do PDF menos 1 (PDF 60 = página impressa 59). Citado como "Manual NICE3000new, PDF M (impressa M-1)".
- **Esquema alternativo (outra revisão, só comparação):** `Esquema Elétrico Elevadores Verticalparts.pdf`, desenho 19060918-ZL, 58 folhas, data 2022-10-11, com anotações em português. Só as folhas dos PDF 4 e 8 foram comparadas (ver "Comparação" no fim).
- **Orientação dos pinos:** as tabelas seguem o desenho da folha /21, lido com a fileira de pinos na vertical, como o próprio desenho (rótulos girados). A numeração segue os dígitos impressos nas pontas das colunas ("1" e o primeiro número da segunda coluna). Quando o conector só traz ponto de pino 1 (sem dígitos), isso é dito. Onde a numeração foi confirmada por outra folha (ex.: KY10 pela /23), a folha está citada.
- Pino "vazio" = célula riscada na diagonal no desenho (sem conexão). O desenho não informa a polaridade de 301 e 302; só a /20 liga M24 a 301 e MCM a 302 (ver ficha 5).
- Os códigos de peça (BOM) foram omitidos de propósito.

---

## Ficha 1: Placa de interface MCTC-KCB-B4A

### Função
- Nome no esquema: "Control cabinet interface board", item do quadro de comando (lista de peças, Esquema /3.a, PDF 5). Nas folhas é a placa que recebe a alimentação de controle (201/202, 501/502), distribui 207/208 e as redes 301/302, concentra a cadeia de segurança (101 a 134), os conectores do cabo de manobra (AA e AB), os da botoeira de inspeção (KY4), da fonte de freio (KY3, KY6, KY8, KY9, KY12, MT), do resgate elétrico (KY10, KY11, SZ) e da placa de abertura avançada (KY7, KY13), além das entradas X e saídas Y levadas à placa principal pelo conector J10 (Esquema /20, PDF 22).
- Tem circuito de proteção contra sobretensão (OVP), três fusíveis (F1, F2, F3), plugues S1 e S2 (bypass) e, na folha /21, uma caixa "Safety disply" (grafia do desenho) sem rótulo de função.

### Dados (valores)
| Item | Valor | Fonte |
|---|---|---|
| F1 "Door/light curtain fuse" | 250 VAC / 4 A | Esquema /10 (PDF 12), localização /10.2:C na lista de peças (PDF 5) |
| F2 "Car fan/light curtain fuse" | 4 A / 250 VAC | Esquema /11 (PDF 13), /11.2:C |
| F3 "Safety circuit fuse" | 250 VAC / 1 A | Esquema /10 (PDF 12) e /19 (PDF 21), /10.6:B |
| OVP "Overvoltage Protection Circuit" | "300VAC protection/285VAC recover" (proteção em 300 VAC, rearme em 285 VAC) | Esquema /10 (PDF 12) |
| Disjuntor que alimenta 201/202 (QFB2) | 2P, In = 6 A, curva C | Esquema /10 (PDF 12) |
| Transformador TRF (ligado a KY8) | primário 220 V / 0P, secundário 125 V / 0S, 50 Hz, 63 VA (3,7 a 22 kW) ou 110 VA (30 a 37 kW) | Esquema /10 (PDF 12) |
| Disjuntor do circuito de segurança (QFB1) | 1P+N, In = 10 A, curva C | Esquema /10 (PDF 12) |

Para o elevador de 7,5 kW, a faixa de potência do transformador é "3,7 a 22 kW", ou seja, 63 VA.

Onde cada fusível está no circuito (pelo desenho):
- F1: na linha 207, entre o ramal 207 (após a OVP) e a saída +CC-207 que vai ao pino AA/1 (Esquema /10 e /11). A linha 208 vai a AA/9 sem fusível.
- F2: na linha 501, entre POW1/1 e AA/8 (507). A linha 502 vai direto de POW1/2 a AA/16 (508) (Esquema /11, PDF 13).
- F3: entre KY5/7 (101) e o ramal 101A, que chega a KY4/12 (Esquema /10 e /19).

### Conectores e pinos (tabelas pino a pino)

Entre parênteses: destino ou referência citada nas folhas. Células vazias aparecem como "vazio".

**KY1 (12 pinos; dígitos 1 e 7 no desenho)**
| Pino | Rede | Observação |
|---|---|---|
| 1 | 130 | vai a X25 da placa principal (CN2/2) (/16, /19) |
| 2 | 134 | vai a X27 (CN2/4) |
| 3 | 133 | vai a X28 (CN2/5) |
| 4 | 131 | vai a X26 (CN2/3) |
| 5 | vazio | |
| 6 | 102 | ligado a CN2/1 (XCM1) (/16, PDF 18) |
| 7 a 12 | vazio | |

**KY2 (10 pinos; dígitos 1 e 6)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | Y1 | 6 | 301 |
| 2 | Y2 | 7 | X6 |
| 3 | Y3 | 8 | X7 |
| 4 | vazio | 9 | X8 |
| 5 | Y2A | 10 | X5 |

**KY3 (2 pinos; dígitos 1 e 2):** 1 = 301, 2 = 302. Vão a J4/1 e J4/4 da PCB-D1 (/10, PDF 12).

**KY4 (12 pinos; dígitos 1 e 7), botoeira de inspeção**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 301 | 7 | 125 |
| 2 | 56 | 8 | 118 |
| 3 | 55 | 9 | 110 |
| 4 | X9 | 10 | 122B |
| 5 | vazio | 11 | 123 |
| 6 | vazio | 12 | 101A |
Confirmado pela /14 (PDF 16), que traz os mesmos números de pino e redes.

**KY5 (8 pinos; dígitos 1 e 5)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 201 | 5 | 202 |
| 2, 3, 4 | vazio | 6 | vazio |
| | | 7 | 101 |
| | | 8 | 102 |
201/202 vêm do QFB2 (saídas 3 e 4) e alimentam o limitador de velocidade de 220 V (Esquema /10, /22).

**KY6 (4 pinos; dígitos 1 e 3):** 1 = 207, 2 = 208, 3 = ZQA1, 4 = ZQ1-. 207/208 vão a J2/1 (L) e J2/2 (N) da PCB-D1 (/10); ZQ1- vai à fonte de freio pelos contatos BY (/13).

**KY7 (14 pinos; dígitos 1 e 8)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 301 | 8 | 130 |
| 2 | 302 | 9 | 134 |
| 3 | FL1 | 10 | 132 |
| 4 | FL2 | 11 | 133 |
| 5 | Y5 | 12 | vazio |
| 6 | X2 | 13 | SGC2 |
| 7 | X19 | 14 | SGC3 |
Pela /15 (PDF 17), KY7/8, /10, /11, /9 vão aos contatos K1, K2, K3, K4 da placa MCTC-SCB-A4/D4 (CN1/3, /4, /7, /8: 130, 132, 133, 134) e KY7/13, /14 (SGC2, SGC3) a K5 e K6 (CN1/1 e /5). Esses contatos são marcados "Add when use SCB-D4" no desenho.

**KY8 (4 pinos; dígitos 1 e 3):** 1 = 207, 2 = 208, 3 = ZQ1+, 4 = ZQA1. 207/208 vão ao primário do transformador (220 V e 0P) (/10). ZQ1+ passa pelo contato 53-54 do contator de marcha SW (/13).

**KY9 (4 pinos; dígitos 1 e 3):** 1 = vazio, 2 = ZQ2+, 3 = ZQA2, 4 = ZQ2-. Ao lado do conector há um símbolo de aviso de tensão perigosa (triângulo com raio) no desenho.

**KY10 (10 pinos; o desenho da /21 não traz dígitos, a numeração foi lida da esquerda para a direita e confirmada pelas folhas /23 e /24)**
| Pino | Rede | Uso (folha) |
|---|---|---|
| 1 | "/" (sem rede) | |
| 2 | 301 | |
| 3 | 302 | COM do ERB (/23) |
| 4 | CAN1+ | "Standby" (/24) |
| 5 | CAN1- | "Standby" (/24) |
| 6 | 302 | MQ- do ERB (/23) |
| 7 | 301 | |
| 8 | FL1 | MQ+ do ERB (/23) |
| 9 | DC12 | soquete SZ/3 (/23) |
| 10 | T02 | soquete SZ/8 (/23) |

**KY11 (6 pinos; ponto de pino 1 em "122"; /23 confirma 5 e 6)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 122 | 4 | SGC2 |
| 2 | 122A | 5 | 133 |
| 3 | SGC3 | 6 | 131 |
KY11/5 e /6 vão a MS+ e MS- do ERB (/23). Na /19, KY11/2 está na cadeia de segurança entre 122A e o conjunto de interruptores da fossa/contrapeso (RCS, KY11/1 etc.).

**KY12 (2 pinos; dígitos 1 e 2):** 1 = CAN+, 2 = CAN-. Vão a J4/2 e J4/5 da PCB-D1 (/24, PDF 26).

**KY13 (8 pinos; dígito 1 na ponta)**
| Pino | Rede |
|---|---|
| 1 | FL1 |
| 2 | vazio |
| 3 | FL2 |
| 4 | vazio |
| 5 | 301 |
| 6 | 302 |
| 7 | CAN+ |
| 8 | CAN- |
Vão a CN2 pinos 1, 3, 5 (24V), 6 (GND), 7, 8 da MCTC-SCB-A4/D4 (/15 e /24).

**POW1 (2 pinos; 1 e 2):** 1 = 501, 2 = 502 (entrada de 220 V do ramal do teto, /11, PDF 13).

**AA (16 pinos; dígitos 1 e 9; ligação ao cabo de manobra)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 207 | 9 | 208 |
| 2 | vazio | 10 | vazio |
| 3 | PE | 11 | 132 |
| 4 | 130 | 12 | 125 |
| 5 | 131A | 13 | 123 |
| 6 | 133 | 14 | 134 |
| 7 | vazio | 15 | vazio |
| 8 | 507 | 16 | 508 |
Confirmado pelas folhas /11 (PDF 13) e /19 (PDF 21). Na /19, "single door, connect AA-P06, AA-P14" indica ponte entre AA/6 (133) e AA/14 (134) quando não há o interruptor de trinco da porta traseira.

**AB (14 pinos; dígitos 1 e 8; ligação ao cabo de manobra)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 102 | 8 | 122A |
| 2 | vazio | 9 | vazio |
| 3 | 301 | 10 | FL2 |
| 4 | 302 | 11 | DC12 |
| 5 | CAN+ | 12 | L |
| 6 | CAN- | 13 | R |
| 7 | FL1 | 14 | DZI |
AB/3, /4, /7, /8, /10 confirmados na /11; AB/5 e /6 na /24 (vão a CB/5 e CB/6 da placa de controle da caixa de teto).

**BA (10 pinos; dígitos 1 e 6)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | PE | 6 | 111 |
| 2 | 118 | 7 | 132 |
| 3 | 121 | 8 | 132 |
| 4 | 131 | 9 | 133 |
| 5 | 122A | 10 | 123 |
Confirmado pela /19 (BA/2 = 118, BA/3 = 121, BA/4 = 131, BA/6 = 111, BA/7 = 132, BA/8 = 132, BA/9 = 133). Na /19 está escrito "single door, connect BA-P08 and BA-P09": ponte BA/8 a BA/9 (132 a 133) quando não há a cadeia de interruptores de camada traseira (1RDS, 2RDS, nRDS).

**BB (dígitos 1 e 8):** coluna esquerda 1 = 301, 2 = 302; coluna direita (marcada "8") MOD+ (base) e MOD- (topo). O desenho rotula a coluna direita com "8", o que não casa com um conector de 4 posições (ver Lacunas).

**BC (dígitos 1 e 8):** coluna esquerda 1 = R, 2 = L; coluna direita (marcada "8") 302 (base) e DC12 (topo).

**BD (dígitos 1 e 8):** coluna esquerda 1 = 301, 2 = 302; coluna direita (marcada "8") ULS1 (base) e ULS2 (topo).

**BE (4 pinos; dígitos 1 e 3):** 1 = 301, 2 = 302, 3 = DLS1, 4 = DLS2. (O desenho usa "ULS" e "DLS" para sensores de desaceleração; ver tabela de entradas.)

**AC (8 pinos; dígitos 1 e 5):** 1 = vazio, 2 = SGC2, 3 = vazio, 4 = 123; 5 = vazio, 6 = SGC1, 7 = vazio, 8 = 122A.

**HW (6 pinos; dígitos 1 e 4; "Use for MR", roda manual)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | vazio | 4 | PE |
| 2 | 111 | 5 | vazio |
| 3 | 110 | 6 | vazio |
Na /19: botão de emergência do motor MES-1 entre HW/3 (110) e 110A; "MES-2" (botão da roda manual, "Use for MR") entre 110A e HW/2 (111). Para MRL o desenho não usa a roda manual.

**OS (6 pinos; dígitos 1 e 4)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | PE | 4 | vazio |
| 2 | 121A | 5 | 122 |
| 3 | 121 | 6 | 121A |
Na /19 aparecem interruptores com o rótulo OS ("OS-G" speed governor electric switch e "OS" safety gear electric switch) com terminais OS/2, /3, /5 e /6 nas redes 122, 121A e 121; a correspondência exata pino a pino não foi conferida.

**ARD (4 pinos; ponto marca o pino 1, sem dígitos):** 1 = 301, 2 = X12, 3 = Y6, 4 = M6. Entrada X12 "Emergency leveling signal" e saída Y6 "Emergency evacuation completed signal" (tabela da /21). O parâmetro F8-10 = 1 na /5 (PDF 7) indica "Emergency evacuation by automatic rescue device (ARD) (optional)".

**FR (4 pinos; ponto no pino 1):** 1 = 301, 2 = X21, 3 = Y4, 4 = M4. X21 "Integrated fire", Y4 "Fire-emergency output" (tabela da /21). F5-29 = 4 "Fire emergency floor arrival signal feedback" (/5).

**TEL3 (8 pinos; ponto no pino 1):** 1 = 302, 2 = DC12, 3 = R, 4 = L, 5 = Y7, 6 = M7, 7 = "301/DC12", 8 = X13. O desenho não diz o que TEL3 liga (ver Lacunas).

**MT (12 pinos; dígitos 1 e 7), plugue do freio**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | X18 | 7 | 301 |
| 2 | X22 | 8 | 301 |
| 3 | X20 | 9 | 301 |
| 4 | vazio | 10 | vazio |
| 5 | ZQ1+ | 11 | ZQ1- |
| 6 | ZQ2+ | 12 | ZQ2- |
Pela /13 (PDF 15) e /9 (PDF 11): MT/5 e /11 vão à bobina BK1; MT/6 e /12 à bobina BK2; MT/7 (301) e MT/1 (X18) ao contato de realimentação BK1-FB (COM2 e NC1); MT/8 (301) e MT/2 (X22) ao de BK2-FB (COM3 e NC2); MT/9 (301) e MT/3 (X20) ao sensor de temperatura PT1 do motor (COM1 e PT1).

**J10 (40 vias, 2 fileiras de 20; dígitos 1 e 2 na ponta esquerda, 39 e 40 na direita):** cabo flat da placa principal (ver abaixo, "Sinais de J10").

**Terminais soltos (sem conector nomeado):** SZ e UCMP aparecem como soquetes na /19 e /23 (ver plugues).

### Sinais de J10 (folha /20, PDF 22)
O desenho da /20 liga a placa principal (MCB) e a KCB com 40 sinais na ordem abaixo (da esquerda para a direita no desenho). Os números de pino 1 a 40 do J10 não aparecem na /20 nem na /21, só a ordem:

1. X1 a X22 (22 sinais, mesmos nomes dos dois lados).
2. W1, W2, W2A, W3, W4, W5, W6, +24V, W7 (9 sinais). Na KCB cada W aparece como saída Y1, Y2, Y2A, Y3, Y4, Y5, Y6 e Y7 (caixas na /20). O desenho liga W1 a W5 e W7 a 301 ("10.7:B / +CC-301") e mostra uma linha que une Y6 ao ponto +24V.
3. Lado MCB: M24, MCM, MCM, MCM, +12V, CAN-, CAN+, MOD1+, MOD1-. Lado KCB, na mesma ordem: 301, 302, 302, 302, T02, CAN-, CAN+, MOD1+, MOD1- (9 sinais).

### Plugues S1 e S2 (bypass) e outros plugues
Origem: Esquema /14 (PDF 16), /16 (PDF 18), /19 (PDF 21), /21 (PDF 23). Aqui "plugue de bypass" é o conector com ponte que o desenho chama de "Bypass plug".

**S1 (5 posições):** 1 = 122B, 2 = 122A, 3 = vazio, 4 = 301, 5 = X4 (/21 e /14).
- Posição normal (plugue de bypass inserido no S1): a /19 desenha a ponte entre S1/1 e S1/2 (122B a 122A, fecha a cadeia de segurança); a /14 desenha a ponte entre S1/4 e S1/5 (301 a X4). A /21 escreve "Normal" sob o S1 e a /16 diz "S1 ON, S2 OFF, X4 ON, normal state".
- Com o plugue fora do S1: X4 OFF (/16). Sobre a cadeia 122B a 122A o desenho só mostra a ponte dentro do plugue; ela fica aberta fora do S1.

**S2 (soquete de bypass das portas):** pela /21 o S2 tem 5 posições preenchidas (e uma vazia). Pela /19 e /16: S2/1 = 134, S2/2 = 133, S2/3 = 131A, S2/4 = 131A, S2/5 = 130, S2/6 = sem rede. Lido na /19:
- "Bypass Car Door GS1": S2/5 a S2/4 (130 a 131A).
- "Bypass Hall Door DS": S2/3 a S2/2 (131A a 133).
- "Bypass Car Door GS2": S2/2 a S2/1 (133 a 134).
- Quadro de estado da /16 (S1 e S2): S1 ON, S2 OFF = normal, X4 ON; S1 OFF, S2 OFF = operação elétrica de emergência (X4 OFF); S1 OFF e S2 (1-5) ON = "Bypass landing door"; S1 OFF e S2 (2-6) ON = "Bypass car door". Nota: "S1 and S2 are ON when the bypass plug is inserted into them".
- Regras do desenho (/16, texto à esquerda): retirar o plugue do S1 e inserir no S2 na posição correspondente; "You can run the elevator only under emergency electrical operation or inspection mode in the door close limit state"; o alarme sonoro e luminoso funciona durante a marcha; ao terminar, voltar o plugue ao S1. A nota da /14 diz que, após ligar o bypass, o dispositivo sonoro e visual do fundo da cabine é acionado.
- Parâmetro (/5, PDF 7): X4 função "118: Door lock bypass input (NC)" (texto da lista de parâmetros, ordem embaralhada no PDF).

**SZ (soquete do resgate, 10 posições; dígitos 1 e 6)**
| Pino | Rede | Pino | Rede |
|---|---|---|---|
| 1 | 101B | 6 | 101 |
| 2 | 133 | 7 | 131 |
| 3 | DC12 | 8 | T02 |
| 4 | 302 | 9 | 302 |
| 5 | FL1 | 10 | vazio |
- Plugue SZ1 (posição normal): só tem ponte entre 1 e 6 (101B a 101), isto é, fecha o circuito de segurança "Use for MRL" (/19, /23).
- Plugue SZ2 (resgate): sem ligação em 1 e 6; 4 a COM, 9 a MQ-, 5 a MQ+, 2 a MS+, 7 a MS- do ERB; ponte entre 3 e 8 (DC12 a T02) (/23).
- A /23 escreve: "Normal plug: when release the brake: please pull up SZ1, and insert SZ2 into SZ".

**MT (plugue) e MT1 (soquete):** o MT plug é o da tabela de MT acima. O MT1 socket só usa as posições 5 (ZQ1+), 6 (ZQ2+), 11 (ZQ1-), 12 (ZQ2-); as outras são vazias. No ERB: MT1/5 e /6 vão a ZQ+ e MT1/12 e /11 a ZQ-. Regra da /23: "when release the brake: please put MT insert MT1".

**UCMP (soquete na KCB, folha /21):** células SGC3, SGC1, vazia, 131, 131A. Na /19 há duas posições UCMP/1 (131A) e UCMP/2 (131) ligadas por uma ponte quando não há a placa UCMP. A /16 traz o procedimento de teste UCMP (ver Lacunas).

### Entradas e saídas do desenho (tabela da folha /21, PDF 23)
Nomes na tabela da /21, com o conector da KCB onde o sinal está desenhado e o nome do sinal na /20 quando diferente. Onde a coluna "Conector" está vazia, a /21 não traz conector com esse nome.

| Marca | Definição (/21) | Conector da KCB | Observação (/20, /5) |
|---|---|---|---|
| X1 | Up-level signal | (via FL1: AB/7) | /11: X1 sai de FL1 |
| X2 | Door-area signal | KY7/6 | /20: "Door-area signal / standby" |
| X3 | Down-level signal | (via FL2: AB/10) | /11: X3 sai de FL2 |
| X4 | Bypass signal | S1/5 | |
| X5 | Brake 2 feedback | KY2/10 | |
| X6 | Run contactor feedback | KY2/7 | |
| X7 | Brake 1 feedback | KY2/8 | |
| X8 | U.V.W short contactor feedback | KY2/9 | |
| X9 | Emg. signal input | KY4/4 | /5: "116: EEO input (NC)" |
| X10 | Emg. up signal input | via 55 (KY4/3) | /5: "09: EEO up input (NO)" |
| X11 | Emg. down signal input | via 56 (KY4/2) | /5: "10: EEO down input (NO)" |
| X12 | Emergency leveling signal | ARD/2 | |
| X13 | Reserved | TEL3/8 | /20: "Standby" |
| X14 | Up deceleration 1 | sem conector nomeado | /5: "48: Up slow-down 1 (NC)" |
| X15 | Up deceleration 1 (repetido na /21) | sem conector nomeado | /20: "Down deceleration 1"; /5: "49: Down slow-down 1 (NC)" |
| X16 | Up deceleration 2 | sem conector nomeado | /5: "50: Up slow-down 2 (NC)" |
| X17 | Down deceleration 2 | sem conector nomeado | /5: "51: Down slow-down 2 (NC)" |
| X18 | Brake switch detection 1 | MT/1 | /5: "58: Brake travel switch 1 (NC)" |
| X19 | Advance door-open output feedback | KY7/7 | /20: "Standby" |
| X20 | Motor overheating protection | MT/3 | /5: "99: Motor over-temperature (NC)" |
| X21 | Integrated fire | FR/2 | |
| X22 | Brake switch detection 2 | MT/2 | /5: "110: Brake travel switch 2 (NC)" |
| X23, X24 | Reserved | sem conector | /9 Nota 3: "x23 and x24 input port only for the use of a function" |
| X25 | Safety circuit detection | (CN2/2 da MCB; entra por KY1/1 = 130) | /5: F5-37 = "4: Safety circuit signal" |
| X26 | Door lock adhesion detection | (CN2/3; KY1/4 = 131) | /5: F5-38 = "7: Door 1 lock shorting signal" |
| X27 | Door detection | (CN2/4; KY1/2 = 134) | /5: F5-39 = "5: Door lock circuit signal" |
| X28 | Door lock adhesion detection | (CN2/5; KY1/3 = 133) | /5: F5-40 = "8: Door 2 lock shorting signal (set for double-door elevators)" |
| Y1 | Run contactor output | KY2/1 | /20: W1 "Brake contactor output"; /5: F5-26 = "1: Run contactor output" |
| Y2 | Brake contactor 1 output | KY2/2 | /5: F5-27 = "2: Brake contactor output" |
| Y2A | Brake contactor 2 output | KY2/5 | |
| Y3 | U.V.W short contactor output | KY2/3 | /5: F5-28 = "12: Shorting motor stator control output" |
| Y4 | Fire-emergency output | FR/3 | /5: F5-29 = "4: Fire emergency floor arrival signal feedback" |
| Y5 | Advanced door-open relay | KY7/5 | /20: "Advanced door-open relay/standby" |
| Y6 | Emergency evacuation completed signal | ARD/3 | /20: "Reserved" |
| Y7 | Reserved | TEL3/5 | /20: "Reserved" |

Os nomes dos sinais da /20 (PDF 22) diferem dos da /21 em alguns pontos (X2, X13, X15, X19, Y6, W1); as diferenças estão na coluna de observação. Na /20 as entradas de baixa tensão X1 a X22 têm indicadores luminosos no lado da placa principal.

### Circuito de proteção contra sobretensão (OVP)
- Nome: "MCTC-KCB-B4A-OVP, Overvoltage Protection Circuit" (lista de peças, Esquema /3.a, localização /10.2:B).
- Valores: "300VAC protection/285VAC recover" (Esquema /10, PDF 12).
- Posição no circuito: entra por KY5/1 e KY5/5 (201 e 202, saídas 3 e 4 do QFB2) e entrega 207 e 208 (Esquema /10). O desenho mostra a OVP como caixa com quatro terminais, sem o interior.
- A caixa da /21 (PDF 23) está rotulada "Overcurrent protection circuit-indicator light" (sobrecorrente), o que contradiz o nome "Overvoltage" da lista de peças e da /10. Ver Lacunas.

### Liga a
- Fonte de freio MCTC-PCB-D1 (KY3, KY6, KY8, KY9, KY12, MT).
- Resgate MCTC-ERB-A1 (KY10, KY11, SZ, MT/MT1, POW1).
- Botoeira de inspeção KKB4-1C-02 (KY4).
- MCTC-SCB-A4/D4 (KY7, KY13) e interfone/telefone via TEL3 (função não definida no desenho).
- Cabo de manobra e caixa de teto (AA, AB, BA, BB, BC, BD, BE, AC, HW, OS).
- Placa principal MCTC-MCB-C3 pelo J10.

### Fonte (resumo)
Esquema /10 (PDF 12), /11 (PDF 13), /13 (PDF 15), /14 (PDF 16), /15 (PDF 17), /16 (PDF 18), /19 (PDF 21), /20 (PDF 22), /21 (PDF 23), /23 (PDF 25), /24 (PDF 26), /5 (PDF 7), lista de peças (PDF 4 e 5).

### Observações do esquema
1. Nota de potência: o transformador TRF informado (63 VA para 3,7 a 22 kW) cobre o motor de 7,5 kW.
2. Na /19, F3 é chamado "Safety circuit fuse" e a sequência é 101B, SZ/1, ponte, SZ/6, 101, F3, 101A, KY4/12. Na /10 aparecem "101 / 23.4:B" e "+CC-101B / 23.4:B" dentro da caixa tracejada "Used for MRL" e a nota "Short when used for MR": para elevador com casa de máquinas, 101 e 101B ficam em curto; para MRL, a continuidade passa pelo soquete SZ do resgate.
3. A rede 207/208 sai também por KY6 (para L e N da PCB-D1) e por KY8 (para o transformador). Só a linha 207 que vai a AA/1 tem F1.
4. Há uma caixa "Safety disply" na /21 sem texto interno nem ligação desenhada.
5. A numeração do MES difere entre a /14 (1 do lado de KY4/9 = 110, 2 do lado de KY4/12 = 101A) e a /19 (1 do lado de KY4/12, 2 do lado de KY4/9).
6. O nome "S1" aparece também na lista de peças (/3.a) como "Speed limiter remote action switch" (/22.2:C), um interruptor do limitador. Não é o plugue S1 da KCB. O mesmo vale para a /22 (PDF 24), onde S1 tem contatos 13-14 e 23-24.
7. Resistores R220, R22, R21 e R23 e diodos D9 e D26 formam, entre ZQ1+ e ZQ1- e entre ZQ2+ e ZQ2-, a rede de descarga das bobinas de freio (/13). Valores não aparecem.
8. Nota da /13: "The left and right brakes on the host side should be completely separated and wired".

### LACUNAS (perguntas ao responsável técnico)
1. Os conectores BB, BC e BD têm colunas de 2 pinos marcadas "1" e "8" na /21. A segunda coluna é 8 e 9, ou 3 e 4 como no BE? Qual a numeração real de pinos desses conectores?
2. KY10 (e ARD, FR, TEL3) não tem dígitos de pino no desenho. A numeração usada aqui (da esquerda para a direita; ponto = pino 1) confere com as folhas /23 e /24 apenas para KY10. Confirmar para ARD, FR e TEL3.
3. Qual é a numeração dos 40 pinos do J10 e a correspondência exata de cada sinal da /20 com o pino 1 a 40? Qual o conector de destino na MCB?
4. Para que serve TEL3 (L, R, DC12, "301/DC12", X13, Y7, M7)? E L, R, DC12 e DZI de AB e BC: são o interfone/telefone, o display, outro serviço? O desenho não nomeia.
5. Qual é o conteúdo da caixa "Safety disply" na /21?
6. A caixa da /21 diz "Overcurrent protection circuit-indicator light". A OVP é de sobretensão (/10 e lista de peças) ou há também proteção de sobrecorrente? Existe indicador luminoso?
7. Tipo dos fusíveis F1, F2, F3 (rápido, retardado, dimensões) e valor de queima de cada um? O desenho só dá corrente e tensão.
8. Qual o valor dos resistores R220, R22, R21, R23 e o tipo dos diodos D9 e D26?
9. A /16 descreve o plugue de bypass com pares "S2 (1-5)" e "S2 (2-6)", mas a /19 e a /21 mostram S2/5-4 (GS1), S2/3-2 (DS) e S2/2-1 (GS2), e os desenhos da própria /16 rotulam os pinos do plugue como S1/5-S1/4, S1/2-S1/1. Qual é o par real de pinos de cada bypass (porta de cabine 1, porta de cabine 2, porta de pavimento)? O esquema alternativo (PDF 8) diz "jumper na parte de baixo do S2" para porta de cabine e "na parte de cima do S2" para porta de pavimento, o que não permite fechar os pares.
10. O plugue S1 fora do lugar abre a ponte 122B a 122A? O desenho só mostra a ponte dentro do plugue.
11. Qual é a função de DC12 e T02 em operação normal (alimentação de 12 V de qual circuito)? Na /20 o T02 da KCB é o "+12V" da placa principal.
12. A /20 mostra Y6 ligado ao ponto +24V por uma linha. É correto ou é erro do desenho?
13. O desenho traz W1 como "Brake contactor output" na /20 e Y1 como "Run contactor output" na /21. Qual é o correto para o quadro de comando de referência?
14. Na /21, X14 e X15 estão ambos como "Up deceleration 1" (a /20 e a /5 dão X15 como descida 1). Em qual pino da KCB chegam os sensores ULS/DLS (BD e BE carregam ULS1, ULS2, DLS1, DLS2) e qual X corresponde a cada um?
15. O teste UCMP (F-8 = 7 no teclado, F3-24 = 2 no painel) e a placa MCTC-SCB-A4/D4 fazem parte do kit de 3 paradas e 1 porta? A /15 pede F6-52 BIT1 = 1.

---

## Ficha 2: Placa fonte do freio MCTC-PCB-D1

### Função
Nome no esquema: "Brake power board of can" (lista de peças, PDF 5; "Can brake board" na /24) e "Brake power board of CAN". Gera a alimentação de 24 V do quadro (redes 301 e 302) e a tensão de freio (110 V padrão) para as bobinas BK1 e BK2, e conversa por CAN com a KCB (Esquema /10, /13, /24).

### Dados (valores)
| Item | Valor | Fonte |
|---|---|---|
| Alimentação | 207 e 208 da KCB (KY6/1 e /2), entradas L e N (J2/1 e J2/2) | Esquema /10 (PDF 12) |
| Saída de 24 V (PS-24V) | 24 VDC, corrente máxima de saída 7 A, proteção de sobrecorrente em 8 A; saídas em J4/1 (301) e J4/4 (302) | Esquema /10 |
| Ajuste da tensão de 24 V | B0-03 = 1: 24 V; 2: 26 V; 3: 28 V; 4: 30 V | Esquema /10 |
| Saída de freio (PS-110V) | "max 5.6A" no bloco; BK1+, BK-, BK2+ em J3/2, J3/1, J3/3 | Esquema /10 |
| Tensão de freio | ajustável de 48 VDC a 207 VDC; padrão 110 VDC (o desenho escreve "48VDV-207VDC") | Esquema /13 (PDF 15) |
| Corrente | impacto máximo (strong strike) 6 A; manutenção máxima 4 A | Esquema /13 |
| Parâmetros do freio | B0-00 tensão de impacto forte ("Strong shock voltage"); B0-01 tensão de manutenção; B0-02 tempo de corte forte da manutenção (0 a 5 s, padrão 3 s) | Esquema /13 |
| Regra | a tensão de manutenção não pode ser maior que a de impacto forte | Esquema /13 |
| Depuração (duas formas) | A: placa separada, celular ligado à porta de gravação por ferramental e app para alterar códigos; B: pela placa-mãe, pelo app ou pelo operador (pressionar o botão da direita por 5 s para entrar na interface dos códigos da placa) | Esquema /10 e /13 |

### Conectores e pinos
| Conector | Pino | Rede | Ligação (folha) |
|---|---|---|---|
| J2 | 1 | L | KY6/1 (207) (/10) |
| J2 | 2 | N | KY6/2 (208) (/10) |
| J3 | 1 | BK- | contatos BY da /13 em série até ZQ- (KY6/4 e KY9/4) |
| J3 | 2 | BK1+ | contato 53-54 do SW e KY8/3 (ZQ1+); também KY8/4 (ZQA1) (/13) |
| J3 | 3 | BK2+ | contato 73-74 do SW e KY9/2 (ZQ2+); também KY9/3 (ZQA2) (/13) |
| J3 | 8 | PE | terra (/10) |
| J4 | 1 | 301 | KY3/1 (/10) |
| J4 | 2 | CAN+ | KY12/1 (/24) |
| J4 | 4 | 302 | KY3/2 (/10) |
| J4 | 5 | CAN- | KY12/2 (/24) |
O desenho não informa quantos pinos têm J2, J3 e J4 (só aparecem os usados).

### Liga a
KCB (KY3, KY6, KY8, KY9, KY12) e, por ela, às bobinas BK1 e BK2 pelo plugue MT (MT/5 e /11 para BK1, MT/6 e /12 para BK2).

### Fonte
Esquema /10 (PDF 12), /13 (PDF 15), /24 (PDF 26), lista de peças (PDF 5).

### Observações do esquema
1. O bloco PS-110V traz "max 5.6A" e a nota da /13 diz "maximum impact current is 6A, and the maximum maintenance current is 4A": os dois valores são do mesmo desenho.
2. O contator de marcha SW tem um contato 53-54 para BK1+ e um 73-74 para BK2+; o contator de freio BY tem três contatos (1-2, 3-4, 5-6) em série na linha BK- (/13).
3. A ligação CAN: KY12/1 (CAN+) a J4/2 e KY12/2 (CAN-) a J4/5 (/24). A topologia completa da /24 também leva CAN+ e CAN- a AB/5 e AB/6 (cabo de manobra, CB/5 e CB/6 da placa de controle da caixa de teto), a KY13/7 e /8 (MCTC-SCB-A4/D4) e a KY10/4 e /5 ("Standby").
4. O desenho coloca as duas bobinas no mesmo plugue MT e diz que os freios esquerdo e direito do lado da máquina devem estar completamente separados e ligados.

### LACUNAS (perguntas)
1. Qual é a tensão de freio efetivamente ajustada (B0-00, B0-01, B0-02) para o freio da máquina de referência de 7,5 kW? O esquema só traz o padrão de 110 V.
2. Quais são a tensão e a corrente nominal da bobina do freio da máquina de referência (para conferir com o limite de 4 A do resgate)?
3. O bloco diz "max 5.6A" e a nota diz impacto máximo de 6 A. Qual vale?
4. Quantos pinos têm J2, J3 e J4?
5. Onde estão documentados os demais parâmetros B0-xx e a interface do app (o manual NICE3000new não traz o grupo B0)?
6. Em /13, KY6/3 (ZQA1) não aparece ligado. É ligação interna da KCB com KY8/4?

---

## Ficha 3: Resgate elétrico MCTC-ERB-A1

### Função
- Dispositivo de liberação elétrica do freio quando falta energia da rede (resgate elétrico). Com a rede normal, carrega a bateria; sem rede, libera o freio pelos botões do painel. O manual diz que o produto "releases the brake to stop the elevator at the expected position when the mains power fails" (ERB EN, PDF 1, painel 1).
- Modelo: MCTC-ERB-A1 é a versão com bateria; A2, sem bateria (ERB EN, PDF 1, figura 1 "Model description"). O esquema usa "MCTC-ERB-A" (lista de peças, /3.a) e "MCTC-ERB-A1" na /23.

### Dados (valores) do manual
| Item | Valor | Fonte |
|---|---|---|
| Freios atendidos | tensão de excitação forte até 110 V e tensão de manutenção até 80 V | ERB EN, PDF 1 (painel 1) e Esquema /23, nota 1 |
| Corrente máxima de excitação forte | 4 A | ERB EN, PDF 1 |
| Entrada | monofásica 220 VAC (-15% a +10%), 50/60 Hz | ERB EN, PDF 1, tabela 1 |
| Saída para o freio | partida em tensão maior 110 VDC; manutenção 80 VDC | ERB EN, PDF 1, tabela 1 |
| Saída de 24 V | corrente máxima 300 mA; só para o sensor de zona de porta do resgate | ERB EN, PDF 1, tabela 1 e tabela de terminais |
| Proteção de sobrecarga na partida (tensão maior) | ≥ 4,5 A; proteção atua quando a sobrecarga dura 200 ms ou mais; nova liberação só depois de 1 minuto | ERB EN, PDF 1 |
| Sobrecarga na manutenção | ≥ 3,5 A (mesma lógica) | ERB EN, PDF 1 |
| Curto-circuito na partida | ≥ 6 A; nova liberação só depois de 5 minutos | ERB EN, PDF 1 |
| Curto-circuito na manutenção | ≥ 4,5 A | ERB EN, PDF 1 |
| Curto-circuito da saída 24 V | tensão vai a 0; volta imediatamente ao eliminar o curto | ERB EN, PDF 1 |
| Subtensão da bateria | não libera o freio se a tensão da bateria for menor que 10,2 V | ERB EN, PDF 1 |
| Bateria | chumbo-ácido 12 V, ≥ 7 Ah, 151 x 100 x 65 mm; vermelho no positivo e preto no negativo | ERB EN, PDF 2 (painel 5 e 8) |
| Consumo parado | sem consumo da bateria, além do próprio da bateria, quando desligado da rede e inativo | ERB EN, PDF 1 |
| Ambiente | -10 a 50 °C, 5 a 95% UR sem condensação, IP20, resfriamento natural, altitude < 3000 m ("derating when the altitude is higher than 100 m" conforme impresso), armazenamento -20 a +60 °C | ERB EN, PDF 1, tabela 1 |
| Massa | 3,73 kg com a bateria de 1,69 kg | ERB EN, PDF 1 (painel 3) |
| Sensor de zona de porta | fotoelétrico: 24 V, 200 mA máx. de entrada, saída 24 V, 5 mA máx.; chave magnética: 24 V, 5 mA | ERB EN, PDF 2 (painel 5) |

Resistência da bobina do freio: o manual (EN e CN) não informa limite de resistência.

### Terminais
Esquema /23 (PDF 25), tabela à esquerda, e manual ERB EN (PDF 1 e 2, painéis 4 e 5):

| Terminal | Função | Observação do manual |
|---|---|---|
| L, N | entrada de 220 VAC | no esquema vêm de 501 e 502 (POW1/1 e /2 da KCB) |
| ZQ1+ e ZQ2- (no esquema, ZQ+ e ZQ-) | polo positivo e negativo da tensão de liberação do freio | no esquema vão aos pinos 5 e 6 (ZQ+) e 12 e 11 (ZQ-) do MT1 |
| 24V, COM | polos positivo e negativo da saída de 24 V | só para o sensor de zona de porta do resgate; no esquema o "24V" fica sem fio e COM vai a KY10/3 (302) pelo SZ2/4 |
| MQ+ | entrada do sinal de zona de porta, nível alto válido | sensor do próprio resgate; não ligar ao sinal de zona de porta do circuito de segurança; só sensor de nível alto válido |
| MQ- | entrada de zona de porta, nível baixo válido (ligar o sinal ao COM) | no esquema MQ- vai a KY10/6 (302) pelo SZ2/9 e MQ+ a KY10/8 (FL1) pelo SZ2/5 |
| MS+, MS- | entrada do sinal de trinco da porta | "If you do not use it, short the MS+ and MS- terminals" (porta fechada por padrão); no esquema MS+ vai a KY11/5 (133) e MS- a KY11/6 (131) pelo SZ2/2 e /7 |
| BAT+, BAT- | bateria interna | o desenho do manual (figura 5) mostra também rótulos "DQ-, DQ+" no lugar de MS-/MS+; a tabela do texto fala de MS+/MS- |

### Soquete SZ, plugues SZ1, SZ2, MT e MT1 (folha /23)
Tabelas completas na Ficha 1. Resumo:
- SZ socket (na KCB): 1 = 101B, 2 = 133, 3 = DC12, 4 = 302, 5 = FL1, 6 = 101, 7 = 131, 8 = T02, 9 = 302, 10 = vazio.
- SZ1 plug (normal): só a ponte 1 a 6 (101B a 101).
- SZ2 plug (resgate): sem 1 e 6; 4 = COM, 9 = MQ-, 5 = MQ+, 2 = MS+, 7 = MS-, ponte 3 a 8 (DC12 a T02).
- MT plug (KCB): 1 = X18, 2 = X22, 3 = X20, 5 = ZQ1+, 6 = ZQ2+, 7, 8 e 9 = 301, 11 = ZQ1-, 12 = ZQ2-.
- MT1 socket: só 5 (ZQ1+), 6 (ZQ2+), 11 (ZQ1-), 12 (ZQ2-) ligados aos terminais ZQ+ e ZQ- do ERB.

### LEDs e botões
Indicadores (verde, vermelho, amarelo, azul, da esquerda para a direita; ERB EN, PDF 2, painel 6; e tabela do esquema /23):
| Indicador | Cor | Estados |
|---|---|---|
| Brake release (saída de tensão de liberação) | verde | aceso fixo: há tensão de liberação; apagado: não há |
| Fault | vermelho | aceso fixo: sobrecarga ou curto na saída do freio; apagado: normal |
| Battery | amarelo | aceso fixo: bateria cheia; piscando devagar: carregando ou descarregando; piscando rápido: nível baixo |
| Door zone | azul | aceso fixo: elevador em zona de porta quando a rede falha; apagado: fora da zona de porta |

Nota do manual: quando a bateria está sendo recarregada o indicador fica aceso; sem recarga, pressionar Start por 1 s acende o indicador e mostra o nível; apaga depois de 3 minutos.

Botões (três, com retorno; só valem enquanto pressionados): Start, Common, Forced.

### Regras do manual (sem passo a passo)
1. Antes de liberar o freio é preciso ativar a bateria: Start por 1 s; a bateria fica ligada por 3 minutos e depois desliga sozinha. Com o freio liberado, desliga 3 minutos após a liberação.
2. Fora da zona de porta: Start e Common juntos liberam o freio. Em zona de porta: Forced e Common juntos. Soltar um dos botões encerra a tensão.
3. O sinal de trinco da porta diz se a porta está fechada; se não estiver, não há tensão de liberação.
4. Lógica de tensão: 110 V por 2 s e depois 80 V por até 120 s; esse ciclo pode se repetir três vezes seguidas; depois é preciso esperar 10 minutos.
5. Bateria: troca recomendada a cada 2 anos; carregar por 12 h antes do primeiro uso; recarregar pelo menos uma vez por semestre; desligar da rede antes de trocar.
6. Regras da /23 (esquema): puxar o plugue SZ1 e inserir SZ2 no soquete SZ; puxar o plugue MT e inseri-lo no soquete MT1; ao final, voltar SZ1 ao SZ e o MT à placa de interface. O esquema também diz que a solução é para liberação do freio na falta da rede, que o sensor de zona de porta é alimentado pela fonte de emergência da caixa de teto e que o sinal de trinco é usado para saber se a porta está fechada.

### Liga a
KCB (POW1, KY10, KY11, SZ, MT, MT1), freio da máquina (bobinas BK1 e BK2 via ZQ+ e ZQ-) e sensor de zona de porta.

### Fonte
ERB EN, PDF 1 (painéis 1 a 4), PDF 2 (painéis 5 a 8); Esquema /23 (PDF 25) e /21 (PDF 23); lista de peças /3.a (PDF 5).

### Observações do esquema
1. O desenho mostra o ERB com os terminais L, N, 24V, COM, MQ-, MQ+, MS+, MS-, ZQ+, ZQ- (/23). O manual usa ZQ1+ e ZQ2- na tabela de terminais e ZQ2- e ZQ1+ na figura de ligação.
2. O terminal "24V" do ERB não recebe nem entrega fio no desenho da /23.
3. A /23 diz que o ERB-A1 serve para freios com tensão de partida e de operação não maiores que 110 VDC e 80 VDC.
4. O fluxograma da figura 6 do manual traz o texto "Press the buttons for at least 120s" ligado a "Elevator stops"; o texto do manual diz que a tensão de manutenção dura até 120 s.

### LACUNAS (perguntas)
1. Qual é a resistência e a corrente da bobina do freio da máquina de referência? O manual não traz limite de resistência; o limite de corrente é 4 A na excitação forte.
2. O ERB do quadro de referência é o A1 (com bateria) ou o A2 (a bateria é do cliente)? O esquema escreve "MCTC-ERB-A" na lista de peças.
3. O sensor de zona de porta do resgate é o mesmo da caixa de teto (FL1, FL2) ou há sensor próprio? O esquema liga MQ+ a FL1 e MQ- a 302.
4. Qual é o significado de "Press the buttons for at least 120s" na figura 6? O limite de 120 s é de manutenção da tensão ou tempo mínimo de aperto?
5. O manual trata como DQ+ e DQ- os terminais que o texto chama MS+ e MS-? Confirmar o rótulo do terminal na peça.
6. O manual dá altitude "< 3000 m (derating when the altitude is higher than 100 m)". Confirmar o limite de derating com o fabricante.

---

## Ficha 4: Botoeira de inspeção ("Emergency electric operation handle KKB4-1C-02")

### Função
Botoeira do quadro de comando usada para a operação elétrica de emergência (EEO). Contém o comutador CIS (quatro elementos de contato), os botões CIU E (subir) e CID E (descer) e o botão de emergência MES (Esquema /14, PDF 16). A /14 traz duas notas: (1) depois de ligado o bypass, o alarme sonoro e visual do fundo da cabine é acionado; (2) a velocidade de manutenção e a da operação elétrica de emergência devem ser separadas para cumprir a norma nacional. O parâmetro F3-25 "EEO speed" = 0,25 (/5).

### Dados e símbolos
Estados dos contatos como desenhados (CIS na posição de repouso): CIS 1-2 e CIS 11-12 fechados (desenhados com o traço de contato fechado); CIS 3-4 e CIS 13-14 abertos. Os números 3-4 e 13-14 de CIU E e CID E aparecem como contatos abertos.

### Conectores e pinos
Ligação à KCB pelo KY4 (12 pinos; tabela na Ficha 1). Rede de cada terminal da botoeira (Esquema /14, PDF 16):

| Elemento | Terminal | Vai para |
|---|---|---|
| CIS elemento 1-2 | 1 | barramento 301 (KY4/1) |
| | 2 | X9 (KY4/4) |
| CIS elemento 3-4 | 3 | barramento 301 (KY4/1) |
| | 4 | barramento que alimenta CIU E/3 e CID E/3 |
| CIS elemento 13-14 | 13 | nó B (saídas 14 de CIU E 13-14 e CID E 13-14 em paralelo) |
| | 14 | 118 (KY4/8) |
| CIS elemento 11-12 | 11 | 123 (KY4/11) |
| | 12 | 122B (KY4/10) |
| CIU E (botão subir), par 3-4 | 3 | barramento vindo de CIS 4 |
| | 4 | 55 (KY4/3), que vai a X10 |
| CIU E, par 13-14 | 13 | nó A, ligado a 125 (KY4/7) |
| | 14 | nó B |
| CID E (botão descer), par 3-4 | 3 | barramento vindo de CIS 4 |
| | 4 | 56 (KY4/2), que vai a X11 |
| CID E, par 13-14 | 13 | nó A, ligado a 125 (KY4/7) |
| | 14 | nó B |
| MES (botão de emergência), terminal 1 | 1 | 110 (KY4/9) pela /14; pela /19, do lado de KY4/12 |
| MES, terminal 2 | 2 | 101A (KY4/12) pela /14; pela /19, do lado de KY4/9 |
Resumo funcional como desenhado: 125 a 118 (KY4/7 a KY4/8) só fecha com CIS 13-14 fechado (comutador em EEO) e CIU E ou CID E apertado; 301 a 55 (ou 56) só com CIS 3-4 fechado e o botão apertado; 301 a X9 está fechado em repouso (X9 usa o parâmetro "116: EEO input (NC)"); 123 a 122B, em série na cadeia de segurança, fecha em repouso; MES 110 a 101A fica em série na cadeia de segurança (/19: 101A, MES, 110, MES-1, 110A, ... ).

### Liga a
KCB, conector KY4. Entradas X9, X10, X11 da MCB (pelo J10).

### Fonte
Esquema /14 (PDF 16), /19 (PDF 21), /5 (PDF 7).

### Observações do esquema
1. Os símbolos de CIS 1-2 e 11-12 mostram contato fechado em repouso; os de 3-4 e 13-14, aberto (ampliado no PDF 16).
2. A cadeia de segurança da /19 passa por KY4/11 (123), CIS 12 a 11, KY4/10 (122B) e S1.
3. Os botões CIU E e CID E também aparecem como "CIU" e "CID" no trecho da /19 ao lado de CIS, em paralelo entre KY4/7 e CIS 13.

### LACUNAS (perguntas)
1. O desenho não indica se os quatro elementos de CIS são de um único comutador de três posições ou de duas. O comutador tem posições "normal" e "inspeção/emergência" apenas?
2. Qual a numeração real dos terminais do MES (1 e 2): a da /14 ou a da /19? A diferença não muda a ligação elétrica.
3. A KKB4-1C-02 tem botão "comum" (como o TCIB da caixa de teto) ou só CIU E e CID E? A /14 não traz.
4. Qual a corrente e tensão de contato da botoeira KKB4-1C-02 (nenhuma folha dá)?

---

## Ficha 5: Placa principal MCTC-MCB-C3 (dentro do inversor)

### Função
- "Main control board", placa principal de controle do NICE3000new integrado ao inversor "NICE-L-C-40XX" (Esquema /9, PDF 11; lista de peças, PDF 5). Recebe as entradas X1 a X22 e entrega as saídas W1 a W7 pelo cabo de 40 vias com a KCB (J10) e tem, além disso, as entradas de alta tensão X25 a X28 em CN2 (Esquema /16 e /19).
- A /9 (PDF 11, Remark 1) diz que a placa PG-D ou PG-E, para máquina síncrona, liga seu J1 ao "J2 of MCTC-MCB-C3", e que o CN1 da PG é a porta do encoder; o manual NICE3000new chama o conector da placa PG de J12.

### Conectores CN1 a CN9 (manual NICE3000new, PDF 60 a 62, impressas 59 a 61)
O esquema Vitinho não desenha CN1, CN4 a CN9; só CN2 (/16, /19) e CN3 (/47, PDF 49). O manual descreve (Tabela 2-15, PDF 61, e Tabela 2-16 e texto, PDF 62):

| Conector | Sinais | Característica (manual) |
|---|---|---|
| CN1 | X1 a X16 | entradas digitais de 10 a 30 VDC; impedância de entrada 4,7 kΩ; isolação por optoacoplador; corrente limitada em 5 mA; funções em F5-01 a F5-24 |
| CN9 | X17 a X24; Al-M, Al+ | X17 a X24 entradas digitais; Al-M e Al+ entrada analógica para o dispositivo de pesagem (célula de carga) |
| CN3 | +12V, MCM, M24, MCM, MOD+, MOD-, CAN1+, CAN1- | +12V/MCM: entrada externa de 12 VDC (emergência); M24/MCM: entrada externa de 24 VDC da placa toda; MOD+/-: RS485 isolado para chamadas de pavimento e display; CAN1+/-: CAN para a placa de cabina (CTB), placa de monitoramento sem casa de máquinas e placa de expansão DI/DO |
| CN2 | XCOM, X25, X26, X27, X28, XCOM | detecção de alta tensão: 110 VAC ± 15% ou 110 VDC ± 20%; cadeia de segurança e circuito de trincos; funções em F5-37 a F5-40 |
| CN7 | Y1/M1 a Y6/M6 | saída a relé, contato NA 5 A / 250 VAC; funções em F5-26 a F5-31 |
| CN8 | USB | interface de comissionamento por celular (Bluetooth), RS232 |
| CN4 | MOD2+, CAN2+, CAN2-, CAN3+, MOD2-, CAN3- | MOD2: RS485 para monitoramento residencial e IoT; CAN2: controle paralelo/grupo; CAN3: reservado |
| CN5 | DB9 | RS232: software de comissionamento, monitoramento, controle paralelo/grupo RS232/RS485, gravação de software da MCB e do DSP |
| CN12 | RJ45 | interface do painel de operação |
| J12 | | interface da placa PG |
| J1, J5, J6, J7, J8, J9, J10, J13, J14 | | reservados de fábrica (J1: aterramento opcional do AI; J5 e J13/J14: terminação; J7 e J8: PE de 24 V; J9/J10: não curtocircuitar) |

Atenção: o "J10" do manual é um conector reservado da MCB; o "J10" do esquema é o conector de 40 vias da KCB. São peças diferentes.

### Conector CN2 e entradas X25 a X28 (esquema /16 e /19)
| Pino de CN2 | Sinal | Rede | Origem na KCB | Parâmetro e função (/5) |
|---|---|---|---|---|
| 1 | XCM1 | 102 | KY1/6 | |
| 2 | X25 | 130 | KY1/1 | F5-37 = 4 "Safety circuit signal" |
| 3 | X26 | 131 | KY1/4 | F5-38 = 7 "Door 1 lock shorting signal" |
| 4 | X27 | 134 | KY1/2 | F5-39 = 5 "Door lock circuit signal" |
| 5 | X28 | 133 | KY1/3 | F5-40 = 8 "Door 2 lock shorting signal (set for double-door elevators)" |
| 6 | XCM2 | 102 | linha de retorno "102 / 17.2:E" | |
Cada entrada tem indicador luminoso e resistor em série no desenho (/16). Redes 130 a 134 formam a cadeia de segurança e trincos (/19: 130 após o interruptor de segurança das portas, 131 após os trincos da cabine, 132 após os trincos de pavimento, 133 após os trincos traseiros, 134 após o trinco GS2). O manual confirma a faixa de 110 VAC ± 15% / 110 VDC ± 20% (mesma tabela, CN2).

### Cabo flat de 40 vias MCB e KCB (J10)
- A /20 (PDF 22) desenha um feixe com os 40 sinais já listados na Ficha 1 ("Sinais de J10"). O desenho não escreve "flat"; mostra o J10 com 2 fileiras de 20 pinos (a /21).
- Lado da MCB, em ordem: X1 a X22, W1, W2, W2A, W3, W4, W5, W6, +24V, W7, M24, MCM, MCM, MCM, +12V, CAN-, CAN+, MOD1+, MOD1-.
- Ligações: X1 a X22 direto; W1 a W7 às saídas Y1 a Y7 da KCB; M24 a 301; os três MCM a 302; +12V a T02; CAN-, CAN+, MOD1+, MOD1- direto.
- O manual NICE3000new não menciona KCB, o cabo de 40 vias nem a ligação com a placa de interface.

### Liga a
KCB (J10 e KY1), placa PG (J1 da PG ao conector da MCB), painel de operação (CN12), placa de cabina (CAN1 em CN3) e, em controle paralelo, a outra MCB (CN3:8 MCM, CN3:9 CAN2+, CN3:10 CAN2- na /47, PDF 49).

### Fonte
Esquema /9 (PDF 11), /16 (PDF 18), /19 (PDF 21), /20 (PDF 22), /47 (PDF 49), /5 (PDF 7); Manual NICE3000new, PDF 60 a 62 (impressas 59 a 61).

### Observações do esquema
1. A numeração de CN3 no esquema (CN3:8, :9, :10 para MCM, CAN2+ e CAN2-, folha /47) não coincide com o manual, em que CN3 tem 8 sinais (sem CAN2) e CAN2 está em CN4.
2. A /9 chama de "J2 of MCTC-MCB-C3" o conector da placa PG; o manual chama de J12.
3. Na /9 (Remark 3): "x23 and x24 input port only for the use of a function, if repeated function, need to find the input point again".
4. Na /9 (Remark 4): "This circuit applies to MRL".
5. Lista de parâmetros da /5: F0-01 = 1; F1-25 define o tipo de motor; F5-25 "CTB input type 1856 (Bit6/8/9/10 are set to 1)"; F6-40 Bit1 = 1 (limite por software); F6-52 Bit1 = 1 suporta MCTC-SCB-A4/D4 e Bit6 = 1 nivelamento por sinal CAN; F8-10 = 1 "Emergency evacuation by automatic rescue device (ARD) (optional)". Nota 1 da /5: o quadro novo liga a caixa de inspeção do teto por comunicação; o sinal de inspeção e o de nivelamento sobe/desce viajam por comunicação.

### LACUNAS (perguntas)
1. O esquema não desenha CN1, CN4 a CN9 da MCB-C3. Existe esquema ou foto da MCB-C3 real que confirme que a numeração e os sinais de CN1 a CN9 são os do manual do NICE3000new (que cobre o controlador integrado)?
2. Qual é o conector da MCB para o cabo de 40 vias da KCB? O esquema só nomeia o J10 do lado KCB.
3. A numeração dos 40 pinos do J10 (ver Ficha 1, lacuna 3).
4. O cabo de 40 vias é flat (fita) de 2 x 20 e qual o comprimento padrão? O esquema não diz.
5. A placa PG do quadro de referência é a MCTC-PG-E (síncrona) ou a PG-A2 (assíncrona)? A /9 cita ambas na Remark 2.

---

## Comparação com o esquema alternativo (só confirmação; não é fonte)
Esquema Elétrico Elevadores Verticalparts.pdf, desenho 19060918-ZL, 58 folhas, 2022-10-11, com anotações em português. Foram comparados os PDF 4 (folha /12, alimentação do comando) e PDF 8 (folha /16, bypass).
- Iguais ao Vitinho: F3 = 250 VAC / 1 A; F1 "Door/light curtain fuse" 250 VAC / 4 A; QFB2 2P / 6 A curva C; OVP "300VAC protection/285VAC recover"; PS-24V 7 A; PS-110V "max 5.6A"; transformador 220 V / 125 V, 50 Hz, 63 VA (3,7 a 22 kW) e 110 VA (30 a 37 kW); ligações KY1/1, /2, /3, /4, /6 a X25, X27, X28, X26 e XCM1; S1 e S2 com os mesmos pinos na /16.
- Diferentes: o disjuntor do circuito de segurança da folha /12 do alternativo é "QF1, 1P / In = 1A / C type" (no Vitinho, QFB1 é 1P+N / In = 10 A / C type). Na /12 do alternativo o F1 aparece desenhado dentro da KCB na linha 207 antes de AA/1; no Vitinho, F1 está na linha para "+CC-207".
- A folha /16 do alternativo traz uma anotação própria: "Funcionamento normal, jumper no S1"; "Bypass de porta de cabina, jumper na parte de baixo do S2"; "Bypass de porta de pavimento, jumper na parte de cima do S2". O quadro de estados do Vitinho (S2 (1-5) ON para porta de pavimento; S2 (2-6) ON para porta de cabine) não foi reconciliado com isso (ver Ficha 1, lacuna 9).
- Valores de resgate, PCB-D1 (B0-xx, 6 A, 4 A) e as demais folhas não foram conferidos no alternativo.
