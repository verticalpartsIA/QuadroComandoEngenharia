# Capítulo 3: fichas de componente (potência e alimentação)

Variante de referência: 7,5 kW / 380 V trifásico, MRL, 3 paradas, 1 porta. Material de apoio para redação. Não é prosa de capítulo.

## 0. Convenções e fontes

**Documentos**
- **Esquema Vitinho**: `Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf`, desenho 19061867-ZL, Inovance, versão A00, 51 folhas. Citado como "Esquema /N (PDF M)". Da folha /4 em diante, PDF = folha + 2.
- **Manual**: `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`, 368 págs. Citado como "Manual PDF M (impr. K)". A página impressa é sempre o PDF menos 1.
- **Esquema alternativo** (só comparação): `Esquema Elétrico Elevadores Verticalparts.pdf`, 37 págs. Citado como "Alt. PDF M".

**Correção de mapeamento das folhas.** No Esquema Vitinho, a lista de peças e a legenda de componentes estão nas folhas /3 e /3.a (PDF 4 e 5). A folha /4 (PDF 6) traz as regras de nomenclatura de fios e a tabela de cores de cabo. A folha /5 (PDF 7) traz a lista de parâmetros.

**Folhas usadas nesta ficha**

| Folha | PDF | Título no esquema |
|---|---|---|
| /3 e /3.a | 4 e 5 | Parts list (legenda de componentes) |
| /4 | 6 | Regras de nomenclatura de fios |
| /5 | 7 | List of Parameters |
| /7 | 9 | Main power supply of MR (variante sala de máquinas, só para comparação) |
| /8 | 10 | Main power supply of MRL |
| /9 | 11 | Drive power supply |
| /10 | 12 | Control power supply 1 |
| /11 | 13 | Control power supply 2 |
| /12 | 14 | Control power supply 3 |
| /13 | 15 | Brake control circuit |
| /16 | 18 | High voltage detection point circuit |
| /17 | 19 | Contactor Control and Feedback |
| /22 | 24 | Speed limiter remote action/release circuit (Use for MRL) |
| /23 | 25 | Electric brake release circuit (Use for MRL) |
| /46 | 48 | Hoistway lighting circuit |

**Observação sobre a notação de posição do esquema.** Referências como "9.2:A" significam folha 9, coluna 2, linha A.

**Fora de escopo.** Versões 220 V e 15 kW: só mencionadas onde o manual mistura as tabelas.

---

## 1. Ficha: inversor NICE3000new (controlador integrado)

### 1.1 Função
Controlador integrado de elevador. Reúne o controlador lógico (placa MCB) e o inversor vetorial de CA. Controla o motor pelo encoder e fala com a caixa de teto (MCTC-CTB) por CAN e com os chamadores por Modbus. (Manual PDF 35 (impr. 34), item 1.5.)

### 1.2 Identificação no esquema
- Rótulo: "NICE-L-C-40XX, Inverter". O esquema não fixa a potência: o "XX" é genérico. (Esquema /9, PDF 11; legenda /3.a, PDF 5.)
- Placa principal do comando (MCB): "MCTC-MCB-C3". (Esquema /16, PDF 18.)
- Placa de PG (encoder) "MCTC-PG-E", ligada ao inversor pelo conector J12 (lado inversor) e J1 (lado PG). (Esquema /9, PDF 11.)

### 1.3 Modelo para 7,5 kW / 380 V (manual)

| Dado | Valor | Fonte |
|---|---|---|
| Modelo | NICE-L-C-4007 | Manual Tabela 1-1, PDF 30 (impr. 29); Tabela 3-21, PDF 111 (impr. 110) |
| Faixa de tensão | trifásica 380 V, faixa 380 a 440 V, 50/60 Hz | Manual Tabela 1-1, PDF 30 |
| Capacidade | 11,0 kVA | Idem |
| Corrente de entrada | 20,5 A | Idem |
| Corrente de saída | 18,0 A | Idem |
| Motor aplicável | 7,5 kW | Idem |
| Tolerância de rede | -15% a +10% em tensão; -5% a +5% em frequência | Manual Tabela 1-2, PDF 31 (impr. 30) |
| Subtensão (classe 400 V) | segue operando acima de 300 VAC; abaixo disso, proteção de subtensão após 15 ms | Manual Tabela 1-2, PDF 31 |
| Sobretensão de entrada (classe 400 V) | acima de 725 V, detectada na parada | Manual Tabela 1-2, PDF 33 (impr. 32) |
| Limite do barramento CC (série 380 V) | sobretensão em 800 V | Manual Tabela 1-2, PDF 33 |
| Sobrecarga do inversor | 60 s a 150% e 10 s a 200% da corrente nominal | Manual Tabela 1-2, PDF 33 |
| Torque de frenagem | 150% com resistor externo; unidade de frenagem interna | Manual Tabela 1-2, PDF 32 (impr. 31) |
| Frequência de saída / portadora | 0 a 99 Hz / 2 a 16 kHz | Manual Tabela 1-2, PDF 32 |
| Grau de proteção, resfriamento, instalação | IP20, ar forçado, montagem em quadro | Manual Tabela 1-2, PDF 34 (impr. 33) |
| Ambiente | -10 a 50 °C (derating acima de 40 °C); umidade abaixo de 95% sem condensação; altitude abaixo de 1000 m (derating de 1% por 100 m acima) | Manual Tabela 1-2, PDF 34 |
| Sistema de distribuição | TN/TT | Manual Tabela 1-2, PDF 34 |

**Nomenclatura do modelo.** "NICE-L-C-4007": L = específico para elevador; C = motor síncrono ou assíncrono; "40" = classe trifásica 380 V; "07" = código de potência 7,5 kW. (Manual PDF 25 (impr. 24), Figura 1-1.) A tabela de designação do manual lista os códigos 02 = 2,2 kW, 03 = 3,7 kW, 37 = 37 kW etc. O código "07" para 7,5 kW não aparece literalmente nessa tabela; ele resulta da Tabela 1-1, onde 4007 corresponde a 7,5 kW.

### 1.4 Bornes de potência (manual)

Disposição para modelos abaixo de 37 kW: (-) (+) R S T / PB U V W; lado esquerdo POWER, lado direito MOTOR. (Manual PDF 50 e 51 (impr. 49 e 50), Figuras 2-12 e 2-13.)

