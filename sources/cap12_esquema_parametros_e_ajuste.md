# Cap. 12 (fonte): esquema Vitinho, lista de parâmetros e instruções de ajuste

Fonte primária: esquema Inovance 19061867-ZL, "Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT)", 51 folhas. Folha /5 "List of Parameters" (PDF 7, versão A00, data 2022/10/11) e folha /6 "Tuning instruction" (PDF 8, versão A00, data 2022/10/10). Página PDF = folha + 2.
Confronto: manual NICE3000new, User Guide A01, 368 págs. Cito a página PDF do manual (página impressa = PDF menos 1). "Padrão" é o valor de fábrica que o manual dá.

Regras desta ficha: o texto do esquema está transcrito (inglês entre aspas) e traduzido; nada foi acrescentado. "Model dependent" e "Based on actual conditions" estão como no desenho. Erros de grafia do desenho foram mantidos e sinalizados. Nenhum trecho das duas folhas ficou ilegível (leitura por texto vetorial e por imagem a 3x).

Observação geral: a tabela da folha /5 não traz coluna de observação. As observações aparecem como texto entre parênteses dentro da própria célula "Setting value" ou como as duas "Notes" no canto inferior direito. Nada foi lido em coluna "observação".

---

## 1. Lista de parâmetros da folha /5

A folha tem quatro blocos de colunas (Para. NO., Parameter Name, Setting value). A ordem abaixo segue o desenho: bloco 1 (esquerda), bloco 2, bloco 3, bloco 4. Total: 70 linhas, 72 códigos (a linha "Fb-04/05/19" reúne três).

### 1.1 Bloco 1

| Código | Nome no esquema (tradução) | Valor ou faixa no esquema | Manual (nome, faixa, padrão, pág. PDF) |
|---|---|---|---|
| F0-00 | Control mode (modo de controle) | 1 | Control mode; 0 SVC, 1 CLVC (vetorial malha fechada), 2 V/F; padrão 1; P183 |
| F0-01 | Command source selection (seleção da fonte de comando) | 1 | Command source selection; 0 painel de operação, 1 controle por distância; padrão 1; P183-184 |
| F0-03 | Running speed (velocidade de operação) | Model dependent | No manual, F0-03 é "Maximum running speed" (velocidade máxima); 0.250 a F0-04; padrão 1.600 m/s; P184. "Running speed under operation panel control" é F0-02 (0.050 a F0-04, padrão 0.050 m/s; P349) |
| F0-04 | Rated speed (velocidade nominal) | Model dependent | Rated elevator speed; 0.250 a 4.000 m/s; padrão 1.600; P184 (a tabela de P160 traz 0.250 a 8.000) |
| F0-05 | Rated load (carga nominal) | Model dependent | Rated elevator load; 300 a 9999 kg; padrão 1000; P184 |
| F1-00 | Encoder type (tipo de encoder) | Lista: 0 SIN/COS encoder (synchronous motor); 1 UVW encoder (synchronous motor); 2 ABZ encoder (asynchronous motor); 3 ECN413/1313 absoulute encoder (grafia do desenho); 4 Weton EA53 communication encoder. O desenho não indica qual opção vale para este elevador | Encoder type; 0 SIN/COS, 1 UVW, 2 ABZ incremental, 3 Endat absoluto; padrão 0; P186. O manual lista só 0 a 3; a opção 4 não consta |
| F1-01 | Rated power (potência nominal) | Model dependent | Rated motor power; 0.7 a 75.0 kW; padrão "Model dependent"; P186 |
| F1-02 | Rated voltage (tensão nominal) | Model dependent | Rated motor voltage; 0 a 600 V; "Model dependent"; P186 |
| F1-03 | Rated current (corrente nominal) | Model dependent | Rated motor current; 0.00 a 655.00 A; "Model dependent"; P186 |
| F1-04 | Rated frequency (frequência nominal) | Model dependent | Rated motor frequency; 0.00 a F0-06 Hz; "Model dependent"; P186 |
| F1-05 | Rated speed (velocidade nominal) | Model dependent | Rated motor speed (rotação nominal do motor); 0 a 3000 RPM; "Model dependent"; P186 |
| F1-11 | Auto-tuning mode (modo de autoajuste) | Lista: 1 With-load auto-tuning (com carga); 2 No-load auto-tuning (sem carga); 3 Shaft auto-tuning (autoajuste do poço) | Auto-tuning mode; 0 sem operação, 1 com carga (estático no assíncrono, rotativo no síncrono), 2 sem carga, 3 autoajuste do poço 1 (não limpa o grupo FR), 4 autoajuste do poço 2 (limpa o grupo FR), 5 autoajuste estático do síncrono; padrão 0; P187 |
| F1-12 | Encoder pulses per revolution (pulsos do encoder por volta) | Model dependent | Encoder pulses per revolution; 0 a 10000 PPR; padrão 2048; P188. Ajustar conforme a plaqueta do encoder |
| F1-25 | Motor type (tipo de motor) | 0 Asynchronous motor (assíncrono); 1 Synchronous motor (síncrono). O desenho não indica a opção | Motor type; 0 assíncrono, 1 síncrono; padrão 1; P189 |
| F2-10 | Elevator running direction (sentido de marcha) | 0 Running direction unchanged (sentido mantido); 1 Running direction changed (sentido invertido). Sem opção indicada | Elevator running direction; 0 mantido, 1 invertido; padrão 0; P191 |
| F3-25 | EEO speed (velocidade de operação elétrica de emergência) | 0.25 | Emergency electric RUN speed; 0.100 a 0.300; padrão 0.250 m/s; P196 (P159 e P349 trazem 0.100 a 0.600) |
| F3-26 | Shaft auto-tuning speed (velocidade do autoajuste do poço) | 0.25 | Shaft auto-tuning speed; 0.250 a 0.630; padrão 0.250 m/s; P196 |
| F5-01 | X1 function selection (função da entrada X1) | 1: Up leveling normally open (NO) (nivelamento de subida, NA) | X1; faixa 0 a 127; padrão 33 (= 01 com NF); P198 e P352 |
| F5-02 | X2 function selection | 0 | X2; padrão 35; P198 e P352 |
| F5-03 | X3 function selection | 2: Down leveling (NO) (nivelamento de descida, NA) | X3; padrão 34; P198 e P352 |

