# Apêndice F. Rastreabilidade

> VERSÃO v0.2 de 15/11/2026. Aprovado pelo Gelson em 15/11/2026. Gerado por `build/gera_rastreabilidade.py` a partir dos capítulos. Mostra de onde vem cada informação do livro: os documentos da base (F.1), as fontes citadas em cada seção (F.2) e os dados que ainda faltam (F.3). A regra do livro é: toda afirmação técnica cita documento e página; o que não tem fonte fica com selo, nunca com suposição.

## F.1 Documentos-fonte

| Documento | Arquivo na base de conhecimento | Capítulos que citam |
|---|---|---|
| Esquema elétrico Vitinho 19061867-ZL (2023-07-18), revisão de esquema válida | `Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf` | 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 14 |
| Esquema elétrico VerticalParts 19060918-ZL (2022-10-11), só referência | `Esquema Elétrico Elevadores Verticalparts.pdf` | 1, 5, 11 |
| Manual do controlador NICE3000new (368 págs., edição 20181130) | `Manual_Usuario_Controlador_NICE3000new_Completo.pdf` | 1, 2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 14 |
| Manual do resgate elétrico MCTC-ERB-A (19010850-B01) | `Manual_Dispositivo_Resgate_Eletrico_ERB-A1_EN.pdf` | 3, 4, 5, 7, 14 |
| Manual da caixa de teto MCTC-CTW-B3 (edição A02, julho de 2022) | `Manual_Caixa_de_Teto_MCTC-CTW-B3_EN.pdf` | 2, 8, 9, 10 |
| Manual do encoder EI53C9.25-2048 | `Manual_Encoder_Seno_Cosseno_EI53C9.25-2048.pdf` | 7 |
| Boletim "Parametrização de Controlador de Porta NICE900" (AD30) | `Parametrização do AD30 (Motor Síncrono).pdf` | 9 |
| Manual de comissionamento do NICE900 (versão 1.0, fevereiro de 2026) | `Manual_Comissionamento_NICE900_VerticalParts.pdf` | 9 |
| Manual da máquina de porta J4210 (22/03/2024) | `Manual_Instrucoes_Operador_de_Porta_J4210-T2.pdf` | 9 |
| POP-ISO-PCP, planejamento, produção e controle de quadros de comando (Rev. 00) | `POP-ISO-PCP ... QUADROS DE COMANDO.pdf` | 5 |
| Cartilha "Manual de Resgate" VP-RES-01 Rev. 02 (versão para validação técnica) | `VerticalParts_Manual_de_Resgate-2.pdf` | 14 |
| Fotos do quadro de 12 e 13/11/2026 | `Fotos do quadro` | 3, 14 |
| Livro do Quadro de Comando Rev. 11 e a auditoria dele | `Livro_..._Rev11.pdf; auditoria/` | 4, 5, 8 |

Hierarquia: quando dois documentos divergem, vale o esquema Vitinho 19061867-ZL para ligações e o manual do fabricante para valores e parâmetros. A lista de fios da produção não é fonte: ela é conferida contra o esquema (Apêndice A). Documentos de outros fabricantes (BST, Glarie) e edições antigas de manual foram lidos só como apoio e não são citados como fonte.

## F.2 Fontes por seção

Cada linha traz as fontes exatamente como a seção as cita (linhas "Fonte:"). As seções sem linha própria usam as fontes do fim do capítulo.

