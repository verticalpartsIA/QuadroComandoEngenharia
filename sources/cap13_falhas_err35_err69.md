# Capítulo 13 (fonte): Falhas Err35 a Err69 do NICE3000new

Fonte: Manual_Usuario_Controlador_NICE3000new_Completo.pdf, seção "7.4 Fault Information and Troubleshooting". Páginas citadas são páginas do PDF (a página impressa é a do PDF menos 1). Atribuição de causa a solução conferida contra a renderização das páginas 278, 280, 281, 283, 285, 286, 287 e 288; as demais seguem a ordem do texto extraído.

Cobertura do escopo: Err35 a Err69 e qualquer código acima de Err69.

- Presentes com conteúdo: Err35, Err36, Err37, Err38, Err39, Err41, Err42, Err43, Err44, Err45, Err46, Err47, Err48, Err49, Err50, Err51, Err52, Err53, Err54, Err55, Err56, Err57, Err58, Err62, Err64, Err65, Err66, Err67, Err69 (29 códigos).
- Presentes como "Reserved" (reservado): Err40, Err59, Err60, Err61 (4 códigos).
- Não constam na tabela: Err63, Err68. Nenhum código acima de Err69 consta na tabela (por exemplo, Err88 não consta).
- Total de entradas estruturadas: 33.

Colunas da tabela do manual: Fault Code (código da falha), Name (nome), Possible Causes (causas possíveis), Solution (solução), Level (nível).

Formatos de código: o manual escreve "Err57" no título da tabela, mas na nota final escreve "E57" ("If faults Err51, Err52, and E57 persist..."). Na solução do Err69 também aparece "E69" ("If the E69 subcode 21 reoccurs"). Além disso, em outros capítulos o manual usa "E35, E41, E42, E51, E52, E58" (fora do escopo da tabela). Os códigos são reproduzidos aqui como o manual os escreve em cada trecho.

---

### Err35. Dados de autoaprendizado do poço anormais (Shaft auto-tuning data abnormal)
- Nível: 4C. Páginas do manual: 278.
- Subcódigos: 101: ao iniciar o autoaprendizado do poço, o elevador não está no andar inferior ou a chave de redução de velocidade de descida é inválida; 102: o sistema não está no estado de inspeção (chave de inspeção não ligada); 103: na energização, julga-se que o autoaprendizado do poço não foi feito; 104, 113, 114: no modo de controle por distância, na partida da corrida, julga-se que o autoaprendizado do poço não foi feito; 105: o sentido de corrida do elevador e a variação dos pulsos são inconsistentes; 106, 107, 109: o comprimento de pulso da placa detectado no nivelamento de subida/descida é anormal; 108, 110: nenhum sinal de nivelamento é recebido em 45 s de corrida contínua; 111, 115: a altura de andar armazenada é menor que 50 cm; 112: o andar em que o autoaprendizado termina não é o andar superior; 116: os sinais de nivelamento de subida e de descida estão em sequência errada.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: ao iniciar o autoaprendizado do poço, o elevador não está no andar inferior ou a chave de redução de velocidade de descida é inválida. | Verificar se a chave de redução de velocidade de descida é válida e se F4-01 (Current floor, andar atual) está ajustado para o número do andar inferior. |
| Subcódigo 102: o sistema não está no estado de inspeção (chave de inspeção não ligada). | O manual traz apenas o texto "when shaft auto-tuning is performed." (ambíguo, ver o original na pág. 278: a frase está truncada e parece continuar a causa; não traz ação). |
| Subcódigo 103: julga-se na energização que o autoaprendizado do poço não foi feito. | Fazer o autoaprendizado do poço novamente. |
| Subcódigos 104, 113, 114: no modo de controle por distância, julga-se na partida da corrida que o autoaprendizado do poço não foi feito. | Fazer o autoaprendizado do poço novamente. |
| Subcódigo 105: o sentido de corrida do elevador e a variação dos pulsos são inconsistentes. | Verificar se o sentido de corrida do elevador é consistente com a variação dos pulsos em F4-03: F4-03 aumenta no sentido de subida e diminui no sentido de descida. |
| Subcódigos 106, 107, 109: o comprimento de pulso da placa detectado no nivelamento de subida/descida é anormal. | Verificar se o estado NO/NC da chave de nivelamento está ajustado corretamente; verificar se as placas de nivelamento estão inseridas corretamente e se há forte interferência de potência caso o sinal da chave de nivelamento pisque. |
| Subcódigos 108, 110: nenhum sinal de nivelamento é recebido em 45 s de corrida contínua. | Verificar se a fiação da chave de nivelamento está correta; verificar se a distância entre andares é grande demais, causando estouro de tempo de corrida. Aumentar a velocidade ajustada em F3-11 e refazer o autoaprendizado do poço, para garantir que o aprendizado dos andares possa ser concluído em 45 s. |
| Subcódigos 111, 115: a altura de andar armazenada é menor que 50 cm. | Habilitar a função de andar super curto se a distância entre andares for menor que 50 cm. Se a distância entre andares for normal, verificar a instalação da placa de nivelamento desse andar e verificar a chave e sua fiação. |
| Subcódigo 112: o andar em que o autoaprendizado termina não é o andar superior. | F6-00 (Top floor of the elevator, andar superior do elevador) está ajustado incorretamente ou falta a placa de nivelamento. |
| Subcódigo 116: os sinais de nivelamento de subida e de descida estão em sequência errada. | Verificar se a fiação de nivelamento de subida e de descida está correta; verificar se os intervalos (gaps) de nivelamento de subida e de descida são adequados. |

- Notas do manual: nenhuma específica. (Ver o Err35 citado em outros capítulos fora da tabela; não faz parte do escopo.)