### 1.2 Bloco 2

Regra do manual para as entradas X (P199 e P352): para o mesmo sinal, valor NF = valor NA + 32. Os códigos usados pelo esquema e o que o manual diz de cada um estão na coluna da direita. Os valores padrão do manual para F5-01 a F5-24 estão em P352 (F5-04 = 4, F5-05 = 5, F5-06 = 38, F5-07 = 39, F5-08 = 22, F5-09 = 40, F5-10 = 09, F5-11 = 10, F5-12 = 44, F5-13 = 45, F5-14 = 48, F5-15 = 49, F5-16 = 50, F5-17 = 51, F5-18 a F5-24 = 00).

| Código | Nome no esquema | Valor no esquema | Manual (código e nome, pág. PDF) |
|---|---|---|---|
| F5-04 | X4 function selection | 118: Door lock bypass input normally closed (NC) (entrada de bypass do circuito de portas, NF) | 86/118 Door lock bypass input NO/NC; P352, P200 |
| F5-05 | X5 | 0 | 0 = Invalid (inválido); padrão 5; P352 |
| F5-06 | X6 | 38: Run contactor output feedback (NC) (retorno do contator de marcha, NF) | 06/38 RUN contactor feedback; P352 |
| F5-07 | X7 | 39: Brake control output feedback (NC) (retorno do comando do freio, NF) | 07/39 Brake contactor feedback; P352 |
| F5-08 | X8 | 30: Shorting motor stator control output feedback (NO) (retorno do curto no estator, NA) | 30/62 Shorting PMSM stator feedback; P352, P201 |
| F5-09 | X9 | 116: EEO input (NC) (entrada de operação elétrica de emergência, NF) | 84/116 Emergency drive signal NO/NC; P352, P200 |
| F5-10 | X10 | 09: EEO up input (NO) (EEO subir, NA) | 09/41 Inspection/emergency drive up signal; P352 |
| F5-11 | X11 | 10: EEO down input (NO) (EEO descer, NA) | 10/42 Inspection/emergency drive down signal; P352 |
| F5-12 | X12 | 0 | padrão 44 (limite de subida NF); P352 |
| F5-13 | X13 | 0 | padrão 45 (limite de descida NF); P352 |
| F5-14 | X14 | 48: Up slow-down 1 (NC) (desaceleração de subida 1, NF) | 16/48 Up slow-down 1 signal; P352 |
| F5-15 | X15 | 49: Down slow-down 1 (NC) | 17/49 Down slow-down 1 signal; P352 |
| F5-16 | X16 | 50: Up slow-down 2 (NC) | 18/50 Up slow-down 2 signal; P352 |
| F5-17 | X17 | 51: Down slow-down 2 (NC) | 19/51 Down slow-down 2 signal; P352 |
| "F1-18" (código impresso) | X18 function selection | 58: Brake travel switch 1 (NC) (fim de curso do freio 1, NF) | O desenho imprime "F1-18" na linha de X18. Pela sequência da coluna e pelo nome, a linha corresponde a F5-18. O manual dá F5-18 padrão 00; 26/58 Brake travel switch 1 NO/NC; P352 |
| F5-19 | X19 | 0 | padrão 00; P352 |
| F5-20 | X20 | 99: Motor over-temperature (NC) (sobretemperatura do motor, NF) | 67/99 Motor overheat signal NO/NC; P352, P202 |
| F5-21 | X21 | 0 | padrão 00; P352 |
| F5-22 | X22 | 110: Brake travel switch 2 (NC) | 78/110 Brake travel switch 2 input NO/NC; P352 |
| F5-23 | X23 | 0 | padrão 00; P352 |
| F5-24 | X24 | 0 | padrão 00; P352 |
| F5-25 | CTB input type (tipo de entrada da CTB, caixa de teto) | 1856 (Bit6/8/9/10 are set to 1) | CTB input type; faixa 0 a 511; padrão 320; P203. O valor 1856 está acima da faixa impressa no manual. Bits no manual: Bit6 Full-load signal (digital), Bit8 Light-load signal (digital), Bit9 Up leveling signal, Bit10 Down leveling signal; 0 = entrada NF, 1 = entrada NA |
| F5-26 | Y1 function selection | 1: Run contactor output (saída do contator de marcha) | Y1; faixa 0 a 31; padrão 1; 01 Running contactor control; P203-204 |
| F5-27 | Y2 | 2: Brake contactor output (saída do contator de freio) | Y2; padrão 2; 02 Brake contactor control; P203-204 |
| F5-28 | Y3 | 12: Shorting motor stator cintrol output (grafia "cintrol" do desenho; curto no estator do motor) | Y3; padrão 3 (Shorting door lock circuit contactor); 12 Shorting PMSM stator contactor; P203-204 |

