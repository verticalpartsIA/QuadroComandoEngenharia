# ROTEIRO_DE_REVISAO.md: o que revisar e o que responder (14/11/2026)

Este roteiro reúne, em um só lugar, o que está pronto, o que você precisa revisar e tudo o que está em aberto, com o jeito de fechar cada item. Pare aqui, revise, vá ao quadro e responda pelo número.

PDF atual: `build/out/Livro_Quadro_de_Comando_NICE3000_VerticalParts_Rev12_base_v0-1.pdf` (121 páginas). Se o PDF antigo estiver aberto no leitor, o Windows impede a gravação e o build gera `..._atualizado.pdf`: abra esse. Para gerar de novo: `python build/build_livro.py`.

## 1. Estado do livro

| Capítulo | Páginas no PDF | Estado | Selos abertos |
|---|---|---|---|
| Capa, controle do documento, aviso legal | 1 e 2 | rascunho | registro CREA ou CFT |
| 1. Princípios e cadeia de segurança | 6 a 11 | rascunho | Q47, Q54, Q59, Q60 |
| 2. Visão geral do sistema | 12 a 15 | rascunho | Q92 |
| 3. Componentes do quadro de comando | 16 a 26 | texto aprovado | Q79 a Q88 |
| 7. Motor, freio e encoder | 27 a 32 | rascunho | Q84, Q95, Q96 |
| 8. Caixa de teto e cabina | 33 a 39 | rascunho | Q98, Q99 |
| 10. Caixa de corrida e cabos de manobra | 40 a 46 | rascunho | Q98, Q101, Q102 |
| 11. Poço | 47 a 50 | rascunho | Q47, Q59, Q101, Q104 |
| 12. Energização, parâmetros e autoajuste | 51 a 85 | rascunho | (dados do motor, no checklist) |
| 13. Diagnóstico de falhas | 86 a 113 | revisado por você | nenhum |
| Apêndice A. Lista de fios conferida | 114 a 119 | rascunho | nenhum |
| Apêndice C. Pendências e correções | 120 a 121 | rascunho | nenhum |

Faltam: 4 (montagem), 5 (testes de bancada), 6 (qualidade, em espera), 9 (operador de porta), 14 (resgate elétrico e manutenção), 15 (normas) e os apêndices B (materiais), D (glossário), E (índice remissivo) e F (rastreabilidade).

## 2. O que você revisa (nesta ordem)

1. Capítulo 2 (páginas 13 a 17): a lista de componentes e as regras do RS-485 estão certas?
2. Capítulo 7 (páginas 31 a 36): em especial a tabela de ligação da PG-E ao encoder (é correspondência por nome de sinal, não vem pronta de documento).
3. Capítulo 12 (páginas 37 a 82): é tradução do manual; revise a seção 12.8 (parâmetros do projeto) e as 12 divergências entre o esquema e o manual.
4. Capítulo 1 (páginas 6 a 12): o alerta sobre os jumpers de bancada e a velocidade de emergência (F3-25 ou F3-26).
5. Apêndice A (páginas 118 a 124): as 22 divergências da lista de fios, em especial L e N da resgate elétrica (fios 20 e 94) e os jumpers 62 a 66.

## 3. O que só o quadro real responde (ida ao quadro)

Use `CHECKLIST_QUADRO_FISICO.md` (21 itens, com o quadro desligado e depois de esperar 10 minutos; só ler etiquetas e fotografar). Fecha: Q54, Q60, Q71, Q98, Q99, Q101, Q102, Q104, Q79, Q80, Q81, Q82, Q83, Q84, Q85, Q86, Q87, Q88, Q92, Q95 e Q96.

## 4. O que só você decide ou fornece

| Item | O que preciso |
|---|---|
| Registro CREA ou CFT (verso da folha de rosto) | número e nome completo; bloqueia o lançamento |
| Q47 | texto da NR-10, da NBR 16858 e da EN 81-20 sobre bloqueio e etiquetagem e cadeia de segurança |
| Q59 | material do fabricante (BST) ou explicação sua sobre o que cada chave da cadeia detecta |
| Q56 | confirmar que BFS1 é o amortecedor do carro e BFS2 o do contrapeso (o esquema VerticalParts diz isso) |
| NR-12 | em espera (fora do livro por enquanto) |
| Q49 a Q52 | capítulo de qualidade do equipamento e dos acabamentos: posição, critérios, checklist da Qualidade e fotos de conforme e não conforme (em espera) |
| Manual de Resgate da VerticalParts | confirmar que está aprovado (vai para o capítulo 14) |
| 220 V | etiquetas reais do inversor, do trafo e a origem dos 220 V, para o adendo |
| Revisão da Qualidade | quem assina os capítulos 1, 3, 4, 5, 12 e 14 (só o departamento "Qualidade") |

## 5. Como responder