| Borne | Nome | Função (Tabela 2-7) |
|---|---|---|
| R, S, T | Entrada trifásica | Alimentação trifásica de CA. Sem exigência de sequência de fases na entrada. |
| (+) e (-) | Barramento CC | Para unidade de frenagem externa e regeneração, em modelos de 37 kW ou mais. Tem tensão residual após desligar: aguardar 10 min e tensão abaixo de 36 VDC. |
| (+) e PB | Resistor de frenagem | Em modelos abaixo de 37 kW, liga o resistor de frenagem. Cabo do resistor menor que 5 m. Proibido ligar o resistor direto ao barramento CC. |
| U, V, W | Saída para o motor | Motor trifásico. Proibido ligar capacitor ou supressor de surto na saída. Cabo blindado, com a blindagem ao terra. |
| PE | Terra | Terminal de aterramento. |

Fonte da tabela: Manual PDF 52 (impr. 51). Cuidados de cada borne: PDF 52 e 53 (impr. 51 e 52).

**Tamanho de terminal e parafuso.** O manual mostra os desenhos dos tamanhos C, D, E (plástico) e F (chapa) com parafusos combinados M4, M5 e M6 (Figura 2-15, PDF 55 (impr. 54)). O texto extraído não amarra o NICE-L-C-4007 a um desses tamanhos. Ver Lacunas.

### 1.5 Bornes de controle (manual, Tabela 2-15, PDF 61 e 62 (impr. 60 e 61))

| Conector | Sinais | Função e dados |
|---|---|---|
| CN1 | X1 a X16 (DI) | Entradas digitais, 10 a 30 VDC, impedância 4,7 kΩ, limite de corrente 5 mA, isolação por optoacoplador. Funções em F5-01 a F5-24. |
| CN9 | X17 a X24 (DI) e Al-M/Al+ (AI) | X17 a X24 como acima. Al-M/Al+ é a entrada analógica para célula de carga. Segundo a seção 2.3.2: faixa de -10 a +10 VDC, impedância 33,9 kΩ, cabo blindado de menos de 20 m. |
| CN3 | +12V/MCM, M24V/MCM, MOD+/MOD-, CAN1+/CAN1- | +12V/MCM: entrada externa de 12 VDC (emergência). M24V/MCM: entrada externa de 24 VDC para a placa toda. MOD+/-: RS485 isolada, para chamadas de pavimento e display. CAN1+/-: comunicação com a caixa de teto (CTB), placa de monitoramento sem sala de máquinas e placa de expansão DI/DO. |
| CN2 | XCOM, X25, X26, X27, X28, XCOM | **Detecção de tensão alta**: 110 VAC ±15% ou 110 VDC ±20%. Usada no circuito de segurança e na cadeia de portas. Funções em F5-37 a F5-40. |
| CN7 | Y1/M1 a Y6/M6 | Saídas a relé, contato NA, 5 A / 250 VAC. Funções em F5-26 a F5-31. |
| CN4 | MOD2+/-, CAN2+/-, CAN3+/- | MOD2: monitoramento residencial e IoT. CAN2: operação em paralelo ou em grupo. CAN3: reservado. |
| CN5 | DB9 (RS232) | Software de comissionamento, monitoramento residencial, paralelo/grupo, download de software da MCB e da placa DSP. |
| CN8 | USB | Interface de comissionamento por celular (Bluetooth). |
| CN12 | RJ45 | Painel de operação. |
| J12 | PG card | Placa de encoder. |
| J1, J5 a J10, J13, J14 | Reservados de fábrica | J1 (terra opcional da AI), J5 e J13/J14 (resistor de terminação de MOD2 e CAN2, ligados por padrão nos pinos "ON"), J7 e J8 (PE de 24 V interna e externa, em curto por padrão), J9/J10 (não fazer curto). |

**Tensão de X25 a X28:** 110 VAC ±15% ou 110 VDC ±20% (Manual PDF 61 (impr. 60)). As demais entradas (X1 a X24): 10 a 30 VDC, nominal 24 VDC.

**Relés Y1 a Y6** (seção 2.3.3, PDF 65 (impr. 64)): 5 A / 250 VAC ou 30 VDC. Corrente máxima de 10 A em Y1 a Y3 e 5 A em Y4 a Y6. Há TVS nos contatos Y1 a Y3, por isso "marcha, freio e curto no estator do motor" devem ficar nas saídas Y1 a Y3. Não é preciso circuito de absorção nas bobinas dos contatores externos. O mesmo texto manda ligar o XCOM ao neutro de 110 V do circuito de segurança.

**Observações do manual a registrar.**
- A Tabela 1-2 (PDF 32) fala em 24 DI de baixa tensão e 3 DI de alta tensão, mas a Tabela 2-15 mostra quatro entradas de alta tensão (X25 a X28).
- A seção 2.3.3 (PDF 65) cita "CN4" para o XCOM, mas a Tabela 2-15 e o esquema usam CN2.
- A Tabela 2-16 (PDF 62 (impr. 61)) diz "X5 a X28" para o LED de alta tensão, provável erro de impressão (esperado X25 a X28).
- Limite de contato do relé: "5A28VDC" na Tabela 1-2 (PDF 32) contra "30 VDC" na seção 2.3.3 (PDF 65).

### 1.6 Recomendações de cabo, disjuntor e contator (NICE-L-C-4007, 380 V)

Manual Tabela 3-2, PDF 87 (impr. 86). Usar cobre.

| Item | Valor |
|---|---|
| Fusível de entrada (Bussmann FWH, certificado UL) | FWH-35B |
| Disjuntor recomendado | 32 A |
| Contator recomendado | 25 A |
| Cabo principal | 4 mm² |
| Cabo de controle | 0,75 mm² |
| Cabo de aterramento | 4 mm² |
| Torque do borne de potência | 2,5 N·m (Tabela 2-9, PDF 56 (impr. 55)) |
| Terminal de cabo recomendado | GTNR4-5 (Tabela 2-9) |

Para conferência: Tabela 2-9 repete corrente de entrada de 20,5 A e cabo de entrada e saída de 4 mm².

**Cabos de controle** (Tabela 2-17, PDF 63 (impr. 62)): 0,2 a 0,75 mm² (AWG24 a 18), torque 0,565 N·m, ponteira tubular isolada com 6 mm de condutor exposto.

**Disjuntor diferencial (ELCB).** O manual diz que a corrente de fuga do controlador passa de 3,5 mA e exige aterramento de proteção. Como o controlador gera corrente de fuga CC no condutor de proteção, o texto manda usar ELCB tipo B com atraso. (Manual PDF 89 (impr. 88).)

