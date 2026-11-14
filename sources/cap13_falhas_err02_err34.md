# Capítulo 13 (Diagnóstico de falhas): tabela de falhas Err02 a Err34

Fonte: manual NICE3000new, seção 7.4 "Fault Information and Troubleshooting". Páginas citadas são as do PDF (a página impressa é a do PDF menos 1). Tradução fiel; nada foi acrescentado ao manual. O manual abre a tabela dizendo: se uma falha for reportada, o sistema faz o processamento correspondente conforme o nível da falha, e a falha deve ser tratada conforme as causas possíveis descritas na tabela.

Os códigos Err01 não constam na tabela. Os demais códigos de Err02 a Err34 constam (Err19 consta; Err27, Err28, Err31 e Err32 constam como "Reservado").

As três notas que o manual traz depois da tabela (pág. 288 do PDF, ao final da tabela) tratam de Err41, Err42, Err51, Err52 e Err57, fora deste escopo (Err02 a Err34). Nenhuma nota do manual está ligada a um código deste arquivo.

### Err01. Não consta na tabela
- Nível: não consta na tabela. Páginas do manual: 268 (a tabela começa em Err02).
- Subcódigos: nenhum.
- Notas do manual: nenhuma.

### Err02. Sobrecorrente durante a aceleração (Overcurrent during acceleration)
- Nível: 5A. Páginas do manual: 268.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A saída do circuito principal está aterrada ou em curto-circuito | Verificar se os cabos do motor e de aterramento estão ligados corretamente; verificar se o contator de curto do estator do motor síncrono causa curto-circuito no lado de saída do controlador; verificar se os cabos do motor têm a capa danificada |
| A autossintonia do motor foi feita de forma inadequada | Verificar se os parâmetros do motor estão de acordo com a placa de identificação; fazer a autossintonia do motor novamente |
| O sinal do encoder está incorreto | Verificar se o número de pulsos por revolução (PPR) do encoder está ajustado corretamente; verificar se o sinal do encoder sofre interferência, se o cabo do encoder passa independente no eletroduto, se o cabo é longo demais e se a malha (shield) está aterrada em uma só extremidade; verificar se o encoder está instalado de forma firme e se o eixo rotativo está ligado ao eixo do motor de forma firme, observando se o encoder está estável durante a marcha em velocidade normal; verificar se a ligação dos fios do encoder está correta. Para o motor assíncrono, executar SVC e comparar a corrente para julgar se o encoder funciona corretamente |
| A sequência de fases do motor está incorreta | Trocar a sequência de fases UVW do motor |
| O tempo de aceleração é muito curto | Reduzir a taxa de aceleração |

- Notas do manual: nenhuma.

### Err03. Sobrecorrente durante a desaceleração (Overcurrent during deceleration)
- Nível: 5A. Páginas do manual: 269.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A saída do circuito principal está aterrada ou em curto-circuito | Verificar se os cabos do motor e de aterramento estão ligados corretamente; verificar se o contator de curto do estator do motor síncrono causa curto-circuito no lado de saída do controlador; verificar se os cabos do motor têm a capa danificada |
| A autossintonia do motor foi feita de forma inadequada | Verificar se os parâmetros do motor estão de acordo com a placa de identificação; fazer a autossintonia do motor novamente |
| O sinal do encoder está incorreto | Verificar se o número de pulsos por revolução (PPR) do encoder está ajustado corretamente; verificar se o sinal do encoder sofre interferência, se o cabo do encoder passa independente no eletroduto, se o cabo é longo demais e se a malha (shield) está aterrada em uma só extremidade; verificar se o encoder está instalado de forma firme e se o eixo rotativo está ligado ao eixo do motor de forma firme, observando se o encoder está estável durante a marcha em velocidade normal; verificar se a ligação dos fios do encoder está correta. Para o motor assíncrono, executar SVC e comparar a corrente para julgar se o encoder funciona corretamente |
| A taxa de desaceleração é muito curta (texto original: "The deceleration rate is too short") | Reduzir a taxa de desaceleração |

- Notas do manual: nenhuma.