### Err36. Realimentação do contator de marcha anormal (RUN contactor feedback abnormal)
- Nível: 5A. Páginas do manual: 279.
- Subcódigos: 101: a realimentação do contator de marcha (RUN) está ativa, mas o contator não tem saída; 102: o controlador emite o sinal RUN mas não recebe realimentação de RUN; 103: a corrente do motor assíncrono do trecho de aceleração ao trecho de velocidade constante é muito pequena (≤ 0,1 A); 104: com as duas realimentações do contator de marcha habilitadas, seus estados são inconsistentes; 105: a realimentação do contator de marcha está ativa antes de o renivelamento ser habilitado.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a realimentação do contator de marcha está ativa, mas o contator não tem saída. | Verificar se o contato de realimentação do contator atua corretamente; verificar a característica do sinal (NO, NC) do contato de realimentação. |
| Subcódigo 102: o controlador emite o sinal RUN mas não recebe realimentação de RUN. | Mesma ação do subcódigo 101 (o manual agrupa 101, 102, 104 e 105 sob as mesmas ações). |
| Subcódigo 104: com as duas realimentações do contator de marcha habilitadas, seus estados são inconsistentes. | Mesma ação do subcódigo 101. |
| Subcódigo 105: a realimentação do contator de marcha está ativa antes de o renivelamento ser habilitado. | Mesma ação do subcódigo 101. |
| Subcódigo 103: a corrente do motor assíncrono do trecho de aceleração ao trecho de velocidade constante é muito pequena (≤ 0,1 A). | Verificar se os cabos de saída UVW do controlador estão conectados corretamente; verificar se o circuito de comando da bobina do contator de marcha (RUN) está normal. |

- Notas do manual: nenhuma.

### Err37. Realimentação do contator de freio anormal (Brake contactor feedback abnormal)
- Nível: 5A. Páginas do manual: 280.
- Subcódigos: 101: a saída do contator de freio é inconsistente com a realimentação; 102: com as duas realimentações do contator de freio habilitadas, seus estados são inconsistentes; 103: a saída do contator de freio é inconsistente com a realimentação da chave de curso do freio 1; 104: com as duas realimentações da chave de curso do freio 1 habilitadas, seus estados são inconsistentes; 105: a realimentação do contator de freio é válida antes de o contator de freio abrir; 106: a saída do contator de freio é inconsistente com a realimentação da chave de curso do freio 2; 107: com as duas realimentações da chave de curso do freio 2 habilitadas, seus estados são inconsistentes; 108: a saída do contator de freio é inconsistente com a realimentação da chave de curso do freio 1 na placa de expansão de E/S (IO expansion board); 109: idem, com a chave de curso do freio 2 na placa de expansão de E/S.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a saída do contator de freio é inconsistente com a realimentação. | Verificar se o contator de freio abre e fecha corretamente; verificar se a característica do sinal (NO, NC) do contato de realimentação do contator de freio está ajustada corretamente; verificar se o circuito de realimentação do contator de freio está normal. |
| Subcódigo 102: com as duas realimentações do contator de freio habilitadas, seus estados são inconsistentes. | Verificar a característica do sinal (NO, NC) do contato de realimentação do contator de freio, se está ajustada corretamente; verificar se os estados dos contatos de realimentação de múltiplas vias são consistentes (o manual marca este segundo item com "b."). |
| Subcódigos 103 e 106: a saída do contator de freio é inconsistente com a realimentação da chave de curso do freio 1 (103) ou 2 (106). | Verificar se a característica do sinal (NO, NC) da realimentação da chave de curso do freio 1/2 está ajustada corretamente; verificar se o circuito da realimentação da chave de curso do freio 1/2 está normal (marcado "b." no manual). |
| Subcódigo 105: a realimentação do contator de freio é válida antes de o contator de freio abrir. | Verificar se o contato de realimentação do contator de freio apresenta mau funcionamento ("mal-functions"). |
| Subcódigos 104 e 107: com as duas realimentações da chave de curso do freio 1 (104) ou 2 (107) habilitadas, seus estados são inconsistentes. | Verificar se a característica do sinal (NO, NC) da realimentação da chave de curso do freio 1/2 está ajustada corretamente; verificar se os estados dos contatos de realimentação de múltiplas vias são consistentes (marcado "b." no manual). Observação: o texto do subcódigo 104 diz "brake travel switch 1" e o do 107 diz "brake travel switch 2", ambos com "feedback signal" no singular, como no original. |
| Subcódigos 108 e 109: a saída do contator de freio é inconsistente com a realimentação da chave de curso do freio 1 (108) ou 2 (109) na placa de expansão de E/S. | Verificar se a característica do sinal (NO, NC) da realimentação da chave de curso do freio 1/2 na placa de expansão de E/S está ajustada corretamente; verificar se o circuito da realimentação da chave de curso do freio 1/2 está normal (marcado "b." no manual). |

- Notas do manual: nenhuma. O manual numera alguns itens de solução com "b." sem existir um item "a.".

### Err38. Sinal do encoder anormal (Encoder signal abnormal)
- Nível: 5A. Páginas do manual: 281.
- Subcódigos: 101: os pulsos em F4-03 não mudam dentro do limite de tempo em F1-13; 102: F4-03 aumenta no sentido de descida; 103: F4-03 diminui no sentido de subida; 104: o SVC é usado no modo de controle por distância; 105: a chave limite de descida atua no sentido de subida enquanto a chave de redução de velocidade de descida 1 está ativa; 106: a chave limite de subida atua no sentido de descida enquanto a chave de redução de velocidade de subida 1 está ativa.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: os pulsos em F4-03 não mudam dentro do limite de tempo em F1-13. | Verificar se o encoder é usado corretamente; verificar se o freio funciona corretamente. |
| Subcódigo 102: F4-03 aumenta no sentido de descida. | Verificar se o ajuste de parâmetros e a fiação do encoder estão corretos; verificar se o aterramento do sistema e o aterramento de sinal estão firmes; verificar a sequência de fases do motor. |
| Subcódigo 103: F4-03 diminui no sentido de subida. | Mesmas ações do subcódigo 102. |
| Subcódigo 104: o SVC é usado no modo de controle por distância. | Ajustar F0-00 (Control mode) para 1 (Closed-loop vector control) no modo de controle por distância. |
| Subcódigos 105 e 106: a chave limite de descida atua no sentido de subida com a redução de velocidade de descida 1 ativa (105); a chave limite de subida atua no sentido de descida com a redução de velocidade de subida 1 ativa (106). | Verificar se a fiação das chaves limite de subida e de descida está normal. |

