# Capítulo 12 (fonte): Energização, parâmetros e autoajuste. Manual NICE3000new, seções 5.1 a 5.4

Tradução fiel do capítulo "5 System Commissioning" do manual do controlador NICE3000new (títulos originais: "System Commissioning Guide", "Safety and Circuit Check", "Power-on and Controller State Check", "Commissioning at Inspection Speed"). Convenções: parâmetros, subcódigos, siglas e teclas ficam como no manual. "Auto-tuning" está traduzido como "autoajuste"; "emergency electric RUN" como "resgate elétrico (emergency electric RUN)". Quando uma frase do original está truncada ou ambígua, ela aparece em inglês entre aspas.

Introdução do capítulo (pág. PDF 143): este capítulo descreve o guia básico de comissionamento do NICE3000new. Seguindo as instruções, é possível realizar o comissionamento completo do sistema do elevador e implementar todas as funções básicas de funcionamento normal do elevador.

---

## 5.1 Guia de comissionamento do sistema (System Commissioning Guide)

**Figura 5-1: fluxograma geral de comissionamento do NICE3000new.** Mostra a sequência, de "Start" a "End", com as etapas em texto:

1. Verificação de segurança e de circuitos (Safety and circuit check).
2. Verificação da energização e do estado do controlador (Power-on and controller state check).
3. Comissionamento em velocidade de inspeção (Commissioning at inspection speed), composto por: autoajuste do motor (Motor auto-tuning) e teste de funcionamento em velocidade de inspeção (Running test at inspection speed).
4. Comissionamento em velocidade normal (Commissioning at normal speed), composto por: autoajuste do poço (Shaft auto-tuning), comissionamento da cabine (Car commissioning) e comissionamento da HCB (HCB commissioning).
5. Ajuste do conforto de viagem (Riding comfort adjustment), composto por: ajuste do conforto de viagem e ajuste da precisão de nivelamento (Leveling accuracy adjustment).

(Ambíguo quanto à ordem exata das caixas dentro do bloco 4 e do bloco 5: o texto extraído lista as caixas fora de ordem; ver o original na pág. PDF 143, Figura 5-1. A ordem acima segue a ordem dos títulos do índice do manual.)

Fonte: manual NICE3000new, págs. PDF 143 (impressa 142).

---

## 5.2 Verificação de segurança e de circuitos (Safety and Circuit Check)

Observe as seguintes precauções antes de realizar o comissionamento:

> **CUIDADO (Caution)**
> Os terminais de entrada e saída do NICE3000new têm ajuste padrão de fábrica na entrega. Você pode alterar o ajuste conforme suas necessidades. Os exemplos deste manual são todos baseados no ajuste padrão dos terminais.

### 1. Diagrama de ligação do sistema (System Wiring Diagram)

Consultar a Figura 2-39.

### 2. Fluxograma da verificação de segurança (Safety Check Flowchart)

**Figura 5-2: fluxograma da verificação de segurança e de circuitos antes da energização.** Quatro etapas em sequência:

1. Etapa 1: verificar a segurança mecânica.
2. Etapa 2: verificar a ligação elétrica.
3. Etapa 3: verificar a segurança elétrica.
4. Etapa 4: verificar o encoder rotativo.

**Etapa 1: verificar a segurança mecânica.**
Verifique que o poço está desobstruído, que não há pessoa no poço, dentro da cabine nem sobre ela, e que as condições para o funcionamento seguro do elevador estão atendidas.

**Etapa 2: verificar a ligação elétrica.** (lista de verificação do manual, com caixa de marcação "□√" para cada item)

| Nº | Pontos de inspeção |
|---|---|
| 1 | Os cabos de alimentação R, S, T estão ligados corretamente e firmes. |
| 2 | Os cabos UVW entre o controlador e o motor estão ligados corretamente e firmes. |
| 3 | O controlador (quadro de comando) e o motor estão aterrados corretamente. |
| 4 | A cadeia de segurança está conduzindo, e os botões e chaves de parada de emergência no quadro de comando e na casa de máquinas podem ser acionados ("can be enabled"). |
| 5 | O circuito de fechaduras está conduzindo. O circuito de fechaduras é desligado quando a porta da cabine ou qualquer porta de pavimento abre. |

> **PERIGO (Danger)** (título do bloco: "Safety Information", "To guarantee safe running of elevator", ou seja, "Para garantir o funcionamento seguro do elevador")
> - Curto-circuite a cadeia de segurança com cautela. Se o elevador começar a funcionar com a cadeia de segurança em curto, isso causará lesão pessoal grave ou até morte.
> - Antes de iniciar o comissionamento, garanta que não há pessoa no poço; caso contrário, isso causará lesão pessoal ou até morte.
> - NUNCA realize comissionamento em velocidade normal com a cadeia de segurança em curto.
> - NUNCA coloque em curto o circuito de fechaduras durante a partida e o funcionamento do elevador. O descumprimento resultará em lesão pessoal grave ou até morte.

**Etapa 3: verificar a segurança elétrica.**