**Contator.** O contator de entrada serve para ligar e cortar a alimentação do controlador; não partir e parar com ele mais de duas vezes por minuto e não usá-lo para partir o controlador direto. (Manual Tabela 3-1, PDF 85 (impr. 84).)

### 1.7 Regras de aterramento (manual)
1. Resistência do cabo de terra do circuito principal menor que 10 Ω. (Manual PDF 54 (impr. 53).)
2. Não ligar o PE ao condutor neutro da alimentação. (Idem.)
3. Condutor PE: seção igual à da fase se S ≤ 16 mm²; 16 mm² se 16 < S ≤ 35 mm²; S/2 se S > 35 mm² (Tabela 2-8). Cor verde e amarela. (Idem.)
4. Instalar o controlador sobre plano metálico condutor, com todo o fundo em bom contato; instalar filtro e controlador no mesmo plano. (Idem.)
5. Cabo entre filtro e bornes de entrada com menos de 30 cm e terras do filtro e do controlador interligados. (Manual PDF 52 (impr. 51) e PDF 95 (impr. 94).)
6. Blindagem do cabo de saída ligada ao cabo de terra, com a ponta de saída da blindagem o mais curta possível e largura de pelo menos 1/5 do comprimento. (Manual PDF 53 e 54.)
7. Em classe 400 V, aterrar o ponto neutro da alimentação do controlador. (Manual PDF 344 (impr. 343), item A.2.4.)
8. Blindagem do cabo de encoder aterrada em uma só ponta, no lado do controlador. (Manual PDF 145 (impr. 144), lista de verificação de comissionamento.)
9. Lista de verificação de fiação: item 11 "Verificar se o cabo de terra está bem aterrado". (Manual Tabela 2-20, PDF 79 (impr. 78).)

### 1.8 Resistor de frenagem (manual)

Manual Tabela 3-12, PDF 100 (impr. 99), linha NICE-L-C-4007 (380 V, motor 7,5 kW):

| Dado | Valor |
|---|---|
| Resistência máxima | 85 Ω |
| Resistência mínima | 65 Ω |
| Potência do resistor | 2500 W |
| Unidade de frenagem | interna (built-in) |

Condições:
- Fórmulas e coeficiente K de aproximadamente 50% e frequência de frenagem D típica de 20% a 30% para elevador (Tabela 3-11, PDF 99 (impr. 98)).
- Nota: o cálculo da tabela toma o motor síncrono como exemplo; para motor assíncrono pode-se reduzir a potência do resistor ou aumentar a resistência (PDF 101 (impr. 100)).
- Cabo do resistor menor que 5 m (PDF 53).

**No esquema:** o resistor aparece como "DBR-B Braking resistor box" com "DBR Braking resistor", ligado aos bornes (+) e PB do inversor; o borne (-) fica sem ligação. A caixa tem PE. Não há valor em ohms ou watts no esquema. (Esquema /9, PDF 11; legenda /3, PDF 4, "External".)

### 1.9 Dimensões e fixação (NICE-L-C-4007, 380 V)

| Dado | Valor | Fonte |
|---|---|---|
| Estrutura | Plástico (faixa 2,2 a 15 kW) | Manual Tabela 2-2, PDF 42 (impr. 41) |
| Altura H | 347 mm | Idem |
| Largura W | 223 mm | Idem |
| Profundidade D | 173,5 mm | Idem |
| Furos de fixação: A (horizontal) e B (vertical) | A = 150 mm, B = 334,5 mm | Idem |
| Diâmetro do furo | 6,5 mm | Idem |
| Peso bruto | 7 kg | Idem |

Folgas de montagem para 2,2 a 15 kW: lateral A ≥ 10 mm, superior e inferior B ≥ 100 mm (Manual PDF 40 (impr. 39), Figura 2-2). Montar na vertical. Calor sai de baixo para cima (PDF 41).

Fixação: montagem em parede dentro do quadro com quatro parafusos; é proibido fixar só os dois parafusos de cima. (Manual PDF 47 (impr. 46).) Recomendações para o projeto do quadro: temperatura interna até 10 °C acima da externa, ventilador em quadro fechado, ar do ventilador não direto sobre o inversor, entrada de ar embaixo (PDF 47).

### 1.10 Filtro EMC recomendado pelo manual para o 4007 (380 V)
- Filtro padrão: Jianli DL-25EBK5 ou Schaffner FN 3258-30-33. (Manual Tabela 3-9, PDF 96 (impr. 95).)
- Filtro simples: Jianli DL-35EB1/10. (Manual Tabela 3-10, PDF 97 (impr. 96).)

### 1.11 Observações do esquema sobre o inversor
- Entrada: TA R, S, T da folha /9 vai aos bornes R, S, T do inversor. Da mesma barra, R e N derivam para "+CC-R / 10.2:A" e "+CC-N / 10.2:A" (alimentação do comando, folha /10). (Esquema /9, PDF 11.)
- Saída: U, V, W do inversor vão aos polos 1, 3, 5 de SW; os polos 2, 4, 6 de SW vão a TA U, V, W. (Esquema /9.)
- PE do inversor ligado ao PE de "+EX-PE". (Esquema /9.)
- Observações 1 a 4 da folha /9: (1) PG-D e PG-E são para máquina síncrona, J1 do PG ao J2 da MCTC-MCB-C3; o CN1 do PG é a porta de sinal do encoder. (2) MCTC-PG-A2 é para máquina assíncrona. (3) "x23 e x24 input port only for the use of a function, if repeated function, need to find the input point again". (4) "This circuit applies to MRL".
- Parâmetros do esquema (folha /5, PDF 7): F0-01 = 1 (fonte de comando), F1-25 (tipo de motor: 0 assíncrono, 1 síncrono; valor não fixado), F8-10 = 1 ("Emergency evacuation by automatic rescue device (ARD), optional"), saídas Y1 = 1 (contator de marcha), Y2 = 2 (contator de freio), Y3 = 12 (controle de curto no estator), entradas X6 = 38, X7 = 39, X8 = 30, X25 = 4, X26 = 7, X27 = 5, X28 = 8.
- Parâmetros do motor (F1-01 a F1-05, F0-03 a F0-05) aparecem como "Model dependent": o esquema não traz valores.