- Notas do manual: nenhuma.

### Err39. Superaquecimento do motor (Motor overheat)
- Nível: 3A. Páginas do manual: 281.
- Subcódigos: 101: a entrada do relé de superaquecimento do motor permanece válida por um certo tempo.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a entrada do relé de superaquecimento do motor permanece válida por um certo tempo. | Verificar se o ajuste de parâmetro (NO, NC) está correto; verificar se a base (socket) do relé de proteção térmica está normal; verificar se o motor é usado corretamente e se está danificado; melhorar as condições de resfriamento do motor. |

- Notas do manual: nenhuma na tabela. Em outro capítulo (fora da tabela de falhas) o manual diz que, com o sinal de superaquecimento ativo por 2 s, o controlador interrompe a saída e reporta Err39, e que quando o sinal fica inativo o Err39 é reiniciado automaticamente e o sistema volta a operar (texto parcial, ver o original na linha do capítulo correspondente; não faz parte da tabela).

### Err40. Reservado (Reserved)
- Nível: 4B. Páginas do manual: 281.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado (Reserved) | Contatar o agente ou a Inovance. |

- Notas do manual: nenhuma.

### Err41. Circuito de segurança desligado (Safety circuit disconnected)
- Nível: 5A. Páginas do manual: 281.
- Subcódigos: 101: o sinal do circuito de segurança passa a OFF.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal do circuito de segurança passa a OFF. | Verificar as chaves do circuito de segurança e seus estados; verificar se a alimentação externa está normal; verificar se o contator do circuito de segurança atua corretamente; confirmar a característica do sinal (NO, NC) do contato de realimentação do contator do circuito de segurança. |

- Notas do manual: "Fault Err41 is not recorded in the elevator stop state." (A falha Err41 não é registrada no estado de parada do elevador.)

### Err42. Fechadura de porta desligada durante a corrida (Door lock disconnected during running)
- Nível: 5A. Páginas do manual: 281.
- Subcódigos: 101, 102: a realimentação do circuito de fechaduras de porta é inválida durante a corrida do elevador.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 101, 102: a realimentação do circuito de fechaduras de porta é inválida durante a corrida do elevador. | Verificar se a fechadura da porta de pavimento e a fechadura da porta de cabina estão em bom contato; verificar se o contator de fechaduras de porta atua corretamente; verificar a característica do sinal (NO, NC) do contato de realimentação do contator de fechaduras de porta; verificar se a alimentação externa está normal. |

- Notas do manual: "Fault Err42 is reset automatically when the door lock circuit is shorted or 1s after the fault occurs in the door zone." (A falha Err42 é reiniciada automaticamente quando o circuito de fechaduras de porta é curto-circuitado ("shorted") ou 1 s depois de a falha ocorrer na zona de porta.)

### Err43. Sinal do limite de subida anormal (Up limit signal abnormal)
- Nível: 4A. Páginas do manual: 282.
- Subcódigos: 101: a chave limite de subida atua quando o elevador corre no sentido de subida.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a chave limite de subida atua quando o elevador corre no sentido de subida. | Verificar a característica do sinal (NO, NC) da chave limite de subida; verificar se a chave limite de subida está em bom contato; verificar se a chave limite está instalada em posição relativamente baixa e atua mesmo quando o elevador chega normalmente ao andar terminal. |

- Notas do manual: nenhuma.

### Err44. Sinal do limite de descida anormal (Down limit signal abnormal)
- Nível: 4A. Páginas do manual: 282.
- Subcódigos: 101: a chave limite de descida atua quando o elevador corre no sentido de descida.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a chave limite de descida atua quando o elevador corre no sentido de descida. | Verificar a característica do sinal (NO, NC) da chave limite de descida; verificar se a chave limite de descida está em bom contato; verificar se a chave limite está instalada em posição relativamente alta e, por isso, atua mesmo quando o elevador chega normalmente ao andar terminal. |

- Notas do manual: nenhuma.

### Err45. Chave de redução de velocidade anormal (Slow-down switch abnormal)
- Nível: 4B. Páginas do manual: 282.
- Subcódigos: 101: a distância de redução de velocidade de descida é insuficiente durante o autoaprendizado do poço; 102: a distância de redução de velocidade de subida é insuficiente durante o autoaprendizado do poço; 103: a chave de redução de velocidade está presa ou anormal durante a corrida normal; 106: as chaves de redução de velocidade 2 de subida e de descida atuam de forma inadequada durante o autoaprendizado do poço; 107: as chaves de redução de velocidade 3 de subida e de descida atuam de forma inadequada durante o autoaprendizado do poço.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 101, 102, 103: distância de redução de velocidade de descida (101) ou de subida (102) insuficiente no autoaprendizado do poço; chave de redução de velocidade presa ou anormal na corrida normal (103). | Verificar se as chaves de redução de velocidade de subida e de descida estão em bom contato; verificar a característica do sinal (NO, NC) das chaves de redução de velocidade de subida e de descida; garantir que a distância de redução de velocidade obtida satisfaça a exigência de redução de velocidade para a velocidade do elevador. |
| Subcódigo 106: as chaves de redução de velocidade 2 de subida e de descida atuam de forma inadequada durante o autoaprendizado do poço. | Verificar se o sinal das chaves de redução de velocidade 2 de subida e de descida está em sequência errada; verificar a característica do sinal (NO, NC) dessas chaves. |
| Subcódigo 107: as chaves de redução de velocidade 3 de subida e de descida atuam de forma inadequada durante o autoaprendizado do poço. | Verificar se o sinal das chaves de redução de velocidade 3 de subida e de descida está em sequência errada; verificar a característica do sinal (NO, NC) dessas chaves. |

