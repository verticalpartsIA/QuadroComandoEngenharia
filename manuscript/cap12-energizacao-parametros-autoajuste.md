# Capítulo 12. Energização, parâmetros e autoajuste

> RASCUNHO v0.1 de 14/11/2026. Aguarda aprovação do Gelson e assinatura da Qualidade. O texto das seções 12.1 a 12.7 é tradução fiel do capítulo 4 e das seções 5.1 a 5.6 do manual do controlador; as seções 12.8 em diante usam o esquema Vitinho. Este arquivo é montado por `build/monta_cap12.py`; edite os arquivos de origem em `sources/` e `manuscript/_cap12-*.md`.

**Parte IV. Comissionamento**

## 12.0 O que você vai aprender

Ao terminar este capítulo você será capaz de:

1. Verificar a segurança e os circuitos do quadro de comando antes da primeira energização.
2. Energizar o controlador e ler o estado dele.
3. Comissionar em velocidade de inspeção, incluindo o autoajuste do motor.
4. Fazer o autoajuste do poço e comissionar em velocidade normal.
5. Ajustar o conforto de viagem e a precisão de nivelamento.
6. Saber quais parâmetros do projeto aparecem no esquema.

> **PERIGO.** Antes de qualquer verificação nos bornes, desligue toda a alimentação e espere no mínimo 10 minutos. Mantenha a cabina livre e sem passageiros durante todo o comissionamento. Antes de energizar, confira que os jumpers de bancada (fios 62 a 66 da lista de fios) foram removidos e que a cadeia de segurança e as fechaduras estão ligadas de verdade (capítulos 1 e 4). Nunca ponteie a cadeia de segurança nem as fechaduras para "ajudar" um autoajuste. Fonte: manual NICE3000new, págs. PDF 20 e 21; esquema Vitinho, folha /19.

> **NOTA.** Os dados do motor da máquina de referência (potência, tensão, corrente, frequência e rotação nominais), o tipo e os pulsos do encoder, a velocidade nominal e a altura entre pavimentos não constam em nenhum documento do projeto. Onde o procedimento pede esses valores, o texto remete à placa do motor e à do encoder. O elevador de referência tem máquina síncrona de ímã permanente e encoder SIN/COS (EI53C9.25-2048), e por isso valem os procedimentos de motor síncrono.

## 12.1 Ferramentas de comissionamento

### 12.1.1 Keypad

O keypad é composto por três LEDs e três botões. Nele é possível ver informações sobre o controlador e inserir comandos simples.

Figura 4-1: aparência do keypad, com os botões PRG, UP e SET e os segmentos de LED rotulados A a G e DP.

Os três botões são PRG, UP e SET. As funções estão na tabela a seguir.

| Botão | Função |
|---|---|
| PRG | Pressione em qualquer estado para exibir o número do grupo de função atual e sair da operação atual. |
| UP | Pressione para aumentar o número do grupo de função ou o dado. No menu do grupo F6, este botão é usado para inserir o comando de abrir porta. |
| SET | Entra no modo de edição do menu de funções; confirma e salva a operação atual. No menu do grupo F6, este botão é usado para inserir o comando de fechar porta. |

A Figura 4-2 mostra o ajuste para aumentar o pavimento chamado (called floor) até 4.

Figura 4-2: Ajuste do pavimento chamado. Fluxo entre o "modo de menu de funções" (sequência F-b, F-C, F-d, F-0, F-1, F-2, F-3, percorrida com UP) e o "modo de edição do menu de funções", com os botões PRG, UP e SET; rótulos "Default (Current floor)", "(Saving)" e "(Without saving)". O texto do fluxo não permite reconstruir a ordem exata das setas (ambíguo, ver o original na pág. PDF 136).

Para os menus de função exibidos no keypad, o manual remete a "6.1 Keypad".

Fonte: manual NICE3000new, págs. PDF 135 a 136 (impressas 134 a 135)

### 12.1.2 Painel de operação (Operation Panel)

Figura 4-3: diagrama do painel de operação com LED, com as legendas: Reserved; RUN indicator; Data display; Programming key; Menu key; RUN key; Up/Down indicator; Auto-tuning indicator; Unit indicator; UP key; Shift key; Stop/Reset key; Confirm key; Down key; Fault hiding key. No painel aparecem ainda os rótulos MF.K, RUN, STOP/RES, QUICK, PRG, ENTER, RUN, LOCAL/REMOT, FWD/REV, TUNE/TC e as unidades RPM, %, A, V, Hz.

#### 12.1.2.1 Descrição das teclas (Description of Keys)

| Tecla | Nome | Função |
|---|---|---|
| PRG | Programming | Entrar ou sair do menu de nível I. |
| ENTER | Enter | Entrar em cada nível da interface de menu. Confirmar o ajuste do parâmetro. |
| Up | Up | Aumentar o dado ou parâmetro. |
| Down | Down | Diminuir o dado ou parâmetro. |
| Shift | Shift | Selecionar, em sequência, os parâmetros exibidos nos estados parado ou em funcionamento. Selecionar o dígito a modificar ao alterar o valor de um parâmetro. |
| RUN | RUN | Dar partida no controlador no modo de controle pelo painel de operação. |
| STOP/RES | Stop/Reset | Parar o controlador quando está no estado RUN. Executar uma operação de reset quando o controlador está no estado FAULT. |
| MF.K | Fault hiding | Exibir ou ocultar a informação de falha no estado de falha, o que facilita a visualização de parâmetros. |
| QUICK | Quick | Entrar ou sair do menu rápido de nível I. |

Os símbolos gráficos das teclas Up, Down e Shift não foram preservados no texto extraído; os nomes acima vêm da coluna "Name" e da legenda da Figura 4-3 (ambíguo, ver o original na pág. PDF 137).

#### 12.1.2.2 Indicadores (Indicators)

Na Tabela 4-1 do manual, os símbolos de aceso, apagado e piscando são figuras; abaixo, aceso = ON, apagado = OFF.

Tabela 4-1: Descrição dos indicadores do painel de operação

| Indicador | Estado | Descrição do estado |
|---|---|---|
| RUN | OFF | Parado (Stop) |
| RUN | ON | Em funcionamento (Running) |
| FWD/REV | OFF | Movimento em sentido direto (Forward running) |
| FWD/REV | ON | Movimento em sentido reverso (Reverse running) |
| TUNE/TC | OFF | -- |
| TUNE/TC | ON | Estado de autoajuste (Auto-tuning state) |
| Unidade (RPM, %, A, V, Hz) | Indicador de Hz aceso | Unidade de frequência: Hz |
| Unidade | Indicador de A aceso | Unidade de corrente: A |
| Unidade | Indicador de V aceso | Unidade de tensão: V |
| Unidade | Indicador de RPM aceso | Unidade de velocidade de rotação: RPM |
| Unidade | Indicador de % aceso | Porcentagem: % |

Qual símbolo de estado vale para cada linha de RUN, FWD/REV e TUNE/TC foi lido da ordem do texto extraído e do rótulo "OFF/ON" (ambíguo quanto ao símbolo gráfico, ver o original na pág. PDF 138).

#### 12.1.2.3 Exibição de dados (Data Display)

O painel de operação tem um display LED de cinco dígitos. Ele exibe a frequência ajustada, a frequência de saída, vários tipos de dados de monitoramento e códigos de falha.

Tabela 4-2: Exibição no LED e dado real (conferida na renderização da página)

| Dado real | Dado real | Dado real | Dado real |
|---|---|---|---|
| 0 | 6 | C | N |
| 1 | 7 | c | P |
| 2 | 8 | D | R |
| 3 | 9 | E | T |
| 4 | A | F | U |
| 5, S | B | L | u |

(No manual, cada dado real é precedido pela imagem do caractere de 7 segmentos correspondente, na ordem de colunas "LED Display / Actual Data" repetida quatro vezes.)

#### 12.1.2.4 Operações básicas (Basic Operations)

O painel de operação adota três níveis de menu:

- Nível I: grupo de código de função (function code group)
- Nível II: código de função (function code)
- Nível III: valor de ajuste do código de função (function code setting value)

Figura (sem número): estrutura de menus. Na energização ou após o reset de fábrica (factory reset) o display mostra 0.000; PRG leva ao menu de nível I (grupos F0, F1, ..., F9, FA, ..., FP, percorridos com Up e Down); ENTER entra no nível II (códigos F0-00, F0-01, ..., F0-07, percorridos com Up e Down); ENTER entra no nível III (valor do parâmetro, por exemplo F0-01); PRG retorna ao nível anterior.

##### 1 Exibição de parâmetros (Parameter display)

O conteúdo específico dos parâmetros exibidos é ajustado em FA-01 (Display in running state, exibição no estado de funcionamento) e FA-02 (Display in stop state, exibição no estado parado). Cada bit binário de FA-01 e FA-02 indica um conteúdo específico de parâmetro (para detalhes, o manual remete à descrição dos parâmetros). Se um bit é ajustado em 1, o parâmetro indicado por esse bit é exibido; se o bit é ajustado em 0, o parâmetro não é exibido.

Nos estados parado ou em funcionamento, vários parâmetros de estado podem ser exibidos pressionando uma tecla do painel de operação (o símbolo da tecla foi perdido na extração; a tecla Shift é a que o manual descreve para esta função em 4.2.1) para alternar entre cada "byte" de FA-01 e FA-02 (ambíguo, ver o original na pág. PDF 140).

- Parâmetros de estado em funcionamento (Running state parameters): há 16 parâmetros de estado disponíveis no estado de funcionamento. A exibição de cada parâmetro correspondente a cada bit é escolhida segundo os bits binários de FA-01 (Display in running state).
- Parâmetros de estado parado (Stop state parameters): há 12 parâmetros de estado disponíveis no estado parado. A exibição de cada parâmetro correspondente a cada bit é escolhida segundo os bits binários de FA-02 (Display in stop state).

NOTA (Note): Para detalhes dos estados, consulte FA-01 e FA-02 em "6 Parameter Description".

##### 2 Visualização de parâmetros (Parameter viewing)

Pressione PRG e depois uma das teclas Up/Down (símbolos perdidos na extração, ambíguo, ver o original na pág. PDF 140) para exibir o menu de nível I, isto é, a classificação dos grupos de parâmetros.