### Err04. Sobrecorrente em velocidade constante (Overcurrent at constant speed)
- Nível: 5A. Páginas do manual: 269.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A saída do circuito principal está aterrada ou em curto-circuito | Verificar se os cabos do motor e de aterramento estão ligados corretamente; verificar se o contator de curto do estator do motor síncrono causa curto-circuito no lado de saída do controlador; verificar se os cabos do motor têm a capa danificada |
| A autossintonia do motor foi feita de forma inadequada | Verificar se os parâmetros do motor estão de acordo com a placa de identificação; fazer a autossintonia do motor novamente |
| O sinal do encoder está incorreto | Verificar se o número de pulsos por revolução (PPR) do encoder está ajustado corretamente; verificar se o sinal do encoder sofre interferência, se o cabo do encoder passa independente no eletroduto, se o cabo é longo demais e se a malha (shield) está aterrada em uma só extremidade; verificar se o encoder está instalado de forma firme e se o eixo rotativo está ligado ao eixo do motor de forma firme, observando se o encoder está estável durante a marcha em velocidade normal; verificar se a ligação dos fios do encoder está correta. Para o motor assíncrono, executar SVC e comparar a corrente para julgar se o encoder funciona corretamente |

- Notas do manual: nenhuma.

### Err05. Sobretensão durante a aceleração (Overvoltage during acceleration)
- Nível: 5A. Páginas do manual: 270.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A tensão de entrada é muito alta | Verificar se a tensão de entrada é muito alta; observar se a tensão do barramento é muito alta (normal: 540 a 580 V para entrada de 380 V) |
| A resistência regenerativa é muito grande, ou a unidade de frenagem falha (texto original: "The regen. resistance is too large, or the braking unit fails") | Verificar o coeficiente de balanceamento; verificar se a tensão do barramento sobe rápido demais durante a marcha. Se sim, o resistor de frenagem não funciona ou seu modelo é inadequado: verificar se o cabo que liga o resistor de frenagem está danificado, se o fio de cobre toca o terra e se a ligação é firme; verificar se a resistência é adequada com base na recomendação do capítulo 4 e selecionar um resistor de frenagem adequado; se uma unidade de frenagem for usada, verificar se ela funciona corretamente e se o modelo é adequado. Se a resistência do resistor de frenagem for adequada e a sobretensão ocorrer toda vez que o elevador atinge a velocidade alvo, diminuir os valores de F2-01 ou F2-04 para reduzir o erro de seguimento da curva e evitar sobretensão por ultrapassagem (overshoot) do sistema |
| A taxa de aceleração é muito curta | Reduzir a taxa de aceleração |

- Notas do manual: nenhuma.

### Err06. Sobretensão durante a desaceleração (Overvoltage during deceleration)
- Nível: 5A. Páginas do manual: 270.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A tensão de entrada é muito alta | Verificar se a tensão de entrada é muito alta; observar se a tensão do barramento é muito alta (normal: 540 a 580 V para entrada de 380 V) |
| A resistência regenerativa é muito grande, ou a unidade de frenagem falha (texto original: "The regen resistance is too large, or the braking unit fails") | Verificar o coeficiente de balanceamento; verificar se a tensão do barramento sobe rápido demais durante a marcha. Se sim, o resistor de frenagem não funciona ou seu modelo é inadequado: verificar se o cabo que liga o resistor de frenagem está danificado, se o fio de cobre toca o terra e se a ligação é firme; verificar se a resistência é adequada com base na recomendação do capítulo 4 e selecionar um resistor de frenagem adequado; se uma unidade de frenagem for usada, verificar se ela funciona corretamente e se o modelo é adequado. Se a resistência do resistor de frenagem for adequada e a sobretensão ocorrer toda vez que o elevador atinge a velocidade alvo, diminuir os valores de F2-01 ou F2-04 para reduzir o erro de seguimento da curva e evitar sobretensão por ultrapassagem (overshoot) do sistema |
| A taxa de desaceleração é muito curta | Reduzir a taxa de desaceleração |

- Notas do manual: nenhuma.

### Err07. Sobretensão em velocidade constante (Overvoltage at constant speed)
- Nível: 5A. Páginas do manual: 271.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A tensão de entrada é muito alta | Verificar se a tensão de entrada é muito alta; observar se a tensão do barramento é muito alta (normal: 540 a 580 V para entrada de 380 V) |
| A resistência regenerativa é muito grande, ou a unidade de frenagem falha | Verificar o coeficiente de balanceamento; verificar se a tensão do barramento sobe rápido demais durante a marcha. Se sim, o resistor de frenagem não funciona ou seu modelo é inadequado: verificar se o cabo que liga o resistor de frenagem está danificado, se o fio de cobre toca o terra e se a ligação é firme; verificar se a resistência é adequada com base na recomendação do capítulo 4 e selecionar um resistor de frenagem adequado; se uma unidade de frenagem for usada, verificar se ela funciona corretamente e se o modelo é adequado. Se a resistência do resistor de frenagem for adequada e a sobretensão ocorrer toda vez que o elevador atinge a velocidade alvo, diminuir os valores de F2-01 ou F2-04 para reduzir o erro de seguimento da curva e evitar sobretensão por ultrapassagem (overshoot) do sistema |