Responda pelo número ("Q79: NICE-L-C-4007"). Qualquer resposta que a documentação não confirme, eu registro com a sua fonte e, se a documentação contradizer, mostro a contradição antes de escrever.

## 6. Depois da revisão

1. Fecho os selos com as suas respostas e removo cada selo resolvido.
2. Retomo os capítulos que faltam, na ordem que você escolher (sugestão: 8, 10, 11, 4, 5, 9, 14).
3. Rodo os testes de qualidade do livro (nenhum selo, fonte e página em tudo, alertas antes dos passos perigosos).
4. A Qualidade assina os capítulos de segurança e o livro sai como Rev. 12.

## Capítulo 9, Operador de porta (15/11/2026)
Rascunho v0.1 (págs. 40 a 47 do PDF atual). Duas camadas: interface do quadro com qualquer operador (9.3) e exemplo AD30/NICE900 com a máquina J4210. O que revisar:
1. Seção 9.3: a lista de sinais vale para todos os operadores? Confirmar contra o seu conhecimento de campo.
2. Seção 9.5: só as 5 primeiras ligações têm base em manual; as 4 últimas são correspondência de função (issue #28).
3. Seções 9.8 a 9.10: mostram os dois documentos do fabricante lado a lado (notação e método de autoajuste), sem escolher um (issues #26, #30 e #31).
4. Seção 9.6 e 9.11: cotas e folhas tiradas do manual J4210, em inglês, traduzidas por mim.
Selos: Q106 a Q111 (issues #26 a #31). Apoio não citado: manual Glarie, NICE3000new antigo, BST BG101/BG201, brochura J5801.

## Capítulo 14, Resgate elétrico e manutenção (15/11/2026)
Rascunho v0.1. Fontes: manual do ERB (Inovance), manual NICE3000new seção 9.13 (UPS e ARD) e cartilha VP-RES-01 Rev. 02 (versão para validação). O que revisar:
1. Seção 14.2: a distinção entre os quatro termos bate com o glossário e com o seu uso em campo?
2. Seção 14.6: sequência de liberação do freio, só o que o manual do dispositivo diz. O manual tem uma caixa "Press the buttons for at least 120s" no fluxograma que não ficou clara; o livro usa só o texto (110 V por 2 s, 80 V por até 120 s, 3 ciclos, 10 min).
3. Seção 14.9: resume a cartilha sem acrescentar passos de resgate; a VerticalParts não faz resgate.
4. Capítulo 3, seção 3.6: remissão corrigida do capítulo 13 para o 14.
Selos: Q86 (A1 ou A2; issue encerrada), Q112 a Q114 (issues abertas).

## Capítulo 4, Montagem e pré-energização (15/11/2026)
Rascunho v0.1. Fontes: manual NICE3000new (cap. 2), esquema Vitinho, manual do ERB e a prática do Rev. 11 (págs. 11 e 12) só no que tem fonte. O que revisar:
1. Seção 4.4: a ordem de 12 etapas é a oficial? (issue Q117).
2. Seção 4.6: o cabo plano usa X14 = subida 1, X15 = descida 1, X16 = subida 2 e X17 = descida 2 (o Rev. 11 tinha X15 e X16 trocados). W1 a W6 não foram mapeados porque a legenda do esquema conflita.
3. Seção 4.7: valores com fonte (terra < 10 Ω, CAN e RS-485 cerca de 60 Ω, torques do inversor); isolação com megôhmetro e torque dos demais componentes ficam como selo (Q116 e Q115).
4. Ficou de fora, de propósito: quadro de corte de fios com bitola e comprimento (vem da lista de fios; fica no Apêndice A), páginas 34 e 35 do Rev. 11 (manual antigo), e o formulário do contrato (capítulo 10).
Selos: Q115, Q116, Q117 (issues abertas).

## Capítulo 5, Testes de bancada e relatório de CQ (15/11/2026)
Rascunho v0.1. Fontes: POP-ISO-PCP Rev. 00, Rev. 11 págs. 32 e 33 (E1 a E12 e R1 a R8, com as correções da auditoria), manual do ERB, esquema Vitinho. O que revisar:
1. Seção 5.2: o caminho Automação, Qualidade, Expedição bate com a prática da fábrica? O POP está em Rev. 00 com código "xxx" e setor "Financeiro" (issue Q119).
2. Seção 5.4: E5, E9, E11 e E12 ficaram sem valor esperado (issue Q118). E6 corrigido (24 V saem da PCB-D1 para a KCB).
3. Seção 5.5: R3 corrigido para 187 a 242 V; R4 corrigido (o indicador azul só indica a posição quando a rede faltou).
4. Seção 5.6 e 5.7: checklist da Qualidade e modelo do relatório de CQ vêm só do POP; critérios por item ficam em espera (Q49 a Q52).
Selos: Q118 e Q119 (issues abertas).

