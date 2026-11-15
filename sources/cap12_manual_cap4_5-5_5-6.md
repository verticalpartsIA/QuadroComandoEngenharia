# Capítulo 12 (fonte): manual NICE3000new, capítulo 4 e seções 5.5 e 5.6

Tradução estruturada e fiel do manual do controlador NICE3000new (Suzhou Inovance). Nada foi acrescentado nem corrigido. Convenções deste arquivo:

- "pág. PDF N" é a página do arquivo PDF de 368 páginas; a página impressa é N-1.
- Valores numéricos, parâmetros, subcódigos, siglas e nomes de teclas ficam como no manual (o ponto decimal do manual foi mantido, pois é o que o painel exibe).
- Avisos: o rótulo original em inglês aparece entre parênteses logo após o rótulo em português.
- Figuras não foram copiadas; cada uma é descrita em uma linha.
- Siglas mantidas: MCB, CTB, CCB, HCB, NO, NC. Onde o manual escreve "Err" e "E" para o mesmo tipo de falha, o original foi mantido.

---

# 4 Ferramentas de comissionamento (Commissioning Tools)

Índice do capítulo (pág. PDF 134): 4.1 Keypad (pág. impressa 134); 4.2 Operation Panel (135); 4.2.1 Descrição das teclas (136); 4.2.2 Indicadores (137); 4.2.3 Exibição de dados (138); 4.2.4 Operações básicas (138); 4.3 Software de comissionamento para celular (140).

## Introdução do capítulo

O NICE3000new aceita quatro ferramentas de comissionamento: o teclado de 3 botões integrado à placa (doravante "keypad"), o painel de operação e exibição de informações com LED (doravante "operation panel"), o software de monitoramento em computador (host computer monitoring software) e o software de comissionamento para celular.

Tabela 4-0 (sem número no manual): ferramentas de comissionamento

| Ferramenta | Função | Observação |
|---|---|---|
| Keypad | Serve para inserir os comandos de comissionamento do poço e ver informações de pavimento. | Padrão (Standard) |
| Painel de operação com LED (MDKE) | Serve para ver e modificar parâmetros relacionados ao acionamento e ao controle do elevador. | Opcional (Optional) |
| Painel de operação com LED (MDKE6) | Serve para carregar (upload), baixar (download), ver e modificar parâmetros do controlador. | Opcional |
| Software de comissionamento para celular (EDSAP) | Um módulo WIFI externo conecta a MCB ao smartphone com o software de comissionamento instalado; por ele é possível comissionar o elevador e carregar e baixar parâmetros. | Opcional |

O manual descreve em detalhe apenas o keypad e o painel de operação com LED (MDKE), de uso mais comum.

Fonte: manual NICE3000new, págs. PDF 134 a 135 (impressas 133 a 134)

## 4.1 Keypad

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

## 4.2 Painel de operação (Operation Panel)

Figura 4-3: diagrama do painel de operação com LED, com as legendas: Reserved; RUN indicator; Data display; Programming key; Menu key; RUN key; Up/Down indicator; Auto-tuning indicator; Unit indicator; UP key; Shift key; Stop/Reset key; Confirm key; Down key; Fault hiding key. No painel aparecem ainda os rótulos MF.K, RUN, STOP/RES, QUICK, PRG, ENTER, RUN, LOCAL/REMOT, FWD/REV, TUNE/TC e as unidades RPM, %, A, V, Hz.

### 4.2.1 Descrição das teclas (Description of Keys)

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

### 4.2.2 Indicadores (Indicators)

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

### 4.2.3 Exibição de dados (Data Display)

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

### 4.2.4 Operações básicas (Basic Operations)

O painel de operação adota três níveis de menu:

- Nível I: grupo de código de função (function code group)
- Nível II: código de função (function code)
- Nível III: valor de ajuste do código de função (function code setting value)

Figura (sem número): estrutura de menus. Na energização ou após o reset de fábrica (factory reset) o display mostra 0.000; PRG leva ao menu de nível I (grupos F0, F1, ..., F9, FA, ..., FP, percorridos com Up e Down); ENTER entra no nível II (códigos F0-00, F0-01, ..., F0-07, percorridos com Up e Down); ENTER entra no nível III (valor do parâmetro, por exemplo F0-01); PRG retorna ao nível anterior.

#### 1 Exibição de parâmetros (Parameter display)

