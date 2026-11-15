# RULES.md: regras do ebook (constituição)

> ATUALIZAÇÃO de 14/11/2026: o Gelson decidiu (Q62) que o produto é uma nova revisão do mesmo livro (Rev. 12 do Livro do Quadro de Comando), com design novo e somando as regras de ebook. Onde a seção 1 abaixo diz "ebook separado", "Rev. 0" ou "sem BOM e sem pendências", vale o PLANO_REV12.md. As demais regras (fonte e página, selos, alertas, glossário, um capítulo por vez) continuam valendo. A base técnica são os esquemas e manuais, não a lista de fios.

Nenhum capítulo pode violar estas regras. Fonte das decisões: rodadas 1 a 6 da entrevista (14/11/2026).

## 1. Produto
- Título: Eletrificação de Elevadores com Monarch NICE3000new e BST Inovance: do Quadro ao Poço.
- Autor: Gelson Simões, Responsável Técnico VerticalParts. Logotipo e identidade visual da VerticalParts.
- Leitor: montador de quadro e técnico de campo.
- Distribuição: NÃO restrita (decisão de 14/11/2026, reverte a Q13 da rodada 2). O aviso legal não pode dizer "distribuição restrita".
- Versão: Rev. 0, independente do livro interno de montagem (que segue em Rev. 12 em diante).
- Tamanho-alvo: 150 a 250 páginas. Formato: PDF gerado de HTML com CSS de impressão e diagramas SVG.

## 2. Escopo
- Geração atual do NICE3000new: MCB-C3, KCB-B4A, PCB-D1, ERB-A1, CTW-B3, AD30/NICE900.
- Elevador de referência: MRL, 3 paradas, 1 porta, 7,5 kW/380 V, sem pesagem, com re-nivelamento, cortina de luz 24 V.
- Variações entram em quadros "Se o seu elevador tiver…" (MR, 2 portas, pesagem, mais paradas).
- Só a variante 380 V é completa. As 220 V saem num adendo depois que as etiquetas reais forem conferidas.
- Geração antiga: só num apêndice de diferenças. A apostila Villarta Monarch serve só para conceitos, nunca para pinagem ou parâmetro.
- Portas: só parte elétrica; mecânica remete ao manual GLORY (T2240 e J2240).
- Decisão de 15/11/2026: os códigos internos de BOM (VPMP, VPB, VPEL) ENTRAM no livro, só no Apêndice B (lista de materiais). Continuam FORA do escopo: chave de afrouxamento de cabos, resgate por desbalanço, NR-12, pendências internas.

## 3. Estrutura
Três Partes e 14 capítulos:
- Parte I Fundamentos: 1 Princípios e cadeia de segurança; 2 Visão geral do sistema.
- Parte II Bancada: 3 Quadro de comando; 4 Montagem e pré-energização; 5 Testes de bancada e relatório de CQ.
- Parte III Campo: 6 Motor, freio e encoder; 7 Caixa de teto e cabina; 8 Operador de porta; 9 Caixa de corrida; 10 Poço; 11 Energização, parâmetros e autoajuste; 12 Resgate elétrico e manutenção; 13 Diagnóstico de falhas; 14 Normas.
- Capítulos com assinatura da Qualidade: 1, 3, 4, 5, 12 e 14. Assinatura geral no fim.
- Elementos de livro (NBR 6029, como método): falsa folha de rosto, folha de rosto e verso, lista de ilustrações, de siglas e de símbolos (IEC 60617), sumário, "Como usar este manual", glossário, apêndices, referências, índice remissivo, colofão. Sem ficha catalográfica, ISBN ou lombada.