Depois de entrar em cada nível de menu, se um dígito do display piscar, ele pode ser modificado com as três teclas indicadas por símbolos (ambíguo, ver o original na pág. PDF 140). A figura seguinte mostra o fluxo de operação.

Figura 4-4: Procedimento de visualização de parâmetros. Sequência de telas: parâmetro de estado (exibição padrão) -> PRG -> menu de nível I -> ENTER (entrar) -> menu de nível II -> ENTER (entrar) -> menu de nível III; em cada nível, PRG retorna ao nível anterior; ENTER (Save) salva; "Switchover" alterna entre itens do mesmo nível; "Cyclic process" indica percurso cíclico.

##### 3 Modificação de parâmetros (Parameter modification)

Depois de entrar em cada nível de menu, se um dígito do display piscar, ele pode ser modificado com as três teclas indicadas por símbolos (ambíguo, ver o original na pág. PDF 140).

Do menu de nível III é possível voltar ao menu de nível II pressionando PRG ou ENTER. A diferença entre os dois é:

- Após pressionar ENTER, o sistema primeiro salva o ajuste do parâmetro, depois volta ao menu de nível II e passa ao parâmetro seguinte.
- Após pressionar PRG, o sistema desiste da modificação do parâmetro atual e retorna diretamente ao menu de nível II, permanecendo no código de função atual.

Ao operar nos menus de nível III, se o parâmetro não tem um dígito piscando, não é permitido alterá-lo. Há duas razões possíveis:

- O parâmetro é somente de leitura, como, por exemplo, o tipo de AC drive, parâmetros realmente detectados e parâmetros de registro de funcionamento.
- Ele só pode ser modificado depois que o motor for parado.

Exemplo (Example): alterar F3-02 de 10.00 Hz para 15.00 Hz.

Figura 4-5: Procedimento de modificação de parâmetro. Sequência de telas: parâmetro de estado (exibição padrão) -> PRG -> menu de nível I -> ENTER -> menu de nível II -> (Switchover) -> ENTER -> menu de nível III -> (alterar o valor) -> ENTER (Save) -> retorno; PRG (Return) retorna sem salvar. Os valores intermediários exibidos em cada tela do exemplo são imagens e não constam do texto (ambíguo, ver o original na pág. PDF 141).

Fonte: manual NICE3000new, págs. PDF 136 a 141 (impressas 135 a 140)

### 12.1.3 Software de comissionamento para celular (Cell phone commissioning software)

Este software implementa principalmente: ajuste de parâmetros, comissionamento de funções, monitoramento do estado de operação em tempo real, carga (upload) e descarga (download) de parâmetros e gravação do firmware (burning) do sistema de controle do elevador no controlador, usando um smartphone.

Para detalhes, o manual remete ao "User Manual of Elevator Commissioning APP via Smartphone", com código de dados (data code) 19010576.

Fonte: manual NICE3000new, pág. PDF 141 (impressa 140)

---

## 12.2 Guia de comissionamento do sistema (System Commissioning Guide)

**Fluxograma do manual (figura 5-1): fluxograma geral de comissionamento do NICE3000new.** Mostra a sequência, de "Start" a "End", com as etapas em texto:

1. Verificação de segurança e de circuitos (Safety and circuit check).
2. Verificação da energização e do estado do controlador (Power-on and controller state check).
3. Comissionamento em velocidade de inspeção (Commissioning at inspection speed), composto por: autoajuste do motor (Motor auto-tuning) e teste de funcionamento em velocidade de inspeção (Running test at inspection speed).
4. Comissionamento em velocidade normal (Commissioning at normal speed), composto por: autoajuste do poço (Shaft auto-tuning), comissionamento da cabine (Car commissioning) e comissionamento da HCB (HCB commissioning).
5. Ajuste do conforto de viagem (Riding comfort adjustment), composto por: ajuste do conforto de viagem e ajuste da precisão de nivelamento (Leveling accuracy adjustment).

(Ambíguo quanto à ordem exata das caixas dentro do bloco 4 e do bloco 5: o texto extraído lista as caixas fora de ordem; ver o original na pág. PDF 143, Figura 5-1. A ordem acima segue a ordem dos títulos do índice do manual.)

Fonte: manual NICE3000new, págs. PDF 143 (impressa 142).

---

## 12.3 Verificação de segurança e de circuitos (Safety and Circuit Check)

Observe as seguintes precauções antes de realizar o comissionamento:

> **CUIDADO (Caution)**
> Os terminais de entrada e saída do NICE3000new têm ajuste padrão de fábrica na entrega. Você pode alterar o ajuste conforme suas necessidades. Os exemplos deste manual são todos baseados no ajuste padrão dos terminais.

### 1. Diagrama de ligação do sistema (System Wiring Diagram)

Consultar a Figura 2-39.

### 2. Fluxograma da verificação de segurança (Safety Check Flowchart)

**Fluxograma do manual (figura 5-2): fluxograma da verificação de segurança e de circuitos antes da energização.** Quatro etapas em sequência:

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

## 12.4 Energização e verificação do estado do controlador (Power-on and Controller State Check)

### 12.4.1 Verificação do estado de energização (Checking Power-on State)

| Nº | Conteúdo da verificação |
|---|---|
| 1 | Aplique a alimentação. Verifique que a tensão de linha das fases R, S, T do controlador está entre 380 e 440 VAC, com grau de desequilíbrio de fase ≤ 3%. Se estiver anormal, desligue a alimentação e verifique a alimentação e a ligação dos cabos R, S, T no controlador. |
| 2 | Verifique que a tensão de entrada de alimentação no terminal de 24 V (CN3) da MCB é 24 VDC ±15%. Se estiver anormal, desligue a alimentação; verifique a fonte chaveada e verifique se o circuito de 24 VDC está ligado corretamente. |

### 12.4.2 Verificação do estado na energização normal (State Check at Normal Power-on)

| Nº | Conteúdo da verificação |
|---|---|
| 1 | Verifique que o teclado (keypad) tem display após a energização. Se não houver display no teclado, verifique se a alimentação do controlador está normal. |
| 2 | Se os indicadores dos sinais de entrada mostrados na figura anterior ficarem ON, isso indica que a alimentação de 24 VDC está normal e que os terminais de entrada X funcionam corretamente. Se nenhum dos indicadores estiver ON, isso indica que a alimentação de 24 VDC está anormal, e é preciso eliminar o problema. |

**Fluxograma do manual (figura 5-3): display da MCB após a energização normal.** Desenho da placa MCB do NICE3000new (integrated elevator controller) com os conectores (CN1, CN2, CN3, CN4, CN7, CN9, CN12, J1 a J14), as teclas PRG, UP, SET, os indicadores de entrada X1 a X28 e os indicadores COP, HOP, CAN2, MOD2 e 232. Legendas: "a. There is display on the LEDs." (a. há display nos LEDs) e "b. Certain inputs on the MCB are active." (b. certas entradas da MCB estão ativas).

### 12.4.3 Estados possíveis do controlador e métodos de tratamento antes do comissionamento (Potential Controller States and Handling Methods Before Commissioning)

#### 1. Verifique o estado do controlador e trate as falhas relacionadas

Durante o comissionamento, especialmente na primeira energização, certas falhas podem ocorrer porque as condições para o funcionamento automático do elevador não são atendidas e certos sinais periféricos não estão ligados. Essas falhas são E41, E42, E35, E51, E52 e E58. A parte a seguir descreve o estado da MCB na falha e o tratamento dessas falhas.

**Fluxograma do manual (figura 5-4): estado da MCB nas falhas durante o comissionamento.** Seis desenhos da placa MCB, um para cada falha (E41, E42, E35, E51, E52, E58), com os indicadores de entrada no estado correspondente. (Ambíguo: quais indicadores estão acesos em cada desenho não consta no texto extraído; ver o original nas págs. PDF 147 e 148, Figura 5-4.)

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

## 12.5 Comissionamento em velocidade de inspeção (Commissioning at Inspection Speed)

> **CUIDADO (Caution)** (bloco "Safety Information")
> - Garanta que toda a instalação e a ligação atendem às especificações de segurança elétrica antes do comissionamento em velocidade de inspeção.
> - Durante o autoajuste envolvendo a cabine, preste atenção ao sentido de rotação do motor e evite que o elevador chegue perto demais do pavimento extremo. Recomenda-se levar a cabine a um pavimento distante (por exemplo, a mais de 2 pavimentos) do pavimento extremo e só então realizar o comissionamento.
> - Em certos quadros de comando, usa-se "emergency electric RUN" (operação elétrica de emergência) em vez de "inspection RUN" (manobra de inspeção). Observe que o "emergency electric RUN" coloca em curto certa parte da cadeia de segurança no poço, e é preciso dar mais atenção à segurança quando a cabine anda perto do pavimento extremo.

> **PERIGO (Danger)** ("To guarantee safe running of elevator", ou seja, "Para garantir o funcionamento seguro do elevador")
> - O motor pode girar durante o autoajuste. Mantenha distância de segurança do motor para evitar lesão pessoal.
> - Durante o autoajuste do motor com carga (with-load), garanta que não há pessoa no poço, para evitar lesão pessoal ou morte.

O comissionamento em velocidade de inspeção inclui o autoajuste do motor e o teste de funcionamento em velocidade de inspeção.

**Figura (sem número no manual, pág. PDF 149): fluxograma do comissionamento em velocidade de inspeção.** Em dois ramos:

- Autoajuste do motor (Motor auto-tuning): autoajuste com carga de motor síncrono (Synchronous motor with-load auto-tuning); autoajuste estático de motor síncrono (Synchronous motor static auto-tuning); autoajuste sem carga de motor síncrono (Synchronous motor no-load auto-tuning); autoajuste semiautomático sem ângulo de motor síncrono (Semi-automatic angle-free auto-tuning of synchronous motor); autoajuste totalmente automático sem ângulo de motor síncrono (Full-automatic angle-free auto-tuning of synchronous motor); autoajuste sem carga de motor assíncrono (Asynchronous motor no-load auto-tuning); autoajuste com carga de motor assíncrono (Asynchronous motor with-load auto-tuning).
- Teste de funcionamento em velocidade de inspeção (Running test at inspection speed), com o autoajuste em velocidade de inspeção ("Auto-tuning at inspection speed") e as verificações: sentido de rotação do motor correto; corrente de funcionamento do motor adequada; inspeção no topo da cabine habilitada ("inspection on top of the car is enabled"); poço desobstruído; chaves de redução de velocidade e de fim de curso do pavimento extremo efetivas.

