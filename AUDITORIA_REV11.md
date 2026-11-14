# AUDITORIA_REV11.md: auditoria do Livro do Quadro de Comando Rev. 11

Marco 2 do PLANO_REV12.md. Regra: só lista divergências com página e fonte. NÃO altera o livro.
Início: 14/11/2026. Estado: concluído (lotes 0 a 4, 6, 7a e 7b).

## Resumo executivo (Marco 2 concluído em 14/11/2026)
Escopo: o livro Rev. 11 inteiro (68 págs.) e as 125 ligações da lista de fios, conferidos contra os dois esquemas e os manuais. O livro NÃO foi alterado. Tabelas fio a fio e afirmação a afirmação estão em `auditoria/` (lotes 2, 3, 4, 6, 7a e 7b).

| Frente | Resultado |
|---|---|
| 125 fios da lista contra o esquema | 91 conferem, 22 divergem, 12 não verificáveis |
| 313 afirmações dos textos (págs. 7 a 35 e 43 a 68) | 218 confirmadas, 66 contradizem as fontes, 29 não verificáveis |
| Citações de página e folha (574 testadas no lote 7b) | 492 exatas, 64 com 1 linha de diferença, 0 ausentes |
| Pendências P1 a P20 | ver tabela abaixo |
| Pendências P21 a P51 | 5 resolvidas, 16 parciais, 5 abertas, 3 não verificáveis, 2 confirmadas |

Os 10 achados que mais pesam:
1. Jumpers 62 a 66 da lista não existem no esquema. Se ficarem num quadro de campo, curto-circuitam a cadeia de segurança e as fechaduras (leitura do desenho; o Gelson indicou que são só de bancada, ainda sem confirmação em campo). Os jumpers 61 e 67 o esquema prevê para porta única.
2. L e N da resgate elétrico estão invertidos na lista (501 no L e 502 no N nos dois esquemas). A entrada da ERB, segundo o agente, é 187 a 242 V e não 187 a 253 V (não conferi eu mesmo no manual da ERB).
3. A lista de fios não veio do esquema VerticalParts nem de nenhum esquema: ela não prova a ligação. As duas revisões de esquema diferem em QFB1, QFB2, filtro EMC e chave de inspeção do poço.
4. Págs. 34 e 35 (conferências) usam valores de um manual antigo que o NICE3000new contradiz: chave de limite 30 a 50 mm (e não 100), chaves de desaceleração 2 e 3 a partir de 2 e 3 m/s, 4 sensores de nível, terra abaixo de 10 ohm. Conferi o terra: o manual NICE3000new diz resistência de aterramento do cabo menor que 10 ohm (pág. PDF 54).
5. Flat de 40 vias: X15 e X16 aparecem trocados no livro.
6. Trafo: os dois esquemas dizem 125 V, 63 VA (110 VA para 30 a 37 kW); o BOM do livro (110 V, 150 VA) não bate com nenhum.
7. Conectores: FAN tem 8 posições (livro: 6); EY3 tem 3 sinais (livro: 5); EY4 tem 20 posições e 14 sinais (livro: faltam 507 e 508 e os pinos 5 a 12 estão errados).
8. Rede da cadeia: o livro diz "121 = 119" e "FLSU e FLSD na rede 121". O desenho: 119, FLSD, 120, FLSU, 121.
9. Contradições menores: X20 é sobretemperatura do motor (não freio); E6 (os 24 V saem da PCB-D1 para a KCB, sentido contrário ao do livro); S1 e TIS da pág. 29 são do limitador e não do bypass; caixa de 1350x350x240 mm e não 1350x450x350.
10. Bitola: nenhuma folha de esquema indica bitola. A coluna "mm²" da lista não tem confirmação em nenhuma fonte lida.