O conteúdo específico dos parâmetros exibidos é ajustado em FA-01 (Display in running state, exibição no estado de funcionamento) e FA-02 (Display in stop state, exibição no estado parado). Cada bit binário de FA-01 e FA-02 indica um conteúdo específico de parâmetro (para detalhes, o manual remete à descrição dos parâmetros). Se um bit é ajustado em 1, o parâmetro indicado por esse bit é exibido; se o bit é ajustado em 0, o parâmetro não é exibido.

Nos estados parado ou em funcionamento, vários parâmetros de estado podem ser exibidos pressionando uma tecla do painel de operação (o símbolo da tecla foi perdido na extração; a tecla Shift é a que o manual descreve para esta função em 4.2.1) para alternar entre cada "byte" de FA-01 e FA-02 (ambíguo, ver o original na pág. PDF 140).

- Parâmetros de estado em funcionamento (Running state parameters): há 16 parâmetros de estado disponíveis no estado de funcionamento. A exibição de cada parâmetro correspondente a cada bit é escolhida segundo os bits binários de FA-01 (Display in running state).
- Parâmetros de estado parado (Stop state parameters): há 12 parâmetros de estado disponíveis no estado parado. A exibição de cada parâmetro correspondente a cada bit é escolhida segundo os bits binários de FA-02 (Display in stop state).

NOTA (Note): Para detalhes dos estados, consulte FA-01 e FA-02 em "6 Parameter Description".

#### 2 Visualização de parâmetros (Parameter viewing)

Pressione PRG e depois uma das teclas Up/Down (símbolos perdidos na extração, ambíguo, ver o original na pág. PDF 140) para exibir o menu de nível I, isto é, a classificação dos grupos de parâmetros.

Depois de entrar em cada nível de menu, se um dígito do display piscar, ele pode ser modificado com as três teclas indicadas por símbolos (ambíguo, ver o original na pág. PDF 140). A figura seguinte mostra o fluxo de operação.

Figura 4-4: Procedimento de visualização de parâmetros. Sequência de telas: parâmetro de estado (exibição padrão) -> PRG -> menu de nível I -> ENTER (entrar) -> menu de nível II -> ENTER (entrar) -> menu de nível III; em cada nível, PRG retorna ao nível anterior; ENTER (Save) salva; "Switchover" alterna entre itens do mesmo nível; "Cyclic process" indica percurso cíclico.

#### 3 Modificação de parâmetros (Parameter modification)

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

## 4.3 Software de comissionamento para celular (Cell phone commissioning software)

Este software implementa principalmente: ajuste de parâmetros, comissionamento de funções, monitoramento do estado de operação em tempo real, carga (upload) e descarga (download) de parâmetros e gravação do firmware (burning) do sistema de controle do elevador no controlador, usando um smartphone.

Para detalhes, o manual remete ao "User Manual of Elevator Commissioning APP via Smartphone", com código de dados (data code) 19010576.

Fonte: manual NICE3000new, pág. PDF 141 (impressa 140)

---

# 5.5 Comissionamento em velocidade normal (Commissioning at Normal Speed)

Figura (sem número): árvore da seção. "Commissioning at normal speed" se divide em três ramos:

- Shaft auto-tuning (autoajuste do poço): Make preparations; Check that shaft auto-tuning conditions are met; Perform shaft auto-tuning; Perform running test at normal speed.
- Car top commissioning (comissionamento da caixa de teto): Light curtain commissioning; Door machine controller commissioning.
- HCB commissioning (comissionamento da caixa de corrida): HCB installation; HCB address setting.

## 5.5.1 Autoajuste do poço (Shaft Auto-tuning)

### 1 Fazer os preparativos para o autoajuste do poço

Figura (sem número): três quadros de verificação, transcritos abaixo.

1. Verificar se as chaves do poço (shaft switches) atuam corretamente. Inclui chaves de fim de curso final (final limit switches), chaves de limite (limit switches), chaves de desaceleração (slowdown switches) e chaves de nivelamento (leveling switches).
2. Verificar se a sequência de atuação das chaves de nivelamento está correta.
   - Em geral, uma chave de nivelamento é instalada. Se várias chaves de nivelamento forem instaladas, verifique se a sequência de atuação está correta. Tome como exemplo a situação com três sensores: (o texto traz a palavra solta "switch", ambíguo, ver o original na pág. PDF 160)
   - (1) Sequência de atuação dos sensores na inspeção em subida (inspection up): chave de nivelamento de subida (up leveling switch) → chave de zona de porta (door zone switch) → chave de nivelamento de descida (down leveling switch).
   - (2) Sequência de atuação dos sensores na inspeção em descida (inspection down): chave de nivelamento de descida → chave de zona de porta → chave de nivelamento de subida.