| Seção | Fontes citadas |
|---|---|
| 1.2 O elevador sem casa de máquinas | esquema Vitinho 19061867-ZL, folhas /7, /8, /19 e /34 (páginas PDF 9, 10, 21 e 36; a página PDF é o número da folha mais 2). |
| 1.3 Cadeia de segurança | manual NICE3000new (20181130), pág. PDF 61 (impressa 60), tabela do conector CN2; pág. PDF 199 (impressa 198), parâmetros de entrada.; esquema Vitinho 19061867-ZL, folhas /19 (cadeia, pág. PDF 21), /34 (caixa de teto, pág. PDF 36), /41 (poço, pág. PDF 43) e /43 (fechaduras, pág. PDF 45); manual NICE3000new, pág. PDF 61.; esquema Vitinho 19061867-ZL, folhas /14 (pág. PDF 16), /19, /34, /41, /42 (pág. PDF 44) e /43. Para BFS1 e BFS2 o esquema Vitinho só traz "Buffer switch 1" e "Buffer switch 2"; a atribuição carro e contrapeso vem do esquema VerticalParts 19060918-ZL (pág. 30 e legenda da pág. 12), confirmada pelo responsável técnico em 15/11/2026.; esquema Vitinho 19061867-ZL, folhas /19, /34 e /43. |
| 1.4 Circuito de fechaduras | manual NICE3000new (20181130), pág. PDF 199 (impressa 198), parâmetros de entrada 04, 05, 29 e 31.; manual NICE3000new (20181130), pág. PDF 281 (impressa 280), tabela de falhas, e pág. PDF 288, notas. |
| 1.5 Bypass de porta | esquema Vitinho 19061867-ZL, folha /14 (nota 1, pág. PDF 16) e folha /19 (pág. PDF 21). |
| 1.6 Inspeção e operação elétrica de emergência | manual NICE3000new (20181130), pág. PDF 200 (impressa 199), parâmetros de entrada 08, 09, 10 e 84; págs. PDF 194 e 196, parâmetros F3-11, F3-25 e F3-26. |
| 1.7 Segurança do trabalho no quadro de comando | manual NICE3000new (20181130), "Safety Instructions", págs. PDF 20 e 21 (impressas 19 e 20). |
| 2.2 O sistema em uma figura | esquema Vitinho 19061867-ZL, folhas /24 e /45 (págs. PDF 26 e 47); manual NICE3000new, págs. PDF 35 e 36; manual da caixa de teto MCTC-CTW-B3. |
| 2.3 Os componentes | esquema Vitinho 19061867-ZL, folhas /3.a, /21, /24, /42 e /45 (págs. PDF 5, 23, 26, 44 e 47); manual NICE3000new, pág. PDF 35; manual da caixa de teto MCTC-CTW-B3, págs. PDF 1 e 2; documento "Parametrização de Controlador de Porta NICE900". |
| 2.4 Como os componentes conversam | manual NICE3000new, seção 2.3.4, págs. PDF 68 e 69 (impressas 67 e 68); a regra do par trançado está nas precauções de EMC, pág. PDF 70 (impressa 69). |
| 2.6 Se o seu elevador tiver outra configuração | esquema Vitinho 19061867-ZL, folhas /19, /24 e /45; manual NICE3000new, págs. PDF 61 e 68. |
| 3.2 O quadro de comando visto de fora | fotos do quadro (12 e 13/11/2026), catalogadas em `sources/cap03_fotos.md`.; fotos do quadro (12 e 13/11/2026) e desenho de furação do quadro; sem escala. |
| 3.4 Placa de interface KCB-B4A | esquema Vitinho 19061867-ZL, folhas /11, /13, /14, /19, /21, /23 e /24 (págs. PDF 13, 15, 16, 21, 23, 25 e 26). |
| 3.5 Placa fonte do freio PCB-D1 | esquema Vitinho, folhas /10, /13 e /24 (PDF 12, 15 e 26). O desenho não informa quantos pinos têm J2, J3 e J4. As fotos não mostram a PCB-D1 com etiqueta: a posição dela no quadro está em `PREENCHER [Q85]`. |
| 3.7 Botoeira de inspeção | esquema Vitinho, folha /14 (pág. PDF 16). As ligações internas de CIS, CIU E e CID E foram conferidas contra o desenho (ver o apêndice A). |
| 3.8 Proteções e transformador | esquema Vitinho 19061867-ZL, folhas /8, /9, /10 e /11 (págs. PDF 10 a 13). |
| 3.9 Contatores SW, BY e FX | esquema Vitinho 19061867-ZL, folhas /9, /13 e /17 (págs. PDF 11, 15 e 19); manual NICE3000new, Tab. 3-12, pág. PDF 100. |
| 3.11 Se o seu elevador tiver outra configuração | esquema Vitinho, folhas /7, /8 e /9; manual NICE3000new, tabelas 1-1 e 3-2. |
| 4.2 Antes de começar | manual NICE3000new, págs. PDF 54, 56 e 63; manual do resgate elétrico, seção 6. |
| 4.3 O ambiente e a fixação do inversor | manual NICE3000new, págs. PDF 39 a 47. |
| 4.4 A ordem de montagem | prática de montagem do Rev. 11, pág. 12, confirmada como ordem oficial em 15/11/2026, e seções 4.2 a 4.7.; Rev. 11, pág. 12 (ordem); manual NICE3000new, seção 2.2.1 (terra e potência). |
| 4.5 Regras de fiação do manual | manual NICE3000new, págs. PDF 52 a 54, 63 e 68 (seções 2.2.1 a 2.3.4). |
| 4.6 O cabo plano de 40 vias entre a MCB-C3 e a KCB-B4A | esquema Vitinho 19061867-ZL, folhas /13, /14 e /20 (págs. PDF 15, 16 e 22); auditoria do Rev. 11, lote 7a. |
| 4.7 Verificações sem tensão | manual NICE3000new, págs. PDF 54, 71, 73 e 143 a 145; esquema Vitinho; Rev. 11, pág. 12. |
| 4.8 Registro da montagem | prática de montagem, Rev. 11; `STANDBY.md`. |
| 4.9 Se o seu elevador tiver outra configuração | manual NICE3000new, Tabelas 2-8 e 2-9. |
| 5.2 Quem faz o quê | POP-ISO-PCP, seções 6.1.12, 6.1.13 e 6.5.; POP-ISO-PCP, págs. 8 a 10 (seções 6.1.12, 6.1.13 e 6.5). |
| 5.3 Preparação da bancada | manual do NICE3000new, capítulo 5 (capítulo 12 deste livro, seção 12.3); Rev. 11, pág. 32. |
| 5.4 Testes de energização do quadro (E1 a E12) | Rev. 11, pág. 32 (E1 a E12), conferida pela auditoria (E6 corrigido: os 24 V saem da PCB-D1 para a KCB); manual do NICE3000new, Tabela 1-1; esquema Vitinho, folhas /4, /10, /11 e /13. |
| 5.5 Teste do resgate elétrico e da bateria (R1 a R8) | manual do resgate elétrico MCTC-ERB-A, págs. PDF 1 e 2; esquema Vitinho, folha /23; Rev. 11, pág. 33, com R3 corrigido (a faixa é 187 a 242 V, não 187 a 253 V) e R4 corrigido pela auditoria. |
| 5.6 Inspeção e liberação pela Qualidade | POP-ISO-PCP, seções 6.1.13 e 6.5 (págs. 9 e 10). |
| 5.7 O relatório de CQ | POP-ISO-PCP, seções 6.1.6, 6.1.12, 6.1.13 e 6.4. |
| 5.8 Se o seu elevador tiver outra configuração | manual do NICE3000new, Tabela 1-1; manual do resgate elétrico. |
| 7.3 O encoder | manual do encoder `Manual_Encoder_Seno_Cosseno_EI53C9.25-2048.pdf`, págs. PDF 1 e 2.; manual NICE3000new, pág. PDF 132 (Figura 3-29, pinos do CN1) e esquema Vitinho, folha /9 (pinos CN1:1 a CN1:13); manual do encoder, pág. PDF 1.; manual NICE3000new, págs. PDF 132 e 133; esquema Vitinho, folha /9; manual do encoder, pág. PDF 1. |
| 7.5 O freio | esquema Vitinho, folha /13 (pág. PDF 15). |
| 7.6 Se o seu elevador tiver outra configuração | manual NICE3000new, págs. PDF 113, 131 e 150 a 153; esquema Vitinho, folhas /7 e /9. |
| 8.2 A caixa de teto MCTC-CTW-B3 | manual CTW-B3, Tabela 2. |
| 8.3 Especificações e instalação | manual CTW-B3, Tabela 3.; manual CTW-B3, Tabela 4 e diagramas; esquema Vitinho 19061867-ZL, folhas /34, /35 e /39 (págs. PDF 36, 37 e 41). |
| 8.4 Bornes da caixa de teto | manual CTW-B3, Tabela 4. A polaridade de 301 e 302 em alguns blocos (por exemplo no WT2) aparece de forma inconsistente no manual; confira no seu equipamento. |
| 8.5 Inspeção do topo da cabina | esquema Vitinho 19061867-ZL, folha /35 (pág. PDF 37). O manual da caixa de teto traz as mesmas redes no terminal Y4. |
| 8.6 A cadeia de segurança na caixa de teto | manual CTW-B3, Tabela 4; esquema Vitinho, folha /34 (pág. PDF 36). |
| 8.8 Iluminação, ventilador, alarme e interfone | manual CTW-B3, Tabelas 1 e 4; esquema Vitinho, folha /39 (pág. PDF 41). |
| 8.9 Placa de comando da cabina | manual CTW-B3, Tabelas 5 a 10, Figuras 6, 8 e 9. |
| 8.10 Armazenamento e manutenção | manual CTW-B3, seção 5. |
| 8.11 Se o seu elevador tiver outra configuração | manual CTW-B3, Tabelas 3 e 4; esquema Vitinho, folhas /34 e /39. |
| 9.2 O que é o operador de porta | manual da caixa de teto MCTC-CTW-B3 (a B3 não inclui o controlador do operador; capítulo 8); manual J4210, seção 4.1. |
| 9.3 O que o quadro espera de qualquer operador | manual CTW-B3, bornes DEN1, DC1, DP e EDP; boletim AD30, pág. 1 e 2.; manual CTW-B3 (bornes DEN1, DC1, DP, EDP1) e boletim AD30 (Figura 1). |
| 9.4 O controlador AD30/NICE900 | boletim AD30, Figura 1 (pág. 2).; boletim "Parametrização de Controlador de Porta NICE900", págs. 1 e 2. |
| 9.5 Ligação do AD30 com a caixa de teto | manual CTW-B3, bornes e figura de ligação; boletim AD30, pág. 2. |
| 9.6 A mecânica da máquina de porta J4210 | manual de instalação e comissionamento da máquina J4210, seções 1.2, 4 e 5. |
| 9.7 Antes de parametrizar | boletim AD30, pág. 3; manual de comissionamento NICE900, págs. 3, 7, 9 e 10. |
| 9.8 Parâmetros do motor e do encoder | boletim AD30, pág. 3; manual de comissionamento NICE900, págs. 3, 4 e 11. |
| 9.9 Os autoajustes | boletim AD30, págs. 4 e 5; manual de comissionamento NICE900, págs. 4 a 8, 11 e 12. |
| 9.10 Se a porta abre ou fecha ao contrário | manual de comissionamento NICE900, pág. 12. |
| 9.11 Problemas comuns e como o fabricante manda resolvê-los | manual J4210, seção 5. |
| 9.12 Manutenção | manual J4210, seção 6. |
| 9.13 O que é igual e o que muda entre operadores | manual CTW-B3, bornes DEN1 e DEN2, DC1 e DC2, EDP1 e EDP2. |
| 10.2 O que sai do quadro de comando | esquema Vitinho 19061867-ZL, folhas /11, /19, /34, /43, /44, /45 e /48 (págs. PDF 13, 21, 36, 45, 46, 47 e 50). |
| 10.3 O cabo de manobra | esquema Vitinho 19061867-ZL, folhas /11, /19, /21, /24, /34 e /38 (págs. PDF 13, 21, 23, 26, 36 e 40); manual da caixa de teto CTW-B3 (manual de A02, figura de fiação). As funções de 123, 125, 130, 131A, 132, 133, 134 e 102 estão no manual da caixa de teto, Tabela 4. |
| 10.4 Os cabos de poço | esquema Vitinho, folhas /19 e /48 (págs. PDF 21 e 50); ficha da KCB (`sources/cap03_fichas_controle.md`). |
| 10.5 As fechaduras das portas de pavimento | esquema Vitinho 19061867-ZL, folhas /19 e /43 (págs. PDF 21 e 45). |
| 10.6 As chaves de posição | manual NICE3000new, seção 2.4, Figura 2-37, pág. PDF 74.; esquema Vitinho, folha /44 (pág. PDF 46). |
| 10.9 Se o seu elevador tiver outra configuração | esquema Vitinho, folhas /19, /43 e /44; manual NICE3000new, seção 2.4. |
| 11.2 O que há no poço | esquema Vitinho 19061867-ZL, folhas /41, /42, /46 e /48 (págs. PDF 43, 44, 48 e 50). |
| 11.3 Os plugues da caixa de inspeção do poço | esquema Vitinho 19061867-ZL, folha /48 (pág. PDF 50). |
| 11.4 A cadeia de segurança no poço | esquema Vitinho, folhas /19 e /41 (págs. PDF 21 e 43). |
| 11.5 A inspeção do poço | esquema Vitinho 19061867-ZL, folhas /42 e /48 (págs. PDF 44 e 50); manual NICE3000new, parâmetros FA-33 e FA-63 (capítulo 12). |
| 11.6 Iluminação, tomadas e interfone | esquema Vitinho, folhas /46 e /48 (págs. PDF 48 e 50). |
| 11.7 Se o seu elevador tiver outra configuração | esquema Vitinho, folhas /19, /41 e /48. |
| 12.1 Ferramentas de comissionamento | manual NICE3000new, págs. PDF 135 a 136 (impressas 134 a 135); manual NICE3000new, págs. PDF 136 a 141 (impressas 135 a 140); manual NICE3000new, pág. PDF 141 (impressa 140) |
| 12.2 Guia de comissionamento do sistema (System Commissioning Guide) | manual NICE3000new, págs. PDF 143 (impressa 142). |
| 12.3 Verificação de segurança e de circuitos (Safety and Circuit Check) | manual NICE3000new, págs. PDF 143 a 145 (impressas 142 a 144). |
| 12.4 Energização e verificação do estado do controlador (Power-on and Controller State Check) | manual NICE3000new, págs. PDF 146 a 148 (impressas 145 a 147). |
| 12.5 Comissionamento em velocidade de inspeção (Commissioning at Inspection Speed) | manual NICE3000new, págs. PDF 149 a 159 (impressas 148 a 158). |
| 12.6 Comissionamento em velocidade normal (Commissioning at Normal Speed) | manual NICE3000new, págs. PDF 160 a 161 (impressas 159 a 160); manual NICE3000new, págs. PDF 162 a 166 (impressas 161 a 165); manual NICE3000new, pág. PDF 167 (impressa 166) |
| 12.7 Ajuste do conforto de viagem (Riding Comfort Adjustment) | manual NICE3000new, págs. PDF 168 a 174 (impressas 167 a 173); manual NICE3000new, págs. PDF 175 a 177 (impressas 174 a 176) |
| 12.9 Se o seu elevador tiver outra configuração | manual NICE3000new, seções 5.4 a 5.6, págs. PDF 150 a 177. |
| 13.2 Como a falha aparece | manual NICE3000new, seção 7.1, pág. PDF 265 (impressa 264), figuras 7-1 e 7-2.; manual NICE3000new, seção 7.1, pág. PDF 265. |
| 13.3 Como reiniciar depois da falha | manual NICE3000new, seção 7.2, pág. PDF 266 (impressa 265).; manual NICE3000new, seção 7.2, pág. PDF 266. |
| 13.4 Os cinco níveis de falha | manual NICE3000new, seção 7.3, Tabela 7-1, pág. PDF 267 (impressa 266).; manual NICE3000new, seção 7.3, Tabela 7-1, pág. PDF 267. |
| 13.5 Como usar a tabela de falhas | manual NICE3000new, seção 7.4, págs. PDF 268 a 289 (impressas 267 a 288). |
| 14.2 Quatro coisas que não se confundem | glossário do projeto; manual NICE3000new, seção 9.13; esquema Vitinho, folha /23. |
| 14.3 O resgate elétrico MCTC-ERB | manual MCTC-ERB-A, págs. PDF 1 e 2 (Tabela 1 e seção de instalação). |
| 14.4 Terminais e ligação | manual MCTC-ERB-A, Figura 5 (pág. PDF 2). |
| 14.5 Indicadores e botões | manual MCTC-ERB-A, págs. PDF 2 (seção 4, Operation Guide). |
| 14.6 Como o resgate elétrico libera o freio | manual MCTC-ERB-A, Figura 6 e seção "Logic of brake release voltage output" (pág. PDF 2).; manual MCTC-ERB-A, págs. PDF 1 e 2. |
| 14.7 Manutenção do resgate elétrico | manual MCTC-ERB-A, págs. PDF 2 e 3 (seções 5 e 6). |
| 14.8 Resgate automático por UPS ou ARD | manual NICE3000new, seção 9.13, págs. PDF 324 a 327. |
| 14.9 Resgate de passageiros: o que a cartilha diz | cartilha "Manual de Resgate" da VerticalParts, VP-RES-01, Rev. 02 (versão para validação técnica), págs. 2 a 12. |
| 14.10 Se o seu elevador tiver outra configuração | manual MCTC-ERB-A; manual NICE3000new, seção 9.13; cartilha VP-RES-01. |