- Notas do manual: nenhuma.

### Err08. Período de aviso de manutenção atingido (Maintenance notification period reached)
- Nível: 5A. Páginas do manual: 271.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| O elevador não foi mantido dentro do período de aviso | Desligar a alimentação e fazer a manutenção do elevador; desativar a função de aviso de manutenção ajustando F9-13 para 0; contatar o agente ou o fabricante |

- Notas do manual: nenhuma.

### Err09. Subtensão (Undervoltage)
- Nível: 5A. Páginas do manual: 271.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Ocorre falta de energia instantânea na alimentação de entrada | Verificar se a energia falha durante a marcha; verificar se a ligação de todos os cabos de entrada de alimentação está firme |
| A tensão de entrada é muito baixa | Verificar se a tensão da alimentação externa é muito baixa |
| A placa de controle do inversor falha | Contatar o agente ou o fabricante |


- Notas do manual: nenhuma.

### Err10. Sobrecarga do controlador (Controller overload)
- Nível: 5A. Páginas do manual: 272.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A resistência mecânica é muito grande | Verificar se o freio está liberado e se a alimentação do freio está normal; verificar se as sapatas de guia estão apertadas demais |
| O coeficiente de balanceamento está inadequado | Verificar se o coeficiente de balanceamento está correto |
| O sinal de realimentação do encoder está anormal | Verificar se o sinal de realimentação do encoder e o ajuste de parâmetros estão corretos, e se o ângulo inicial do encoder para o PMSM está correto |
| A autossintonia do motor não foi feita corretamente (neste caso, a corrente de marcha do elevador é maior que a normal) | Verificar o ajuste dos parâmetros do motor e fazer a autossintonia do motor novamente; se esta falha for reportada quando o experimento de escorregamento (slip) é realizado, fazer o experimento de escorregamento usando a função ajustada em F3-24 |
| A sequência de fases do motor está incorreta | Verificar se a sequência de fases UVW do motor está correta |
| O modelo do inversor (AC drive) é de classe de potência baixa demais | Verificar se a corrente excedeu a corrente nominal do inversor durante a marcha em velocidade estável do elevador com a cabina vazia |

- Notas do manual: nenhuma.

### Err11. Sobrecarga do motor (Motor overload)
- Nível: 5A. Páginas do manual: 272.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A resistência mecânica é muito grande | Verificar se o freio está liberado e se a alimentação do freio está normal; verificar se as sapatas de guia estão apertadas demais |
| O coeficiente de balanceamento está inadequado | Verificar se o coeficiente de balanceamento está correto |
| A autossintonia do motor não foi feita corretamente (neste caso, a corrente de marcha do elevador é maior que a normal) | Verificar o ajuste dos parâmetros do motor e fazer a autossintonia do motor novamente; se esta falha for reportada quando o experimento de escorregamento (slip) é realizado, fazer o experimento de escorregamento usando a função ajustada em F3-24 |
| A sequência de fases do motor está incorreta | Verificar se a sequência de fases UVW do motor está correta |
| O modelo do motor é de classe de potência baixa demais | Verificar se a corrente excedeu a corrente nominal do motor durante a marcha em velocidade estável do elevador com a cabina vazia |

- Notas do manual: nenhuma.

### Err12. Falta de fase na alimentação (Power supply phase loss)
- Nível: 5A. Páginas do manual: 272.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| As fases da entrada de alimentação não são simétricas | Verificar se alguma das três fases da alimentação foi perdida; verificar se as três fases da alimentação estão equilibradas; verificar se a tensão da alimentação está normal e, se não estiver, ajustar a alimentação |
| A placa de controle do inversor falha | Contatar o agente ou o fabricante |

- Notas do manual: nenhuma.