(Ambíguo: as setas que ligam cada modo de autoajuste ao ramo "Auto-tuning at inspection speed" não podem ser lidas no texto extraído; ver o original na pág. PDF 149.)

### 12.5.1 Autoajuste do motor (Motor Auto-tuning)

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
| F1-22 | Seleção da função de autoajuste (Auto-tuning function selection) | F1-22 = 2: autoajuste semiautomático sem ângulo; o autoajuste de ângulo é realizado na primeira inspeção ou no primeira operação elétrica de emergência (emergency electric RUN) após desligar e ligar a alimentação novamente. F1-22 = 6: autoajuste totalmente automático sem ângulo; o autoajuste de ângulo é realizado na primeira corrida após desligar e ligar a alimentação novamente (sem diferenciar estados do elevador). |

#### 2. Fluxogramas de autoajuste do motor

Em todos os fluxogramas, cada caixa de etapa tem ao lado uma observação do manual. A sequência de cada fluxograma está transcrita abaixo. Nos fluxogramas síncronos conferidos na imagem (Figuras 5-5 e 5-9), a observação da primeira caixa é: "O indicador X9 na MCB está OFF, indicando que o elevador entrou no estado de operação elétrica de emergência (emergency electric RUN)."

##### 1) Autoajuste de motor síncrono (Synchronous motor auto-tuning)

###### Autoajuste com carga de motor síncrono (motor ligado à cabine)

**Fluxograma do manual (figura 5-5): autoajuste com carga de motor síncrono.** Procedimento:

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN). Observação: indicador X9 OFF (ver acima).
2. Verificar F0-01 = 1. Observação: F0-01 deve ser ajustado em 1 durante o autoajuste com carga.
3. Ajustar o tipo de motor: F1-25 = 1. Observação: ajuste F1-25 em 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05. Observações: (1) obtenha a potência nominal, a tensão nominal, a corrente nominal, a frequência nominal e a rotação nominal do motor na placa de identificação do motor; (2) garanta que os parâmetros do motor estão ajustados corretamente; caso contrário, ocorrerão falhas.
5. Ajustar os parâmetros do encoder: F1-00 e F1-12. Observações: (1) ajuste F1-00 conforme o tipo real de encoder: 0: encoder SIN/COS; 1: encoder UVW; 2: encoder ABZ; 3: encoder Endat; (2) ajuste F1-12 (pulsos do encoder por rotação) conforme a placa de identificação do encoder.
6. F1-11 = 1. Observação: após ajustar F1-11 em 1, pressione ENTER. Se o painel de operação exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se o painel de operação exibir "F1-12", o sistema não conseguiu entrar no estado de autoajuste do motor; é preciso verificar: (1) se o elevador está em estado de inspeção; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 1.
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste. Observação: mantenha pressionado o botão de acionamento de emergência UP/DOWN durante o autoajuste. Depois que o motor emite um som por 5 s, o freio é aberto. A força de tração gira cerca de duas voltas ("The traction force rotates about two circles", ambíguo, ver o original na pág. PDF 151). O controlador interrompe a saída automaticamente. O autoajuste está concluído. Neste momento, solte o botão de acionamento de emergência UP/DOWN.
8. Autoajuste concluído. Observações: (1) se o autoajuste for bem-sucedido, a MCB exibe o ângulo do encoder aprendido por 3 s. Se o autoajuste falhar, a MCB exibe Err; (2) garanta que o desvio do valor de F1-06 fique dentro de ±5° ao longo de várias execuções de autoajuste; (3) F1-08 é ajustado, na maioria dos casos, em 0 ou 8. F1-08 permanece inalterado ao longo de várias execuções de autoajuste.

###### Autoajuste estático de motor síncrono (motor ligado à cabine, freio não liberado e motor não gira)

**Fluxograma do manual (figura 5-6): autoajuste estático de motor síncrono.** Procedimento:

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN).
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

**Fluxograma do manual (figura 5-7): autoajuste semiautomático sem ângulo de motor síncrono.** Procedimento:

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN). Observação: (1) o autoajuste sem ângulo é realizado automaticamente na operação elétrica de emergência; em seguida, o motor funciona na velocidade da operação elétrica de emergência; (2) depois que o autoajuste for bem-sucedido, nenhum autoajuste é realizado antes do próximo desligamento.
2. Verificar F0-01 = 1. Observação: "F0-01 must be set to 1 during with-load auto-tuning." (texto do original).
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12. Observações: F1-00 conforme o tipo real (0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat); F1-12 conforme a placa de identificação do encoder.
6. F1-22 = 2. Observação do original: "Set F1-12 to 2 to enable semi-automatic angle-free auto-tuning." (ambíguo, ver o original na pág. PDF 153: o texto cita F1-12, enquanto a caixa da etapa e a tabela da pág. PDF 150 indicam F1-22 = 2).
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste no estado de operação elétrica de emergência.
8. Autoajuste concluído. Observações: (1) se as falhas Err19 e Err20 forem reportadas durante o autoajuste, o autoajuste falhou; (2) se nenhuma falha for reportada e o elevador funcionar normalmente na velocidade de inspeção, o autoajuste foi bem-sucedido.

###### Autoajuste totalmente automático sem ângulo ("Automatic angle-free auto-tuning")

**Fluxograma do manual (figura 5-8): autoajuste totalmente automático sem ângulo de motor síncrono.** Procedimento:

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN). Observação: (1) o autoajuste totalmente automático sem ângulo é realizado na operação elétrica de emergência ou no estado de funcionamento automático; (2) depois que o autoajuste for bem-sucedido, nenhum autoajuste é realizado antes do próximo desligamento.
2. Verificar F0-01 = 1. Observação: "F0-01 must be set to 1 during with-load auto-tuning." (texto do original).
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-22 = 6. Observação do original: "Set F1-12 to 6 to enable full-automatic angle-free auto-tuning." (ambíguo, ver o original na pág. PDF 154: o texto cita F1-12, enquanto a caixa da etapa e a tabela indicam F1-22 = 6).
7. Manter pressionado o botão de acionamento de emergência UP/DOWN e realizar o autoajuste no estado de operação elétrica de emergência.
8. Autoajuste concluído. Observações: (1) se as falhas Err19 e Err20 forem reportadas durante o autoajuste, o autoajuste falhou; (2) se nenhuma falha for reportada e o elevador funcionar normalmente na velocidade de inspeção, o autoajuste foi bem-sucedido.

###### Autoajuste sem carga de motor síncrono (motor desligado da cabine)

**Fluxograma do manual (figura 5-9): autoajuste sem carga de motor síncrono.** Procedimento (conferido na imagem):

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN). Observação: indicador X9 OFF na MCB.
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste sem carga.
3. Ajustar o tipo de motor: F1-25 = 1.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 2. Observação: após ajustar F1-11 em 2, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de operação elétrica de emergência; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
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

**Fluxograma do manual (figura 5-10): autoajuste com carga de motor assíncrono.** Procedimento (a ordem das caixas segue o padrão das figuras 5-5 e 5-9 e não foi conferida na imagem do manual; confira no original antes de usar):

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN).
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste com carga.
3. Ajustar o tipo de motor: F1-25 = 0.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 1. Observação: após ajustar F1-11 em 1, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de operação elétrica de emergência; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
7. Pressionar a tecla RUN no painel de operação para iniciar o autoajuste.
8. Autoajuste concluído. Observações: (1) durante o autoajuste com carga, o motor não gira, mas há ruído de corrente. O processo de autoajuste dura cerca de várias dezenas de segundos; (2) após a conclusão, o controlador interrompe a saída automaticamente; (3) são obtidos os cinco parâmetros F1-14 a F1-18.
9. Restaurar F0-01 para 1. Observação: após a conclusão do autoajuste, F0-01 deve ser restaurado para 1. Caso contrário, o elevador não pode funcionar em velocidade de inspeção.

###### b) Autoajuste sem carga de motor assíncrono

**Fluxograma do manual (figura 5-11): autoajuste sem carga de motor assíncrono.** Procedimento (a mesma ressalva: ordem das caixas não conferida na imagem do manual):

1. Entrar no estado de operação elétrica de emergência (emergency electric RUN).
2. Verificar F0-01 = 0. Observação: F0-01 deve ser ajustado em 0 durante o autoajuste sem carga.
3. Ajustar o tipo de motor: F1-25 = 0.
4. Ajustar os parâmetros do motor: F1-01 a F1-05 (dados da placa de identificação; parâmetros corretos, senão ocorrerão falhas).
5. Ajustar os parâmetros do encoder: F1-00 e F1-12 (F1-00: 0: SIN/COS; 1: UVW; 2: ABZ; 3: Endat; F1-12 conforme a placa de identificação do encoder).
6. F1-11 = 2. Observação: após ajustar F1-11 em 2, pressione ENTER. Se o painel exibir "TUNE", o sistema entrou no estado de autoajuste do motor. Se exibir "F1-12", o sistema não conseguiu entrar; é preciso verificar: (1) se o elevador está em estado de operação elétrica de emergência; (2) se a MCB exibe falhas a serem corrigidas; (3) se F0-01 está ajustado em 0.
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

### 12.5.2 Teste de funcionamento em velocidade de inspeção (Running Test at Inspection Speed)

(tabela conferida na imagem)

| Parâmetro | Descrição do parâmetro | Descrição | Padrão |
|---|---|---|---|
| F2-10 | Sentido de marcha do elevador (Elevator running direction) | 0: sentido inalterado. 1: sentido invertido. | 0 |
| F3-25 | Velocidade da operação elétrica de emergência (Emergency electric RUN speed) | 0,100 a 0,600 m/s | 0,250 m/s |

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

## 12.6 Comissionamento em velocidade normal (Commissioning at Normal Speed)

Figura (sem número): árvore da seção. "Commissioning at normal speed" se divide em três ramos:

- Shaft auto-tuning (autoajuste do poço): Make preparations; Check that shaft auto-tuning conditions are met; Perform shaft auto-tuning; Perform running test at normal speed.
- Car top commissioning (comissionamento da caixa de teto): Light curtain commissioning; Door machine controller commissioning.
- HCB commissioning (comissionamento da placa de chamada dos pavimentos (HCB)): HCB installation; HCB address setting.

### 12.6.1 Autoajuste do poço (Shaft Auto-tuning)

#### 1 Fazer os preparativos para o autoajuste do poço

Figura (sem número): três quadros de verificação, transcritos abaixo.

1. Verificar se as chaves do poço (shaft switches) atuam corretamente. Inclui chaves de fim de curso final (final limit switches), chaves de limite (limit switches), chaves de desaceleração (slowdown switches) e chaves de nivelamento (leveling switches).
2. Verificar se a sequência de atuação das chaves de nivelamento está correta.
   - Em geral, uma chave de nivelamento é instalada. Se várias chaves de nivelamento forem instaladas, verifique se a sequência de atuação está correta. Tome como exemplo a situação com três sensores: (o texto traz a palavra solta "switch", ambíguo, ver o original na pág. PDF 160)
   - (1) Sequência de atuação dos sensores na inspeção em subida (inspection up): chave de nivelamento de subida (up leveling switch) → chave de zona de porta (door zone switch) → chave de nivelamento de descida (down leveling switch).
   - (2) Sequência de atuação dos sensores na inspeção em descida (inspection down): chave de nivelamento de descida → chave de zona de porta → chave de nivelamento de subida.
3. Verificar o estado da comunicação CANbus.
   - Verifique o estado da comunicação CANbus. Se a falha E51 não for reportada e o indicador CAN1 na MCB estiver aceso fixo (steady ON), a comunicação CANbus entre a MCB e a CTB está normal. Se a comunicação CANbus estiver anormal, corrija a falha E51 conforme a solução descrita na capítulo 13.

Parâmetros (Parameters)

| Parâmetro | Descrição do parâmetro | Faixa (Description) | Padrão (Default) | Observações (Remarks) |
|---|---|---|---|---|
| F0-04 | Velocidade nominal do elevador (Rated elevator speed) | 0.250–8.000 m/s | 1.600 m/s | - |
| F6-00 | Pavimento mais alto do elevador (Top floor of the elevator) | F6-01 to F6-56 | 9 | "Actual number of floors + 1 - Bottom floor" (ambíguo, ver o original na pág. PDF 160) |
| F6-01 | Pavimento mais baixo do elevador (Bottom floor of the elevator) | 1 to F6-00 | 1 | - |
| F3-26 | Velocidade de autoajuste do poço (Shaft auto-tuning speed) | 0.250 to 0.630 | 0.250 | - |

NOTA (Note): Depois que F0-04 for alterado, o autoajuste do poço deve ser executado novamente. Caso contrário, ocorrerá uma anormalidade durante o funcionamento do elevador.

#### 2 Verificar se as condições para o autoajuste do poço foram atendidas

- O elevador está no estado de acionamento de emergência (emergency drive state).
- O elevador precisa ir até abaixo da posição de nivelamento mais baixa, isto é, pelo menos uma chave de nivelamento fica abaixo da placa de nivelamento (leveling plate). O sinal da chave de desaceleração de descida 1 (down slow-down switch 1) que entra na MCB está ativo. (Esta condição vale apenas para o caso de dois pavimentos.)
- O NICE3000new não está em estado de falha. Se houver falha, pressione STOP/RES para resetá-la.

#### 3 Executar o autoajuste do poço

Atendidas as condições anteriores, inicie o autoajuste do poço por um dos métodos a seguir:

- Ajuste F1-11 em 3 no painel de operação. Passe o acionamento de emergência para normal (Switch emergency drive to normal).
- Ajuste F7 em 1 no keypad da MCB. Passe o acionamento de emergência para normal. ("Set F7 to 1" é o texto do manual, ambíguo quanto ao código completo, ver o original na pág. PDF 161.)

Depois que o autoajuste do poço começa, o elevador corre na velocidade ajustada em F3-26. O elevador vai automaticamente até a placa de nivelamento do pavimento mais baixo, depois sobe até a placa de nivelamento do pavimento mais alto e para ao chegar a ela. Em seguida, o keypad da MCB exibe o número do pavimento atual (pavimento mais alto), indicando que o autoajuste do poço foi bem-sucedido.

Se a falha Err35 for reportada durante o processo, o autoajuste do poço falhou. É preciso corrigir a falha conforme a solução descrita no Capítulo 7 e executar o autoajuste do poço novamente.

#### 4 Executar o teste de funcionamento em velocidade normal

Depois que o autoajuste do poço é concluído com sucesso, o funcionamento em velocidade normal pode não ser bem-sucedido porque o controlador de porta e a função de plena carga/sobrecarga (full-load/overload) não foram comissionados. É possível ajustar parâmetros para que o sistema proíba a abertura de porta e permita sobrecarga, e então executar o teste de funcionamento em velocidade normal.

Figura (sem número): fluxograma, transcrito como procedimento.

1. Ajustar F7-05 em 1. (A abertura da porta do elevador fica desabilitada.)
2. Ajustar F7-06 em 1. (O funcionamento do elevador com sobrecarga na inspeção normal é permitido.)
3. Passar a chave de inspeção para o estado "Normal".
4. Ajustar F7-00 para registrar uma chamada de pavimento e testar o funcionamento em velocidade normal.
   - (1) A chamada ajustada em F7-00 é igual à chamada de cabine dentro do elevador (car call). Ajuste F7-00 em qualquer número de pavimento e faça o elevador funcionar em velocidade normal; verifique se o motor, o elevador e o controlador apresentam anormalidade durante o funcionamento.
   - (2) Recomenda-se ajustar F0-03 (Maximum running speed, velocidade máxima de funcionamento) em um valor pequeno para os testes iniciais; depois de vários testes bem-sucedidos, ajuste F0-03 no valor necessário.
5. Teste concluído (Testing completed).
6. Restaurar F7-00 a F7-07 em 0. (Depois de concluído o teste, restaure F7-00 a F7-07 em 0.)

NOTA (Note): O controlador restaura F7-00 a F7-02 e F7-05 a F7-07 em 0 após nova energização (power-on again). Se for preciso continuar o teste, ajuste esses parâmetros novamente.

Fonte: manual NICE3000new, págs. PDF 160 a 161 (impressas 159 a 160)

### 12.6.2 Comissionamento da caixa de teto (Car Top Commissioning)

#### Informações de segurança (Safety Information)

CUIDADO (Caution):

- Durante o comissionamento da caixa de teto (car top commissioning), o operador fica em cima da cabine; para garantir a segurança pessoal, certifique-se de que a inspeção no teto da cabine (car top inspection) esteja habilitada (a inspeção no teto da cabine tem precedência sobre a inspeção na sala de equipamentos, "equipment room").
- A MCTC-CTB é ativa em nível alto (high level active) por padrão.

Esta seção toma como exemplo o sistema de elevador de porta única (porta 1) para descrever o comissionamento. Os sinais relacionados incluem a cortina de luz 1 (light curtain 1), o sinal de limite de abertura/fechamento da porta 1 e o sinal de saída de abertura/fechamento da porta 1, descritos na tabela a seguir.

Tabela 5-3: Sinais relacionados ao comissionamento da caixa de teto

| Terminal da CTB | Definição do terminal |
|---|---|
| P24 | Comum das entradas X1 a X8 |
| X1 | Entrada da cortina de luz 1 |
| X3 | Entrada do limite de abertura da porta 1 |
| X5 | Entrada do limite de fechamento da porta 1 |
| BM | Comum das saídas da porta 1 |
| B1 | Saída de abertura da porta 1 |
| B2 | Saída de fechamento da porta 1 |

Para o sistema de elevador de porta dupla, os terminais que controlam os sinais da porta 2, como os sinais da cortina de luz 2 e os sinais de limite de abertura/fechamento da porta 2, têm o mesmo princípio e o mesmo modo de monitoramento que os da porta 1. Os detalhes não são descritos aqui.

O sistema pode monitorar o estado de entrada e saída dos sinais da cortina de luz e do controlador da máquina de porta (door machine) e se esses sinais estão ativos.

- É possível ver os indicadores de sinal na CTB para conhecer o estado de entrada/saída.

Figura 5-12: Estado de entrada/saída indicado pelos indicadores de sinal da CTB. Mostra a placa MCTC-CTB-A(B) com os bornes (MOD+, MOD-, 24V, COM, X1 a X8, 24V, A, B, AM, CAN+, CAN-, 24V, AI, M, D2, D1, DM, C3, C3M, C2, C1, CM, B3, B2, B1, BM, E, E1), conectores CN1 a CN10, chaves J1, J2, J9, RESET e LEDs X1 a X8 e D2 a B1.

Tabela 5-4: Estado dos indicadores de sinal

| Indicador | Descrição do estado |
|---|---|
| Indicador de sinal de entrada X1 a X8 aceso (ON) | Há entrada em nível alto nos terminais de entrada correspondentes. |
| Indicador de sinal de saída B1 a B3 aceso (ON) | O terminal de saída correspondente tem saída. |

- É possível ver F5-35 na MCB para saber se os sinais da cortina de luz e da máquina de porta estão ativos.

Figura 5-13: Método de monitoramento de F5-35. Mostra o display de cinco dígitos do keypad da MCB, numerados de 1 a 5 da direita para a esquerda, com os LEDs 1 e 3 circulados, e um dígito de 7 segmentos com os segmentos A a G.

Tabela 5-5: Descrição do monitoramento de F5-35 (no manual o cabeçalho traz "F-35 LEDs")

| LED nº | Segmento | Sinal indicado (segmento aceso indica que o E/S correspondente é válido) |
|---|---|---|
| LED 1 | A | Sinal da cortina de luz da porta 1 |
| LED 1 | C | Sinal de limite de abertura da porta 1 |
| LED 1 | E | Sinal de limite de fechamento da porta 1 |
| LED 3 | A | Saída de abertura da porta 1 |
| LED 3 | B | Saída de fechamento da porta 1 |