### 1.3 Bloco 3

| Código | Nome no esquema | Valor ou faixa no esquema | Manual (nome, faixa, padrão, pág. PDF) |
|---|---|---|---|
| F5-29 | Y4 function selection | 4: Fire emergency floor arrival signal feedback (retorno de chegada ao andar de emergência de incêndio) | Y4; padrão 4; 04 igual; P203-204 |
| F5-30 | Y5 | 0 | padrão 0; 00 Invalid; P203-204 |
| F5-31 | Y6 | 0 | padrão 0; P203. Só Y6 pode receber 13 (evacuação automática); P204 |
| F5-36 | Load cell input selection (seleção da entrada da célula de carga) | Lista: 0 MCB digital output; 1 CTB digital output; 2 CTB analog output; 3 MCB analog output. O desenho diz "output" (saída). Sem opção indicada | Load cell input selection; 0 a 3; padrão 1; P208-209. O manual diz "input" (entrada): 0 MCB digital, 1 CTB digital, 2 CTB analógica, 3 MCB analógica |
| F5-37 | X25 function selection | 4: Safety circuit signal (sinal do circuito de segurança) | X25; padrão 0; 4 Safety circuit signal; P209 |
| F5-38 | X26 | 7: Door 1 lock shorting signal (sinal de curto do circuito de portas 1) | X26; padrão 0; 7 Door lock 1 shorting; P209 |
| F5-39 | X27 | 5: Door lock circuit signal (sinal do circuito de portas) | X27; padrão 0; 5 Door lock circuit signal 1; P209 |
| F5-40 | X28 | 8: Door 2 lock shorting signal (set for double-door elevators) (curto do circuito de portas 2; "para elevadores de porta dupla") | X28; padrão 0; 8 Door lock 2 shorting; P209 |
| F6-00 | Top floor of the elevator (andar mais alto) | Based on actual conditions (conforme as condições reais) | Top floor of the elevator; F6-01 a 40; padrão 9; P210 (P160 traz F6-01 a F6-56, padrão 9, com a anotação "Actual number of floors + 1") |
| F6-01 | Bottom floor of the elevator (andar mais baixo) | Based on actual conditions | Bottom floor; 1 a F6-00; padrão 1; P210 |
| F6-40 | Program control selection 1 | Bit1=1: Software limit function (função de limite por software) | Program control selection 1; 0 a 65535; padrão 0; Bit1 Soft limit function; P217-218 |
| F6-52 | Function selection | Bit1=1: Supports MCTC-SCB-A4/D4. Bit6=1: Can communication leveling signal (sinal de nivelamento por comunicação CAN) | Program function selection; 0 a 65535; padrão 0; Bit6 CAN communication leveling signal; P225. No texto extraído do manual, a tabela de bits traz Bit2, Bit6 e Bit7; o Bit1 não aparece |
| F8-01 | Pre-torque selection (seleção do pré-torque) | 2: Automatic pre-torque compensation (compensação automática de pré-torque) | Pre-torque selection; 0 a 3; padrão 2; 2 = compensação automática; P228 |
| F8-10 | Emergency evacuation power supply at power failure (fonte de energia para evacuação de emergência na falta de energia) | 1: Emergency evacuation by automatic rescue device (ARD) (optional) (evacuação por dispositivo de resgate automático, opcional) | O manual chama de "Emergency evacuation operation mode at power failure"; 0 a 2; padrão 1; 0 motor parado, 1 UPS, 2 bateria de 48 V; P230. Nome e opção 1 diferem do esquema |
| Fb-00 | Number of door operator(s) (número de operadores de porta) | 1: Single entrance car (cabine de entrada única); 2: Through type car (cabine de duas entradas). Sem opção indicada | Number of door machine(s); 1 a 2; padrão 1; P244 |
| Fb-02 | Service floor 1 of door operator 1 | Set based on actual conditions (binary) (conforme as condições reais, em binário). Bit0=1, Bit1=2, Bit2=4, Bit3=8, Bit4=16, Bit5=32, Bit6=64, Bit7=128, Bit8=256, Bit9=512, Bit10=1024, Bit11=2048, Bit12=4096, Bit13=8192, Bit14=16384, Bit15=32768. "Service floors 1, 2 and 3 are set in the same way as F6-05, F6-06 and F6-35." | Door machine 1 service floors 1; 0 a 65535; padrão 65535; Service floor 1 corresponde aos andares 1 a 16 e Service floor 2 aos 17 a 32; P245 |
| Fb-03 | Service floor 2 of door operator 1 | (mesma célula de Fb-02) | Door machine 1 service floors 2; 0 a 65535; padrão 65535; P245 |
| Fb-18 | Service floor 3 of door operator 1 | (mesma célula de Fb-02) | Door machine 1 service floors 3; 0 a 65535; padrão 65535; P245 |
| Fb-04 / Fb-05 / Fb-19 | Service floor 1/2/3 of door operator 2 | 0 | Door machine 2 service floors 1, 2 e 3; 0 a 65535; padrão 65535; P245 |
| FC-04 | Double-door control selection (seleção de controle de porta dupla) | 0: Door open/close on both sides if the car/hall call is active on either side. 1: Door open on the same side if the hall call is active, and door open on both sides if the car call is active. 2: Door open on the same side if the hall call is active, and door open only on one side if the car call is active (manual selection). 3: Door open on the same side if the hall call is active. Sem opção indicada | Opposite door selection; 0 a 3; padrão 0; 0 controle simultâneo; 1 chamada de pavimento independente, chamada de cabine simultânea; 2 chamada de pavimento independente, chamada de cabine por seleção manual; 3 chamada de pavimento independente, chamada de cabine independente; P249 |