### Err13. Falta de fase na saída (Power output phase loss)
- Nível: 5A. Páginas do manual: 272.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A ligação de saída do circuito principal está solta | Verificar se a ligação do motor está firme; verificar se o contator RUN do lado da saída está normal |
| O motor está danificado | Verificar se o motor está anormal internamente |

- Notas do manual: nenhuma.

### Err14. Superaquecimento do módulo (Module overheat)
- Nível: 5A. Páginas do manual: 273.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A temperatura ambiente é muito alta | Reduzir a temperatura ambiente |
| O ventilador está danificado | Trocar o ventilador |
| O filtro de ar está bloqueado | Limpar o filtro de ar; verificar se a folga de instalação do controlador atende ao requisito |

- Notas do manual: nenhuma.

### Err15. Saída anormal (Output abnormal)
- Nível: 5A. Páginas do manual: 273.
- Subcódigos: 1: o resistor regenerativo está em curto-circuito; 2: o IGBT de frenagem está em curto-circuito.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 1: o resistor regenerativo está em curto-circuito | Verificar se a ligação do resistor regenerativo e da unidade de frenagem está correta, sem curto-circuito; verificar se o contator principal funciona corretamente e se há problema de arco ou de travamento (texto original: "arch or stuck problem") |
| Subcódigo 2: o IGBT de frenagem está em curto-circuito | Contatar o agente ou a Inovance |

- Notas do manual: nenhuma.

### Err16. Falha de controle de corrente (Current control fault)
- Nível: 5A. Páginas do manual: 273.
- Subcódigos: 1: o desvio da corrente de excitação é grande demais; 2: o desvio da corrente de torque é grande demais; 3: o desvio de velocidade é grande demais.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 1: o desvio da corrente de excitação é grande demais; Subcódigo 2: o desvio da corrente de torque é grande demais (as duas causas dividem o mesmo bloco de soluções, conforme o PDF) | Verificar se a tensão de entrada está baixa (frequente em alimentação provisória); verificar se a ligação do cabo entre o controlador e o motor está firme; verificar se o contator RUN funciona corretamente |
| Subcódigo 3: o desvio de velocidade é grande demais | Verificar o circuito do encoder; verificar se o número de pulsos por revolução (PPR) do encoder está ajustado corretamente; verificar se o sinal do encoder sofre interferência; verificar se o cabo do encoder passa independente no eletroduto, se o cabo é longo demais ou se a malha (shield) está aterrada em uma só extremidade; verificar se o encoder está instalado de forma firme, se o eixo rotativo está ligado ao eixo do motor de forma firme ou se o encoder está estável durante a marcha em velocidade normal; verificar se os parâmetros do motor estão corretos e fazer a autossintonia do motor novamente; aumentar o limite superior de torque em F2-08 |

- Notas do manual: nenhuma.

### Err17. Interferência no encoder durante a autossintonia do motor (Encoder interference during motor auto-tuning)
- Nível: 5A. Páginas do manual: 273.
- Subcódigos: 1: reservado; 2: o sinal do encoder SIN/COS está anormal; 3: o sinal do encoder UVW está anormal.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 1: reservado | Reservado |
| Subcódigo 2: o sinal do encoder SIN/COS está anormal | Existe interferência séria nos sinais C, D e Z do encoder SIN/COS; verificar se o cabo do encoder está passado separado dos cabos de potência e se o aterramento do sistema é confiável; verificar se a placa PG está ligada corretamente |
| Subcódigo 3: o sinal do encoder UVW está anormal | Existe interferência séria nos sinais U, V e W do encoder UVW; verificar se o cabo do encoder está passado separado dos cabos de potência e se o aterramento do sistema é confiável; verificar se a placa PG está ligada corretamente |

- Notas do manual: nenhuma.

### Err18. Falha de detecção de corrente (Current detection fault)
- Nível: 5A. Páginas do manual: 274.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A placa de controle do inversor falha | Contatar o agente ou o fabricante |

- Notas do manual: nenhuma.