É preciso ajustar em F5-25 as características NO/NC dos sinais de entrada da CTB e garantir que o ajuste seja coerente com a característica NO/NC das chaves elétricas reais (cortina de luz e chaves de limite de abertura/fechamento de porta). O controle pela CTB só pode ser realizado depois que o ajuste for feito corretamente. Se o ajuste NO/NC for incoerente com as condições reais, a porta não consegue abrir ou fechar corretamente ou a falha E53 é reportada.

| Bit de F5-25 | Sinal de entrada da CTB |
|---|---|
| Bit0 | Usado para ajustar a característica NO/NC do sinal da cortina de luz da porta 1 |
| Bit2 | Usado para ajustar a característica NO/NC do sinal de limite de abertura da porta 1 |
| Bit4 | Usado para ajustar a característica NO/NC do sinal de limite de fechamento da porta 1 |

#### 1 Comissionamento da cortina de luz (Light Curtain Commissioning)

- Verifique se a fiação da cortina de luz está correta e firme e se a tensão de alimentação é adequada.
- Observe o estado ON/OFF do indicador de sinal correspondente na CTB para verificar se a cortina de luz funciona em estado normal. Se o estado do indicador do sinal X1 permanecer inalterado ou mudar de forma anormal, isso indica que a cortina de luz está anormal.

Tabela 5-6: Verificação do estado da cortina de luz pelo indicador do sinal X1

| Ajuste do sinal da cortina de luz | Estado de bloqueio da cortina de luz | Estado do indicador do sinal X1 |
|---|---|---|
| NO | Desbloqueada (Unblocked) | OFF |
| NO | Bloqueada (Blocked) | ON |
| NC | Desbloqueada | ON |
| NC | Bloqueada | OFF |

- Depois de concluído o comissionamento da cortina de luz, verifique se o ajuste de F5-25 Bit0 é coerente com a característica NO/NC real da cortina de luz.

Tabela 5-7: Verificação da coerência entre F5-25 e a cortina de luz real (segmentos lidos da renderização da página)

| Sinal monitorado | Segmento A do LED 1 em F5-35 com cortina desbloqueada | Segmento A do LED 1 em F5-35 com cortina bloqueada | Julgamento do estado do sinal | Reajuste de F5-25 Bit0 |
|---|---|---|---|---|
| Sinal da cortina de luz (segmento A do LED 1 em F5-35) | Apagado | Aceso | Normal | Não necessário (Not required) |
| Sinal da cortina de luz (segmento A do LED 1 em F5-35) | Aceso | Apagado | Anormal | Ajustar F5-25 Bit0 para o estado oposto: se o valor original for 0, mudar para 1; se o valor original for 1, mudar para 0. |

#### 2 Comissionamento do controlador da máquina de porta (Door Machine Controller Commissioning)

O contato entre o controlador da máquina de porta e o sistema do elevador inclui os comandos de abrir e fechar porta emitidos pela saída da CTB, bem como os sinais de limite de abertura e fechamento de porta realimentados pelo controlador da máquina de porta.

Depois de concluídos o comissionamento e a instalação da máquina de porta, é necessário verificar se a fiação está correta e se os sinais de limite são coerentes com os padrões do sistema. O procedimento de comissionamento do controlador da máquina de porta é o seguinte:

1. Verificar que F7-05 (Door open forbidden, abertura de porta proibida) é 0 (No).
2. Verificar se a fiação do controlador da máquina de porta está correta e firme e se a tensão de alimentação é adequada.
3. Comissionar o controlador da máquina de porta e verificar que a entrada e a saída do controlador da máquina de porta estão normais no modo de controle por terminais (terminal control mode).
4. Verificar se a saída de abrir/fechar porta está normal: curto-circuitar BM/B1 na CTB, e a porta 1 abre; curto-circuitar BM/B2, e a porta 1 fecha. Se a porta atuar de forma anormal após curto-circuitar BM/B1 ou BM/B2 na CTB, verificar:
   - se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta;
   - se o ajuste de função dos terminais de entrada de abrir/fechar porta está correto;
   - se o comissionamento do controlador da máquina de porta falhou. Em caso afirmativo, comissionar novamente.
5. Verificar se a realimentação do sinal de limite de abrir/fechar porta vinda do controlador da máquina de porta está normal: observe os indicadores de sinal dos terminais X na CTB e julgue se a realimentação dos limites de abertura e fechamento vinda do controlador está normal conforme a tabela a seguir.

Tabela 5-8: Julgamento do limite de abertura/fechamento de porta

| Ajuste do sinal de limite de abertura/fechamento | Estado da porta | Indicador do sinal X3 | Indicador do sinal X5 |
|---|---|---|---|
| NO | No limite de abertura (At Door Open Limit) | Aceso fixo (Steady ON) | Apagado fixo (Steady OFF) |
| NO | Durante abertura/fechamento (During door open/close) | Apagado fixo | Apagado fixo |
| NO | No limite de fechamento (At Door Close Limit) | Apagado fixo | Aceso fixo |
| NC | No limite de abertura | Apagado fixo | Aceso fixo |
| NC | Durante abertura/fechamento | Aceso fixo | Aceso fixo |
| NC | No limite de fechamento | Aceso fixo | Apagado fixo |

Se os estados dos indicadores dos sinais X3 e X5 forem incoerentes com o estado real da porta ou permanecerem inalterados, verificar:

- se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta;
- se o ajuste de função dos terminais de saída de abrir/fechar porta está correto;
- se o comissionamento do controlador da máquina de porta falhou. Em caso afirmativo, comissionar novamente.

6. Depois de concluído o comissionamento do controlador da máquina de porta, verificar se o ajuste de F5-25 Bit2/Bit4 é coerente com a característica NO/NC real dos sinais de limite de abertura/fechamento de porta.

Tabela 5-9: Verificação da coerência entre F5-25 e os sinais reais de limite de abertura/fechamento (segmentos lidos da renderização da página)

| Sinal | Monitoramento: no limite de abertura | Monitoramento: no limite de fechamento | Julgamento | Reajuste de F5-25 Bit2/Bit4 |
|---|---|---|---|---|
| Sinal de limite de abertura (segmento C do LED 1 em F5-35) | Segmento C aceso | Segmento C apagado | Normal | Não necessário |
| Sinal de limite de abertura (segmento C do LED 1 em F5-35) | Segmento C apagado | Segmento C aceso | Anormal | Ajustar F5-25 Bit2 para o estado oposto: se o valor original for 0, mudar para 1; se for 1, mudar para 0. |
| Sinal de limite de fechamento (segmento E do LED 1 em F5-35) | Segmento E apagado | Segmento E aceso | Normal | Não necessário |
| Sinal de limite de fechamento (segmento E do LED 1 em F5-35) | Segmento E aceso | Segmento E apagado | Anormal | Ajustar F5-25 Bit4 para o estado oposto: se o valor original for 0, mudar para 1; se for 1, mudar para 0. |

##### Tratamento de problemas comuns de controle de porta (Handling of Common Door Control Problems)

- No estado de porta fechada, o sistema envia um comando de abrir porta, mas a porta não abre.
  - Verificar se o sinal de limite de abertura está sempre ativo.
  - Verificar se há saída de abertura de porta vendo o segmento 1 do LED 1 em FA-34. Se há saída (segmento 1 aceso), verificar: se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta e se o controlador da máquina de porta funciona corretamente.
- No estado de limite de abertura, o sistema envia um comando de fechar porta, mas a porta não fecha.
  - Verificar se o sinal da cortina de luz está sempre ativo.
  - Verificar se há saída de fechamento de porta vendo o segmento 2 do LED 1 em FA-34. Se há saída (segmento 2 aceso), verificar: se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta e se o controlador da máquina de porta funciona corretamente.
- O elevador não abre a porta na área da zona de porta e a falha Err53 é reportada. Corrigir a falha conforme a solução descrita no Capítulo 7.

Fonte: manual NICE3000new, págs. PDF 162 a 166 (impressas 161 a 165)

### 12.6.3 Instalação e ajuste da HCB (HCB Installation and Setting)

Esta seção descreve a instalação e o ajuste da HCB (placa de chamada dos pavimentos) do sistema de elevador independente de porta única. Para detalhes sobre a instalação e o ajuste da HCB do sistema de elevadores em paralelo (parallel) e do sistema de elevador de portas opostas (opposite door), o manual remete às seções correspondentes.

#### 1 Instalação da HCB

Instalar uma HCB para cada pavimento de serviço (pavimentos sem serviço não exigem HCB), como mostra a Figura 5-14.

A HCB comunica com a MCB por Modbus. Todas as HCBs são ligadas em paralelo e depois conectadas à MCB.

#### 2 Ajuste do endereço da HCB

Ajuste um endereço para cada HCB. Caso contrário, a HCB não pode ser usada.

O endereço de cada HCB deve ser único. HCBs com o mesmo endereço não podem ser usadas. Para detalhes de como ajustar o endereço, veja a descrição da HCB correspondente.

Ajuste o endereço com base no número da placa de nivelamento do pavimento. A partir do pavimento mais baixo, ajuste o endereço da HCB do pavimento onde está a N-ésima placa de nivelamento em N, como mostra a figura a seguir (Figura 5-14).

Figura 5-14: Instalação da HCB e ajuste de endereço. Mostra os pavimentos 1 a 4 com as placas de nivelamento 1 a 4; as HCBs dos pavimentos com placas 1, 2 e 4 têm os endereços 1, 2 e 4; o pavimento 3 está rotulado "Non-service floor, HCB not installed".

Depois de concluídas a instalação e o ajuste de endereço das HCBs, é possível chamar o elevador pela HCB para iniciar o funcionamento em velocidade normal.

NOTA (Note): Quando a placa de exibição (display board) é usada dentro da cabine, o endereço deve ser ajustado em 0.

Fonte: manual NICE3000new, pág. PDF 167 (impressa 166)

---

## 12.7 Ajuste do conforto de viagem (Riding Comfort Adjustment)

Figura (sem número): árvore da seção. "Riding comfort adjustment" se divide em "Riding comfort adjustment during running" (com "Riding comfort adjustment at elevator startup and stop" e "Riding comfort adjustment to the running curve") e "Leveling accuracy adjustment" (com "Description of leveling components", "All-floor leveling accuracy adjustment" e "Single-floor leveling accuracy adjustment").