Tradução das quatro opções de FC-04 conforme o desenho: 0, abrir e fechar os dois lados se a chamada de cabine ou de pavimento estiver ativa em qualquer lado; 1, abrir o mesmo lado se a chamada de pavimento estiver ativa, e os dois lados se for chamada de cabine; 2, abrir o mesmo lado se a chamada de pavimento estiver ativa, e só um lado se for chamada de cabine (seleção manual); 3, abrir o mesmo lado se a chamada de pavimento estiver ativa.

### 1.4 Bloco 4

| Código | Nome no esquema | Valor no esquema | Manual (nome, faixa, padrão, pág. PDF) |
|---|---|---|---|
| F2-33 | Torque amplitude (amplitude de torque) | 15% of the reted (grafia do desenho) motor torque (15% do torque nominal do motor) | O único F2-33 do manual é "Torque limit"; 1 a 150% do torque nominal; padrão 110; 0 usa 110%; P320 (tabela do teste de força de frenagem). Não há correspondência de nome |
| F6-07 | Number of elevators in group control (número de elevadores em grupo) | Based on actual conditions | Number of elevators in parallel/group mode; 1 a 8; padrão 1; P213 |
| F6-08 | Elevator NO. (número do elevador) | Group control: elevator NO. set based on actual conditions. Parallel control: 1 as the master elevator and 2 as the slave elevator (grupo: número conforme as condições reais; paralelo: 1 principal, 2 auxiliar) | Elevator No.; 1 a 8; padrão 1; P213 |
| F6-09 | Program selection | Bit3=1: Parallel/group control via CAN2 | Program control selection; padrão 0; Bit3 Parallel/Group control implemented at CAN2; P213 |
| F8-16 | Start address of hall call auxiliary command | 0-48 (Double-door set) (porta dupla) | Start address of hall call auxiliary command; 0 a 40; padrão 0; endereço da HCB da porta de trás = endereço da frente no mesmo andar + F8-16; P230-231 |