### Err19. Falha de autossintonia do motor (Motor auto-tuning fault)
- Nível: 5A. Páginas do manual: 274.
- Subcódigos: 1: a autossintonia da resistência do estator falha; 5: a autossintonia da posição do polo magnético falha; 8: a autossintonia estática do motor síncrono foi selecionada, mas o tipo de encoder não é SIN/COS; 9: a flutuação do sinal CD é grande demais na autossintonia estática do motor síncrono; 12: o ângulo inicial do encoder não foi aprendido durante a autossintonia sem ângulo (angle-free) do motor síncrono, e por isso é emitido um alarme.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 1: a autossintonia da resistência do estator falha; Subcódigo 5: a autossintonia da posição do polo magnético falha | Verificar a ligação do motor |
| Subcódigo 8: a autossintonia estática do motor síncrono foi selecionada, mas o tipo de encoder não é SIN/COS | Selecionar outros modos de autossintonia ou mudar o tipo de encoder para encoder SIN/COS |
| Subcódigo 9: a flutuação do sinal CD é grande demais na autossintonia estática do motor síncrono | Existe interferência de hardware nos sinais CD do encoder SIN/COS; verificar se o aterramento está normal |
| Subcódigo 12: o ângulo inicial do encoder não foi aprendido durante a autossintonia sem ângulo do motor síncrono, e por isso é emitido um alarme | Na autossintonia sem ângulo semiautomática, o elevador só pode rodar em velocidade normal depois que o ângulo inicial do encoder for obtido no modo de inspeção |

- Notas do manual: nenhuma.

### Err20. Realimentação de velocidade incorreta (Speed feedback incorrect)
- Nível: 5A. Páginas do manual: 275.
- Subcódigos: 1: o sinal do encoder não é detectado durante a autossintonia sem carga do motor síncrono; 2 e 8: reservado; 3 e 15: ver as duas linhas abaixo (o manual traz duas linhas para "3, 15"); 4: o sinal Z não pode ser detectado durante a autossintonia do motor síncrono; 5: os cabos do encoder SIN/COS estão rompidos; 7: os cabos do encoder UVW estão rompidos; 9: o desvio de velocidade é grande demais; 12: os sinais AB do encoder são perdidos na partida; 13: os sinais AB do encoder são perdidos durante a marcha; 14: o sinal Z é perdido durante a marcha normal; 19: os sinais do encoder SIN/COS sofrem interferência séria durante a marcha; 55: os sinais do encoder SIN/COS sofrem interferência séria ou os sinais CD estão incorretos durante a autossintonia do motor.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 1: o sinal do encoder não é detectado durante a autossintonia sem carga do motor síncrono | Verificar se o circuito do sinal do encoder está normal; verificar se a placa PG está normal; verificar se o freio foi liberado |
| Subcódigos 4, 5, 7 e 14 (sinal Z não detectado na autossintonia do motor síncrono; cabos do encoder SIN/COS rompidos; cabos do encoder UVW rompidos; sinal Z perdido durante a marcha normal; as quatro causas dividem o mesmo bloco de soluções, conforme o PDF) | Verificar se o circuito do sinal do encoder está normal; verificar se a placa PG está normal |
| Subcódigos 2, 8: reservado | Reservado |
| Subcódigos 3, 15: a sequência dos cabos do motor está incorreta, o freio do motor não foi acionado, ou a qualidade do sinal do encoder é ruim (texto original: "the motor brake is not started") | Trocar a sequência dos cabos de quaisquer duas das fases U, V e W do motor; verificar se o freio é acionado durante a autossintonia com carga do motor síncrono (texto original: "Check whether the brake is started during synchronous motor with-load auto-tuning"); verificar o circuito do sinal do encoder |
| Subcódigos 3, 15: a sequência de fases do motor está incorreta (segunda linha para os mesmos subcódigos, como no manual) | Trocar quaisquer duas fases dos cabos UVW do motor; verificar se o freio é liberado durante a autossintonia com carga do motor síncrono |
| Subcódigo 9: o desvio de velocidade é grande demais | O ângulo do motor síncrono está anormal; fazer a autossintonia do motor novamente; reduzir o KP do laço de velocidade de travamento de posição (texto original: "position lock speed loop KP"); o ganho proporcional do laço de velocidade é excessivo ou o tempo integral é insuficiente: diminuir o ganho proporcional ou aumentar adequadamente o tempo integral; verificar a sequência de fases do motor |
| Subcódigo 12: os sinais AB do encoder são perdidos na partida | Verificar se o freio foi liberado; verificar se os cabos de sinal AB do encoder estão rompidos; se o motor não puder ser partido no experimento de escorregamento (slip), fazer o experimento de escorregamento usando a função ajustada em F3-24 |
| Subcódigo 13: os sinais AB do encoder são perdidos durante a marcha | Os sinais AB do encoder são perdidos de repente; verificar se a ligação do encoder está correta, se existe interferência forte ou se o motor ficou travado por falta repentina de alimentação do freio durante a marcha |
| Subcódigo 19: os sinais do encoder SIN/COS sofrem interferência séria durante a marcha | Os sinais analógicos do encoder sofrem interferência séria durante a marcha do motor, ou os sinais do encoder estão com mau contato; é preciso verificar o circuito do encoder |
| Subcódigo 55: os sinais do encoder SIN/COS sofrem interferência séria ou os sinais CD estão incorretos durante a autossintonia do motor | Os sinais analógicos do encoder sofrem interferência séria durante a autossintonia do motor, ou os sinais CD do encoder estão em sequência errada |