**Seções sem linha "Fonte:" própria** (citam a fonte dentro do texto ou das tabelas, ou usam as fontes do fim do capítulo): 2.5 Alimentação, em uma frase; 3.3 Inversor NICE3000new e placa principal MCB-C3; 3.6 Resgate elétrico ERB-A1; 3.10 Bornes, tomada e terra; 7.2 A máquina de tração; 7.4 Parâmetros do encoder e do motor; 8.7 Nivelamento, renivelamento e pesagem; 10.7 Chamadas externas; 10.8 Iluminação da caixa de corrida; 12.8 Parâmetros do projeto (esquema Vitinho); 13.6 Tabela de falhas.

## F.3 Dados que ainda faltam, por seção

Cada selo `PREENCHER [Qn]` é um dado sem fonte. O livro só é liberado sem nenhum. O assunto vem do controle de issues do projeto.

| Seção | Selo | Assunto |
|---|---|---|
| 1.3 | Q59 | Função de cada chave da cadeia de segurança |
| 1.7 | Q47 | Textos das normas: bloqueio e etiquetagem, cadeia de segurança, acesso ao poço |
| 3.2 | Q85 | Posição da PCB-D1, do QFB4 e da base do quadro; polos do barramento de terra |
| 3.3 | Q82 | Dados do QF, tipo dos QFB3 e QFB4 e proteção diferencial |
| 3.4 | Q83 | Pinos do plugue S2 e posição dos jumpers |
| 3.5 | Q84 | Parâmetros B0 e dados da bobina do freio |
| 3.5 | Q85 | Posição da PCB-D1, do QFB4 e da base do quadro; polos do barramento de terra |
| 3.8 | Q81 | Função de DQFB1, DQFB2 e DQFB3 |
| 3.8 | Q82 | Dados do QF, tipo dos QFB3 e QFB4 e proteção diferencial |
| 3.9 | Q88 | Dados dos contatores SW, BY e FX |
| 3.10 | Q85 | Posição da PCB-D1, do QFB4 e da base do quadro; polos do barramento de terra |
| 4.2 | Q47 | Textos das normas: bloqueio e etiquetagem, cadeia de segurança, acesso ao poço |
| 4.2 | Q115 | Torque de aperto do QF, QFB, DQFB, contatores e bornes de passagem |
| 4.7 | Q83 | Pinos do plugue S2 e posição dos jumpers |
| 4.7 | Q115 | Torque de aperto do QF, QFB, DQFB, contatores e bornes de passagem |
| 4.7 | Q116 | Critério de isolação com megôhmetro antes de energizar |
| 5.2 | Q119 | Critérios do checklist da Qualidade e situação do POP-ISO-PCP |
| 5.4 | Q84 | Parâmetros B0 e dados da bobina do freio |
| 5.4 | Q118 | Valores esperados dos testes de bancada que ainda não têm critério |
| 5.6 | Q119 | Critérios do checklist da Qualidade e situação do POP-ISO-PCP |
| 7.5 | Q84 | Parâmetros B0 e dados da bobina do freio |
| 9.5 | Q108 | Ligação real entre o DEN1 da caixa de teto e o AD30 |
| 9.10 | Q111 | Sentido invertido: trocar U e V, mudar o F215 ou os dois? |
| 11.2 | Q47 | Textos das normas: bloqueio e etiquetagem, cadeia de segurança, acesso ao poço |
| 11.4 | Q59 | Função de cada chave da cadeia de segurança |
| 11.5 | Q104 | Qual é a placa do poço instalada? |
| 14.7 | Q113 | Plano de manutenção periódica do quadro de comando |
| 14.9 | Q114 | A cartilha de resgate da VerticalParts (VP-RES-01 Rev. 02) está aprovada? |