### 1.5 Notas da folha /5 (canto inferior direito)

1. "The new generation of control cabinet id connected to the car top inspection box through communication. The car top inspection signal and up/down leveling signal are transmitted through communication." Tradução: a nova geração de quadro é ligada à caixa de inspeção do teto da cabine por comunicação; o sinal de inspeção do teto e o sinal de nivelamento de subida/descida são transmitidos por comunicação. ("id" é a grafia do desenho.)
2. "The up and down limits are realied through the software limit funcation. Therefore, the up and down limit switches are not needed." Tradução: os limites de subida e descida são realizados pela função de limite por software; por isso as chaves de limite de subida e de descida não são necessárias. (Grafias "realied" e "funcation" do desenho.)

---

## 2. Instruções de ajuste da folha /6 ("Tuning instruction")

A folha é um fluxograma de caixas com setas tracejadas. Há 11 caixas de passo e rótulos de ramo. Ordem de leitura abaixo; a folha não numera os passos (a numeração é só para citação).

Passos comuns:

1. "Set F1-25 based on the motor type". Ajustar F1-25 conforme o tipo de motor.
2. "Set encoder parameter: F1-00, F1-12 and the motor parameter: F1-01 to F1-05, make sure the parameter right". Ajustar os parâmetros do encoder (F1-00, F1-12) e do motor (F1-01 a F1-05) e conferir se estão certos.

Ramo "Asynchronous Motor F1-25=0" (motor assíncrono):

3. "Set F0-01=0 (operation panel control)". Ajustar F0-01=0 (controle pelo painel de operação).
4. Rótulo "With-load tuning". "Set F1-11=1, The operate panel display TUNE, then press the RUN key. Motor static tuning begins." Ajustar F1-11=1; o painel mostra TUNE; apertar a tecla RUN; começa o ajuste estático do motor. A seta desta caixa vai para a caixa 8.
5. Rótulo "Non-load tuning". "Set F1-11=2, The operate panel display TUNE, release the brake manually, press the RUN key, the motor begin to run (the tuning begins)." Ajustar F1-11=2; o painel mostra TUNE; soltar o freio manualmente; apertar RUN; o motor começa a girar (o ajuste começa).
6. "Get the motor parameters F1-14 to F1-18 after tuning. Set F1-01=1 (distance control). The tuning finished." Obter os parâmetros do motor F1-14 a F1-18 após o ajuste. "Set F1-01=1 (distance control)" é o texto impresso; o ajuste terminado. Aviso: F1-01 é a potência nominal e "distance control" é o valor 1 de F0-01. Transcrito como está, sem correção (ver 4.3).

Ramo "synchronous Motor F1-25=1" (motor síncrono), duas variantes:

7. Rótulo "With-load tuning". Caixa "F0-01=1 / F1-11=1".
8. "Set F1-11=1, The operate panel display TUNE, press the insp. UP/DOWN button, the motor begin to run (the tuning begins)." Ajustar F1-11=1; o painel mostra TUNE; apertar o botão de inspeção SUBIR/DESCER; o motor começa a girar (o ajuste começa).
9. "Check the initial angle and wiring mode of the encoder (F1-06, F1-08), tuning several times to ensure the difference between values of F1-06 within 5 degree, and the value of F1-08 are the same." Verificar o ângulo inicial e o modo de ligação do encoder (F1-06, F1-08); ajustar várias vezes para garantir que a diferença entre os valores de F1-06 fique dentro de 5 graus e que o valor de F1-08 seja o mesmo.
10. "Get the motor parameters (F1-06, 07, 08, 14, 19, 20) and current loop parameters. Set F0-01=1 (distance control). The tuning finished." Obter os parâmetros do motor (F1-06, F1-07, F1-08, F1-14, F1-19, F1-20) e os parâmetros da malha de corrente; ajustar F0-01=1 (controle por distância); ajuste terminado.
11. Rótulo "Non-load tuning". Caixa "F0-01=0 / F1-11=2", que leva à mesma caixa do passo 5 ("Set F1-11=2 ... release the brake manually, press the RUN key"). Daquela caixa saem duas setas: uma para a direita, para o passo 6 (F1-14 a F1-18), e uma para baixo, para o passo 9 (verificação do ângulo inicial), seguida do passo 10.

Notas da folha /6: não há bloco de notas. Todo o texto está nas caixas e nos rótulos acima.

Resumo do cruzamento com o manual, só para conferência (nada foi acrescentado ao desenho):
- Manual: F0-01 deve ser 1 no autoajuste com carga e 0 no autoajuste sem carga (P151 e seguintes, P155 e seguintes). Coincide com o desenho.
- Manual: após ajustar F1-11, "press ENTER"; se o painel mostrar TUNE, o sistema entrou em autoajuste; se mostrar "F1-12", não entrou (P151). O desenho diz "press the RUN key".
- Manual: no ajuste com carga do síncrono o elevador precisa estar em inspeção, e o texto fala em manter apertado o botão de emergência SUBIR/DESCER (P151). O desenho diz "insp. UP/DOWN button".
- Manual: o desvio de F1-06 deve ficar em ±5° após vários ajustes (P186). Coincide com o desenho.
- Manual: F1-08 par indica sequência de fases correta; ímpar, trocar duas fases do motor (P187). Não consta no desenho.
- Manual: F1-14 a F1-18 são parâmetros do motor assíncrono (resistência do estator, resistência do rotor, indutância de dispersão, indutância mútua, corrente a vazio; P188). F1-19 e F1-20 são indutâncias de eixo Q e D do síncrono (P188). F1-06 ângulo inicial do encoder, F1-07 ângulo no desligamento, F1-08 modo de ligação do síncrono (P186).

---

## 3. Parâmetros citados em notas de outras folhas

Pesquisa feita no texto de todas as 51 folhas. Os parâmetros F5-26 a F5-28, F8-10, F5-01 a F5-24, F1-xx e F2-xx **não** aparecem em notas de outras folhas. Só aparecem na folha /5. Os que aparecem:

| Folha (PDF) | Título da folha | Parâmetros citados e o que a nota diz |
|---|---|---|
| /10 (PDF 12) | Control power supply 1 | B0-03=1: saída DC24V; B0-03=2: DC26V; B0-03=3: DC28V; B0-03=4: DC30V (a tensão de 24 V é ajustável). Dois métodos de depuração: (A) placa de alimentação do freio com comunicação separada, com celular ligado à porta de gravação por ferramenta e app móvel para alterar o código de função; (B) pela placa-mãe, alterando o código pelo app ou pelo operador (apertar o botão direito por 5 s para entrar na interface de códigos da placa de potência) |
| /13 (PDF 15) | Brake control circuit | B0-00 tensão de choque forte; B0-01 tensão de manutenção; B0-02 tempo de manutenção do corte do choque forte. Nota: a tensão de manutenção não pode ser maior que a de choque forte; o tempo é de 0 a 5 s, padrão 3 s. Fonte do freio: saída ajustável de 48 a 207 VDC, padrão 110 VDC; corrente máxima de impacto 6 A, de manutenção 4 A. Mesmos dois métodos de depuração de /10 |
| /15 (PDF 17) | UCMP board | F6-52 BIT1=1 no painel mestre do quadro quando se usa SCB-A4/D4. Observação: síncrono porta única usa SCB-A4; síncrono portas opostas usa SCB-D4; assíncrono usa SCB-D4 |
| /16 (PDF 18) | Bypass e teste UCMP | Teste UCMP: no teclado F-8=7; no painel de operação F3-24=2 (o MCB mostra E88 ao entrar no estado de teste) |
| /25 (PDF 27) | Door zone sensor | F6-52 BIT6=1 (comunicação de nivelamento pelo teto da cabine, quando há abertura antecipada de porta e renivelamento); F5-25: Bit9=1 sinal de nivelamento de subida, Bit10=1 sinal de nivelamento de descida |
| /26 (PDF 28) | Front door machine control circuit | F6-52 Bit7=1 habilita a função de sobretemperatura do motor da porta; F5-25: Bit2=0 limite de abertura da porta 1, Bit4=0 limite de fechamento da porta 1, Bit11=0 detecção de sobretemperatura. Inversor de porta NICE900: F9-09=2, F9-11=1, F9-05=1, F9-06=1, e "F0-01=1 (Distance control)", "F0-02=1 (Door machine terminal control)". Estes últimos são códigos do inversor de porta, não do controlador do quadro |
| /27 (PDF 29) | Rear door machine control circuit | Idem /26 para a porta 2: F6-52 Bit7=1; F5-25 Bit3=0, Bit5=0; FB-39 Bit2=0 detecção de sobretemperatura; NICE900 com os mesmos códigos |
| /28 (PDF 30) | Front door (encoder de comunicação) | F6-52 Bit7=1; F5-25 Bit4=0 limite de fechamento da porta 1, Bit11=0 sobretemperatura |
| /29 (PDF 31) | Rear door (encoder de comunicação) | F6-52 Bit7=1; F5-25 Bit5=0 limite de fechamento da porta 2; FB-39 Bit2=0 sobretemperatura |
| /30 (PDF 32) | Front door light curtain / safety edge | F5-25: Bit0=0 detecção da cortina de luz da porta 1; Bit12=0 detecção do painel de toque da porta 1 |
| /31 (PDF 33) | Back door light curtain / safety edge | F5-25: Bit1=0 cortina de luz da porta 2; Bit13=0 painel de toque da porta 2 |
| /32 (PDF 34) | Car fan and light | F9-01 escolhe o modo de economia de energia da cabine; padrão 2 min |
| /33 (PDF 35) | Load weighing / Audible alarm | F5-36=1 habilita a pesagem digital; F5-36=2 habilita a pesagem analógica; F5-25: Bit6=1 carga cheia (Full-load), Bit7=0 sobrecarga (Over-load), Bit8=1 carga leve (light load) |
| /35 (PDF 37) | Car top insp. circuit | FA-33 Bit12 sinal de inspeção, Bit13 inspeção subir, Bit14 inspeção descer; FA-63 estado da inspeção do teto: bit0 inspeção da cabine imposta, bit1 inspeção do poço imposta, bit2 bypass imposto, bit3 inspeção sem autoajuste do poço |

Observações sobre este quadro:
- A folha /3.a (PDF 6) traz só regras de nomenclatura de fios e cores, sem parâmetros. As folhas /2.a e /3 (PDF 4 e 5) são lista de componentes, sem parâmetros.
- Cruzamentos com a folha /5: F5-25 = 1856 (Bit6, 8, 9, 10) é coerente com /25 (Bit9, Bit10) e /33 (Bit6=1, Bit7=0, Bit8=1). F6-52 Bit1 e Bit6 constam em /15 e /25. F6-52 Bit7 (porta) consta em /26 a /29 mas não na lista da folha /5. F5-36 aparece em /33 com valores 1 e 2, mas a folha /5 lista as quatro opções sem escolher uma.
- B0-00 a B0-03 e FA-33/FA-63, FB-39, F9-xx, F-8 não estão na lista da folha /5. B0-xx não consta no manual de 368 páginas (não encontrado). F3-24 existe no manual como "Program function selection" (P196 e P349), com "1: Slip experiment" entre os valores; o valor 2 usado em /16 não foi confrontado.