## Método
1. A base de verdade são os esquemas (Vitinho 19061867-ZL e VerticalParts 19060918-ZL) e os manuais, não a lista de fios.
2. Cada ligação da tabela mestre do Rev. 11 (125 fios) é conferida contra o desenho. Resultado por fio: CONFERE, DIVERGE ou NÃO VERIFICÁVEL (o desenho lido não mostra o componente).
3. Leitura do desenho é visual (sem extração automática de texto), então a confiança é "alta" quando o pino e a rede aparecem legíveis no desenho e "média" quando a leitura depende de seguir um traço longo.

## Lote 0. Tabela mestre do Rev. 11 contra a lista de fios original
- Fontes: Rev. 11 págs. PDF 36 a 38 (tabela mestre) e `Lista de fios.xlsx` (idêntico em `Downloads` e em `ArquivosParaTratar`, mesmo hash).
- Resultado: 125 de 125 linhas iguais (componente, borne, tag, bitola e comprimento). A tabela do Rev. 11 é cópia fiel da lista. Isso confirma que ela herda qualquer erro que a lista tenha.
- Observação sobre a lista: 59 fios têm tag (rede) e 66 não têm. Nos 66, a rede só se descobre pelo esquema.

## Lote 1. Botoeira de inspeção e limitador: CIS, CIU E, CID E, MES, TIS e S1 (21 ligações)
Desenho de referência: Vitinho folha /14 "Emergency electrical operation/Bypass" (PDF pág. 16). Rede dos pinos da KCB KY4 no desenho: 1=301, 2=56 (X11), 3=55 (X10), 4=X9, 7=125, 8=118, 9=110, 10=122B, 11=123, 12=101A.

| Fio | Ligação na lista | Esquema | Resultado |
|---|---|---|---|
| 6 | CID E/3 a CIU E/3 | CID E 3 liga ao 3 do CIU E | CONFERE (alta) |
| 7 | KY4/2 (X11) a CID E/4 | KY4 2 = rede 56 (X11), vai ao 4 do CID E | CONFERE (alta) |
| 8 | CIS/13 a CID E/14 | 13 do CIS liga ao 14 do CID E | CONFERE (média) |
| 9 | CIS/3 a CIS/1 (tag 301) | 3 do CIS ligado à rede 301 (pino 1) | CONFERE (média) |
| 10 | CIS/4 a CIU E/3 | 4 do CIS liga ao 3 do CIU E | CONFERE (média) |
| 11 | CIS/13 a CIU E/14 | 13 do CIS liga ao 14 do CIU E | CONFERE (média) |
| 12 | CIU E/13 a CID E/13 | 13 de CIU E e de CID E em comum | CONFERE (média) |
| 13 | CIU E/13 a KY4/7 (tag 125) | KY4 7 = rede 125, vai ao comum 13 | CONFERE (média) |
| 38 | KY4/1 a CIS/1 (tag 301) | KY4 1 = rede 301, vai ao 1 do CIS | CONFERE (alta) |
| 39 | KY4/4 a CIS/2 (tag X9) | KY4 4 = X9, vai ao 2 do CIS | CONFERE (alta) |
| 40 | KY4/8 a CIS/14 (tag 118) | KY4 8 = rede 118, vai ao 14 do CIS | CONFERE (alta) |
| 41 | KY4/10 a CIS/12 (tag 122B) | KY4 10 = rede 122B, vai ao 12 do CIS | CONFERE (alta) |
| 42 | KY4/11 a CIS/11 (tag 123) | KY4 11 = rede 123, vai ao 11 do CIS | CONFERE (alta) |
| 43 | KY4/3 a CIU E/4 (tag X10) | KY4 3 = rede 55 (X10), vai ao 4 do CIU E | CONFERE (alta) |
| 49 | KY4/12 a MES/2 (tag 101A) | KY4 12 = rede 101A, vai ao 2 do MES | CONFERE (alta) |
| 50 | KY4/9 a MES/1 (tag 110) | KY4 9 = rede 110, vai ao 1 do MES | CONFERE (alta) |

Resultado do lote: 16 de 16 ligações com esquema CONFEREM. Nenhuma divergência.