3. Verificar o estado da comunicação CANbus.
   - Verifique o estado da comunicação CANbus. Se a falha E51 não for reportada e o indicador CAN1 na MCB estiver aceso fixo (steady ON), a comunicação CANbus entre a MCB e a CTB está normal. Se a comunicação CANbus estiver anormal, corrija a falha E51 conforme a solução descrita na seção 7.4.

Parâmetros (Parameters)

| Parâmetro | Descrição do parâmetro | Faixa (Description) | Padrão (Default) | Observações (Remarks) |
|---|---|---|---|---|
| F0-04 | Velocidade nominal do elevador (Rated elevator speed) | 0.250–8.000 m/s | 1.600 m/s | - |
| F6-00 | Pavimento mais alto do elevador (Top floor of the elevator) | F6-01 to F6-56 | 9 | "Actual number of floors + 1 - Bottom floor" (ambíguo, ver o original na pág. PDF 160) |
| F6-01 | Pavimento mais baixo do elevador (Bottom floor of the elevator) | 1 to F6-00 | 1 | - |
| F3-26 | Velocidade de autoajuste do poço (Shaft auto-tuning speed) | 0.250 to 0.630 | 0.250 | - |

NOTA (Note): Depois que F0-04 for alterado, o autoajuste do poço deve ser executado novamente. Caso contrário, ocorrerá uma anormalidade durante o funcionamento do elevador.

### 2 Verificar se as condições para o autoajuste do poço foram atendidas

- O elevador está no estado de acionamento de emergência (emergency drive state).
- O elevador precisa ir até abaixo da posição de nivelamento mais baixa, isto é, pelo menos uma chave de nivelamento fica abaixo da placa de nivelamento (leveling plate). O sinal da chave de desaceleração de descida 1 (down slow-down switch 1) que entra na MCB está ativo. (Esta condição vale apenas para o caso de dois pavimentos.)
- O NICE3000new não está em estado de falha. Se houver falha, pressione STOP/RES para resetá-la.

### 3 Executar o autoajuste do poço

Atendidas as condições anteriores, inicie o autoajuste do poço por um dos métodos a seguir:

- Ajuste F1-11 em 3 no painel de operação. Passe o acionamento de emergência para normal (Switch emergency drive to normal).
- Ajuste F7 em 1 no keypad da MCB. Passe o acionamento de emergência para normal. ("Set F7 to 1" é o texto do manual, ambíguo quanto ao código completo, ver o original na pág. PDF 161.)

Depois que o autoajuste do poço começa, o elevador corre na velocidade ajustada em F3-26. O elevador vai automaticamente até a placa de nivelamento do pavimento mais baixo, depois sobe até a placa de nivelamento do pavimento mais alto e para ao chegar a ela. Em seguida, o keypad da MCB exibe o número do pavimento atual (pavimento mais alto), indicando que o autoajuste do poço foi bem-sucedido.

Se a falha Err35 for reportada durante o processo, o autoajuste do poço falhou. É preciso corrigir a falha conforme a solução descrita no Capítulo 7 e executar o autoajuste do poço novamente.

### 4 Executar o teste de funcionamento em velocidade normal

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

## 5.5.2 Comissionamento da caixa de teto (Car Top Commissioning)

### Informações de segurança (Safety Information)

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

### 1 Comissionamento da cortina de luz (Light Curtain Commissioning)

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

### 2 Comissionamento do controlador da máquina de porta (Door Machine Controller Commissioning)

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

#### Tratamento de problemas comuns de controle de porta (Handling of Common Door Control Problems)

- No estado de porta fechada, o sistema envia um comando de abrir porta, mas a porta não abre.
  - Verificar se o sinal de limite de abertura está sempre ativo.
  - Verificar se há saída de abertura de porta vendo o segmento 1 do LED 1 em FA-34. Se há saída (segmento 1 aceso), verificar: se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta e se o controlador da máquina de porta funciona corretamente.
- No estado de limite de abertura, o sistema envia um comando de fechar porta, mas a porta não fecha.
  - Verificar se o sinal da cortina de luz está sempre ativo.
  - Verificar se há saída de fechamento de porta vendo o segmento 2 do LED 1 em FA-34. Se há saída (segmento 2 aceso), verificar: se a conexão do cabo entre a CTB e o controlador da máquina de porta está correta e se o controlador da máquina de porta funciona corretamente.