---

## 4. Ambiguidades e dependências de dados do projeto

### 4.1 Dados que o esquema deixa para o projeto
- "Model dependent": F0-03, F0-04, F0-05, F1-01 (potência), F1-02 (tensão), F1-03 (corrente), F1-04 (frequência), F1-05 (rotação nominal), F1-12 (pulsos do encoder por volta). O esquema não dá número para o elevador de referência (7,5 kW, 380 V, síncrono de ímã permanente). Esses valores vêm da plaqueta do motor e do encoder (o manual manda ajustar F1-01 a F1-05 pela plaqueta do motor, P186, e F1-12 pela plaqueta do encoder, P188).
- "Based on actual conditions": F6-00, F6-01, F6-07, F6-08 (e "set based on actual conditions" em Fb-02, Fb-03, Fb-18). O esquema não dá o número de andares do projeto nem o valor binário das paradas atendidas.
- Listas sem opção marcada: F1-00, F1-11, F1-25, F2-10, F5-36, Fb-00, FC-04. A folha mostra as opções do manual do fabricante, não a escolhida. A escolha de F1-25 (síncrono = 1) e F1-00 depende do motor e do encoder reais.
- F8-16 traz "0-48 (Double-door set)", que é uma faixa, não um valor.

### 4.2 Divergências entre esquema e manual (conferidas, não corrigidas)
1. F0-03: o esquema chama de "Running speed"; no manual F0-03 é "Maximum running speed" e "Running speed" (painel) é F0-02.
2. F1-00 opção 4 (Weton EA53) e opção 3 "ECN413/1313": o manual lista só 0 a 3 e chama a 3 de Endat.
3. F5-25 = 1856, acima da faixa 0 a 511 do manual (P203).
4. F5-36: o esquema diz "output" onde o manual diz "input".
5. F8-10: nome e opção 1 diferem (esquema: fonte de energia, ARD; manual: modo de operação, 1 = UPS).
6. F2-33: o esquema diz "Torque amplitude, 15%"; o manual só traz F2-33 como "Torque limit" (padrão 110%).
7. F8-16: faixa 0-48 no esquema, 0 a 40 no manual.
8. F6-52 Bit1: não aparece na tabela de bits do texto extraído do manual.
9. F3-25: manual com faixa 0.100 a 0.300 (P196) e 0.100 a 0.600 (P159, P349).
10. F6-00: manual com F6-01 a 40 (P210) e F6-01 a F6-56 (P160).
11. F1-11: o esquema lista 1, 2, 3; o manual tem 0 a 5.
12. FC-04: as quatro descrições do esquema são diferentes do texto do manual (mesma ideia de quatro modos, redação distinta).

### 4.3 Erros de grafia ou de código no desenho (mantidos como estão)
- Linha de X18 impressa com código "F1-18" (esperado F5-18 pela sequência; F1-18 é "No-load current" no manual).
- Passo 6 do ajuste: "Set F1-01=1 (distance control)"; no desenho o mesmo comando é F0-01=1 no passo 10, e no manual F0-01 é a fonte de comando.
- Grafias: "absoulute", "cintrol", "reted", "id connected", "realied", "funcation", "operator(s)" (nomeia "door operator", o manual diz "door machine").

### 4.4 Pontos de interpretação
- Passo 5 e passo 11: a caixa "Set F1-11=2 ..." serve às duas rotas sem carga (assíncrono e síncrono). A divisão das duas setas de saída (para F1-14 a F1-18, e para a verificação de F1-06/F1-08) é a leitura do desenho.
- F5-39 do esquema diz "Door lock circuit signal"; no manual o valor 5 é "Door lock circuit signal 1".
- F5-40 (X28 = 8) e Fb-04/05/19 (porta 2): o próprio desenho marca "set for double-door elevators". O desenho não diz se se aplica ao elevador de referência de uma porta; não decidido aqui.
- O esquema usa as mesmas siglas de entradas X1 a X28 da placa MCB; a folha /20 (I/O control, PDF 22) mostra os terminais, mas essa folha não foi parte deste levantamento.
- Valores NF dos códigos (48, 49, 50, 51, 58, 99, 110, 116, 118, 38, 39) seguem a regra do manual "NF = NA + 32" (P352); a tabela do manual lista cada um.