### 1.12 Lacunas (perguntas ao responsável técnico)
1. O esquema não fixa o modelo do inversor ("40XX"). Confirmar que o inversor entregue na variante de 7,5 kW é o NICE-L-C-4007 (e não outro de potência maior).
2. Qual tamanho de borneira (C, D ou E, M4/M5/M6) tem o NICE-L-C-4007? O texto extraído do manual não liga o modelo ao desenho.
3. Qual resistor de frenagem é realmente instalado na caixa "DBR-B" (ohms, watts)? O esquema não informa. O manual recomenda entre 65 e 85 Ω e 2500 W para o 4007.
4. O motor é síncrono (com FX) ou assíncrono? O esquema marca FX como "Add when synchronous". O parâmetro F1-25 não vem preenchido.
5. O filtro EMC fica no "EMC filter cabinet" no poço (+H) conforme o esquema, e o manual exige cabo de menos de 30 cm entre filtro e inversor. Como é a instalação real?
6. A alimentação trifásica do inversor passa por contator de entrada? No esquema não existe contator entre o filtro EMC e os bornes R, S, T (o contator de potência SW fica na saída, entre inversor e motor).

---

## 2. Ficha: disjuntor geral QF e disjuntores QFB1, QFB2, QFB3, QFB4

### 2.1 Quadro-resumo (Esquema Vitinho)

| Tag | Descrição no esquema | Tipo, polos, corrente | Folha | Observação |
|---|---|---|---|---|
| QF | "Main switch" (disjuntor geral) | 4 polos (bornes 1 a 8, para L1, L2, L3, N). Corrente não indicada. | /8 (PDF 10), /7 (PDF 9) | Legenda: "Main switch", no quadro de comando (/8.2:C). |
| QFB1 | "Safety circuit breaker" (disjuntor do circuito de segurança) | 1P+N, In = 10 A, curva C ("1P+N/In=10A/C type") | /10 (PDF 12) | Alimentado pelo secundário de 125 V do TRF. |
| QFB2 | "Air breaker for control power" (disjuntor da alimentação de comando) | 2P, In = 6 A, curva C ("2P/In=6A/C type") | /10 (PDF 12) | Alimentado por +CC-R e +CC-N (derivados de TA R e N). |
| QFB3 | "RCD for car top" (diferencial da caixa de teto) | 2P, In = 6 A, IΔn = 0,03 A, tipo D ("2P/In=6A/IΔn=0.03A/D type") | /8 (PDF 10) | Ligado antes do QF. |
| QFB4 | "RCD for history lighting" (diferencial da iluminação do poço, "history" no esquema) | 2P, In = 6 A, IΔn = 0,03 A, tipo D | /8 (PDF 10) | Ligado antes do QF. |

Na folha /7 (variante sala de máquinas, só comparação), QFB3 e QFB4 aparecem como "tipo C" (PDF 9). Na folha /8 (MRL), como "tipo D" (PDF 10).

### 2.2 Para onde vai cada saída

**QF** (Esquema /8, PDF 10)
- Entrada: bornes 1, 3, 5, 7 recebem L1, L2, L3, N de XA R, S, T, N (do alimentador externo L1, L2, L3, N, PE).
- Saída: bornes 2, 4, 6, 8 vão às entradas L1, L2, L3, N do filtro EMC ("EMC filter cabinet", no poço +H); as saídas R, S, T, N do filtro seguem para "9.2:A" (TA da folha /9).

**QFB3**
- Entrada: bornes 1 e 3, tomados a montante do QF: fase da linha L1/R e neutro N.
- Saída: borne 2 vai a 501 e borne 4 vai a 502. A 501/502 alimentam "7.4:F" (folha /7) e "11.2:A" (folha /11, entrada POW1 1 e 2 da placa MCTC-KCB-B4A, com fusível F2, 4 A / 250 VAC, até 507/508 no ventilador e iluminação da cabina) e a iluminação do quadro de comando (CTRL, com chave). (Esquema /8, PDF 10; /11, PDF 13.)
- A folha /23 mostra 501/502 também alimentando L e N do dispositivo de resgate elétrico MCTC-ERB-A ("AC220V input"). (Esquema /23, PDF 25.)

**QFB4**
- Entrada: bornes 1 e 3, tomados a montante do QF (fase da linha L1/R e neutro N).
- Saída: borne 2 vai a LIHS1 (borne comum 11) e ao pino 2 da tomada CZ; borne 4 vai a XB 802 e ao pino 1 da tomada CZ. LIHS1: 12 vai a XB 807 e 14 vai a XB 809. (Esquema /8, PDF 10, leitura em detalhe.)
- XB 807, 809, 802 e +H-PE seguem para a folha /46, iluminação do poço. (Ver ficha 5.)

**QFB2**
- Entrada: +CC-R e +CC-N, vindos de TA R e N da folha /9 (nos pontos 9.3:B). Aparecem como bornes 1 e 2 do disjuntor.
- Saída: bornes 3 e 4 vão a 201 e 202. Esses dois fios alimentam o circuito de acionamento remoto do limitador de velocidade ("Used for speed limiter remote action/release circuit", folha /22) e a placa MCTC-KCB-B4A (KY5-1 = 201 e KY5-5 = 202), que passa pela proteção contra sobretensão (OVP) e gera 207/208. (Esquema /10, PDF 12.)

**QFB1**
- Entrada: borne N vai a 0S do TRF; borne 1 vai a 125 V do TRF.
- Saída: borne N vai a KY5-8 (rede 102); borne 2 vai a KY5-7 (rede 101, com fusível F3 de 250 VAC / 1 A, e "101A"). Na caixa tracejada "Used for MRL": a rede 101 recebe "101 / 23.4:B" e sai "+CC-101B / 23.4:B", com a nota "Short when used for MR". (Esquema /10, PDF 12.)

### 2.3 Dados do manual relevantes para o QF
- Disjuntor recomendado pelo fabricante do inversor 4007: 32 A. Fusível FWH-35B. (Manual Tabela 3-2, PDF 87 (impr. 86).)
- Disjuntor "short circuit breaker" ou ELCB, entre a rede e o controlador. Ver também a exigência de ELCB tipo B com atraso para a corrente de fuga CC (Manual PDF 85 e 89).