| Nº | Pontos de inspeção |
|---|---|
| 1 | A tensão de linha da alimentação do usuário está entre 380 e 440 V, e o grau de desequilíbrio de fase não excede 3%. |
| 2 | A bitola total do cabo de entrada e a capacidade total da chave atendem aos requisitos. |
| 3 | Não há curto-circuito entre fases nem para a terra na alimentação R, S, T. |
| 4 | Não há curto-circuito entre fases nem para a terra nas fases U, V, W do controlador. Não há curto-circuito para a terra nas fases U, V, W do motor. |
| 5 | Não há curto-circuito para a terra no lado de saída do transformador. |
| 6 | Não há curto-circuito entre fases nem para a terra na alimentação de 220 V. |
| 7 | A alimentação de 24 V não tem curto-circuito entre positivo e negativo nem para a terra. |
| 8 | O cabo de comunicação CANbus/Modbus não tem curto-circuito com a alimentação de 24 V nem para a terra. |

**Etapa 4: verificar o encoder rotativo.**

| Nº | Pontos de inspeção |
|---|---|
| 1 | O encoder está instalado de forma confiável e com a ligação correta. |
| 2 | Os cabos de sinal do encoder e o circuito de corrente forte são passados em dutos diferentes, para evitar interferência. |
| 3 | Os cabos do encoder são, de preferência, ligados diretamente ao quadro de comando. Se o cabo não for longo o suficiente e for necessária uma extensão, a extensão deve ser um cabo blindado e, de preferência, soldada aos cabos originais do encoder com ferro de solda. |
| 4 | A blindagem dos cabos do encoder é aterrada na extremidade ligada ao controlador (apenas uma extremidade é aterrada, para evitar interferência). |

Fonte: manual NICE3000new, págs. PDF 143 a 145 (impressas 142 a 144).

---

## 5.3 Energização e verificação do estado do controlador (Power-on and Controller State Check)

### 5.3.1 Verificação do estado de energização (Checking Power-on State)

| Nº | Conteúdo da verificação |
|---|---|
| 1 | Aplique a alimentação. Verifique que a tensão de linha das fases R, S, T do controlador está entre 380 e 440 VAC, com grau de desequilíbrio de fase ≤ 3%. Se estiver anormal, desligue a alimentação e verifique a alimentação e a ligação dos cabos R, S, T no controlador. |
| 2 | Verifique que a tensão de entrada de alimentação no terminal de 24 V (CN3) da MCB é 24 VDC ±15%. Se estiver anormal, desligue a alimentação; verifique a fonte chaveada e verifique se o circuito de 24 VDC está ligado corretamente. |

### 5.3.2 Verificação do estado na energização normal (State Check at Normal Power-on)

| Nº | Conteúdo da verificação |
|---|---|
| 1 | Verifique que o teclado (keypad) tem display após a energização. Se não houver display no teclado, verifique se a alimentação do controlador está normal. |
| 2 | Se os indicadores dos sinais de entrada mostrados na figura anterior ficarem ON, isso indica que a alimentação de 24 VDC está normal e que os terminais de entrada X funcionam corretamente. Se nenhum dos indicadores estiver ON, isso indica que a alimentação de 24 VDC está anormal, e é preciso eliminar o problema. |

**Figura 5-3: display da MCB após a energização normal.** Desenho da placa MCB do NICE3000new (integrated elevator controller) com os conectores (CN1, CN2, CN3, CN4, CN7, CN9, CN12, J1 a J14), as teclas PRG, UP, SET, os indicadores de entrada X1 a X28 e os indicadores COP, HOP, CAN2, MOD2 e 232. Legendas: "a. There is display on the LEDs." (a. há display nos LEDs) e "b. Certain inputs on the MCB are active." (b. certas entradas da MCB estão ativas).

### 5.3.3 Estados possíveis do controlador e métodos de tratamento antes do comissionamento (Potential Controller States and Handling Methods Before Commissioning)

#### 1. Verifique o estado do controlador e trate as falhas relacionadas

Durante o comissionamento, especialmente na primeira energização, certas falhas podem ocorrer porque as condições para o funcionamento automático do elevador não são atendidas e certos sinais periféricos não estão ligados. Essas falhas são E41, E42, E35, E51, E52 e E58. A parte a seguir descreve o estado da MCB na falha e o tratamento dessas falhas.

**Figura 5-4: estado da MCB nas falhas durante o comissionamento.** Seis desenhos da placa MCB, um para cada falha (E41, E42, E35, E51, E52, E58), com os indicadores de entrada no estado correspondente. (Ambíguo: quais indicadores estão acesos em cada desenho não consta no texto extraído; ver o original nas págs. PDF 147 e 148, Figura 5-4.)

#### 2. Tratamento das falhas E41, E42, E35, E51, E52 e E58 antes do comissionamento em velocidade de inspeção

**Tabela 5-1: tratamento de falhas antes do comissionamento em velocidade de inspeção** (tabela conferida na imagem da página)