- Notas do manual: nenhuma.

### Err46. Renivelamento anormal (Re-leveling abnormal)
- Nível: 2B. Páginas do manual: 282.
- Subcódigos: 101: o sinal de nivelamento está inativo durante o renivelamento; 102: a velocidade de corrida do renivelamento excede 0,1 m/s.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de nivelamento está inativo durante o renivelamento. | Verificar se o sinal de nivelamento está normal. |
| Subcódigo 102: a velocidade de corrida do renivelamento excede 0,1 m/s. | Verificar se o encoder é usado corretamente. |

- Notas do manual: nenhuma.

### Err47. Contator de curto do circuito de fechaduras de porta anormal (Shorting door lock circuit contactor abnormal)
- Nível: 2B. Páginas do manual: 283.
- Subcódigos: 101: o contator de curto do circuito de fechaduras de porta tem saída por 2 s contínuos, mas a realimentação é inválida e a fechadura de porta está desconectada; 102: o contator não tem saída, mas a realimentação é válida por 2 s contínuos; 103: durante o renivelamento ou a corrida de pré-abertura, o tempo de saída do contator é maior que 15 s; 106: a realimentação da fechadura de porta é detectada como válida antes do renivelamento.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o contator de curto do circuito de fechaduras de porta tem saída por 2 s contínuos, mas a realimentação é inválida e a fechadura de porta está desconectada. | Verificar a característica do sinal (NO, NC) do contato de realimentação do contator de curto do circuito de fechaduras de porta; verificar se esse contator atua corretamente. |
| Subcódigo 102: o contator não tem saída, mas a realimentação é válida por 2 s contínuos. | Mesmas ações do subcódigo 101. |
| Subcódigo 106: a realimentação da fechadura de porta é detectada como válida antes do renivelamento. | Mesmas ações do subcódigo 101. |
| Subcódigo 103: durante o renivelamento ou a corrida de pré-abertura (pre-open running), o tempo de saída do contator de curto do circuito de fechaduras de porta é maior que 15 s. | Verificar se os sinais de nivelamento e de renivelamento estão normais; verificar se a velocidade de renivelamento está ajustada baixa demais. |

- Notas do manual: nenhuma.

### Err48. Falha de abertura de porta (Door open fault)
- Nível: 5A. Páginas do manual: 283.
- Subcódigos: 101: o número de vezes consecutivas em que a porta não abre até o limite atinge o valor ajustado em Fb-09.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o número de vezes consecutivas em que a porta não abre até o limite atinge o valor ajustado em Fb-09. | Verificar se o sistema do operador de porta funciona corretamente; verificar se a saída da CTB está normal; verificar se o sinal de limite de abertura de porta e o sinal de fechadura de porta estão normais. |

- Notas do manual: nenhuma.

### Err49. Falha de fechamento de porta (Door close fault)
- Nível: 5A. Páginas do manual: 283.
- Subcódigos: 101: o número de vezes consecutivas em que a porta não fecha até o limite atinge o valor ajustado em Fb-09.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o número de vezes consecutivas em que a porta não fecha até o limite atinge o valor ajustado em Fb-09. | Verificar se o sistema do operador de porta funciona corretamente; verificar se a saída da CTB está normal; verificar se o sinal de limite de fechamento de porta e o sinal de fechadura de porta estão normais. |

- Notas do manual: nenhuma.

### Err50. Perda consecutiva do sinal de nivelamento (Consecutive loss of leveling signal)
- Nível: 5A. Páginas do manual: 283.
- Subcódigos: 101: sinal de nivelamento travado (stuck) detectado três vezes consecutivas; 102: perda do sinal de nivelamento detectada três vezes consecutivas.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: sinal de nivelamento travado detectado três vezes consecutivas. | Verificar se as chaves de nivelamento e de zona de porta funcionam corretamente; verificar a verticalidade e a profundidade de instalação das placas de nivelamento; verificar os pontos de entrada do sinal de nivelamento da MCB; verificar se o cabo de aço (steel rope) escorrega. |
| Subcódigo 102: perda do sinal de nivelamento detectada três vezes consecutivas. | Mesmas ações do subcódigo 101. |

- Notas do manual: nenhuma.

### Err51. Falha de comunicação CAN (CAN communication fault)
- Nível: 1A. Páginas do manual: 283.
- Subcódigos: 101: os dados de realimentação da comunicação CANbus com a CTB permanecem incorretos.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: os dados de realimentação da comunicação CANbus com a CTB permanecem incorretos. | O primeiro item de solução está em branco no manual: aparece apenas um marcador seguido de um ponto, "◆ ." (ambíguo, ver o original na pág. 283); verificar a alimentação da CTB; verificar se a alimentação de 24 V do controlador está normal; verificar se há interferência de forte potência na comunicação. |

- Notas do manual: "If faults Err51, Err52, and E57 persist, they are recorded once every one hour." (Se as falhas Err51, Err52 e E57 persistirem, elas são registradas uma vez a cada hora.) Ver também a nota em Err52 e Err57.

### Err52. Comunicação com a HCB anormal (HCB communication abnormal)
- Nível: 1A. Páginas do manual: 283.
- Subcódigos: 101: os dados de realimentação da comunicação Modbus com a HCB permanecem incorretos.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: os dados de realimentação da comunicação Modbus com a HCB permanecem incorretos. | Verificar a conexão do cabo de comunicação; verificar se a alimentação de 24 V do controlador está normal; verificar se os endereços das HCB estão repetidos; verificar se há interferência de forte potência na comunicação. |

- Notas do manual: "If faults Err51, Err52, and E57 persist, they are recorded once every one hour." (mesma nota do Err51.)