### 2.4 Observações do esquema
- Aviso, folhas /8 e /7: "CAUTION! After disconnecting the main switch QF, there will still be voltage in the QFB3/4 loop". Ou seja, QFB3 e QFB4 são alimentados antes do QF.
- QFB1 e QFB2 têm o mesmo símbolo gráfico de QFB3 e QFB4 (bobina e bloco "I>"), mas a especificação em texto não traz IΔn. O desenho não deixa claro se há bloco diferencial.
- A legenda (/3 e /3.a, PDF 4 e 5) lista QF, QFB3 e QFB4 também em "Power box" (caixa de força da variante sala de máquinas, folha /7) e QF, QFB1 a QFB4 em "Control cabinat".
- Esquema alternativo (comparação de nomes): QF "Disjuntor principal", QFB2 "Disjuntor do comando", QFB1 "Disjuntor do circuito de segurança", QFB3 "Disjuntor da luz da cabina", QFB4 "Disjuntor da iluminação da caixa (de corrida)". (Alt. PDF 2 e 4.) Os nomes em português do alternativo não coincidem com os do Vitinho para QFB3 e QFB4 ("RCD for car top" e "RCD for history lighting"). O Vitinho é a base.

### 2.5 Lacunas
1. Corrente nominal, poder de corte e curva do QF não constam no esquema. Qual disjuntor é instalado (o manual recomenda 32 A para o inversor, mas o QF também protege o transformador e QFB1 a QFB4 não, pois estes ficam a montante)?
2. QF é disjuntor tripolar com neutro (4P)? O esquema desenha 4 polos. Confirmar se o quarto polo seccionaria o neutro de fato.
3. QFB1 e QFB2 têm bloco diferencial? O manual (PDF 89) pede ELCB tipo B com atraso apenas para o circuito do inversor; o esquema não coloca diferencial na linha do inversor (QF não é diferencial). Confirmar a decisão de projeto.
4. QFB3 e QFB4: o esquema diz tipo D na folha /8 (MRL) e tipo C na folha /7. Confirmar o tipo instalado.
5. O rótulo "history lighting" de QFB4 e LIHS1 ("History lighting switch") parece tradução do chinês para iluminação do poço (folha /46 chama o circuito de "Hoistway lighting circuit"). Confirmar a terminologia a usar no livro (iluminação do poço).
6. A tomada CZ está ligada no circuito QFB4 (folha /8), mas a legenda a descreve como "Female receptacle" sem corrente. Confirmar potência máxima e se a tomada fica ativa com a chave LIHS1 em qualquer posição (no desenho ela fica antes de LIHS1).

---

## 3. Ficha: transformador TRF

### 3.1 Função
Transformador de comando. Do primário em 220 V (ligado a 207 e 208) gera um secundário de 125 V para o circuito de segurança e de detecção de tensão alta. (Esquema /10, PDF 12.)

### 3.2 Dados (esquema)

| Dado | Valor | Fonte |
|---|---|---|
| Frequência | 50 Hz | Esquema /10, PDF 12 |
| Potência | 63 VA (para motores de 3,7 a 22 kW) e 110 VA (para 30 a 37 kW) | Idem |
| Primário | bornes "220V" e "0P" | Idem |
| Secundário | bornes "125V" e "0S" | Idem |
| Terra | símbolo PE ligado ao núcleo ou blindagem (linha tracejada com PE) | Idem |
| Localização | quadro de comando (legenda: "TRF Control cabinat Transformer /10.4:D") | Legenda /3.a, PDF 5 |

**Para 7,5 kW: 63 VA**, pela faixa "3.7-22KW" impressa no esquema.

### 3.3 Bornes e ligações

| Borne | Liga a | Detalhe |
|---|---|---|
| 220V (primário) | KY8-1 (rede 207) da placa MCTC-KCB-B4A | Rede 207 vem de 201 depois da OVP. (Esquema /10) |
| 0P (primário) | KY8-2 (rede 208) | Rede 208 vem de 202 depois da OVP. |
| 125V (secundário) | QFB1 borne 1 (entrada) | Esquema /10 |
| 0S (secundário) | QFB1 borne N (entrada) | Esquema /10 |
| PE | terra | Esquema /10 |

### 3.4 De onde alimenta e o que alimenta
- **Alimenta-se de:** 201/202, que vêm de QFB2 (6 A, curva C), que por sua vez vem de TA R e N (fase e neutro da rede de 380 V). Os fios 201/202 passam por KY5-1 e KY5-5, pela proteção contra sobretensão (OVP) da placa MCTC-KCB-B4A ("300VAC protection / 285VAC recover") e saem como 207/208 em KY8. (Esquema /9 e /10.)
- **Alimenta:** o circuito de segurança de 125 V (QFB1, depois as redes 101 e 102, fusível F3 de 1 A). A rede 101/101A/102 alimenta, conforme as referências cruzadas do esquema, as folhas 14.1, 16.4, 17.2, 19.1, 19.4, 19.5, 19.8, entre elas os pontos de detecção de tensão alta X25 a X28 (folha /16) e o comando das bobinas dos contatores (folha /17). (Esquema /10, PDF 12; /16, PDF 18; /17, PDF 19.)

### 3.5 Observações do esquema
- A tensão do secundário está rotulada 125 V, mas a regra de nomenclatura (folha /4) diz que os fios 101 a 199 são "relevant circuit of AC110V", e as entradas X25 a X28 do manual são de 110 VAC ±15% (faixa 93,5 a 126,5 V). A regra de nomenclatura também diz que o secundário do transformador é "AC220V = 201, 202; DC110V = L+, L-", o que não corresponde ao que está desenhado na folha /10. (Esquema /4, PDF 6.)
- O desenho do TRF coloca o primário em 220 V; QFB2 é alimentado por R e N de uma rede trifásica 380 V. Logo, os 220 V são fase-neutro (inferência a partir do desenho; não há tensão escrita em +CC-R/+CC-N).

### 3.6 Lacunas
1. Tensão nominal real do secundário: 125 V (rótulo da folha /10) ou 110 V (regra de nomenclatura da folha /4 e manual)? Qual a tolerância?
2. O primário é de fase-neutro 220 V? Confirmar que a rede é 380 V entre fases com neutro (TN-S) e que a tensão R-N é 220 V.
3. Qual transformador físico (marca, classe, proteção térmica)? O esquema só dá potência por faixa de motor.
4. Os 63 VA são adequados para os contatores SW, BY e FX e as seis ligações de segurança na variante com FX? Qual a carga de cada bobina (VA)?

---

## 4. Ficha: contatores SW, BY e FX

### 4.1 Resumo