| Falha | Nome da falha | Descrição da falha | Método de tratamento |
|---|---|---|---|
| E41 | Falha da cadeia de segurança (Safety circuit fault) | 1. Nesta falha, o elevador não pode funcionar nem ser comissionado. 2. Por padrão, o sinal de entrada da cadeia de segurança está ligado aos terminais X4 e X25. | Observe se o indicador de sinal dos terminais de entrada X4 e X25 está ON. Se este indicador estiver OFF, a cadeia de segurança está desligada. Neste caso, é preciso reparar a cadeia de segurança. Depois, pode-se realizar o comissionamento em velocidade de inspeção. |
| E42 | Falha do circuito de fechaduras (Door lock circuit fault) | 1. Nesta falha, o elevador não pode funcionar nem ser comissionado. 2. Por padrão, o sinal do circuito de fechaduras está ligado aos terminais X5, X26 e X27. | Observe se o indicador de sinal dos terminais X5, X26 e X27 está ON. Se este indicador estiver OFF, o circuito de fechaduras está desligado. Neste caso, é preciso reparar o circuito de fechaduras. Depois, pode-se realizar o comissionamento em velocidade de inspeção. NUNCA coloque em curto o circuito de fechaduras para o comissionamento. |
| E35 | Dados de autoajuste do poço anormais (Shaft auto-tuning data abnormal) | Esta falha é reportada a cada energização porque o autoajuste do poço não foi realizado. Não afeta o comissionamento em velocidade de inspeção. | Pressione a tecla MF.K no painel de operação para ocultar a indicação da falha. Depois, pode-se realizar o comissionamento em velocidade de inspeção. (O mesmo método de tratamento, em célula única, vale para E35, E51 e E52.) |
| E51 | Falha de comunicação CAN (CAN communication fault) | 1. Esta falha não afeta o comissionamento em velocidade de inspeção; afeta apenas o comissionamento em velocidade normal. 2. O indicador COP está OFF nesta falha. | (mesma célula de E35: pressionar MF.K para ocultar a indicação da falha; depois, comissionar em velocidade de inspeção) |
| E52 | Comunicação com a HCB anormal (HCB communication abnormal) | 1. Esta falha não afeta o autoajuste do motor nem o comissionamento em velocidade de inspeção. 2. O indicador HOP está OFF nesta falha. | (mesma célula de E35: pressionar MF.K para ocultar a indicação da falha; depois, comissionar em velocidade de inspeção) |
| E58 | Chaves de posição do poço anormais (Shaft position switches abnormal) | 1. O elevador não pode funcionar. É preciso corrigir a falha primeiro e só então realizar o comissionamento em velocidade de inspeção. 2. A causa da falha pode ser: as entradas de realimentação das duas chaves de redução de velocidade 1 (subida e descida) estão ativas; as entradas de realimentação das duas chaves de fim de curso (subida e descida) estão ativas simultaneamente. | 1. Os terminais X14 e X15 estão ligados às chaves de redução de velocidade 1 (entrada NC). Observe se os indicadores de sinal de X14 e X15 estão ambos OFF. Verifique se as chaves de redução de velocidade 1 estão ligadas a X14 e X15 e atuam corretamente. 2. Os terminais X12 e X13 estão ligados às chaves de fim de curso de subida e descida (entrada NC). Observe se os indicadores de sinal de X12 e X13 estão ambos OFF. Verifique se as chaves de fim de curso estão ligadas a X12 e X13 e atuam corretamente. |

Fonte: manual NICE3000new, págs. PDF 146 a 148 (impressas 145 a 147).

---

## 5.4 Comissionamento em velocidade de inspeção (Commissioning at Inspection Speed)

> **CUIDADO (Caution)** (bloco "Safety Information")
> - Garanta que toda a instalação e a ligação atendem às especificações de segurança elétrica antes do comissionamento em velocidade de inspeção.
> - Durante o autoajuste envolvendo a cabine, preste atenção ao sentido de rotação do motor e evite que o elevador chegue perto demais do pavimento extremo. Recomenda-se levar a cabine a um pavimento distante (por exemplo, a mais de 2 pavimentos) do pavimento extremo e só então realizar o comissionamento.
> - Em certos quadros de comando, usa-se "emergency electric RUN" (resgate elétrico) em vez de "inspection RUN" (manobra de inspeção). Observe que o "emergency electric RUN" coloca em curto certa parte da cadeia de segurança no poço, e é preciso dar mais atenção à segurança quando a cabine anda perto do pavimento extremo.

> **PERIGO (Danger)** ("To guarantee safe running of elevator", ou seja, "Para garantir o funcionamento seguro do elevador")
> - O motor pode girar durante o autoajuste. Mantenha distância de segurança do motor para evitar lesão pessoal.
> - Durante o autoajuste do motor com carga (with-load), garanta que não há pessoa no poço, para evitar lesão pessoal ou morte.

O comissionamento em velocidade de inspeção inclui o autoajuste do motor e o teste de funcionamento em velocidade de inspeção.

**Figura (sem número no manual, pág. PDF 149): fluxograma do comissionamento em velocidade de inspeção.** Em dois ramos:

- Autoajuste do motor (Motor auto-tuning): autoajuste com carga de motor síncrono (Synchronous motor with-load auto-tuning); autoajuste estático de motor síncrono (Synchronous motor static auto-tuning); autoajuste sem carga de motor síncrono (Synchronous motor no-load auto-tuning); autoajuste semiautomático sem ângulo de motor síncrono (Semi-automatic angle-free auto-tuning of synchronous motor); autoajuste totalmente automático sem ângulo de motor síncrono (Full-automatic angle-free auto-tuning of synchronous motor); autoajuste sem carga de motor assíncrono (Asynchronous motor no-load auto-tuning); autoajuste com carga de motor assíncrono (Asynchronous motor with-load auto-tuning).
- Teste de funcionamento em velocidade de inspeção (Running test at inspection speed), com o autoajuste em velocidade de inspeção ("Auto-tuning at inspection speed") e as verificações: sentido de rotação do motor correto; corrente de funcionamento do motor adequada; inspeção no topo da cabine habilitada ("inspection on top of the car is enabled"); poço desobstruído; chaves de redução de velocidade e de fim de curso do pavimento extremo efetivas.

(Ambíguo: as setas que ligam cada modo de autoajuste ao ramo "Auto-tuning at inspection speed" não podem ser lidas no texto extraído; ver o original na pág. PDF 149.)

### 5.4.1 Autoajuste do motor (Motor Auto-tuning)

#### 1. Parâmetros relacionados ao autoajuste do motor

(tabela conferida na imagem da página)

| Parâmetro | Descrição do parâmetro | Descrição |
|---|---|---|
| F1-25 | Tipo de motor (Motor type) | 0: motor assíncrono. 1: motor síncrono. |
| F1-00 | Tipo de encoder (Encoder type) | 0: encoder SIN/COS. 1: encoder UVW. 2: encoder incremental ABZ. 3: encoder absoluto Endat. |
| F1-12 | Pulsos do encoder por rotação (Encoder pulses per revolution) | 0 a 10000. |
| F1-01 a F1-05 | Potência nominal do motor; tensão nominal do motor; corrente nominal do motor; frequência nominal do motor; rotação nominal do motor | Estes parâmetros dependem do modelo e é preciso inseri-los manualmente conforme a placa de identificação. |
| F0-01 | Seleção da fonte de comando (Command source selection) | 0: controle pelo painel de operação. 1: controle por distância ("Distance control"). |
| F1-11 | Modo de autoajuste (Auto-tuning mode) | 0: sem operação. 1: autoajuste com carga. 2: autoajuste sem carga. 3: autoajuste do poço 1 (Shaft auto-tuning 1). 4: autoajuste do poço 2 (Shaft auto-tuning 2). 5: autoajuste estático de motor síncrono. |
| F1-22 | Seleção da função de autoajuste (Auto-tuning function selection) | F1-22 = 2: autoajuste semiautomático sem ângulo; o autoajuste de ângulo é realizado na primeira inspeção ou no primeiro resgate elétrico (emergency electric RUN) após desligar e ligar a alimentação novamente. F1-22 = 6: autoajuste totalmente automático sem ângulo; o autoajuste de ângulo é realizado na primeira corrida após desligar e ligar a alimentação novamente (sem diferenciar estados do elevador). |

#### 2. Fluxogramas de autoajuste do motor

Em todos os fluxogramas, cada caixa de etapa tem ao lado uma observação do manual. A sequência de cada fluxograma está transcrita abaixo. Nos fluxogramas síncronos conferidos na imagem (Figuras 5-5 e 5-9), a observação da primeira caixa é: "O indicador X9 na MCB está OFF, indicando que o elevador entrou no estado de resgate elétrico (emergency electric RUN)."

##### 1) Autoajuste de motor síncrono (Synchronous motor auto-tuning)

###### Autoajuste com carga de motor síncrono (motor ligado à cabine)

**Figura 5-5: autoajuste com carga de motor síncrono.** Procedimento:

1. Entrar no estado de resgate elétrico (emergency electric RUN). Observação: indicador X9 OFF (ver acima).
2. Verificar F0-01 = 1. Observação: F0-01 deve ser ajustado em 1 durante o autoajuste com carga.
3. Ajustar o tipo de motor: F1-25 = 1. Observação: ajuste F1-25 em 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05. Observações: (1) obtenha a potência nominal, a tensão nominal, a corrente nominal, a frequência nominal e a rotação nominal do motor na placa de identificação do motor; (2) garanta que os parâmetros do motor estão ajustados corretamente; caso contrário, ocorrerão falhas.
5. Ajustar os parâmetros do encoder: F1-00 e F1-12. Observações: (1) ajuste F1-00 conforme o tipo real de encoder: 0: encoder SIN/COS; 1: encoder UVW; 2: encoder ABZ; 3: encoder Endat; (2) ajuste F1-12 (pulsos do encoder por rotação) conforme a placa de identificação do encoder.
6. F1-11 = 1. Observação: após ajustar F1-11 em 1, pressione ENTER. Se o painel de operação exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se o painel de operação exibir "F1-12", o sistema não conseguiu entrar no estado de autoajuste do motor; é preciso verificar: (1) se o elevador está em estado de inspeção; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 1.
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste. Observação: mantenha pressionado o botão de acionamento de emergência UP/DOWN durante o autoajuste. Depois que o motor emite um som por 5 s, o freio é aberto. A força de tração gira cerca de duas voltas ("The traction force rotates about two circles", ambíguo, ver o original na pág. PDF 151). O controlador interrompe a saída automaticamente. O autoajuste está concluído. Neste momento, solte o botão de acionamento de emergência UP/DOWN.
8. Autoajuste concluído. Observações: (1) se o autoajuste for bem-sucedido, a MCB exibe o ângulo do encoder aprendido por 3 s. Se o autoajuste falhar, a MCB exibe Err; (2) garanta que o desvio do valor de F1-06 fique dentro de ±5° ao longo de várias execuções de autoajuste; (3) F1-08 é ajustado, na maioria dos casos, em 0 ou 8. F1-08 permanece inalterado ao longo de várias execuções de autoajuste.

###### Autoajuste estático de motor síncrono (motor ligado à cabine, freio não liberado e motor não gira)

**Figura 5-6: autoajuste estático de motor síncrono.** Procedimento:

1. Entrar no estado de resgate elétrico (emergency electric RUN).
2. Verificar F0-01 = 1. Observação: F0-01 deve ser ajustado em 1 durante o autoajuste com carga ("with-load").
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (mesmas observações do procedimento anterior: dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12. Observações: (1) ajuste F1-00 conforme o tipo real de encoder: 0: encoder SIN/COS; 3: encoder Endat; (2) ajuste F1-12 conforme a placa de identificação do encoder.
6. F1-11 = 5. Observação: após ajustar F1-11 em 5, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se o painel exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de inspeção; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 1.
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste. Observação: mantenha pressionado o botão durante o autoajuste. Após a conclusão do autoajuste, o controlador interrompe a saída automaticamente, e então o botão pode ser solto.
8. Autoajuste concluído. Observações: (1) se for bem-sucedido, a MCB exibe o ângulo do encoder aprendido por 3 s. Se falhar, a MCB exibe Err; (2) desvio de F1-06 dentro de ±5° ao longo de várias execuções; (3) F1-08 é ajustado, na maioria dos casos, em 0. F1-08 permanece inalterado ao longo de várias execuções.

> **NOTA (Note)**
> - O autoajuste estático está disponível apenas para o encoder SIN/COS e o encoder absoluto do motor síncrono. A sequência dos cabos de potência de saída do controlador deve ser consistente com a sequência dos cabos do encoder.
> - Durante o autoajuste, F1-08 deve ser ajustado em 0. Se a sequência de fases real do encoder for 8, ajuste F1-24 BIT6 em 1 e F1-08 em 0.

###### Autoajuste semiautomático sem ângulo de motor síncrono

**Figura 5-7: autoajuste semiautomático sem ângulo de motor síncrono.** Procedimento:

1. Entrar no estado de resgate elétrico (emergency electric RUN). Observação: (1) o autoajuste sem ângulo é realizado automaticamente no resgate elétrico; em seguida, o motor funciona na velocidade do resgate elétrico; (2) depois que o autoajuste for bem-sucedido, nenhum autoajuste é realizado antes do próximo desligamento.
2. Verificar F0-01 = 1. Observação: "F0-01 must be set to 1 during with-load auto-tuning." (texto do original).
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12. Observações: F1-00 conforme o tipo real (0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat); F1-12 conforme a placa de identificação do encoder.
6. F1-22 = 2. Observação do original: "Set F1-12 to 2 to enable semi-automatic angle-free auto-tuning." (ambíguo, ver o original na pág. PDF 153: o texto cita F1-12, enquanto a caixa da etapa e a tabela da pág. PDF 150 indicam F1-22 = 2).
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste no estado de resgate elétrico.
8. Autoajuste concluído. Observações: (1) se as falhas Err19 e Err20 forem reportadas durante o autoajuste, o autoajuste falhou; (2) se nenhuma falha for reportada e o elevador funcionar normalmente na velocidade de inspeção, o autoajuste foi bem-sucedido.

###### Autoajuste totalmente automático sem ângulo ("Automatic angle-free auto-tuning")

**Figura 5-8: autoajuste totalmente automático sem ângulo de motor síncrono.** Procedimento:

1. Entrar no estado de resgate elétrico (emergency electric RUN). Observação: (1) o autoajuste totalmente automático sem ângulo é realizado no resgate elétrico ou no estado de funcionamento automático; (2) depois que o autoajuste for bem-sucedido, nenhum autoajuste é realizado antes do próximo desligamento.
2. Verificar F0-01 = 1. Observação: "F0-01 must be set to 1 during with-load auto-tuning." (texto do original).
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-22 = 6. Observação do original: "Set F1-12 to 6 to enable full-automatic angle-free auto-tuning." (ambíguo, ver o original na pág. PDF 154: o texto cita F1-12, enquanto a caixa da etapa e a tabela indicam F1-22 = 6).
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste no estado de resgate elétrico.
8. Autoajuste concluído. Observações: (1) se as falhas Err19 e Err20 forem reportadas durante o autoajuste, o autoajuste falhou; (2) se nenhuma falha for reportada e o elevador funcionar normalmente na velocidade de inspeção, o autoajuste foi bem-sucedido.

###### Autoajuste sem carga de motor síncrono (motor desligado da cabine)

**Figura 5-9: autoajuste sem carga de motor síncrono.** Procedimento (conferido na imagem):

1. Entrar no estado de resgate elétrico (emergency electric RUN). Observação: indicador X9 OFF na MCB.
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste sem carga.
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 2. Observação: após ajustar F1-11 em 2, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de resgate elétrico; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
7. Realizar o autoajuste: (1) liberar o freio manualmente; (2) pressionar a tecla RUN no painel de operação para iniciar o autoajuste. Observação: o freio deve ser liberado manualmente no estado de autoajuste sem carga. Após a conclusão do autoajuste, o controlador interrompe a saída automaticamente.
8. Autoajuste concluído. Observações: (1) se for bem-sucedido, a MCB exibe o ângulo do encoder aprendido por 3 s. Se falhar, a MCB exibe Err; (2) desvio de F1-06 dentro de ±5° ao longo de várias execuções; (3) F1-08 é ajustado, na maioria dos casos, em 0 ou 8; F1-08 permanece inalterado ao longo de várias execuções.
9. Restaurar F0-01 para 1. Observação: após a conclusão do autoajuste, F0-01 deve ser restaurado para 1. Caso contrário, o elevador não pode funcionar.

**Precauções durante o autoajuste de motor síncrono:**

- O autoajuste de motor síncrono aprende o ângulo polar inicial do motor, o ângulo inicial do encoder, o modo de ligação do motor e a indutância do eixo D e do eixo Q ("shaft-D and shaft-Q inductance").
- Realize três ou mais autoajustes; compare os valores obtidos de F1-06 (ângulo inicial do encoder), e o desvio do valor de F1-06 deve ficar dentro de ±5°.
- Cada vez que o encoder, a conexão do cabo do encoder ou a sequência de ligação do motor, bem como a corrente, a frequência e a rotação nominais do motor, forem alterados, realize o autoajuste do motor novamente.
- É possível modificar F1-06 manualmente. A modificação tem efeito imediato. Portanto, ao substituir a MCB, pode-se fazer o controlador funcionar diretamente ajustando manualmente F1-06 para o valor original, em vez de realizar o autoajuste do motor.

##### 2) Autoajuste de motor assíncrono (Asynchronous motor auto-tuning)

###### a) Autoajuste com carga de motor assíncrono (motor ligado à cabine)

**Figura 5-10: autoajuste com carga de motor assíncrono.** Procedimento (ordem das caixas conforme o padrão das Figuras 5-5 e 5-9; ver nota em "Lacunas e dúvidas"):

1. Entrar no estado de resgate elétrico (emergency electric RUN).
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste com carga.
3. Ajustar o tipo de motor: F1-25 = 0.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 1. Observação: após ajustar F1-11 em 1, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de resgate elétrico; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
7. Pressionar a tecla RUN no painel de operação para iniciar o autoajuste.
8. Autoajuste concluído. Observações: (1) durante o autoajuste com carga, o motor não gira, mas há ruído de corrente. O processo de autoajuste dura cerca de várias dezenas de segundos; (2) após a conclusão, o controlador interrompe a saída automaticamente; (3) são obtidos os cinco parâmetros F1-14 a F1-18.
9. Restaurar F0-01 para 1. Observação: após a conclusão do autoajuste, F0-01 deve ser restaurado para 1. Caso contrário, o elevador não pode funcionar em velocidade de inspeção.

###### b) Autoajuste sem carga de motor assíncrono

**Figura 5-11: autoajuste sem carga de motor assíncrono.** Procedimento (mesma ressalva de ordem):

1. Entrar no estado de resgate elétrico (emergency electric RUN).
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste sem carga.
3. Ajustar o tipo de motor: F1-25 = 0.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 2. Observação: após ajustar F1-11 em 2, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de resgate elétrico; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
7. Realizar o autoajuste: (1) liberar o freio manualmente; (2) pressionar a tecla RUN no painel de operação para iniciar o autoajuste.
8. Autoajuste concluído. Observações: (1) durante o autoajuste sem carga, o motor gira, mas o freio deve ser liberado manualmente. O processo de autoajuste dura cerca de várias dezenas de segundos; (2) após a conclusão, o controlador interrompe a saída automaticamente; (3) são obtidos os cinco parâmetros F1-14 a F1-18.
9. Restaurar F0-01 para 1. Observação: após a conclusão do autoajuste, F0-01 deve ser restaurado para 1. Caso contrário, o elevador não pode funcionar.

**Precauções durante o autoajuste de motor assíncrono:**

- A sequência das fases A e B do encoder deve estar correta. Se a sequência estiver incorreta, a falha Err38 é reportada. Para resolver o problema, troque as fases A e B do encoder.

O sistema trata os comandos de saída para o contator de marcha (RUN contactor) ou o contator do freio (brake contactor) de forma diferente nos diferentes modos de autoajuste do motor, como descrito na tabela a seguir.

**Tabela 5-2: estado de saída dos contatores de marcha e de freio e estado do motor** (tabela conferida na imagem; a primeira célula do cabeçalho tem o eixo "Auto-tuning Mode" por "Working Mode" por "Controlled Object", isto é, modo de autoajuste, modo de trabalho e objeto controlado)

| Objeto controlado | Sem carga: motor síncrono | Sem carga: motor assíncrono | Com carga: motor síncrono | Com carga: autoajuste estático de motor síncrono | Com carga: motor assíncrono |
|---|---|---|---|---|---|
| Contator de marcha (RUN contactor) | Working (atuando) | Working | Working | Working | Working |
| Contator do freio (Brake contactor) | Not working (não atuando) | Not working | Working | Not working | Not working |
| Motor | Rotate (gira) | Rotate | Rotate | Not rotate (não gira) | Not rotate |

#### Falhas possíveis e tratamento (Possible faults and handling)

(tabela conferida na imagem)

| Falha de autoajuste | Sintoma da falha | Método de tratamento |
|---|---|---|
| O autoajuste falha (Auto-tuning fails). | Falha E19 é reportada. | Verifique se o cabo do encoder está rompido; troque por uma nova placa PG (PG card) e realize o autoajuste novamente. Verifique se os cabos do encoder estão rompidos; troque por uma nova placa PG e realize o autoajuste novamente. (As duas frases aparecem assim no original, repetidas.) |
| (mesma linha de falha: o autoajuste falha) | O autoajuste falha e a falha Err20 é reportada. | a. Verifique se os cabos do encoder e o circuito de corrente forte estão em calhas separadas. b. Verifique se o freio está completamente liberado. Se não, verifique se a alimentação do freio e o circuito de potência estão normais. c. Verifique se os cabos do encoder estão rompidos. d. Verifique se há interferência nos cabos do encoder, observando se eles estão muito próximos dos cabos de potência do motor. e. Verifique se o encoder está em bom estado e instalado com firmeza. f. O motor de baixa potência (por exemplo, P ≤ 5,5 kW) pode vibrar ("jitter") depois que o autoajuste começa. Diminua o valor de F2-00 para dentro de 10 a 40. |
| A sequência de ligação do motor está incorreta. | Err20 e Err33 podem ser reportadas. | Troque os cabos do motor. Depois, realize o autoajuste novamente. A figura a seguir mostra a troca dos cabos do motor (veja a figura abaixo). **Nota: sintomas da falha.** 1. Durante o autoajuste sem carga, se a sequência de ligação do motor estiver incorreta, Err20 (E0-00) com subcódigo de falha 3 (E0-01) será reportada. 2. Durante o autoajuste com carga, se a sequência de ligação do motor estiver incorreta, o motor síncrono vibrará de forma anormal durante o autoajuste, Err33 será reportada e o autoajuste para. Para o motor assíncrono, não há aviso durante o autoajuste, mas Err33 é reportada durante o funcionamento em velocidade de inspeção. |

**Figura (sem número, dentro da Tabela de falhas): troca dos cabos do motor.** Mostra o bloco de bornes do controlador (aterramento, +, −, R, S, T, PB, U, V, W, aterramento; grupos "POWER" e "MOTOR") em dois desenhos, antes e depois: dois dos três cabos ligados a U, V, W (setas circulares vermelhas entre eles) são trocados de posição, e a seta tracejada vermelha leva ao desenho "depois".

> **NOTA (Note)**
> - Quando os dois problemas acima ocorrem, a sequência de ligação do motor ao controlador precisa ser alterada.
> - Para alterar a sequência de ligação: troque quaisquer dois fios de fases adjacentes, apenas uma vez.

(Observação de fidelidade: o original usa "E19" na coluna de sintoma e "Err19" nas Figuras 5-7 e 5-8; mantido como no manual.)

### 5.4.2 Teste de funcionamento em velocidade de inspeção (Running Test at Inspection Speed)

(tabela conferida na imagem)

| Parâmetro | Descrição do parâmetro | Descrição | Padrão |
|---|---|---|---|
| F2-10 | Sentido de marcha do elevador (Elevator running direction) | 0: sentido inalterado. 1: sentido invertido. | 0 |
| F3-25 | Velocidade do resgate elétrico (Emergency electric RUN speed) | 0,100 a 0,600 m/s | 0,250 m/s |

**Fluxo do teste de funcionamento em velocidade de inspeção (Running Test Flow at Inspection Speed)**, cinco verificações (conferido na imagem):

1. Verificar que o sentido de rotação do motor está correto. Depois que o autoajuste for concluído com sucesso, faça uma marcha de teste em velocidade de inspeção para verificar se o sentido real do motor é o mesmo do sentido comandado. Se não for, altere F2-10 para corrigir o sentido.
2. Verificar que a corrente de funcionamento do motor está normal. Durante a marcha em velocidade de inspeção, a corrente do motor em funcionamento sem carga é menor que 1 A, e a corrente real durante a marcha em velocidade constante com carga não é maior que a corrente nominal do motor. Se, depois de várias execuções de autoajuste, o desvio do ângulo do encoder for pequeno mas a corrente durante a marcha em velocidade constante com carga for maior que a corrente nominal do motor, verifique:
   - □ se o freio está completamente liberado;
   - □ se o coeficiente de balanceamento do elevador está normal;
   - □ se as sapatas-guia da cabine ou do contrapeso estão muito apertadas.
3. Verificar que a inspeção no topo da cabine está habilitada. Verifique que a inspeção no topo da cabine está habilitada e que a inspeção na casa de máquinas está desabilitada. Ou seja, a inspeção no topo da cabine tem precedência sobre a inspeção na casa de máquinas.
4. Verificar que o poço está desobstruído. Verifique que o poço está desobstruído, sem quaisquer obstáculos, para que a cabine não seja danificada.
5. Verificar que as chaves de redução de velocidade e as chaves de fim de curso são efetivas. Verifique que as chaves de redução de velocidade e as chaves de fim de curso são efetivas e dê atenção especial à segurança ao levar a cabine ao pavimento extremo. Recomenda-se que o tempo e a distância de marcha não sejam longos a cada vez, evitando que a cabine ultrapasse o extremo ("over travel terminal") ou seja danificada.

Fonte: manual NICE3000new, págs. PDF 149 a 159 (impressas 148 a 158).

---

## Lacunas e dúvidas

1. **Dados do motor de referência.** Potência, tensão, corrente, frequência e rotação nominais (F1-01 a F1-05) e o tipo de motor (F1-25: síncrono ou assíncrono) dependem da placa de identificação do motor do elevador de referência. Nenhum valor foi preenchido.
2. **Encoder.** Tipo (F1-00) e pulsos por rotação (F1-12) dependem da placa do encoder do elevador de referência. A escolha entre autoajuste estático (só SIN/COS e Endat), com carga, sem carga ou sem ângulo (F1-22 = 2 ou 6) depende do tipo de encoder, de o motor estar ou não ligado à cabine e da configuração do projeto.
3. **Velocidade.** F3-25 (velocidade do resgate elétrico, padrão 0,250 m/s, faixa 0,100 a 0,600 m/s) deve ser conferida contra a velocidade de inspeção definida no projeto. A velocidade nominal do elevador de referência não consta nestas seções.
4. **Altura de pavimento e posição da cabine.** O manual recomenda levar a cabine a mais de 2 pavimentos do pavimento extremo antes do autoajuste. A altura de pavimento e o número de paradas do elevador de referência não constam nestas seções e dependem do projeto.
5. **Terminais de entrada.** As indicações X4/X25 (cadeia de segurança), X5/X26/X27 (circuito de fechaduras), X12/X13 (fim de curso), X14/X15 (redução de velocidade 1) valem para o ajuste padrão de fábrica (aviso CUIDADO da seção 5.2). Se o projeto alterou a configuração dos terminais, é preciso conferir.
6. **Quadro de comando com "emergency electric RUN" no lugar de "inspection RUN".** O manual diz que isso ocorre "em certos quadros de comando" sem dizer quais. Depende do quadro do projeto.
7. **Trechos ambíguos do texto original:** (a) Figura 5-1, ordem das caixas dentro dos blocos (pág. PDF 143); (b) Figura 5-4, indicadores acesos em cada falha (págs. PDF 147 e 148); (c) fluxograma sem número da pág. PDF 149, ligações entre os modos de autoajuste; (d) Figuras 5-7 e 5-8, observação cita "F1-12" onde a etapa indica F1-22 (págs. PDF 153 e 154); (e) tabela de falhas, frase de E19 repetida e uso de "E19" contra "Err19" (pág. PDF 158); (f) Figuras 5-6, 5-7, 5-8, 5-10 e 5-11 não foram conferidas visualmente (apenas 5-5 e 5-9); a ordem das caixas segue o texto extraído e o padrão das figuras conferidas; (g) pág. PDF 142 contém apenas o sumário do capítulo, e o conteúdo da 5.1 começa na PDF 143; (h) E51 e E52 não têm método de tratamento próprio no original: a célula única de E35 ocupa as três linhas.
8. **Termos do glossário.** "Carro/car" foi traduzido como "cabine" e "equipment room" como "casa de máquinas"; "traction force rotates about two circles" foi traduzido literalmente (frase possivelmente truncada no original). "Shaft auto-tuning" está como "autoajuste do poço" (descrito na seção 5.5.1, fora deste escopo).