TIS e S1 da lista (correção de 14/11/2026, após resposta do Gelson à Q68). Eu havia escrito que eles não existiam no esquema; estava errado, porque só procurei na folha /14. Estão na folha /22 do Vitinho, "Speed limiter remote action/release circuit (Use for MRL)" (PDF pág. 24), e na pág. PDF 15 do esquema VerticalParts ("TIS, chave acionamento manual limitador"). TIS = "Speed limiter remote action switch" (contatos 13 e 14). S1 da lista = a chave de ação remota (contatos 13/14) e de rearme remoto (contatos 23/24) do limitador. Conferência contra a folha /22 (versão AC 220 V, à esquerda do desenho):
| Fio | Ligação na lista | Esquema | Resultado |
|---|---|---|---|
| 17 | DQFB2/2 a TIS/13 (tag 201) | rede 201 entra no 13 do TIS | CONFERE (alta) |
| 110 | TIS/14 a S1/13 | 14 do TIS alimenta o 13 do S1 | CONFERE (alta) |
| 111 | TIS/14 a S1/23 | 14 do TIS alimenta o 23 do S1 | CONFERE (alta) |
| 95 | S1/14 a XB 203 | 14 do S1 sai para o borne XB 203 | CONFERE (alta) |
| 96 | S1/24 a XB 205 | 24 do S1 sai para o borne XB 205 | CONFERE (alta) |
Observação: a mesma folha traz a versão DC 24 V (redes 301/302, bornes XB 303 e 305). A lista cobre a versão AC 220 V. Falta saber qual versão o elevador de referência usa (pergunta Q69).

Sem verificação neste lote: fio 28 (ERB-A1 PE a chapa da botoeira PE), ligação de terra que não aparece como ponto de ligação nas folhas de sinais.

## Achados até agora (para o Rev. 12)
1. A tabela mestre do Rev. 11 é só a lista de fios reformatada. Ela não prova nada sobre o esquema; a prova é este tipo de conferência.
2. TIS e S1 da lista existem no esquema (folha /22) e são do circuito de ação e rearme remoto do limitador de velocidade. O Rev. 11 os marca "função a confirmar" (Q68 respondida pelo Gelson e confirmada nesta auditoria).
3. A KCB-B4A tem um plugue S1 e outro S2 (bypass, folhas /14 e /19). A lista usa "S1" para a chave do limitador. Isso confunde e o Rev. 12 deve renomear um dos dois.

## Lotes 2, 3 e 4. Os 104 fios restantes (conferência por agentes, amostra conferida por mim)
Arquivos com a tabela fio a fio, folha, página e confiança: `auditoria/lote2_kcb.md`, `auditoria/lote3_contatores_resgate.md` e `auditoria/lote4_potencia_terra.md`. Esquema usado: Vitinho 19061867-ZL.

| Lote | Fios | CONFERE | DIVERGE | NÃO VERIFICÁVEL |
|---|---|---|---|---|
| 1 (botoeira de inspeção, TIS e S1) | 21 | 21 | 0 | 0 |
| 2 (KCB-B4A) | 48 | 35 | 11 | 2 |
| 3 (contatores, resgate, SZ) | 32 | 22 | 7 | 3 |
| 4 (potência e terra) | 24 | 11 | 4 | 9 |
| **Total (após o lote 6)** | **125** | **91** | **22** | **12** |