| Tag | Nome no esquema (legenda /3.a, PDF 5) | Função | Entrada no esquema |
|---|---|---|---|
| SW | "Run contactor" (contator de marcha) | Liga e desliga as três fases entre o inversor e o motor (potência). | /9 (PDF 11), /13 (PDF 15), /17 (PDF 19) |
| BY | "Brake contactor" (contator de freio) | Liga e desliga o polo negativo (BK-) do freio. | /13, /17 |
| FX | "U.V.W short contactor" (contator de curto U, V, W) | Em curto as fases do motor quando desenergizado (motor síncrono). | /9, /17 |

Esquema alternativo (comparação de nomes): "SW - Contatora do motor", "BY - Contatora do freio da máquina", "FX - Contatora auxiliar se motor Síncrono". (Alt. PDF 3, 5 e 9.)

### 4.2 SW: bornes

| Borne | Tipo | Liga a | Fonte |
|---|---|---|---|
| 1 e 2 | Contato principal (polo 1) | 1 vem de U do inversor; 2 vai a TA U | Esquema /9, PDF 11 (posição 9.2:C) |
| 3 e 4 | Contato principal (polo 2) | 3 vem de V; 4 vai a TA V | Idem |
| 5 e 6 | Contato principal (polo 3) | 5 vem de W; 6 vai a TA W | Idem |
| 11 e 12 | Auxiliar NF | 11 recebe 301, 12 vai à entrada X6 (feedback) | Esquema /17, PDF 19 (posição 17.5:D) |
| 53 e 54 | Auxiliar NA | em série com BK1+ (freio 1) | Esquema /13, PDF 15 (posição 13.4:C) |
| 73 e 74 | Auxiliar NA | em série com BK2+ (freio 2) | Esquema /13 (posição 13.6:C) |
| A1 | Bobina | KY2-1 (saída Y1) da placa MCTC-KCB-B4A | Esquema /17 |
| A2 | Bobina | rede 102 ("16.8:B / 102") | Esquema /17 |

### 4.3 BY: bornes

| Borne | Tipo | Liga a | Fonte |
|---|---|---|---|
| 1-2, 3-4, 5-6 | Três contatos principais NA em série | No fio BK- do freio, entre a placa de freio MCTC-PCB-D1 (J3-1, BK-) e os retornos ZQ1- e ZQ2- da placa MCTC-KCB-B4A (KY6-4 e KY9-4) | Esquema /13, PDF 15 (posições 13.5:B e 13.5:C) |
| 11 e 12 | Auxiliar NF | 11 recebe 301, 12 vai a X7 (feedback) | Esquema /17 (posição 17.6:D) |
| A1 | Bobina | KY2-2 (saída Y2) | Esquema /17 |
| A2 | Bobina | rede 102 | Esquema /17 |

### 4.4 FX: bornes (somente na versão síncrona)

| Borne | Tipo | Liga a | Fonte |
|---|---|---|---|
| 21-22 e 31-32 | Contatos principais, desenhados NF | 22 liga ao polo 2 de SW (lado do motor, fase U); 32 liga ao polo 4 de SW (fase V); 21 e 31 unidos e ligados ao polo 6 de SW (fase W). O resultado é o curto entre as fases do motor com FX desenergizado. | Esquema /9, PDF 11 (posição 9.3:C) |
| 13 e 14 | Auxiliar NA | 13 recebe 301, 14 vai a X8 (feedback) | Esquema /17 (posição 17.7:D) |
| A1 | Bobina | KY2-3 (saída Y3) | Esquema /17 |
| A2 | Bobina | rede 102 | Esquema /17 |

Observação: a leitura do tipo NF dos contatos 21-22 e 31-32 vem do símbolo do desenho; o texto "short" confirma a função de curto. O curto no estator quando FX está desenergizado é consequência do contato NF.

### 4.5 Comando e realimentação (folha /17, PDF 19)

| Saída da placa | Função (parâmetro, folha /5) | Alimenta | Alimentação do contato da saída |
|---|---|---|---|
| Y1 (KY2-1) | F5-26 = 1, "Run contactor output" | bobina de SW | rail "+CC-134" (cadeia de portas) |
| Y2 (KY2-2) | F5-27 = 2, "Brake contactor output" | bobina de BY | rail "+CC-134" |
| Y3 (KY2-3) | F5-28 = 12, "Shorting motor stator control output" | bobina de FX | rail "101A" |
| Y2A (KY2-5) | sem carga na folha /17 | n.d. | rail "+CC-134" |

| Entrada | Função (parâmetro) | Contato |
|---|---|---|
| X6 | F5-06 = 38, "Run contactor output feedback (NC)" | SW 11-12 |
| X7 | F5-07 = 39, "Brake control output feedback (NC)" | BY 11-12 |
| X8 | F5-08 = 30, "Shorting motor stator control output feedback (NO)" | FX 13-14 |

Todas as bobinas retornam em 102 (A2). Cada saída tem circuito RC de supressão (C296/R414, C297/R415, C1/R19, C298/R416) na placa. O manual diz que não é preciso absorvedor nos terminais da bobina do contator externo (Manual PDF 65 (impr. 64)). Os contatos X6 a X8 compartilham a rede 301 (24 VDC, "+CC-301"; X5 está em KY2-10, sem contato na folha /17).

### 4.6 Observações do esquema
- Folha /9: caixa tracejada "Add when synchronous" em torno de FX. Folha /17: o mesmo aviso para a bobina de FX e para o contato auxiliar de FX.
- Folha /13: nota "The left and right brakes on the host side should be completely separated and wired" (os dois freios da máquina devem ser ligados totalmente separados).
- Os contatos auxiliares 53-54 e 73-74 de SW intertravam o positivo dos freios: o freio só recebe tensão com SW fechado.

### 4.7 Lacunas
1. O esquema não dá a corrente nominal (AC-3), a tensão de bobina e a marca dos contatores SW, BY, FX. O manual recomenda contator de 25 A para o 4007 como contator de entrada (Manual Tabela 3-2, PDF 87). Qual é o contator de marcha instalado?
2. A bobina é alimentada pela rede 101/102 (rótulo 125 V no TRF, "AC110V" na regra de nomenclatura). Qual é a tensão de bobina dos contatores?
3. O contator BY tem três contatos principais em série no BK-; só dois freios (BK1 e BK2) são usados. Confirmar o motivo da tripla série.
4. Quais contatos auxiliares são de fato NF/NA nos componentes adquiridos (SW 11-12, BY 11-12, FX 13-14)? O esquema indica pelo símbolo e pelos parâmetros.
5. Y2A (KY2-5): para que serve na variante MRL? Na folha /17 não há carga.
6. Em motor assíncrono o FX é removido junto com a ligação a X8? O esquema só diz "Add when synchronous".