### Err53. Falha de fechadura de porta (Door lock fault)
- Nível: 5A. Páginas do manual: 284.
- Subcódigos: 101: o sinal de realimentação da fechadura de porta permanece ativo 3 s após a saída de abertura de porta, com o curto do circuito de fechaduras de porta desabilitado; 102: os estados dos contatos de realimentação de múltiplas vias da fechadura de porta são inconsistentes 3 s após a saída de abertura de porta; 104: os sinais de fechadura de porta de tensão mais alta e de tensão baixa são inconsistentes; 105: o sinal de curto da fechadura de porta 1 permanece ativo 3 s após a saída de abertura de porta, com o curto do circuito de fechaduras de porta habilitado; 106: idem, para o sinal de curto da fechadura de porta 2; 107: o parâmetro de entrada de curto das fechaduras de porta está selecionado, mas o sinal de realimentação está continuamente desconectado ou não está conectado.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de realimentação da fechadura de porta permanece ativo 3 s após a saída de abertura de porta, com o curto do circuito de fechaduras de porta desabilitado. | Verificar se o circuito de fechaduras de porta está em curto-circuito; verificar se o contato de realimentação do contator de fechaduras de porta atua corretamente. |
| Subcódigo 102: os estados dos contatos de realimentação de múltiplas vias da fechadura de porta são inconsistentes 3 s após a saída de abertura de porta. | Mesmas ações do subcódigo 101. |
| Subcódigo 105: o sinal de curto da fechadura de porta 1 permanece ativo 3 s após a saída de abertura de porta, com o curto do circuito de fechaduras de porta habilitado. | Mesmas ações do subcódigo 101. |
| Subcódigo 106: o sinal de curto da fechadura de porta 2 permanece ativo 3 s após a saída de abertura de porta, com o curto do circuito de fechaduras de porta habilitado. | Mesmas ações do subcódigo 101. |
| Subcódigo 104: os sinais de fechadura de porta de tensão mais alta e de tensão baixa são inconsistentes. | Verificar se os sinais de fechadura de porta de tensão mais alta e de tensão baixa são inconsistentes. Se o tempo em que a MCB recebe os dois sinais tem desvio acima de 1,5 s, esta falha é reportada. Este subcódigo é reiniciado ao desligar e ligar novamente a energia. |
| Subcódigo 107: o parâmetro de entrada de curto das fechaduras de porta está selecionado, mas o sinal de realimentação está continuamente desconectado ou não está conectado. | Verificar se o cabo do sinal de realimentação de curto da fechadura de porta não está conectado ou está rompido. |

- Notas do manual: nenhuma na tabela.

### Err54. Sobrecorrente na partida em inspeção (Overcurrent at inspection startup)
- Nível: 5A. Páginas do manual: 284.
- Subcódigos: 102: a corrente na partida em inspeção excede 120% da corrente nominal. (O manual não lista subcódigo 101 para este código.)

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 102: a corrente na partida em inspeção excede 120% da corrente nominal. | Reduzir a carga; verificar a sequência de fases do motor; mudar o Bit1 de FC-00 para 1 para cancelar a função de detecção de corrente de partida. |

- Notas do manual: nenhuma.

### Err55. Parada em outro andar (Stop at another landing floor)
- Nível: 1A. Páginas do manual: 284.
- Subcódigos: 101: durante a corrida automática do elevador, o limite de abertura de porta não é recebido dentro do limite de tempo em Fb-06.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: durante a corrida automática do elevador, o limite de abertura de porta não é recebido dentro do limite de tempo em Fb-06. | Verificar o sinal de limite de abertura de porta no andar atual. |

- Notas do manual: nenhuma na tabela. Em outro trecho do manual (fora da tabela) consta que o elevador corre automaticamente até o andar seguinte e o sistema reporta a falha Err55.

### Err56. Falha do sinal de abertura/fechamento de porta (Door open/close signal fault)
- Nível: 5A. Páginas do manual: 285.
- Subcódigos: 101: o sinal de limite de abertura/fechamento de porta está ativo durante a corrida; 102: o sinal de limite de fechamento de porta está inativo durante a corrida; 103: os sinais de limite de abertura e de limite de fechamento de porta são ambos válidos; 104: o sinal de limite de fechamento de porta está continuamente conectado 3 s após a porta abrir. Este subcódigo é detectado depois de o desvio (bypass) da fechadura de porta ser ajustado.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de limite de abertura/fechamento de porta está ativo durante a corrida. | Verificar o ajuste NO/NC do sinal de limite de abertura/fechamento de porta em F5-25; verificar a fiação do sinal de abertura/fechamento de porta. |
| Subcódigo 102: o sinal de limite de fechamento de porta está inativo durante a corrida. | Mesmas ações do subcódigo 101. |
| Subcódigo 103: os sinais de limite de abertura e de fechamento de porta são ambos válidos. | Mesmas ações do subcódigo 101. |
| Subcódigo 104: o sinal de limite de fechamento de porta está continuamente conectado 3 s após a porta abrir. Este subcódigo é detectado depois de o desvio da fechadura de porta ser ajustado. | Verificar se o sinal de limite de fechamento de porta está sempre ativo. |

- Notas do manual: nenhuma.

### Err57. Comunicação por interface periférica serial (SPI) anormal (Serial peripheral interface (SPI) communication abnormal)
- Nível: 5A. Páginas do manual: 285.
- Subcódigos: 101, 102: a comunicação da MCB com a placa DSP da unidade de acionamento é anormal; 103: a MCB não é compatível com o inversor CA (AC drive).

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 101, 102: a comunicação da MCB com a placa DSP da unidade de acionamento é anormal. | Verificar a fiação entre a placa de controle e a placa de acionamento. |
| Subcódigo 103: a MCB não é compatível com o inversor CA ("does not match"). | Contatar o agente ou a Inovance. |

- Notas do manual: "If faults Err51, Err52, and E57 persist, they are recorded once every one hour." O manual escreve aqui "E57" (não "Err57"); presume-se tratar-se do mesmo código Err57, mas o manual não o afirma.