## 4. Fontes e rigor
- Nada técnico entra sem fonte e página. Toda tabela, parâmetro, fórmula e figura traz `Fonte:` com documento e página (ou folha do esquema).
- Parâmetros e falhas vêm só do manual `Manual_Usuario_Controlador_NICE3000new_Completo.pdf` (368 páginas; idêntico ao 19010735-A01). Falhas no formato `ErrNN` (a tabela do capítulo 7 do manual traz 66 códigos distintos, de Err02 a Err69; o texto também abrevia alguns como `E57`); grupos F0 a FE, Fb, Fr e FP, conforme o manual. Como o código aparece: o teclado da placa MCB mostra "E", o número e o subcódigo (exemplo E22-101); o painel de operação mostra "Err22" (manual, seção 7.1, pág. PDF 265). Correção de 14/11/2026: uma versão anterior deste arquivo dizia "formato E" como se só existisse esse; os dois formatos existem. O manual de 209 páginas (`467455182…`) não é fonte.
- E88 é indicação de tela durante o teste F8, não falha. Err35 é "Shaft auto-tuning data abnormal" (falha do estudo de poço), manual pág. PDF 278 (impressa 277).
- Tempo de espera após desligar antes de tocar no equipamento: no mínimo 10 minutos (manual, "Safety Instructions", pág. PDF 20 e 21).
- Encoder de referência: EI53C9.25-2048, incremental sin/cos, 5 V, sinais A/A-, B/B-, Z/Z-, C/C-, D/D-. Confirmar o modelo no motor real antes de fechar o capítulo 6.
- Códigos originais (F0-00, E35) ficam ao lado do nome em português.
- Normas: citar NBR 16858, EN 81-20 e NR-10 com item e explicação própria; só entra valor lido na fonte entregue. Normas editoriais (IEC/IEEE 82079-1, NBR 6029, 6024, 6023, IEC 60617) são "método seguido", nunca declaração de conformidade.
- Exemplos resolvidos (só com fórmula citada e com página): desaceleração, bitola e disjuntor, resgate (ERB/UPS), comprimento do cabo de manobra, corrente do freio e resistor de frenagem. Peso e queda de tensão do cabo de manobra só com fórmula de fonte.
- Selos de trabalho do livro interno valem só em rascunhos e em `sources/`; não podem existir no texto final. `[Certeza]` = está escrito num documento da pasta; `[Provável]` = dedução forte, ainda não escrita; `[Chute]` = lacuna preenchida por inferência; `PREENCHER` = dado ausente. Regra de trabalho (decisão do Gelson, 14/11/2026): em vez de deixar um selo, perguntar ao Gelson até ter certeza; o objetivo é que os selos deixem de existir. Proibido inventar: sem certeza, pergunta.
- Qualidade: nos documentos do ebook aparece só o departamento "Qualidade", nunca nomes de pessoas.
- Capítulo sobre qualidade do equipamento e dos acabamentos: decidido que deve existir e ser forte (14/11/2026). Posição, conteúdo e critérios ainda dependem de respostas do Gelson (ver perguntas Q47 a Q52). Os critérios de checklist da Qualidade, no POP-ISO-PCP 6.1.13, estão listados como "a definir pela empresa".

## 5. Segurança e redação
- Quatro níveis de alerta, sempre ANTES do passo perigoso: Perigo, Atenção, Cuidado, Nota.
- Procedimento: verbo no imperativo; ação primeiro, explicação em nota abaixo; no máximo 9 passos por procedimento (regra da casa, sem atribuir à norma).
- Tempo de descarga do barramento CC e qualquer valor de segurança: só do manual do fabricante.
- Terminologia: apenas os termos de `GLOSSARY.md`.

## 6. Ilustração
- SVG para teoria, circuitos, ordem de montagem e fluxos. Diagrama em blocos antes do esquema completo. Callouts numerados, legenda abaixo da figura, figura junto do passo.
- Fotos reais só para "como deve ficar" e para identificar conectores, com callouts. Rostos, números de série e dados sensíveis cobertos antes de entrar; lista de fotos tratadas é mostrada ao Gelson.
- Cores funcionais (potência, comando, terra) valem só nos diagramas. O texto avisa que os fios reais do quadro são pretos e se identificam por anilha.
- Identidade visual: tokens de `009_DesignSystem` (`build/tokens.css`).

## 7. Produção e liberação
- Um capítulo por vez: spec, rascunho, aprovação do Gelson, depois o próximo.
- Critério de pronto: (1) fonte e página em tudo; (2) zero selos de trabalho; (3) termos no glossário; (4) figuras com legenda e fonte; (5) Gelson aprovou; (6) Qualidade assinou, nos capítulos 1, 3, 4, 5, 12 e 14.
- Pendência de lançamento: o registro profissional (CREA ou CFT) do responsável técnico ainda não foi informado. O marcador `PENDENTE-REGISTRO` no verso da folha de rosto bloqueia o build de lançamento.
- O aviso legal precisa de revisão do jurídico ou da Qualidade antes de publicar.