---

## 5. Ficha: bornes de entrada XA, TA, XB, XPE; filtro EMC; tomada CZ

**Resultado da busca de tags no Esquema Vitinho:** XA, TA, XB, EMC e CZ existem. **XPE não existe** em nenhuma folha do esquema (nem nas folhas /8, /9 e /46).

### 5.1 XA (R, S, T, N): bornes de entrada no quadro de comando (folha /8, PDF 10)
- Rótulo: "XA Terminal-guide", dentro de "+CC Control cabinet", com bornes R, S, T, N.
- Liga a: rede externa L1, L2, L3, N (de fora do quadro) nas entradas; saídas para o QF (bornes 1, 3, 5, 7) e, antes do QF, para QFB3 e QFB4.
- PE: entra por "PE" separado e aterra a caixa do quadro.
- **Atenção:** na folha /9 (PDF 11) e na /13 (PDF 15) a tag "XA" volta, mas na área "+MR Machine room" e com outros bornes: XA U, V, W (motor, com U1, V1, W1), XA COM1/PT1 (termistor do motor), XA COM2 (feedback do freio 1) e XA COM3 (feedback do freio 2). São régua da sala de máquinas (aqui, a própria máquina). O livro deve distinguir "XA de entrada" de "XA do motor".

### 5.2 TA (R, S, T, N e U, V, W): "Barrier Terminal Block" (folha /9, PDF 11)
- Bloco superior: TA R, S, T, N. Entra do filtro EMC ("9.2:A" da folha /8). R, S, T vão ao inversor; R e N saem em "+CC-R / 10.2:A" e "+CC-N / 10.2:A" para a alimentação de comando.
- Bloco inferior: TA U, V, W. Entram dos polos 2, 4, 6 de SW e saem para os bornes XA U, V, W do motor na sala de máquinas.
- PE: símbolos PE ligados à estrutura.
- Nota: o esquema chama de "Barrier Terminal Block" ("TA"); o texto do pedido associava TA a U, V, W apenas. O esquema usa TA para R, S, T, N também.

### 5.3 XB: régua de saída de iluminação e do limitador
- Folha /8 (PDF 10): XB "Terminal-guide" com 807, 809, 802 (iluminação do poço) e uma barra PE (+H-PE).
- Folha /22 (PDF 24): XB 203, 205 e 202 (limitador de velocidade em 220 VAC) e XB 303, 305 e 302 (limitador de velocidade em 24 VDC).

### 5.4 XPE
Não consta no esquema Vitinho. O esquema representa o terra por símbolos PE e setas (por exemplo "+EX-PE" na folha /9, "PE" em /8, "+H-PE" em /46) e por terminais PE na placa MCTC-KCB-B4A ("AA PE", folha /11; "CC-PE" referenciado em 10.2:C). Ver Lacunas.

### 5.5 Filtro EMC (folha /8, PDF 10; legenda /3.a, PDF 5)
- Rótulo: "EMC filter cabinet", na caixa "+H Hoistway" do esquema. Legenda: "EMC | Hoistway | EMC filter cabinet | /7.2:D".
- Bornes: PE, L1, L2, L3, N na entrada (do QF) e PE, R, S, T, N na saída (para TA da folha /9). O PE de saída vai a "11.1:D" (PE da folha /9).
- Modelo, corrente e fabricante: não constam no esquema.
- Manual, para o 4007: padrão Jianli DL-25EBK5 / Schaffner FN 3258-30-33 (Tabela 3-9, PDF 96); simples Jianli DL-35EB1/10 (Tabela 3-10, PDF 97). Cabo filtro a inversor menor que 30 cm e terras interligados (PDF 52 e 95).

### 5.6 Tomada CZ (folha /8, PDF 10)
- Rótulo: "CZ Female receptacle", com bornes 1, 2 e PE, dentro do quadro de comando (legenda: "Control cabinat Female receptacle /8.8:E"; também listada em "Power box /7.8:D").
- Ligação lida no desenho: pino 2 na linha do borne 2 de QFB4; pino 1 na linha do borne 4 de QFB4 (a mesma linha de XB 802); PE ao terra.
- Dados (corrente, padrão da tomada) não constam no esquema.

### 5.7 Lacunas
1. O que é "XPE" no quadro real? Não existe no esquema Vitinho. É a barra de terra do quadro? Qual a bitola e como os PE de TRF, CZ, inversor, filtro e placas se ligam a ela?
2. XA, TA, XB: qual a corrente e a seção máxima das réguas? O esquema só dá os nomes ("Terminal-guide", "Barrier Terminal Block").
3. A régua XA da sala de máquinas (U, V, W, COM1, PT1, COM2, COM3) é a mesma peça física que a XA de entrada? No MRL não há sala de máquinas; onde ficam esses bornes?
4. O filtro EMC está no poço ("+H") no esquema. Confirmar o local físico real e o modelo (o manual recomenda DL-25EBK5 ou FN 3258-30-33 para o 4007).
5. CZ: confirmar o circuito que a alimenta. Na folha /8 ela está na saída de QFB4; confirmar se isso é o que está instalado e a potência liberada.

---

## 6. Ficha: redes de alimentação de comando

Referência geral: Esquema /4 (PDF 6), regras de nomenclatura; /10, /11 e /12 (PDF 12 a 14) para as redes de comando.

### 6.1 Regras de nomenclatura (folha /4)
- Linhas de potência: R, S, T, N, PE antes do disjuntor geral. A rede de iluminação de 220 V antes do disjuntor do quadro de força: Xa, Xb; depois: 501, 502.
- Secundário do transformador: regra diz AC 220 V = 201, 202 e DC 110 V = L+, L-. Saída de 24 V = 301, 302.
- Faixas de numeração: 101 a 199 = circuitos de AC 110 V; 201 a 299 = circuitos de AC 220 V; 501 a 599 = AC 220 V da iluminação do carro; 801 a 810 = iluminação do poço, AC 220 V.
- Cores de cabo (tabela da folha /4): potência CA principal, N, PE (verde e amarelo), controle CC, CA ≤ 50 V, tensão externa, etc., conforme a tabela da folha.

### 6.2 Redes