Trecho com duas linhas para "3, 15": o PDF mostra mesmo duas linhas com os subcódigos 3 e 15 (pág. 275), com causas e soluções diferentes; mantidas como no manual.

- Notas do manual: nenhuma.

### Err21. Parâmetros ajustados incorretamente (Parameters are incorrectly set)
- Nível: 5A. Páginas do manual: 276.
- Subcódigos: 2: o valor ajustado da frequência máxima é menor que a frequência nominal do motor; 3: o tipo de encoder está ajustado incorretamente.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 2: o valor ajustado da frequência máxima é menor que a frequência nominal do motor | Aumentar o valor de F0-06 para que seja maior que a frequência nominal do motor |
| Subcódigo 3: o tipo de encoder está ajustado incorretamente | O encoder SIN/COS, absoluto ou ABZ está ajustado incorretamente como encoder UVW; testar se o valor ajustado de F1-00 corresponde ao encoder |

- Notas do manual: nenhuma.

### Err22. Sinal de nivelamento anormal (Leveling signal abnormal)
- Nível: 1A. Páginas do manual: 276.
- Subcódigos: 101: o sinal de nivelamento está travado (stuck); 102: o sinal de nivelamento está perdido; 103: o desvio da posição de nivelamento é grande demais no estado de marcha automática do elevador.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de nivelamento está travado; Subcódigo 102: o sinal de nivelamento está perdido (as duas causas dividem o mesmo bloco de soluções, conforme o PDF) | Verificar se os interruptores de nivelamento e de zona de porta funcionam corretamente; verificar a verticalidade e a profundidade de instalação das placas de nivelamento; verificar os pontos de entrada do sinal de nivelamento da MCB |
| Subcódigo 103: o desvio da posição de nivelamento é grande demais no estado de marcha automática do elevador | Verificar se o cabo de aço (steel rope) escorrega |

- Notas do manual: nenhuma.

### Err23. Curto-circuito (Short circuit)
- Nível: 5A. Páginas do manual: 276.
- Subcódigos: 1, 2, 3: existe curto-circuito para o terra; 4: existe curto-circuito entre fases.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 1, 2, 3: existe curto-circuito para o terra | Verificar se a saída trifásica do inversor (AC drive) está em curto-circuito para o terra |
| Subcódigo 4: existe curto-circuito entre fases | Verificar se a saída trifásica do inversor (AC drive) está em curto-circuito entre fases ou para o terra |

- Notas do manual: nenhuma.

### Err24. Falha do relógio RTC (RTC clock fault)
- Nível: 3B. Páginas do manual: 276.
- Subcódigos: 101: a informação do relógio RTC da MCB está anormal.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a informação do relógio RTC da MCB está anormal | Trocar a bateria do relógio; trocar a MCB |

- Notas do manual: nenhuma.

### Err25. Dados armazenados anormais (Storage data abnormal)
- Nível: 4A. Páginas do manual: 276.
- Subcódigos: 101, 102, 103: os dados armazenados da MCB estão anormais.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 101, 102, 103: os dados armazenados da MCB estão anormais | Contatar o agente ou o fabricante |

- Notas do manual: nenhuma.

### Err26. Sinal de terremoto (Earthquake signal)
- Nível: 3B. Páginas do manual: 276.
- Subcódigos: 101: o sinal de terremoto está ativo e a duração excede 2 s.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de terremoto está ativo e a duração excede 2 s | Subcódigo 101: verificar se o sinal de terremoto é coerente com o ajuste de parâmetro (NC, NO) da MCB |

- Notas do manual: nenhuma.

### Err27. Falha do controlador especial (Fault of special controller)
- Nível: "-" (sem nível na tabela). Páginas do manual: 276.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado | Contatar o agente ou a Inovance |

- Notas do manual: nenhuma.