### Err58. Chaves de posição do poço anormais (Shaft position switches abnormal)
- Nível: 4B. Páginas do manual: 285.
- Subcódigos: 101: a chave de redução de velocidade de subida e a chave de redução de velocidade de descida estão desconectadas simultaneamente; 102: a realimentação do limite de subida e a realimentação do limite de descida estão desconectadas simultaneamente.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: a chave de redução de velocidade de subida e a de descida estão desconectadas simultaneamente. | Verificar se a característica do sinal (NO, NC) das chaves de redução de velocidade e das chaves limite é consistente com o ajuste de parâmetro da MCB (o texto extraído quebra a frase em dois itens, "are" / "consistent with the parameter setting of the MCB", e foi aqui reunido); verificar se há mau funcionamento das chaves de redução de velocidade e das chaves limite. |
| Subcódigo 102: a realimentação do limite de subida e a do limite de descida estão desconectadas simultaneamente. | Mesmas ações do subcódigo 101. |

- Notas do manual: nenhuma na tabela.

### Err59. Reservado (Reserved)
- Nível: "-" (traço). Páginas do manual: 285.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado (Reserved) | Reservado (Reserved). |

- Notas do manual: nenhuma.

### Err60. Reservado (Reserved)
- Nível: "-" (traço). Páginas do manual: 285.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado (Reserved) | Reservado (Reserved). |

- Notas do manual: nenhuma.

### Err61. Reservado (Reserved)
- Nível: "-" (traço). Páginas do manual: 285.
- Subcódigos: nenhum.

| Causa possível | O que verificar ou fazer |
|---|---|
| Reservado (Reserved) | Reservado (Reserved). |

- Notas do manual: nenhuma.

### Err62. Cabo de entrada analógica rompido (Analog input cable broken)
- Nível: 3B. Páginas do manual: 285.
- Subcódigos: 101: o cabo de entrada analógica da célula de carga (load cell) está rompido.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o cabo de entrada analógica da célula de carga está rompido. | Verificar se F5-36 está ajustado corretamente; verificar se o cabo de entrada analógica da CTB ou da MCB está conectado incorretamente ou rompido; ajustar a função da chave da célula de carga ("load cell switch function"). |

- Notas do manual: nenhuma.

### Err63. Não consta na tabela
- Nível: não consta. Páginas do manual: 285 (a tabela passa de Err62 para Err64).
- Subcódigos: não consta.
- O manual não traz o código Err63.

### Err64. Falha externa (External fault)
- Nível: 5A. Páginas do manual: 285.
- Subcódigos: 101: o sinal de falha externa está continuamente ativo por 2 s.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 101: o sinal de falha externa está continuamente ativo por 2 s. | Verificar o ajuste NO/NC do terminal de falha externa; verificar o estado do sinal de entrada do terminal de falha externa. |

- Notas do manual: nenhuma.

### Err65. Teste UCMP anormal (UCMP test abnormal)
- Nível: 5A. Páginas do manual: 285.
- Subcódigos: nenhum (a coluna de causas traz duas frases sem subcódigo).

| Causa possível | O que verificar ou fazer |
|---|---|
| Esta falha é reportada quando o teste da função UCMP está habilitado. | Verificar se o freio está totalmente fechado e se a cabina não se move de forma não intencional ("unintendedly"). |
| Esta falha é reportada quando a cabina se move de forma não intencional. | Mesma ação da linha anterior (o manual traz uma única célula de solução para as duas frases). |

- Notas do manual: nenhuma.

### Err66. Teste de força de frenagem anormal (Braking force test abnormal)
- Nível: 5A. Páginas do manual: 285.
- Subcódigos: nenhum (a causa é uma frase sem subcódigo).

| Causa possível | O que verificar ou fazer |
|---|---|
| Esta falha é reportada quando o teste de força de frenagem está habilitado e é detectada força de frenagem insuficiente. | Verificar a folga do freio (brake clearance). |

- Notas do manual: nenhuma.

### Err67. Falha do AFE (AFE fault)
- Nível: 5A. Páginas do manual: 286 a 287.
- Subcódigos: 01: sobrecorrente; 02: superaquecimento do AFE; 04: subtensão do barramento; 06: sobretensão do barramento; 07: sobrecarga do AFE; 08: sobretensão da rede elétrica (Power grid overvoltage); 09: subtensão da rede ("undervoltage of the mains"); 10: sobrefrequência da rede ("overfrequency of the mains"); 11: subfrequência da rede ("underfrequency of the mains"); 12: tensão da rede assimétrica; 13: falha de travamento de fase ("phase lock") da tensão da rede; 14: corrente do AFE assimétrica; 15: falha de limite de corrente pulso a pulso; 16: falha de corrente de sequência zero; 17: falha de deslocamento de zero da corrente; 19: comunicação CAN anormal; 21: falha de comunicação RS485 em paralelo; 201/202: comunicação CAN anormal; 23: conexão do barramento em sequência errada.

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigo 01: sobrecorrente. | Verificar se existe aterramento ou curto-circuito do AFE ou do inversor CA; verificar se os parâmetros do controlador estão ajustados de forma irracional ("unreasonably"); verificar se a rede elétrica está anormal e se existe oscilação de saída; verificar qualquer falha interna da máquina; contatar a Inovance. |
| Subcódigos 02 (superaquecimento do AFE) e 04 (subtensão do barramento). | Verificar se a temperatura ambiente está alta demais; verificar se o ventilador está com defeito e se o filtro de ar está entupido; verificar se o módulo está danificado; testar a falha do circuito e contatar a Inovance; reduzir a carga se a carga estiver pesada demais; verificar se o teste da tensão do barramento está anormal e contatar a Inovance. (O manual não separa quais itens valem para 02 e quais para 04.) |
| Subcódigo 06: sobretensão do barramento. | Instalar um resistor regenerativo ("regen. resistor") no inversor CA; verificar se a tensão e a fiação da rede elétrica estão normais; verificar a compatibilidade de modelo e as condições; contatar a Inovance e verificar se o circuito e a malha de tensão estão ajustados de forma razoável. |
| Subcódigo 07: sobrecarga do AFE. | Verificar se a combinação (matching) da potência da máquina é razoável. |
| Subcódigos 08, 09, 10, 11: sobretensão, subtensão, sobrefrequência e subfrequência da rede elétrica. | Verificar se a tensão da rede elétrica está normal; contatar a Inovance e verificar se o circuito está normal. |
| Subcódigos 12, 13: tensão da rede assimétrica; falha de travamento de fase da tensão da rede. | Verificar se as três fases da tensão da rede estão normais; verificar se a conexão do cabo de entrada está normal; contatar a Inovance e verificar se o circuito está normal. |
| Subcódigos 14, 15, 16, 17: corrente do AFE assimétrica; falha de limite de corrente pulso a pulso; falha de corrente de sequência zero; falha de deslocamento de zero da corrente. | Verificar se a entrada trifásica está normal; verificar se a carga é grande demais; verificar se o sistema está em curto-circuito para o terra; contatar a Inovance e verificar se o circuito está normal. |
| Subcódigos 19, 21, 201/202: comunicação CAN anormal (19); falha de comunicação RS485 em paralelo (21); comunicação CAN anormal (201/202). | Verificar se o software da MCB suporta AFE; verificar se F6-52 BIT2 nos parâmetros da MCB está ajustado de forma razoável; verificar se o cabo de comunicação está rompido ou em mau contato. |
| Subcódigo 23: conexão do barramento em sequência errada. | Verificar a conexão do barramento e trocar a polaridade. |