| Rede | Origem | Alimenta | Folha |
|---|---|---|---|
| R, S, T, N (após filtro) | QF e filtro EMC | Entrada do inversor (R, S, T) e, por derivação de R e N, o comando (+CC-R, +CC-N). | /8, /9 |
| +CC-R / +CC-N | TA R e TA N | Entrada de QFB2 (bornes 1 e 2). | /9, /10 |
| 201 / 202 | QFB2 (bornes 3 e 4) | Placa MCTC-KCB-B4A (KY5-1 e KY5-5, depois OVP); circuito de acionamento remoto do limitador de velocidade (folha /22, em 220 VAC, via XB 203, 205 e 202). | /10, /22 |
| 207 / 208 | Saída da OVP da MCTC-KCB-B4A | Placa de freio MCTC-PCB-D1 (J2-1 = L e J2-2 = N), primário do TRF (KY8-1 e KY8-2), fusível F1 (250 VAC / 4 A, "door/light curtain fuse") e saída para os circuitos de operador de porta e cortina de luz ("+CC-207/208", 11.3:C; folhas /26 e /28 na tabela da folha /11). | /10, /11 |
| 101 / 101A | QFB1 borne 2 (125 V), fusível F3 (250 VAC / 1 A) | Circuito de segurança, bobina de FX (Y3), resgate elétrico (101 vai ao MCTC-ERB-A via SZ, 101B). | /10, /17, /23 |
| 102 | QFB1 borne N (0S) | Neutro de 125 V: comum dos contatos de detecção X25 a X28 (XCM1, XCM2), retorno de todas as bobinas SW, BY, FX. | /10, /16, /17 |
| 130, 131, 133, 134 | Cadeias do circuito de segurança e das portas | Entradas X25 (130, circuito de segurança), X26 (131, curto de porta 1), X28 (133, curto de porta 2), X27 (134, circuito de portas). | /11, /12, /16 |
| 301 / 302 | Fonte PS-24V da MCTC-PCB-D1 (J4-1 e J4-4) | 24 VDC para as entradas X1 a X24, realimentação dos contatores (X6, X7, X8), placa de interface, circuitos da folha /25 (sinais de nivelamento), comunicação externa (folha /45, via +H-301/302). | /10, /11, /12 |
| BK1+, BK-, BK2+ | Fonte PS-110V da MCTC-PCB-D1 | Bobinas BK1 e BK2 do freio, via contatos SW 53-54 e 73-74 e BY. | /10, /13 |
| 501 / 502 | QFB3 (bornes 2 e 4) | Ventilador e iluminação do carro (F2, 4 A / 250 VAC, saída 507/508, folha /32), iluminação do quadro de comando (CTRL) e resgate elétrico MCTC-ERB-A (L e N). | /8, /11, /23 |
| 807, 809, 802 e +H-PE | QFB4 e chave LIHS1 | Iluminação do poço: 802 neutro, 807 e 809 selecionados por LIHS1. | /8, /46 |
| 110 | Não aparece como rede nomeada nas folhas lidas. | n.d. | n.d. |

### 6.3 Fontes de 24 V e de freio (placa MCTC-PCB-D1, folha /10, PDF 12)
- **PS-24V:** "24VDC/7A". O texto do esquema diz "DC24V maximum output current 7A, 8A overcurrent protection". A tensão é ajustável por parâmetros: B0-03 = 1 (24 V), 2 (26 V), 3 (28 V), 4 (30 V). Saídas 301 e 302 (J4-1, J4-4).
- **PS-110V:** "max 5.6A". Alimenta BK1+, BK- e BK2+. Folha /13: saída ajustável de 48 a 207 VDC, padrão 110 VDC; corrente máxima de impacto de 6 A e de manutenção de 4 A; parâmetros B0-00 (tensão de impacto), B0-01 (tensão de manutenção) e B0-02 (tempo de corte da tensão forte, 0 a 5 s, padrão 3 s). A tensão de manutenção não pode ser maior que a de impacto.
- Ambas as fontes recebem L e N das redes 207/208 (J2-1 e J2-2).
- A placa MCTC-PCB-D1 tem terra em J3-8 (PE).

### 6.4 Proteção contra sobretensão e fusíveis (placa MCTC-KCB-B4A)
- OVP: "300VAC protection / 285VAC recover" (entre 201/202 e 207/208). (Esquema /10.)
- Fusíveis, conforme as folhas /10 e /11 e a legenda /3.a: F1 250 VAC / 4 A (portas e cortina de luz), F2 4 A / 250 VAC (ventilador do carro e cortina de luz), F3 250 VAC / 1 A (circuito de segurança).

### 6.5 Lacunas
1. A rede "110" citada no pedido não existe como rede nomeada nas folhas lidas. Existem 101, 101A, 101B e 102 (125 V ou 110 V, ver ficha 3). Confirmar a que "110" o responsável se referia.
2. Tensão real do circuito de segurança (125 V no TRF ou 110 V na regra de nomenclatura).
3. A rede 201/202 alimenta o limitador de velocidade de 220 VAC; as redes 301/302 alimentam o limitador de 24 VDC (folha /22 traz as duas opções). Qual está instalado? (Folha /10 mostra a nota "Used for speed limiter remote action/release circuit".)
4. As folhas /11 e /12 mostram redes de sinal (111, 118, 121, 122A, 123, 125, 132) sem descrição de função nesta ficha. Não foram analisadas por estarem fora do escopo de potência.
5. Seção dos cabos de cada rede: o esquema não traz bitolas. A tabela de cores da folha /4 é a única referência.

---

## 7. Lista consolidada das lacunas mais importantes (para o responsável técnico)

1. Modelo exato do inversor entregue (esquema diz só "NICE-L-C-40XX"; manual indica NICE-L-C-4007 para 7,5 kW / 380 V).
2. Dados nominais de QF, SW, BY, FX, TRF físico, filtro EMC e resistor de frenagem (nenhum consta no esquema).
3. Tensão do circuito de segurança: 125 V (rótulo no TRF) ou 110 V (regra de nomenclatura e entradas X25 a X28 do manual).
4. XPE: tag inexistente no esquema Vitinho.
5. Posição do filtro EMC no poço contra a exigência do manual de menos de 30 cm até o inversor.
6. Corrente de fuga: o manual pede ELCB tipo B com atraso; no esquema o QF não é diferencial.
7. Tipo C ou D dos diferenciais QFB3 e QFB4 (variantes /7 e /8 divergem).
8. Motor síncrono ou assíncrono (define a presença de FX).
9. Limitador de velocidade em 220 VAC ou 24 VDC.
10. Tamanho de borneira do NICE-L-C-4007 (C, D ou E) e torque correspondente.