### 12.7.1 Ajuste do conforto de viagem (Riding Comfort Adjustment)

O conforto de viagem é um fator importante do desempenho global do elevador. A instalação inadequada de peças mecânicas e ajustes de parâmetros inadequados causam desconforto. Melhorar o conforto de viagem envolve principalmente o ajuste da saída do controlador e da construção mecânica do elevador.

#### 1 Ajuste de desempenho do controle do sistema (Performance adjustment of system control)

Figura 5-15: Sequência temporal de funcionamento (Running time sequence). Gráfico de V (velocidade) contra t (tempo), com as linhas: RUN contactor; Brake contactor; Shorting door lock circuit contactor; Shorting PMSM stator contactor; Internal running status; Leveling signal; RUN contactor feedback; Brake contactor feedback; Shorting door lock circuit contactor feedback; Shorting PMSM stator contactor feedback. Os parâmetros F2-16, F3-18, F3-19, F3-20, F8-11 e F2-17 aparecem marcados nos intervalos do gráfico.

##### 1) Ajuste do conforto na partida e na parada do elevador (Riding comfort adjustment at elevator startup and stop)

Parâmetros relacionados:

| Código | Nome do parâmetro | Faixa | Padrão |
|---|---|---|---|
| F2-00 | Speed loop proportional gain 1 (ganho proporcional 1 do laço de velocidade) | 0 to 100 | 40 |
| F2-01 | Speed loop integral time 1 (tempo integral 1 do laço de velocidade) | 0.01 to 10.00s | 0.60s |
| F2-03 | Speed loop proportional gain 2 | 0 to 100 | 35 |
| F2-04 | Speed loop integral time 2 | 0.01 to 10.00s | 0.80s |

**a) Ajuste de partida anormal do motor (Adjustment to abnormal motor startup)**

F2-00, F2-01, F2-03 e F2-04 são usados para ajustar as características de resposta dinâmica de velocidade do motor.

Para obter uma resposta mais rápida do sistema, aumente o ganho proporcional e reduza o tempo integral. Porém, ganho proporcional grande demais ou tempo integral pequeno demais pode levar o sistema a oscilar.

Diminuir o ganho proporcional e aumentar o tempo integral torna mais lenta a resposta dinâmica do motor. Porém, ganho proporcional pequeno demais ou tempo integral grande demais pode causar anormalidade no rastreamento de velocidade do motor, resultando na falha E33 ou em nivelamento instável na parada.

O ajuste padrão é adequado para a maioria dos motores de grande potência, e não é necessário modificar esses parâmetros. Esses parâmetros precisam ser ajustados apenas para motores de pequena potência (P ≤ 5.5 kW), porque eles podem oscilar. Para eliminar a oscilação, proceda assim:

1. Diminua primeiro o ganho proporcional (entre 10 e 40) para garantir que o sistema não oscile.
2. Depois reduza o tempo integral (entre 0.1 e 0.8) para garantir que o sistema tenha resposta rápida, mas pequeno sobressinal (overshoot).

**b) Ajuste da partida do elevador (Adjustment to elevator startup)**

*Ajuste para partida sem célula de carga (Adjustment for no-load-cell startup)*

O ajuste de parâmetros relacionado ao retrocesso (rollback) na partida e na parada do elevador é descrito na tabela a seguir.

| Código | Nome | Faixa | Padrão | Descrição |
|---|---|---|---|---|
| F8-01 | Pre-torque selection (seleção de pré-torque) | 0: Pre-torque invalid; 1: Load cell pre-torque compensation; 2: Automatic pre-torque compensation; 3: Load cell pre-torque and automatic compensation both in effect | 2 | A função de partida sem célula de carga é habilitada quando F8-01 é ajustado em 2. (2: Pre-torque automatic compensation) |
| F2-11 | Zero servo current coefficient (coeficiente de corrente do servo zero) | 2.0% to 50.0% | 15.0% | Parâmetros de ajuste do servo zero; válidos apenas quando F8-01 é ajustado em 2 ou 3. |
| F2-12 | Zero servo speed loop Kp | 0.00 to 2.00 | 0.50 | (idem) |
| F2-13 | Zero servo speed loop Ti | 0.00 to 2.00 | 0.60 | (idem) |

Notas (Notes, texto do manual, sem rótulo de aviso):

- Quando a compensação de pré-torque sem célula de carga é usada (F8-01 = 2), nenhuma célula de carga analógica é necessária, e o controlador compensa rapidamente o torque com base na leve variação de rotação do encoder na partida.
- O ajuste padrão de F2-11 a F2-13 é adequado para a maioria dos motores de grande potência, e não é necessário modificar esses parâmetros. Para o motor de pequena potência (P ≤ 5.5 kW), o motor pode ter oscilação ou ruído na partida com carga, e os passageiros na cabine podem sentir forte solavanco da cabine (car lurch). Para eliminar a oscilação, proceda assim:
  1. Diminua o valor de F2-11 (entre 5 e 15) para eliminar a oscilação do motor.
  2. Diminua os valores de F2-12 e F2-13 (entre 0.1 e 0.8) para reduzir o ruído do motor e melhorar o conforto na partida.

*Ajuste para partida com célula de carga (Adjustment for load cell startup)*

O ajuste de parâmetros relacionado ao retrocesso na partida e na parada do elevador é descrito na tabela a seguir.

| Código | Nome | Faixa | Padrão | Descrição |
|---|---|---|---|---|
| F8-01 | Pre-torque selection | 0: Pre-torque invalid; 1: Weighing pre-torque compensation; 2: Pre-torque automatic compensation; 3: Weighing pre-torque and automatic compensation both in effect | 2 | Quando uma célula de carga é usada, ajuste F8-01 em 1. (1: Weighing pre-torque compensation) |
| F8-02 | Pre-torque offset (deslocamento do pré-torque) | 0.0% to 100.0% | 50.0% | Parâmetros de regulagem do pré-torque. |
| F8-03 | Drive gain (ganho de acionamento) | 0.00 to 2.00 | 0.60 | (idem) |
| F8-04 | Brake gain (ganho de frenagem) | 0.00 to 2.00 | 0.60 | (idem) |

Notas do manual:

- Quando uma célula de carga analógica é usada (F8-01 = 1 neste caso), o controlador identifica o estado de frenagem ou de acionamento conforme o sinal da célula de carga e calcula automaticamente o valor de compensação de torque necessário. F8-03 e F8-04 são usados para ajustar a partida do elevador quando a célula de carga analógica é usada. O método de ajuste dos dois parâmetros é o seguinte:
  - No estado de acionamento (driving state), aumente F8-03 adequadamente se houver retrocesso na partida do elevador, e diminua F8-03 se houver solavanco da cabine na partida.
  - No estado de frenagem (braking state), aumente F8-04 adequadamente se houver arranque (jerk) no sentido do comando na partida do elevador, e diminua F8-04 se houver solavanco da cabine na partida.
- Mais detalhes sobre esses parâmetros: F8-02 (Pre-torque offset) é, na prática, o coeficiente de balanceamento do elevador, isto é, a porcentagem da carga da cabine em relação à carga nominal quando a cabine e o contrapeso estão equilibrados. Este parâmetro deve ser ajustado corretamente. F8-03 (Drive gain) ou F8-04 (Brake gain) multiplica o coeficiente de pré-torque atual do elevador quando o motor funciona no lado de acionamento ou de frenagem. Se o ganho ajustado for maior, o valor calculado da compensação de pré-torque de partida é maior ("startup pro-torque compensation", como está no manual).
- Os estados do motor são definidos assim: estado de acionamento do motor (driving state): subida com carga plena, descida sem carga. Estado de frenagem do motor (braking state): descida com carga plena, subida sem carga.

*Ajuste de conforto habilitado quando a compensação por pesagem e a compensação automática estão ambas em vigor (Comfort adjustment is enabled when the weighing compensation and automatic compensation are both in effect)*

| Código | Nome | Faixa | Padrão | Descrição |
|---|---|---|---|---|
| F8-01 | Pre-torque selection | 0: Pre-torque invalid; 1: Weighing pre-torque compensation; 2: Pre-torque automatic compensation; 3: Weighing pre-torque and automatic compensation both in effect | 2 | Quando uma célula de carga é usada e a inconsistência dos efeitos de partida em cargas diferentes é causada por linearidade inadequada da célula de carga, ajuste F8-01 em 3. (3: Weighing pre-torque and automatic compensation both in effect) |
| F8-02 | Pre-torque offset | 0.0% to 100.0% | 50.0% | Parâmetros de regulagem do pré-torque. |
| F8-03 | Drive gain | 0.00 to 2.00 | 0.60 | (idem) |
| F8-04 | Brake gain | 0.00 to 2.00 | 0.60 | (idem) |
| F2-11 | Zero servo current coefficient | 2.0% to 50.0% | 15.0% | Parâmetros de ajuste da compensação automática de pré-torque. |
| F2-12 | Zero servo speed loop Kp | 0.00 to 2.00 | 0.50 | (idem) |
| F2-13 | Zero servo speed loop Ti | 0.00 to 2.00 | 0.60 | (idem) |

Notas do manual:

- Quando F8-01 é ajustado em 3, o controlador identifica o estado de frenagem ou de acionamento conforme o sinal da célula de carga, calcula automaticamente o valor de compensação de torque necessário e corrige rapidamente esse valor conforme a leve variação de rotação do encoder no instante da partida.
- O ajuste se baseia na combinação do "ajuste de conforto de partida sem célula de carga" com o "ajuste de conforto de partida com célula de carga".

**c) Tratamento do retrocesso na partida e na parada do elevador (Handling of rollback at elevator startup and stop)**

O ajuste de parâmetros relacionado ao retrocesso na partida e na parada do elevador é descrito na tabela a seguir.

| Código | Nome | Faixa | Padrão |
|---|---|---|---|
| F3-19 | Brake release delay | 0.000 to 2.000s | 0.600s |
| F8-11 | Brake release delay | 0.200 to 1.500s | 0.600s |