### Err28. Falha de manutenção (Maintenance fault)
- Nível: "-" (sem nível na tabela). Páginas do manual: 276.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado | Contatar o agente ou a Inovance |

- Notas do manual: nenhuma.

### Err29. Realimentação anormal do contator de curto do estator do motor síncrono (Shorting motor stator contactor feedback abnormal)
- Nível: 5A. Páginas do manual: 276.
- Subcódigos: 101: a realimentação do contator de curto do estator do motor da MCB está anormal; 102: a realimentação do contator de curto do estator do motor síncrono (texto original: "shorting PMSM stator contactor") da placa de expansão de E/S (IO expansion board) está anormal.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a realimentação do contator de curto do estator do motor da MCB está anormal; Subcódigo 102: a realimentação do contator de curto do estator do motor síncrono da placa de expansão de E/S está anormal (as duas causas dividem o mesmo bloco de soluções, conforme o PDF) | Verificar se a característica do sinal (NO, NC) do contato de realimentação do contator está correta; verificar se o contator e o contato de realimentação correspondente atuam corretamente; verificar o circuito da bobina do contator de curto do estator do motor |

- Notas do manual: nenhuma.

### Err30. Posição do elevador anormal (Elevator position abnormal)
- Nível: 4A. Páginas do manual: 276.
- Subcódigos: 101, 102: no modo de marcha em velocidade normal ou de remarcha de renivelamento (re-leveling), o tempo de marcha é maior que o valor de F9-02, mas o sinal de nivelamento não tem mudança.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 101, 102: no modo de marcha em velocidade normal ou de renivelamento, o tempo de marcha é maior que o valor de F9-02, mas o sinal de nivelamento não tem mudança | Verificar se os cabos do sinal de nivelamento estão ligados de forma firme e se os fios de cobre do sinal podem tocar o terra ou entrar em curto-circuito com outros cabos de sinal; verificar se a distância entre dois andares é grande demais ou se o tempo de renivelamento ajustado em F3-21 é curto demais, causando tempo de marcha de renivelamento longo demais |

- Notas do manual: nenhuma.

### Err31. Reservado (Reserved)
- Nível: "-" (sem nível na tabela). Páginas do manual: 276.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado | Reservado |

- Notas do manual: nenhuma.

### Err32. Reservado (Reserved)
- Nível: "-" (sem nível na tabela). Páginas do manual: 277.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado | Reservado |

- Notas do manual: nenhuma.

### Err33. Velocidade do elevador anormal (Elevator speed abnormal)
- Nível: 5A. Páginas do manual: 277.
- Subcódigos: 101: a velocidade de marcha detectada na marcha em velocidade normal excede o limite; 102: a velocidade excede o limite durante a inspeção ou a autossintonia do poço (texto original: "shaft autotuning"); 103: a velocidade excede o limite no modo de frenagem por curto do estator (texto original: "shorting stator braking mode"); 104, 105: a velocidade excede o limite durante a marcha de emergência; 106: o desvio de medição de velocidade da MCB é grande demais.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a velocidade de marcha detectada na marcha em velocidade normal excede o limite | Verificar se o ajuste de parâmetros e a ligação do encoder estão corretos; verificar o ajuste dos parâmetros de placa do motor e fazer a autossintonia do motor novamente |
| Subcódigo 102: a velocidade excede o limite durante a inspeção ou a autossintonia do poço | Tentar diminuir a velocidade de inspeção ou fazer a autossintonia do motor novamente |
| Subcódigo 103: a velocidade excede o limite no modo de frenagem por curto do estator | Verificar se a função de curto do estator do motor está habilitada; verificar se a sequência de fases UVW do motor está correta |
| Subcódigos 104, 105: a velocidade excede o limite durante a marcha de emergência | Verificar se a capacidade da alimentação de emergência atende aos requisitos; verificar se a velocidade de marcha de emergência está ajustada de forma adequada |
| Subcódigo 106: o desvio de medição de velocidade da MCB é grande demais | Verificar a ligação do encoder; verificar se a qualidade da comunicação SPI entre a MCB e o inversor (AC drive) é excelente |

- Notas do manual: nenhuma.

### Err34. Falha de lógica (Logic fault)
- Nível: 5A. Páginas do manual: 277.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| A lógica da MCB está anormal | Contatar o agente ou a Inovance para trocar a MCB |

- Notas do manual: nenhuma.
