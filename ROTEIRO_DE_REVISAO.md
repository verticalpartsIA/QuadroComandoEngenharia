# ROTEIRO_DE_REVISAO.md: o que revisar e o que responder (14/11/2026)

Este roteiro reúne, em um só lugar, o que está pronto, o que você precisa revisar e tudo o que está em aberto, com o jeito de fechar cada item. Pare aqui, revise, vá ao quadro e responda pelo número.

PDF atual: `build/out/Livro_Quadro_de_Comando_NICE3000_VerticalParts_Rev12_base_v0-1.pdf` (135 páginas). Se o PDF antigo estiver aberto no leitor, o Windows impede a gravação e o build gera `..._atualizado.pdf`: abra esse. Para gerar de novo: `python build/build_livro.py`.

## 1. Estado do livro

| Capítulo | Páginas no PDF | Estado | Selos abertos |
|---|---|---|---|
| Capa, controle do documento, aviso legal | 1 e 2 | rascunho | registro CREA ou CFT |
| 1. Princípios e cadeia de segurança | 6 a 12 | rascunho | Q47, Q54, Q59, Q60 |
| 2. Visão geral do sistema | 13 a 17 | rascunho | Q92 |
| 3. Componentes do quadro de comando | 18 a 30 | texto aprovado | Q79 a Q88 |
| 8. Caixa de teto e cabina | 31 a 39 | rascunho | Q98, Q99 |
| 7. Motor, freio e encoder | 40 a 45 | rascunho | Q84, Q95, Q96 |
| 12. Energização, parâmetros e autoajuste | 46 a 91 | rascunho | (dados do motor, no checklist) |
| 13. Diagnóstico de falhas | 92 a 126 | revisado por você | nenhum |
| Apêndice A. Lista de fios conferida | 127 a 133 | rascunho | nenhum |
| Apêndice C. Pendências e correções | 134 a 135 | rascunho | nenhum |

Faltam: 4 (montagem), 5 (testes de bancada), 6 (qualidade, em espera), 9 (operador de porta), 10 (caixa de corrida), 11 (poço), 14 (resgate elétrico e manutenção), 15 (normas) e os apêndices B (materiais), D (glossário), E (índice remissivo) e F (rastreabilidade).

## 2. O que você revisa (nesta ordem)

1. Capítulo 2 (páginas 13 a 17): a lista de componentes e as regras do RS-485 estão certas?
2. Capítulo 7 (páginas 31 a 36): em especial a tabela de ligação da PG-E ao encoder (é correspondência por nome de sinal, não vem pronta de documento).
3. Capítulo 12 (páginas 37 a 82): é tradução do manual; revise a seção 12.8 (parâmetros do projeto) e as 12 divergências entre o esquema e o manual.
4. Capítulo 1 (páginas 6 a 12): o alerta sobre os jumpers de bancada e a velocidade de emergência (F3-25 ou F3-26).
5. Apêndice A (páginas 118 a 124): as 22 divergências da lista de fios, em especial L e N da resgate elétrica (fios 20 e 94) e os jumpers 62 a 66.

## 3. O que só o quadro real responde (ida ao quadro)

Use `CHECKLIST_QUADRO_FISICO.md` (21 itens, com o quadro desligado e depois de esperar 10 minutos; só ler etiquetas e fotografar). Fecha: Q54, Q60, Q71, Q98, Q99, Q79, Q80, Q81, Q82, Q83, Q84, Q85, Q86, Q87, Q88, Q92, Q95 e Q96.

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