- Notas do manual: nenhuma específica. Os subcódigos do Err67 são escritos com dois dígitos (01, 02...), diferente dos de três dígitos de outros códigos. A tabela continua na página 287 sem repetir o código e o nome nas colunas da esquerda.

### Err68. Não consta na tabela
- Nível: não consta. Páginas do manual: 287 a 288 (a tabela passa de Err67 para Err69).
- Subcódigos: não consta.
- O manual não traz o código Err68.

### Err69. Falha do ARD (ARD fault)
- Nível: 1A. Páginas do manual: 288.
- Subcódigos: 22 e 103: falha de comunicação do ARD; 1 a 3 e 8: falha de sobrecorrente do ARD; 10: sobrecarga do ARD; 4 a 7: falha da bateria do ARD; 11: sobretensão do barramento do ARD; 12: subtensão do barramento do ARD; 13: sobretensão da unidade de acionamento do ARD; 16: sobretensão de entrada da rede elétrica; 21 (relé travado, "Relay stuck"); 21 (alarme de nível muito baixo da bateria de lítio). O subcódigo 21 aparece duas vezes na tabela, com dois significados diferentes (ambíguo, ver o original na pág. 288).

| Causa possível | O que verificar ou fazer |
|---|---|
| Subcódigos 22 e 103: falha de comunicação do ARD. | Verificar a conexão do cabo de comunicação; verificar se a alimentação do ARD está normal; verificar se a alimentação de 24 V do controlador está normal; verificar se há interferência de forte potência na comunicação. |
| Subcódigos 1 a 3 e 8: falha de sobrecorrente do ARD; subcódigo 10: sobrecarga do ARD. | Verificar se a carga está normal; verificar se a fiação está correta; verificar se a carga é grande demais; contatar a Inovance. |
| Subcódigos 4 a 7: falha da bateria do ARD. | Verificar se o fio da bateria está conectado corretamente; verificar se o modelo da bateria está correto (48 V); "The battery life is reduced. Replace the battery." (A vida útil da bateria está reduzida. Substituir a bateria.); "The machine operates too long or the ambient temperature is too high." (A máquina opera por tempo demais ou a temperatura ambiente está alta demais.) Os dois últimos itens estão redigidos como afirmações, não como ações de verificar, e o manual não indica a que item da lista cada um se refere. |
| Subcódigos 11 (sobretensão do barramento do ARD), 12 (subtensão do barramento do ARD), 13 (sobretensão da unidade de acionamento do ARD). | Verificar se o nível da bateria está dentro de uma faixa correta; verificar se a tensão da bateria está normal; contatar a Inovance. |
| Subcódigo 16: sobretensão de entrada da rede elétrica. | Verificar se a tensão da rede está normal "and is incorrectly connected to 380 V" (ambíguo, ver o original na pág. 288: a frase diz literalmente "normal e está incorretamente conectada a 380 V"); contatar a Inovance. |
| Subcódigo 21: relé travado ("Relay stuck"). | Desligar e ligar novamente a energia do quadro de comando; se o "E69 subcode 21" reocorrer, testar a situação de travamento; testar se o relé principal K4 está travado; testar se o relé da unidade de acionamento K2 está travado; testar se o relé de liberação do freio K1 está travado. |
| Subcódigo 21: alarme de nível muito baixo da bateria de lítio. | Testar se a bateria de lítio está danificada; "The lithium battery is discharged excessively and must be charged." (A bateria de lítio está descarregada em excesso e deve ser carregada.) |

- Notas do manual: nenhuma específica ao Err69. A solução do subcódigo 21 usa a forma "E69" em vez de "Err69". O "ARD" é mantido como sigla do manual (o manual não o expande nesta tabela).

---

## Notas gerais da tabela (NOTE, pág. 288)

O manual traz, ao fim da tabela, o quadro "NOTE" com três itens. Tradução fiel:

1. "Fault Err41 is not recorded in the elevator stop state." Ligada ao Err41: a falha Err41 não é registrada no estado de parada do elevador.
2. "Fault Err42 is reset automatically when the door lock circuit is shorted or 1s after the fault occurs in the door zone." Ligada ao Err42: a falha Err42 é reiniciada automaticamente quando o circuito de fechaduras de porta é curto-circuitado ou 1 s depois de a falha ocorrer na zona de porta.
3. "If faults Err51, Err52, and E57 persist, they are recorded once every one hour." Ligada ao Err51, Err52 e Err57: se as falhas persistirem, são registradas uma vez a cada hora. Formato de código: o manual escreve "Err51" e "Err52", mas "E57" (e não "Err57") neste item.