- O elevador não abre a porta na área da zona de porta e a falha Err53 é reportada. Corrigir a falha conforme a solução descrita no Capítulo 7.

Fonte: manual NICE3000new, págs. PDF 162 a 166 (impressas 161 a 165)

## 5.5.3 Instalação e ajuste da HCB (HCB Installation and Setting)

Esta seção descreve a instalação e o ajuste da HCB (caixa de corrida) do sistema de elevador independente de porta única. Para detalhes sobre a instalação e o ajuste da HCB do sistema de elevadores em paralelo (parallel) e do sistema de elevador de portas opostas (opposite door), o manual remete às seções correspondentes.

### 1 Instalação da HCB

Instalar uma HCB para cada pavimento de serviço (pavimentos sem serviço não exigem HCB), como mostra a Figura 5-14.

A HCB comunica com a MCB por Modbus. Todas as HCBs são ligadas em paralelo e depois conectadas à MCB.

### 2 Ajuste do endereço da HCB

Ajuste um endereço para cada HCB. Caso contrário, a HCB não pode ser usada.

O endereço de cada HCB deve ser único. HCBs com o mesmo endereço não podem ser usadas. Para detalhes de como ajustar o endereço, veja a descrição da HCB correspondente.

Ajuste o endereço com base no número da placa de nivelamento do pavimento. A partir do pavimento mais baixo, ajuste o endereço da HCB do pavimento onde está a N-ésima placa de nivelamento em N, como mostra a figura a seguir (Figura 5-14).

Figura 5-14: Instalação da HCB e ajuste de endereço. Mostra os pavimentos 1 a 4 com as placas de nivelamento 1 a 4; as HCBs dos pavimentos com placas 1, 2 e 4 têm os endereços 1, 2 e 4; o pavimento 3 está rotulado "Non-service floor, HCB not installed".

Depois de concluídas a instalação e o ajuste de endereço das HCBs, é possível chamar o elevador pela HCB para iniciar o funcionamento em velocidade normal.

NOTA (Note): Quando a placa de exibição (display board) é usada dentro da cabine, o endereço deve ser ajustado em 0.

Fonte: manual NICE3000new, pág. PDF 167 (impressa 166)

---

# 5.6 Ajuste do conforto de viagem (Riding Comfort Adjustment)

Figura (sem número): árvore da seção. "Riding comfort adjustment" se divide em "Riding comfort adjustment during running" (com "Riding comfort adjustment at elevator startup and stop" e "Riding comfort adjustment to the running curve") e "Leveling accuracy adjustment" (com "Description of leveling components", "All-floor leveling accuracy adjustment" e "Single-floor leveling accuracy adjustment").

## 5.6.1 Ajuste do conforto de viagem (Riding Comfort Adjustment)

O conforto de viagem é um fator importante do desempenho global do elevador. A instalação inadequada de peças mecânicas e ajustes de parâmetros inadequados causam desconforto. Melhorar o conforto de viagem envolve principalmente o ajuste da saída do controlador e da construção mecânica do elevador.

### 1 Ajuste de desempenho do controle do sistema (Performance adjustment of system control)

Figura 5-15: Sequência temporal de funcionamento (Running time sequence). Gráfico de V (velocidade) contra t (tempo), com as linhas: RUN contactor; Brake contactor; Shorting door lock circuit contactor; Shorting PMSM stator contactor; Internal running status; Leveling signal; RUN contactor feedback; Brake contactor feedback; Shorting door lock circuit contactor feedback; Shorting PMSM stator contactor feedback. Os parâmetros F2-16, F3-18, F3-19, F3-20, F8-11 e F2-17 aparecem marcados nos intervalos do gráfico.

#### 1) Ajuste do conforto na partida e na parada do elevador (Riding comfort adjustment at elevator startup and stop)

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

#### 2) Ajuste do conforto de viagem à curva de funcionamento (Riding comfort adjustment to the running curve)

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

### 2 Ajuste da construção mecânica (Adjustment of mechanical construction)

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

## 5.6.2 Ajuste da precisão de nivelamento (Leveling Accuracy Adjustment)

### 1 Descrição dos componentes de nivelamento (Description of leveling components)