- F3-19 (Brake release delay) especifica o tempo desde o instante em que o sistema envia o comando de liberar o freio até o instante em que o freio está completamente liberado, período durante o qual o sistema mantém a saída da corrente de torque de velocidade zero. Se houver retrocesso evidente na partida do elevador, aumente F3-19 adequadamente.
- O sistema mantém a saída da corrente de torque de velocidade zero durante o tempo ajustado em F8-11, a partir do instante em que o sistema envia o comando de aplicar o freio (brake apply); isto serve para evitar retrocesso. Se houver retrocesso evidente na partida do elevador, aumente F8-11 adequadamente.

**d) Tratamento do ruído de corrente na partida e na parada do motor (Handling of current noise at motor startup and stop)**

Durante a partida ou a parada do elevador, certos motores podem gerar ruído quando a corrente é aplicada antes da liberação do freio ou quando a corrente é removida depois da aplicação do freio. Para reduzir o ruído do motor, aumente F2-16 ou F2-17 adequadamente.

| Código | Nome | Faixa | Padrão |
|---|---|---|---|
| F2-16 | Torque acceleration time | 1 to 500 | 1 |
| F2-17 | Torque deceleration time | 1 to 3000 | 350 |

**e) Ajuste com grande atrito estático mecânico (Adjustment at large mechanical static friction)**

| Código | Nome | Faixa | Padrão |
|---|---|---|---|
| F3-00 | Startup speed | 0.000–0.050 m/s | 0.000m/s |
| F3-01 | Startup holding time | 0.000 to 5.000s | 0.000s |

Figura 5-16: Sequência temporal de partida para eliminar o atrito estático. Dois gráficos de V (velocidade) contra t (tempo), com os valores F3-00 (velocidade de partida) e F3-01 (tempo de manutenção da partida) marcados.

Em elevadores de moradias (villa elevators), é comum haver mau conforto de viagem causado por atrito estático. Quando há grande atrito entre as sapatas de guia e os trilhos-guia, grande atrito estático é gerado no instante da partida, levando a mau conforto de viagem. Faça o sistema partir na velocidade especificada ajustando esses parâmetros, para eliminar o atrito e melhorar o conforto de viagem.

##### 2) Ajuste do conforto de viagem à curva de funcionamento (Riding comfort adjustment to the running curve)

| Código | Nome | Faixa | Padrão |
|---|---|---|---|
| F3-02 | Acceleration rate | 0.200 to 1.500 | 0.700 |
| F3-03 | Acceleration start jerk time | 0.300 to 4.000 | 1.500 |
| F3-04 | Acceleration end jerk time | 0.300 to 4.000 | 1.500 |
| F3-05 | Deceleration rate | 0.200 to 1.500 | 0.700 |
| F3-06 | Deceleration end jerk time | 0.300 to 4.000 | 1.500 |
| F3-07 | Deceleration start jerk time | 0.300 to 4.000 | 1.500 |

Figura 5-17: Curva de funcionamento. Gráfico de V (velocidade) contra t (tempo) com os trechos de aceleração (F3-02 com F3-03 no início e F3-04 no fim) e de desaceleração (F3-05 com F3-06 e F3-07).

F3-02, F3-03 e F3-04 são usados para ajustar a curva de funcionamento durante a qual o elevador acelera da partida até a velocidade máxima. Se o processo de aceleração for curto demais, causando mau conforto de viagem, diminua F3-02 e aumente F3-03 e F3-04 para tornar a curva de aceleração mais suave. Se o processo de aceleração for longo demais, aumente o valor de F3-02 e diminua os valores de F3-03 e F3-04.

Ajuste F3-05, F3-06 e F3-07 de modo semelhante para tornar o processo de desaceleração apropriado.

#### 2 Ajuste da construção mecânica (Adjustment of mechanical construction)

A construção mecânica que afeta o conforto de viagem envolve a instalação do trilho-guia, da sapata de guia, do cabo de aço e do freio, o balanceamento da cabine, e a ressonância causada pela cabine, pelo trilho-guia e pelo motor. Para motor assíncrono, o desgaste ou a instalação inadequada da caixa de engrenagens (gearbox) pode causar mau conforto de viagem.

| Nº | Fator mecânico | Descrição |
|---|---|---|
| 1 | Trilho-guia (Guide rail) | A instalação do trilho-guia envolve principalmente a verticalidade e a planeza de superfície do trilho-guia, a suavidade da junção dos trilhos-guia e o paralelismo entre dois trilhos-guia (incluindo os trilhos-guia do lado do contrapeso). |
| 2 | Sapata de guia (Guide shoe) | O aperto das sapatas de guia (incluindo a do lado do contrapeso) também influencia o conforto de viagem. As sapatas de guia não devem ficar nem soltas nem apertadas demais. |
| 3 | Cabo de aço (Steel rope) | A transmissão do motor até a cabine depende totalmente do cabo de aço. Grande flexibilidade do cabo de aço, com resistência irregular durante o funcionamento da cabine, pode causar oscilação em curva ("curly oscillation") da cabine. Além disso, tensão desequilibrada entre vários cabos de aço pode fazer a cabine tremer durante o funcionamento. |
| 4 | Freio (Brake) | O conforto de viagem durante o funcionamento pode ser influenciado se o braço do freio for instalado apertado demais ou liberado de forma incompleta. |
| 5 | Balanceamento da cabine (Balance of the car) | Se o peso da cabine for desequilibrado, haverá tensão desigual nas sapatas de guia que ligam a cabine ao trilho-guia. Como resultado, as sapatas de guia roçarão no trilho-guia durante o funcionamento, afetando o conforto de viagem. |
| 6 | Caixa de engrenagens (Gearbox) | Para motor assíncrono, o desgaste ou a instalação inadequada da caixa de engrenagens também pode afetar o conforto de viagem. |
| 7 | Ressonância causada pela cabine, pelo trilho-guia e pelo motor | Ressonância é uma característica inerente de um sistema físico, relacionada ao material e à qualidade dos componentes do sistema. Se você tiver certeza de que a oscilação é causada por ressonância, reduza a ressonância aumentando ou diminuindo o peso da cabine ou do contrapeso e acrescentando absorvedores de ressonância nas conexões dos componentes (por exemplo, colocar uma manta de borracha sob o motor). |

Fonte: manual NICE3000new, págs. PDF 168 a 174 (impressas 167 a 173)

### 12.7.2 Ajuste da precisão de nivelamento (Leveling Accuracy Adjustment)

#### 1 Descrição dos componentes de nivelamento (Description of leveling components)

- Placa de nivelamento (Leveling plate): o comprimento da placa de nivelamento precisa combinar com a chave de nivelamento. Quando a chave de nivelamento passa pela placa de nivelamento, cada extremidade da placa de nivelamento deve sobressair da chave de nivelamento em pelo menos 10 mm. Todas as placas de nivelamento devem ter o mesmo comprimento, com desvio menor que 5 mm.
- Chave de nivelamento (leveling switch): a placa de nivelamento deve ser vertical em relação à chave de nivelamento. Quando a cabine chega, a placa de nivelamento deve entrar na chave de nivelamento em 2/3 do seu próprio comprimento.
- Chave optoeletrônica (Optoelectronic switch): recomendam-se chaves fotoelétricas do tipo NO para melhorar a estabilidade da detecção do sinal.

#### 2 Métodos de ajuste da precisão de nivelamento (Leveling accuracy adjustment methods)

Há dois métodos de ajuste da precisão de nivelamento, descritos a seguir.

**Ajuste de todos os pavimentos (All-floor adjustment)**

| Código | Nome | Faixa | Padrão |
|---|---|---|---|
| F4-00 | Leveling adjustment | 0 to 60 | 30 |

F4-00 é usado para ajustar a posição de parada da cabine em todos os pavimentos e o padrão é 30. O ajuste de F4-00 vale para todos os pavimentos.

Aumente F4-00 se ocorrer subnivelamento (under-leveling) em todos os pavimentos e diminua F4-00 se ocorrer sobrenivelamento (over-leveling) em todos os pavimentos.

**Ajuste por pavimento (Single-floor adjustment)**

Ajuste a posição de parada da cabine em cada pavimento separadamente ajustando os parâmetros do grupo Fr. Parâmetros de ajuste de nivelamento no grupo Fr:

| Código | Nome | Faixa | Padrão | Unidade |
|---|---|---|---|---|
| Fr-00 | Leveling adjustment function | 0 to 1 | 0 | - |
| Fr-01 | Leveling adjustment record 1 | 00000 to 60060 | 30030 | mm |
| Fr-02 | Leveling adjustment record 2 | 00000 to 60060 | 30030 | mm |
| ... | ... | ... | ... | ... |
| Fr-28 | Leveling adjustment record 28 | 00000 to 60060 | 30030 | mm |

(A faixa "00000 to 60060" aparece uma só vez, mesclada, na coluna da faixa; a linha "to to to to" do texto extraído indica as reticências entre Fr-02 e Fr-28.)

O fluxograma de ajuste da precisão de nivelamento por pavimento é mostrado na figura seguinte (Figura 5-18), transcrito como procedimento:

1. Ajustar Fr-00 em 1.
2. Entrar na cabine depois que o elevador correr automaticamente até o pavimento mais alto.
3. Ajustar os dados de nivelamento com base no erro real: pressionar uma vez o botão do pavimento mais alto muda a posição de parada 1 mm para cima; pressionar uma vez o botão do pavimento mais baixo muda a posição de parada 1 mm para baixo.
4. Pressionar ao mesmo tempo o botão do pavimento mais alto e o botão do pavimento mais baixo na cabine para salvar o resultado do ajuste.
5. Pergunta: o ajuste de todos os pavimentos foi concluído? Se não, levar a cabine ao pavimento seguinte e fazer o ajuste (voltando ao passo 3). Se sim, restaurar Fr-00 em 0.
6. Fim (End).

Figura 5-18: Ajuste da precisão de nivelamento por pavimento (fluxograma acima).

NOTA (Note):