### O que as 22 divergências são (agrupadas por natureza)
1. **Jumpers 62 a 66 (5 fios): ligações que o esquema não mostra.** Conferi eu mesmo na folha /21 que HW/3 = rede 110, AA/4 = 130, AA/5 = 131A, AA/6 = 133 e AA/14 = 134. O fio 64 (HW/3 a AA/4) liga o início da cadeia de segurança (110, depois do MES) ao fim dela (130, que chega à entrada X25). Pelas redes do desenho, se ele ficar instalado, todos os contatos entre esses dois pontos ficam em curto. Os fios 65 e 66 fazem o mesmo com as fechaduras da cabina e dos pavimentos (X26 e X28). Os fios 62 e 63 ligam as entradas de desaceleração (X14 e X15) à rede 301. Isto é uma leitura do desenho, não está provado que os jumpers existam no quadro de campo: o Rev. 11 já pergunta na pendência P8 se eles são só de bancada. É o achado mais importante da auditoria (pergunta Q71).
2. **L e N da resgate elétrico invertidos (fios 20 e 94).** O esquema liga 501 ao L e 502 ao N da ERB-A1; a lista faz o contrário. Conferido por mim na folha /23. É a pendência P10 do Rev. 11, agora respondida pelo esquema.
3. **SZ: numeração diferente (fios 29, 32, 36, 37, 105, 106, 107, 108, 109).** A lista numera os bornes do SZ em pares (3/4, 13/14, 23/24, 33/34); o esquema define o SZ como tomada de 9 pinos. Em todos esses fios a rede e o pino da KCB conferem. É diferença de implementação, não prova erro de ligação (pergunta Q70).
4. **Fio 30:** ERB ZQ+ listado para SW 73; no desenho está no nó ZQ1+, que vai ao SW 53 (confiança média).
5. **Disjuntor QFB2 (fios 16, 88 e 118):** o desenho numera 1 e 2 na entrada e 3 e 4 na saída; a lista usa a numeração do disjuntor físico (1 e 3 na entrada, 2 e 4 na saída). A topologia é a mesma. Conferi o QFB2 na folha /10.
6. **Tomada CZ (fios 18 e 91):** o agente leu no esquema que a tomada é alimentada pelo QFB4 (iluminação da caixa) e a lista a liga ao QFB3 (501 e 502). Não conferi esta folha eu mesmo.

### Não verificáveis (12 fios, após o lote 6)
Fio 28, 68, 76, 77, 114, 121, 122, 123, 124 e 125 (terras: os esquemas mostram só o símbolo PE, e o XPE e o MCB-C2 não aparecem) e fios 15 e 92 (DQFB1 e DQFB3 não estão desenhados). Os fios 90 e 120 (XB 202) foram confirmados no lote 6.

### Outros achados
1. **Trafo:** o desenho mostra primário 220V e 0P e secundário 125V e 0S, 63 VA para 3,7 a 22 kW. O BOM do Rev. 11 diz "220 V para 110 V, 150 VA". Confirma a pendência P3 do Rev. 11.
2. **Bitola:** nenhuma folha do esquema indica bitola de fio. A coluna "mm²" da lista não foi conferida contra nada. A fonte de bitola precisa ser outra (manual do inversor, norma ou projeto).
3. **MCB-C2:** não existe no esquema; a placa é a MCB-C3 (pendência P11 do Rev. 11, confirmada).
4. **Fios 61 e 67 (jumpers de porta única):** o desenho os prevê só para elevador de uma porta. Em elevador com porta traseira eles anulam a supervisão das fechaduras traseiras.
5. **Filtro EMC e borne TA:** a lista não os cita nas ligações de entrada (fios 83 a 86); o desenho mostra a rede passando por eles.

### Limites da auditoria
1. Leitura visual dos desenhos; confiança alta, média ou baixa por fio, nos arquivos dos lotes.
2. Só o esquema Vitinho 19061867-ZL foi a base. O esquema VerticalParts 19060918-ZL (outra revisão) só serviu em pontos isolados. A comparação entre as duas revisões é o lote 6.
3. A conferência é da ligação lógica (componente, pino, rede). Torque, comprimento, terminal e bitola não são verificáveis pelo esquema.