---

## Outros conteúdos do capítulo 7

Depois da tabela e da nota (pág. 288 do PDF), o capítulo 7 ("7 Troubleshooting") não traz nenhum outro procedimento ou tabela dentro das páginas 289 a 295 lidas.

- Pág. 289 do PDF (impressa 288): página de anotações em branco, com o cabeçalho "Memo NO." e "Date" e linhas pontilhadas para escrever. Não há conteúdo técnico.

Início do capítulo 8 ("8 Inspection and Maintenance"), apenas registrado por ser o conteúdo seguinte, sem fazer parte do escopo da tabela de falhas:

- Pág. 290 do PDF (impressa 289): índice do capítulo 8: 8.1 Daily Maintenance (8.1.1 Daily Inspection Items), 8.2 Periodic Inspection (8.2.1 Periodic Inspection Items, 8.2.2 Main Circuit Insulation Test), 8.3 Replacement of Vulnerable Components (8.3.1 Lifetime of Wear Parts, 8.3.2 Cooling Fan, 8.3.3 Electrolytic Capacitor), 8.4 Storage. O índice indica as páginas impressas 291, 292, 293, 295 e 296 para essas seções.
- Pág. 291 (impressa 290): "Safety Information". Em "Danger" (para evitar choque elétrico): nunca fazer fiação com a energia ligada; cortar todas as alimentações e esperar pelo menos dez minutos para a tensão residual dos capacitores descarregar com segurança; nunca modificar a fiação, desconectar o cabo, remover a placa opcional ou trocar o ventilador de resfriamento com o controlador em funcionamento; ligar o terminal de aterramento do motor à terra; inspeção, manutenção e reparo só por pessoal elétrico qualificado. Em "Warning" (para evitar incêndio): nunca operar o controlador com a tampa de proteção removida; apertar todos os parafusos de terminal com o torque especificado; nunca ligar o circuito principal de forma errada; manter materiais inflamáveis longe do controlador. Em "Caution": trocar o ventilador da forma especificada, com a direção correta de saída de ar; nunca instalar ou remover o motor com o controlador em funcionamento; usar cabos blindados no circuito de comando, com a blindagem aterrada em uma das pontas; nunca modificar o circuito do controlador; ligar corretamente os terminais de saída do controlador aos terminais do motor; nunca operar um controlador danificado.
- Pág. 292 (impressa 291): "8.1 Daily Maintenance / 8.1.1 Daily Inspection Items". Texto introdutório sobre a influência de temperatura, umidade, poeira e vibração no envelhecimento dos componentes e sobre encurtar os ciclos de verificação em ambientes severos. Tabela de checklist diário com colunas Inspection Item, Inspection Points, Correction, Checked, com os itens: motor (oscilação ou ruído anormal), ventilador de resfriamento (controlador e motor), ambiente de instalação (armário e canaleta de cabos), carga (corrente de saída acima da nominal por certo tempo; vibração mecânica "< 0.6 g on normal condition"), tensão de entrada (alimentação principal e tensão de comando).
- Pág. 293 (impressa 292): "8.2 Periodic Inspection / 8.2.1 Periodic Inspection Items". Precauções (nunca inspecionar com a energia ligada; esperar pelo menos dez minutos) e tabela de inspeção periódica: geral (sujeira e poeira; aspirar com aspirador), cabos (descoloração, isolação envelhecida ou rachada), dispositivos periféricos como contator eletromagnético, filtro de ar e ventilação, circuito de comando.
- Pág. 294 (impressa 293): "8.2.2 Main Circuit Insulation Test" (megôhmetro de 500 VDC recomendado, desconectar os cabos do circuito principal, não testar o circuito de comando com o megôhmetro, não é necessário refazer o ensaio de alta tensão, resistência de isolação medida deve ser maior que 5 MΩ, remover o parafuso do varistor ("piezoresistor") antes de testar; Figura 8-3). "8.3.1 Lifetime of Wear Parts": ventilador de resfriamento ≥ 5 anos e capacitor eletrolítico ≥ 5 anos, com condições de base de temperatura ambiente 40ºC, taxa de carga 80% e taxa de operação 12 horas/dia. Início de "8.3.2 Cooling Fan" (causas possíveis: rolamento do ventilador desgastado, envelhecimento das pás).
- Pág. 295 (impressa 294): critérios de avaliação do ventilador (trinca na pá, ruído de vibração anormal na partida, pás funcionando normalmente) e procedimento de substituição do ventilador (estrutura plástica): pressionar os ganchos da tampa e puxar para cima; levantar o ventilador, desconectar os cabos de alimentação do ventilador e removê-lo; reinstalar em ordem inversa, observando a seta de direção para o fluxo de ar para cima.
- Pág. 296 (impressa 295): procedimento de remoção do ventilador com parafusos na tampa (soltar parafusos, levantar a tampa e o ventilador, desconectar o cabo, remover) e de reinstalação (alinhar furos, garantir o sentido do fluxo de ar). "8.3.3 Electrolytic Capacitor": causas possíveis (alimentação de má qualidade, temperatura ambiente alta, saltos frequentes de carga, envelhecimento do eletrolítico).
- Pág. 297 (impressa 296): critérios do capacitor eletrolítico (vazamento de líquido, válvula de segurança projetada, medir capacitância estática, medir resistência de isolação) e substituição: "Do not replace the electrolytic capacitor yourself. If replacement is required, contact us." "8.4 Storage": embalar com a caixa original da Inovance; não colocar em ambiente de alta umidade ou temperatura nem sob luz solar direta por muito tempo; o armazenamento de longo prazo degrada o capacitor eletrolítico, por isso o controlador deve ser energizado uma vez a cada seis meses, por pelo menos 5 horas cada vez, elevando a tensão de entrada lentamente até o valor nominal com o regulador.

(As páginas 296 e 297 vão além do intervalo pedido, 289 a 295, e foram lidas apenas para fechar o resumo da seção.)
