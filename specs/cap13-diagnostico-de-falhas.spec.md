# Spec: Capítulo 13, Diagnóstico de falhas

Status: SPEC (14/11/2026). Parte IV, Comissionamento. Capítulo novo: o Rev. 11 não tinha tabela de falhas.

## 1. Objetivo pedagógico
Ao terminar, o leitor sabe ler um código de falha do NICE3000new no teclado da placa MCB e no painel de operação, sabe o que cada nível de falha faz com o elevador, sabe reiniciar depois da falha do jeito certo e, dado um código, encontra a causa provável e a ação do manual.

## 2. Leitor e pré-requisito
Montador de quadro e técnico de campo. Pré-requisito: capítulos 1 e 3.

## 3. Conteúdo
1. 13.1 Como a falha aparece: teclado da MCB (código e subcódigo, exemplo E22-101) e painel de operação (Err22); histórico das últimas 10 falhas pelo F-2 igual a 2 (manual 7.1).
2. 13.2 Como reiniciar depois da falha: reinício automático, reset manual (tecla STOP/RES ou F-2 igual a 1) e reset desligando e religando o controlador (manual 7.2).
3. 13.3 Os cinco níveis de falha (manual 7.3, Tabela 7-1) e o que cada subnível faz.
4. 13.4 Como usar a tabela de falhas (colunas, subcódigos, notas).
5. 13.5 Tabela de falhas Err02 a Err69, com nome em português, nível, causas e ações, traduzidas do manual (7.4).
6. 13.6 Falhas que o livro cita em outros capítulos (Err35, Err41, Err42) com remissão.
7. 13.7 Roteiro de diagnóstico por sintoma (só com o que o manual diz; sem inventar árvore de decisão).

## 4. Fontes permitidas
- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`, capítulo 7, págs. PDF 264 a 289 (impressas 263 a 288); parâmetros dos grupos E0 a E9 e FC-11 a FC-210 só por remissão.
- Esquema Vitinho 19061867-ZL, só para remissões a conectores e redes.
- Extratos em `sources/cap13_falhas_err02_err34.md` e `sources/cap13_falhas_err35_err69.md`.

## 5. Fora de escopo
Parâmetros do inversor (capítulo 12), tabela de falhas do manual antigo (não vale para o NICE3000new), falhas da caixa de teto CTW-B3 e do operador de porta (capítulos 8 e 9), qualquer causa ou solução que o manual não traga.

## 6. Figuras previstas
1. Como o código aparece no teclado e no painel (SVG, com E22-101 e Err22).
2. Quadro dos cinco níveis de falha, com o que o elevador faz em cada um.
3. Fluxo de reinício depois da falha (automático, manual, religando).

## 7. Alertas obrigatórios
Espera de 10 minutos e desenergização antes de qualquer verificação nos bornes; nunca pontear a cadeia de segurança para "testar" uma falha (remissão ao capítulo 1); desligar antes de trocar fiação do encoder ou do motor.

## 8. Perguntas de verificação
1. Qual é a diferença entre "E22-101" e "Err22"?
2. O que diferencia a falha de nível 5 da de nível 3?
3. Quando é preciso desligar e religar o controlador para reiniciar?
4. Onde se vê o histórico das últimas 10 falhas?
5. O que o manual manda verificar na Err41?

## 9. Dependências do Gelson
Aprovar o texto traduzido do capítulo (a tabela é tradução do manual; a revisão técnica é dele e da Qualidade). Indicar se o roteiro por sintoma deve entrar ou ficar para depois.
