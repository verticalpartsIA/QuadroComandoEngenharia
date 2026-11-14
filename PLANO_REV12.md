# PLANO_REV12.md: melhoria do Livro do Quadro de Comando (Rev. 11 para Rev. 12)

Status: PLANO PARA APROVAÇÃO (14/11/2026). Nada do Rev. 11 foi alterado.
Decisão do Gelson em 14/11/2026: o produto é uma nova revisão do mesmo livro (Q62), com design novo e somando as novas informações e as regras de ebook. Isso substitui a ideia de ebook separado em Rev. 0 (RULES.md, seção 1, decisões de "Versão" e de excluir BOM e pendências).

## 1. Princípio que muda
O Rev. 11 diz na capa que foi "gerado a partir da Lista de fios". Isso inverte a ordem certa. No Rev. 12:
1. A base de verdade são os esquemas elétricos e os manuais dos fabricantes (pasta `Conhecimento_Claude\PDF`, 83 arquivos).
2. A lista de fios deixa de ser a base. Vira um apêndice que sai dos esquemas e é conferido contra eles, ligação por ligação. Onde a lista divergir do esquema, o esquema vale e a divergência fica registrada.
3. Cada afirmação técnica cita o documento e a página (regra da casa).

## 2. Estrutura proposta do Rev. 12
- **Parte I. Fundamentos:** 1 Princípios e cadeia de segurança (rascunho v0.1 pronto); 2 Visão geral do sistema.
- **Parte II. O quadro de comando:** 3 Componentes do quadro (reescrito a partir dos esquemas; aproveita as seções 1 a 8 do Rev. 11); 4 Montagem e pré-energização (conferências do Rev. 11, págs. 11 a 15 e 34 e 35); 5 Testes de bancada e relatório de CQ; 6 Qualidade do equipamento e dos acabamentos (em espera, ver STANDBY.md).
- **Parte III. Instalação em campo:** 7 Motor, freio e encoder; 8 Caixa de teto e cabina (Parte III do Rev. 11); 9 Operador de porta AD30/NICE900; 10 Caixa de corrida e cabos de manobra (Parte II do Rev. 11); 11 Poço (Parte IV do Rev. 11).
- **Parte IV. Comissionamento:** 12 Energização, parâmetros e autoajuste; 13 Resgate elétrico e manutenção; 14 Diagnóstico de falhas (tabela do manual, Err02 a Err69).
- **Parte V. Normas:** 15 NBR 16858, EN 81-20 e NR-10 (texto das normas pendente, STANDBY.md).
- **Apêndices:** A. Lista de fios derivada dos esquemas e conferida; B. Lista de materiais e comparativo das variantes; C. Pendências abertas (cada uma com dono e data; sai do livro quando resolvida); D. Glossário; E. Índice remissivo; F. Rastreabilidade (cada fio ou dado, o documento e a página).

Numeração provisória: ela muda se você decidir de outro jeito.

## 3. O que se reaproveita do Rev. 11 e o que muda
| Do Rev. 11 | O que acontece |
|---|---|
| Glossário, árvore do diagrama, convenções | Mantém e amplia. A árvore passa a ser um diagrama em SVG. |
| Pendências P1 a P20 (e as P21 a P50 citadas) | Mantém no Apêndice C. Cada uma ganha dono, data e fonte para resolver. |
| Layout do quadro (desenho em texto) | Refaz em SVG, com callouts numerados, a partir das fotos. |
| Seções por peça (1 a 8) | Reescreve a partir do esquema e do manual de cada peça, com a fiação conferida. |
| Tabela mestre dos 125 fios | Vai para o Apêndice A, derivada e verificada. |
| Partes II, III e IV (cabos de campo, caixa de teto, poço) | Reescreve nos capítulos 8, 10 e 11, com a pinagem conferida nos esquemas e no manual da CTW-B3. |
| Selos `[Certeza]`, `[Provável]`, `[Chute]` e `PREENCHER` | Continuam nos rascunhos. No Rev. 12 liberado, nenhum selo; o que sobrar vira pendência no Apêndice C. |

## 4. Design novo
- Identidade: tokens do `009_DesignSystem` (já extraídos em `build/tokens.css`), logotipo, Poppins.
- Quatro níveis de alerta (Perigo, Atenção, Cuidado, Nota), sempre antes do passo perigoso.
- Diagramas em SVG, com cores funcionais só nos desenhos; fotos reais com callouts numerados.
- Procedimentos: verbo no imperativo, ação antes da explicação, até 9 passos.
- Elementos de livro (NBR 6029 como método): folha de rosto, listas de ilustrações, siglas e símbolos, sumário, "Como usar", glossário, índice remissivo, colofão.
- PDF com marcadores e links internos, como o Rev. 11 já tem.

## 5. Regras que valem (do que já foi decidido)
Ver RULES.md. Em resumo: nada sem fonte e página; parâmetros e falhas só do manual de 368 páginas; nenhuma afirmação de conformidade com norma sem o texto; terminologia do GLOSSARY.md; um capítulo por vez, com sua aprovação; assinatura da Qualidade nos capítulos de segurança.

## 6. Como o trabalho anda (marcos)
1. **Marco 1. Este plano aprovado.**
2. **Marco 2. Auditoria do Rev. 11:** lista de divergências com página e fonte (lista de fios contra esquemas, textos contra manuais), em arquivo `.md`, sem alterar o livro. Por parte, na ordem das seções.
3. **Marco 3. Rev. 12 base:** conteúdo atual corrigido, com o design novo e o Capítulo 1 integrado.
4. **Marco 4 em diante:** capítulos novos, um de cada vez (spec, rascunho, sua aprovação).
Datas: dependem das suas respostas e do material pendente. Cada marco entrega um arquivo que você pode abrir.

## 7. Pendências que travam capítulos (de STANDBY.md)
Texto da NR-10, NBR 16858 e EN 81-20; respostas Q54, Q59 e Q60; capítulo de qualidade (Q49 a Q52); registro CREA ou CFT; manual de resgate aprovado; encoder do motor real; etiquetas das variantes 220 V.