- Certifique-se de que o autoajuste do poço foi concluído com sucesso e de que o elevador funciona corretamente em velocidade normal.
- Depois de ajustar Fr-00 em 1, o elevador bloqueia as chamadas de pavimento (shields hall calls), corre automaticamente até o pavimento mais alto e mantém a porta aberta após a chegada.
- Durante o ajuste, a CCB exibe "00" ou o valor após o ajuste. Valor positivo: seta para cima + valor; valor negativo: seta para baixo + valor; faixa de ajuste: ±30 mm.
- Depois de salvar o resultado do ajuste, a CCB exibe o pavimento atual.
- Note que, se um determinado pavimento não precisa de ajuste, também é preciso salvar o dado uma vez. Caso contrário, não é possível registrar a chamada de cabine (car call).

#### 3 Diretrizes de ajuste da precisão de nivelamento (Leveling accuracy adjustment guidelines)

- Se as posições de parada na chegada do elevador a cada pavimento são fixas e iguais nos sentidos de subida e descida e a cabine não está nivelada com a soleira do pavimento (hall sill), faça o ajuste dos pavimentos relacionados ajustando os parâmetros do grupo Fr.
- Se as posições de parada na chegada do elevador a cada pavimento são fixas, mas diferentes nos sentidos de subida e descida, faça o ajuste ajustando tanto F4-00 quanto os parâmetros do grupo Fr. O método específico de ajuste é o seguinte:

Primeiro, ajuste o desvio de nivelamento em todos os pavimentos por meio de F4-00. Suponha que as posições de parada nos sentidos de descida e de subida sejam, respectivamente, a e b, e execute a operação conforme a tabela a seguir.

| Tipo | Diagrama | Cálculo | Operação de ajuste |
|---|---|---|---|
| Subnivelamento (Under-leveling) | Duas linhas horizontais: a (parada vindo de Down) acima, b (parada vindo de Up) abaixo | H = (a – b)/2 | (F4-00) + H |
| Sobrenivelamento (Over-leveling) | Duas linhas horizontais: b acima, a abaixo | H = (b – a)/2 | (F4-00) – H |

Depois, ajuste as posições de parada dos pavimentos relacionados por meio dos parâmetros do grupo Fr.

Observe as seguintes precauções ("Pay attentions to the following precautions"):

- Evite o sobreajuste nos parâmetros do grupo Fr quando o desvio de nivelamento for grande demais.
- Suponha que, quando a cabine chega à zona de nivelamento (leveling zone), a distância entre a borda do sensor de nivelamento e a borda da placa de nivelamento seja A, e o desvio de altura entre a soleira da cabine (car sill) e a soleira do pavimento na chegada da cabine seja B. Se B ≥ A para um determinado pavimento, é preciso ajustar a posição da placa de nivelamento desse pavimento, para garantir que B ≤ A na chegada da cabine. Caso contrário, embora você tenha ajustado a precisão de nivelamento pelos parâmetros do grupo Fr, o elevador ainda pode parar fora da zona de nivelamento.

Figura 5-19: Diagrama da distância de nivelamento. Mostra a cabine, a soleira da cabine (Car sill), a soleira do pavimento (Hall sill), a placa de nivelamento, os sinais de nivelamento de descida e de subida (Down leveling signal, Up leveling signal) e as cotas A e B.

- Se a posição de parada da cabine não é fixa no mesmo pavimento em percursos ou cargas diferentes, e o desvio de altura entre a posição da cabine e a soleira do pavimento é inconsistente no mesmo pavimento, isso pode ser causado por parâmetros de laço de velocidade inadequados (parâmetros do grupo F2). Para resolver o problema, aumente o ganho proporcional do laço de velocidade ou diminua o tempo integral do laço de velocidade adequadamente.

Fonte: manual NICE3000new, págs. PDF 175 a 177 (impressas 174 a 176)

---

## 12.8 Parâmetros do projeto (esquema Vitinho)

O esquema traz a lista de parâmetros do projeto na folha /5 e as instruções de ajuste na folha /6. Cada parâmetro abaixo foi confrontado com o manual NICE3000new (nome, faixa, padrão e página PDF). Onde o desenho diz "Model dependent" ou "Based on actual conditions", o valor depende do motor e do projeto e não é dado aqui. A tabela completa de todos os parâmetros do manual (F0 a FE, Fb, Fr e FP) fica em apêndice próprio. Fonte: esquema Vitinho 19061867-ZL, folhas /5 e /6 (págs. PDF 7 e 8); manual NICE3000new, págs. PDF 159 a 215.

### 12.8.1 Lista de parâmetros da folha /5

A folha tem quatro blocos de colunas (Para. NO., Parameter Name, Setting value). A ordem abaixo segue o desenho: bloco 1 (esquerda), bloco 2, bloco 3, bloco 4. Total: 70 linhas, 72 códigos (a linha "Fb-04/05/19" reúne três).

#### Bloco 1

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

#### Bloco 2

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

#### Bloco 3

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

#### Bloco 4

| Código | Nome no esquema | Valor no esquema | Manual (nome, faixa, padrão, pág. PDF) |
|---|---|---|---|
| F2-33 | Torque amplitude (amplitude de torque) | 15% of the reted (grafia do desenho) motor torque (15% do torque nominal do motor) | O único F2-33 do manual é "Torque limit"; 1 a 150% do torque nominal; padrão 110; 0 usa 110%; P320 (tabela do teste de força de frenagem). Não há correspondência de nome |
| F6-07 | Number of elevators in group control (número de elevadores em grupo) | Based on actual conditions | Number of elevators in parallel/group mode; 1 a 8; padrão 1; P213 |
| F6-08 | Elevator NO. (número do elevador) | Group control: elevator NO. set based on actual conditions. Parallel control: 1 as the master elevator and 2 as the slave elevator (grupo: número conforme as condições reais; paralelo: 1 principal, 2 auxiliar) | Elevator No.; 1 a 8; padrão 1; P213 |
| F6-09 | Program selection | Bit3=1: Parallel/group control via CAN2 | Program control selection; padrão 0; Bit3 Parallel/Group control implemented at CAN2; P213 |
| F8-16 | Start address of hall call auxiliary command | 0-48 (Double-door set) (porta dupla) | Start address of hall call auxiliary command; 0 a 40; padrão 0; endereço da HCB da porta de trás = endereço da frente no mesmo andar + F8-16; P230-231 |

#### Notas da folha /5 (canto inferior direito)

1. "The new generation of control cabinet id connected to the car top inspection box through communication. The car top inspection signal and up/down leveling signal are transmitted through communication." Tradução: a nova geração de quadro é ligada à caixa de inspeção do teto da cabine por comunicação; o sinal de inspeção do teto e o sinal de nivelamento de subida/descida são transmitidos por comunicação. ("id" é a grafia do desenho.)
2. "The up and down limits are realied through the software limit funcation. Therefore, the up and down limit switches are not needed." Tradução: os limites de subida e descida são realizados pela função de limite por software; por isso as chaves de limite de subida e de descida não são necessárias. (Grafias "realied" e "funcation" do desenho.)

---

### 12.8.2 Instruções de ajuste da folha /6 ("Tuning instruction")

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

### 12.8.3 Dados que o esquema deixa para o projeto
- "Model dependent": F0-03, F0-04, F0-05, F1-01 (potência), F1-02 (tensão), F1-03 (corrente), F1-04 (frequência), F1-05 (rotação nominal), F1-12 (pulsos do encoder por volta). O esquema não dá número para o elevador de referência (7,5 kW, 380 V, síncrono de ímã permanente). Esses valores vêm da plaqueta do motor e do encoder (o manual manda ajustar F1-01 a F1-05 pela plaqueta do motor, P186, e F1-12 pela plaqueta do encoder, P188).
- "Based on actual conditions": F6-00, F6-01, F6-07, F6-08 (e "set based on actual conditions" em Fb-02, Fb-03, Fb-18). O esquema não dá o número de andares do projeto nem o valor binário das paradas atendidas.
- Listas sem opção marcada: F1-00, F1-11, F1-25, F2-10, F5-36, Fb-00, FC-04. A folha mostra as opções do manual do fabricante, não a escolhida. A escolha de F1-25 (síncrono = 1) e F1-00 depende do motor e do encoder reais.
- F8-16 traz "0-48 (Double-door set)", que é uma faixa, não um valor.

### 12.8.4 Divergências entre o esquema e o manual (conferidas, não corrigidas)
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

## 12.9 Se o seu elevador tiver outra configuração

| Se o seu elevador tiver | O que muda neste capítulo |
|---|---|
| Motor assíncrono | Vale o autoajuste de motor assíncrono (com carga e sem carga) da seção 12.5.1, o tipo de motor F1-25 diferente e o encoder do tipo ABZ; não há o contator FX nem a ligação ao X8 |
| Encoder UVW, ABZ ou Endat | O tipo de encoder em F1-00 e os autoajustes disponíveis mudam; o autoajuste estático só vale para encoder SIN/COS e absoluto de motor síncrono |
| Outra velocidade nominal | Os parâmetros F0-03, F0-04 e F3-xx mudam, e o autoajuste do poço deve ser refeito depois de alterar F0-04 |
| Mais de 3 pavimentos | A altura entre pavimentos e o número de paradas entram no autoajuste do poço e nas placas de chamada de cada pavimento (seção 12.6.3) |
| Porta traseira | Entram os sinais e parâmetros da porta traseira (capítulos 1 e 9) |

Fonte: manual NICE3000new, seções 5.4 a 5.6, págs. PDF 150 a 177.

## 12.10 Teste o que você aprendeu

1. O que se verifica antes da primeira energização? *(Seção 12.3: a lista de verificação de segurança e de circuitos.)*
2. Em que ordem se comissiona o sistema? *(Seção 12.2: verificação de segurança, energização e estado do controlador, velocidade de inspeção com autoajuste do motor, velocidade normal com autoajuste do poço, conforto de viagem.)*
3. Que falha o controlador mostra se o autoajuste do poço falha? *(Capítulo 13, Err35.)*
4. O que muda no autoajuste do motor se o encoder for SIN/COS e o motor, síncrono? *(Seção 12.5.1: o autoajuste estático está disponível.)*
5. Onde ficam os parâmetros do projeto? *(Seção 12.8.)*

## Fontes do capítulo

- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf` (368 páginas, edição 20181130), capítulo 4 e seções 5.1 a 5.6, págs. PDF 134 a 177.
- Esquema Vitinho 19061867-ZL, folhas /5 e /6 (págs. PDF 7 e 8).