- Placa de nivelamento (Leveling plate): o comprimento da placa de nivelamento precisa combinar com a chave de nivelamento. Quando a chave de nivelamento passa pela placa de nivelamento, cada extremidade da placa de nivelamento deve sobressair da chave de nivelamento em pelo menos 10 mm. Todas as placas de nivelamento devem ter o mesmo comprimento, com desvio menor que 5 mm.
- Chave de nivelamento (leveling switch): a placa de nivelamento deve ser vertical em relação à chave de nivelamento. Quando a cabine chega, a placa de nivelamento deve entrar na chave de nivelamento em 2/3 do seu próprio comprimento.
- Chave optoeletrônica (Optoelectronic switch): recomendam-se chaves fotoelétricas do tipo NO para melhorar a estabilidade da detecção do sinal.

### 2 Métodos de ajuste da precisão de nivelamento (Leveling accuracy adjustment methods)

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

### 3 Diretrizes de ajuste da precisão de nivelamento (Leveling accuracy adjustment guidelines)

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

# Lacunas e dúvidas

Pontos que dependem de dados do elevador de referência ou do projeto, ou que o manual deixa em aberto. Nenhum valor foi inventado.

1. Valores reais do elevador de referência: F0-04 (velocidade nominal), F6-00 e F6-01 (pavimentos mais alto e mais baixo), F3-26 (velocidade de autoajuste), F0-03 (velocidade máxima) e potência do motor (o manual separa condutas para P ≤ 5.5 kW). O capítulo só pode citar os padrões do manual.
2. Tipo de célula de carga do elevador de referência (sem célula de carga, analógica, ou ambas), que decide qual dos três quadros de F8-01 vale (valores 2, 1 ou 3).
3. Características NO/NC reais da cortina de luz e dos limites de porta do projeto, que definem os bits Bit0, Bit2 e Bit4 de F5-25. O manual não informa o valor padrão desses bits.
4. Elevador de porta única ou dupla, independente, em paralelo ou de portas opostas: o manual descreve só porta única independente e remete a outras seções para os demais casos (fora do escopo deste arquivo).
5. Número de pavimentos de serviço e pavimentos sem serviço, para a numeração dos endereços das HCBs. O manual fixa a regra (endereço N para a N-ésima placa de nivelamento), mas o exemplo da Figura 5-14 é ilustrativo.
6. Modelo do painel de operação disponível no projeto (MDKE ou MDKE6) e se haverá uso do software de celular (EDSAP) com módulo WIFI; o manual dá só a descrição geral e remete a outro manual (código 19010576).
7. Tradução de "emergency drive" (usada no manual 5.5.1): o glossário do projeto traz "resgate elétrico". Foi usado "acionamento de emergência" literal; decidir se mapeia para "resgate elétrico". Idem para "HCB" como "caixa de corrida" e "CTB" como "caixa de teto" (assumidos pelo glossário); MCB e CCB ficaram como siglas por não constarem do glossário.
8. Inconsistências de texto do manual mantidas sem correção:
   - o cabeçalho da Tabela 5-5 diz "F-35 LEDs", enquanto o texto diz F5-35;
   - o manual cita "FA-34" para ver as saídas de abrir/fechar porta, enquanto o monitoramento anterior usa F5-35 (pág. PDF 166);
   - falhas citadas como "E51", "E53", "E33" e como "Err35", "Err53";
   - o exemplo da Figura 4-5 altera F3-02 "de 10.00 Hz para 15.00 Hz", enquanto a tabela 5.6.1 chama F3-02 de "Acceleration rate" (sem unidade em Hz);
   - F3-19 e F8-11 têm o mesmo nome "Brake release delay" no manual;
   - "Set F7 to 1" sem subcódigo (pág. PDF 161);
   - nome do pré-torque por pesagem aparece como "Load cell pre-torque compensation" e como "Weighing pre-torque compensation".
9. Conteúdo gráfico não transcrito (só descrito): sequência de teclas das Figuras 4-2, 4-4 e 4-5, estados dos símbolos da Tabela 4-1 e a posição exata de F3-xx e F2-xx nas Figuras 5-15 a 5-17. Ver o PDF nas páginas indicadas se o capítulo precisar de ilustração própria.
10. O manual remete a seções fora do escopo: 6.1 Keypad, Capítulo 6 (descrição de FA-01/FA-02), seção 7.4 e Capítulo 7 (falhas E51, Err35, Err53). O capítulo do livro deve buscar esses dados nas fontes correspondentes.