## Lote 6. As duas revisões de esquema (Vitinho 19061867-ZL e VerticalParts 19060918-ZL)
Arquivo: `auditoria/lote6_duas_revisoes.md`. Hipótese testada: a lista de fios teria sido feita a partir do esquema VerticalParts, e as divergências contra o Vitinho seriam ligações que ele confirma.
Resultado: a hipótese NÃO se sustenta, com evidência forte.
1. Nas 22 divergências, o esquema VerticalParts concorda com o Vitinho e não com a lista: L e N da ERB (501 no L, 502 no N, PDF pág. 16 do VerticalParts), tomada CZ no QFB4, SZ de 9 pinos, ZQ+ no SW 53, trafo com secundário de 125 V e 63 VA. Os jumpers 62 a 66 não aparecem em nenhum dos dois.
2. A lista traz ligações que só existem no Vitinho (CIS 11/12 e CIU/CID 13/14; no VerticalParts há um fio ponte no lugar) e usa um QFB1 de bornes 3 e 4 (no VerticalParts o QFB1 tem um polo e 1 A). Logo, a lista não veio do esquema VerticalParts.
3. Fios 90 e 120 (XB 202): o esquema VerticalParts os mostra (pág. 15) e o Vitinho também (folha /22). Passam de "não verificável" para "confere".
4. Contagem corrigida do total de 125 fios: 91 conferem, 22 divergem e 12 não verificáveis.
5. Trafo: os dois esquemas dizem 125 V e 63 VA (110 VA para 30 a 37 kW). O BOM do Rev. 11 (110 V, 150 VA) não bate com nenhum.
6. Diferenças entre as revisões com efeito na segurança ou na fiação: QFB1 (1P+N 10 A no Vitinho; 1P 1 A no VerticalParts), QFB2 com bloco diferencial só no Vitinho, filtro EMC só no Vitinho, chave de inspeção do poço só no Vitinho, contatos CIS/CIU/CID só no Vitinho.
7. O PDF do esquema VerticalParts que está na pasta tem só 37 das 58 folhas; "não mostra" vale só para as folhas disponíveis. A revisão que vale para produção é decisão do Gelson (pendência P20 do Rev. 11).

## Lote 7a. Textos do livro, págs. 7 a 35 (arquivo `auditoria/lote7a_livro_p7_a_p42.md`)
158 afirmações: 110 confirmam, 35 contradizem, 13 não verificáveis. Selos das págs. 7 a 35: 30 `[Certeza]`, 40 `[Provável]`, 8 `[Chute]` e 45 `PREENCHER`; 13 grupos têm algo resolvido pelas fontes, 10 foram contraditos, o resto fica aberto por falta de foto ou de ficha de componente.

### Pendências P1 a P20: o que as fontes resolvem
| P | Assunto | Situação após a auditoria |
|---|---|---|
| P1 | inversor 220 V | Modelo RESOLVIDO (manual: 220-NICE-L-C-4015 para 7,5 kW e 220-NICE-L-C-4022 para 15 kW; "2015" não existe). ABERTO: ler a etiqueta do inversor recebido. |
| P2 | origem dos 220 V de comando | ABERTO (decisão por variante). Corrigir a faixa da ERB (187 a 242 V, segundo o agente). |
| P3 | trafo | Bornes RESOLVIDOS (220V, 0P, 125V, 0S; 63 VA). ABERTO: etiqueta e medição sem carga. "OP" do livro é "0P" (zero). |
| P4 | bitola e terminais | Cabo RESOLVIDO (6 mm² e 10 mm², manual). ABERTO: parafuso e torque dos 220 V. |
| P5 | resistor de frenagem | Resistores CONFIRMADOS. ABERTO: bitola, terminal e fixação. |
| P6 | mapa dos contatores | ABERTO (multímetro). O esquema define o esperado; sem ficha WEG o mapa impresso não se resolve. |
| P7 | botoeira | O desenho mostra o handle KKB4-1C-02 (CIS, CIU, CID e MES) e nenhum botão vermelho extra. ABERTO: mapa furo a botão. |
| P8 | plugues S1/S2 e jumpers | Tag "S1" da lista = limitador de velocidade: RESOLVIDO. Jumpers 62 a 66: ver achado 1. |
| P9 | QFB4 | QFB4 e LIHS1 CONFIRMADOS no esquema (não estão na lista nem no BOM). ABERTO: decidir se entram. |
| P10 | L/N da ERB | RESOLVIDO no esquema. ABERTO: conferir a serigrafia da ERB e corrigir a lista. |
| P11 | MCB-C2 ou C3 | RESOLVIDO (só existe a C3). Corrigir fios 77 e 123. |
| P12 | fora do checklist | Parcial: SCB-A4/D4 e limitador AC 220 V ou DC 24 V (Gelson: AC 220 V). |
| P13 | terminais no BOM | Contagens conferem. Falta tubular 6 mm² (19 na lista e 16 no BOM). O "10% de reserva" é [Chute] e não consta no POP. |
| P14 | XPE de 6 polos | ABERTO (decisão de projeto). |
| P15 | BC-1 | ABERTO (inconsistência interna: BC-1 ou BC-A). |
| P16 | bateria da ERB | ABERTO (abrir a tampa). "BPQ" não consta no manual. |
| P17 | bornes 2 x 7 | ABERTO (contar na montagem). |
| P18 | comprimento dos fios | ABERTO (PCP). A caixa real é 1350 x 350 x 240 mm. |
| P19 | zona de porta da ERB | Parcial. Teste R5 e R6 ou consulta à Inovance. |
| P20 | duas revisões de esquema | Diferença CONFIRMADA. ABERTO: o Gelson decide qual vale. |

## Lote 7b. Textos do livro, págs. 43 a 68 (arquivo `auditoria/lote7b_livro_p43_a_p68.md`)
155 afirmações: 108 confirmam, 31 contradizem, 16 não verificáveis. 44 grupos de selos: 12 confirmados, 16 resolvidos, 9 parciais, 7 abertos. Pendências P21 a P51: 5 resolvidas, 16 parciais, 5 abertas, 3 não verificáveis, 2 confirmadas.
Resolvidos pelas fontes: CAN trançado e blindado; funções das redes 130 a 134, 102 e L/R; ligação do DZI; cotas de furação da caixa (254 x 340 mm, M6); pinagem do encoder PG-E (P25); curto do MSC entre 10 e 12 (P39); iluminação do poço sai do QFB4 (P43); ERB usa FL1 do RDZ (P45); PCB-D1 (P48); FX = contator de curto das fases U, V e W.
Pinagens que batem com o desenho: AA, AB, BA, BB, BC, BD, BE, MT, OS, HW, AC, CA, CB, MSC, PG, COB, EDP e plugues do poço.
Corrigir no livro: FAN (8 posições), EY3 (3 sinais), EY4 (20 posições e 14 sinais), "121 = 119", jumpers de porta única AA 6 com 14 e BA 8 com 9 na seção IV.4, X20 (sobretemperatura), P38 (o manual A00 já traz ambiente e IP21).

## Como esta auditoria foi feita e o que eu conferi pessoalmente
1. Os lotes 2, 3, 4, 6, 7a e 7b foram conferidos por agentes, em paralelo, lendo os desenhos em imagem. Eu conferi por mim mesmo: o lote 1 inteiro; a folha /19 (cadeia); a ERB na folha /23; o QFB2 e o trafo na folha /10; os pinos HW/3 = 110, AA/4 = 130, AA/5 = 131A, AA/6 = 133 e AA/14 = 134 na folha /21; o terra menor que 10 ohm no manual.
2. Não conferi por mim: a faixa de 187 a 242 V da ERB, os valores de limite de 30 a 50 mm e de desaceleração das págs. 34 e 35, a alimentação da tomada CZ pelo QFB4, e a maior parte das 313 linhas dos lotes 7a e 7b.
3. A confiança por linha (alta, média, baixa) está em cada arquivo de lote.

## Estado e próximos passos
Marco 2 concluído: nenhum lote pendente. Em seguida (Marco 3): aplicar as correções, reescrever a tabela de fios como apêndice derivado e integrar o Capítulo 1.
