# Spec: Capítulo 1, Princípios e cadeia de segurança

Status: SPEC EM REVISÃO (nada escrito ainda). Capítulo com assinatura da Qualidade.
Parte I, Fundamentos.

## 1. Objetivo pedagógico
Ao terminar, o leitor sabe explicar, sem olhar o esquema: o que é um elevador MRL, o caminho da cadeia de segurança do poço à cabina e ao quadro, por que cada contato dela existe, e como trabalhar com segurança no quadro (desenergizar, bloquear, etiquetar, esperar a descarga).

## 2. Leitor e pré-requisitos
Montador de quadro e técnico de campo. Pré-requisito: eletricidade básica (tensão, corrente, contato NA e NF). O capítulo explica o resto.

## 3. Conteúdo previsto (a confirmar com o Gelson)
1. O que é um elevador MRL: componentes do quadro ao poço, em um diagrama em blocos (SVG).
2. Conceito da cadeia de segurança: série de contatos NF que, se qualquer um abrir, para o elevador. Quais dispositivos entram no elevador de referência (poço, cabina, caixa de corrida, fechaduras das portas de pavimento).
3. Fechaduras das portas e circuito de portas: papel de cada contato.
4. Entradas do inversor que recebem a cadeia (X25 a X27 no NICE3000new).
5. Bypass de porta e modo inspeção: o que ligam e o risco de deixar em bypass.
6. Segurança do trabalho no quadro: desenergização, LOTO (bloqueio e etiquetagem), descarga do barramento CC, EPI. Base: NR-10 e manual do fabricante.
7. Quadro "Se o seu elevador tiver…": porta traseira e outras variações da cadeia.

## 4. Fontes permitidas (páginas PDF candidatas, ainda NÃO lidas, a confirmar antes de usar)
- Manual NICE3000new (368 pp.): cadeia e circuito de portas em torno das pp. 144, 148, 199, 281 a 284, 338; inspeção em pp. 148, 159, 200, 293; descarga e barramento CC em pp. 20, 21, 52, 53; capacitores em pp. 297 e 348.
- Esquema Vitinho 19061867-ZL: folhas /18, /19 (cadeia), /34, /35 (cabina), /41, /42, /43 (poço e fechaduras). Página do PDF = número do carimbo + 2.
- Esquema VerticalParts 19060918-ZL, para comparar com o Vitinho.
- Apostila Villarta Monarch V5.0: só conceito.
- NR-10, NBR 16858 e EN 81-20: texto ainda NÃO fornecido. Nenhum valor ou item de norma entra até o Gelson passar o trecho.

## 4b. Cadeia de segurança verificada no esquema (lido em 14/11/2026)
Fonte: Vitinho 19061867-ZL, folha /19 "General drawing of system safety circuit (D1/D2/D3)", PDF pág. 21, e folha /41 "Safety circuit wiring diagram in pit", PDF pág. 43.
Dispositivos que aparecem na cadeia (ordem de leitura do desenho, da esquerda para a direita; a ordem exata de ligação ainda será conferida no rascunho):
- Fusível F3 (250 VAC / 1 A) e jumper SZ ("Use for MRL").
- MES, botão de parada do quadro (rotulado "Emergent stop button").
- PES2 e PES1, botões de parada do poço ("Pit emergency stop button 1").
- GTS, chave elétrica da polia tensora ("Tensioner electric switch").
- Chave de inspeção do poço PIT, com PITU, PITD e PITB.
- BFS1 e BFS2. O Vitinho 19061867-ZL rotula só "Buffer switch 1" e "Buffer switch 2". O esquema VerticalParts 19060918-ZL (PDF pág. 30 e legenda na pág. 12) diz: BFS1 = "Contato do parachoque do carro" e BFS2 = "Contato do parachoque do contrapeso". Decisão do Gelson (Q56): no texto, "chave do amortecedor 1" e "chave do amortecedor 2" até ele confirmar que vale a atribuição do esquema VerticalParts.
- FLSD ("Down ultimate switch") e FLSU ("Up ultimate switch"), ambos contatos na cadeia. Ordem no desenho da folha /19: rede 119, FLSD, rede 120, FLSU, rede 121 (correção de 14/11/2026: a frase anterior, "ligados à rede 121", vinha do Rev. 11 e estava incompleta; a auditoria do lote 7b apontou o erro). A folha /41 mostra os dois na caixa de corrida, cada um com um terminal em PE.
- CIS: o mesmo componente tem dois rótulos no Vitinho. "Emergency electric operation switch" (folha /14, PDF pág. 16, parte do "Emergency electric operation handle KKB4-1C-02", junto com CIU E, CID E e MES) e "Emergency insp. switch" (folha /19). A folha /14 também mostra o "Bypass plug" no conector S1 da KCB. Não há rótulo em português no Vitinho. O esquema VerticalParts 19060918-ZL (PDF pág. 6 e legenda na pág. 12) o chama "CIS - Chave manual/automático da botoeira de resgate". Decisão do Gelson (Q58): no texto, "chave de operação elétrica de emergência (CIS)", com a nota de que o esquema também a rotula "chave de inspeção de emergência".
- SOS, "Safety gear electric switch" (cunha de segurança da cabina).
- TCI, chave de inspeção da caixa de teto; TCIU, TCID e TCIB (botões de inspeção); TES, botão de parada da caixa de teto.
- Opcionais ("When needed, otherwise short circuit", no desenho): RCS (rope gripper switch), CWSG ("Counterweight Safety gear electric switch") e OS-G ("Counterweight Speed governor electric switch", ou seja, do contrapeso, NÃO o limitador principal). Se o elevador de referência tem ou não cada um deles: os documentos não dizem e o Gelson não tem a resposta (14/11/2026). Selo no rascunho: `PREENCHER [Q54]` em cada menção. O selo bloqueia o build de lançamento.
- Caixa de teto (folha /34, PDF pág. 36): SOS (123 e 123A), MSC (123A e 124, desenhado com jumper curto 10 a 12), SUP2 (127 e 129), SUP1 (129 e 130), GS1 (porta de cabina, 130 e 131A) e GS2 (porta traseira, 133 e 134). Para um elevador de 1 porta, GS2 e as fechaduras traseiras nRDS ficam fora.
- Fechaduras das portas (folha /43, PDF pág. 45): 1DS, 2DS e nDS (portas de pavimento) e 1RDS, 2RDS e nRDS (traseiras, fora do escopo). Cada contato tem PE.
- Só para casa de máquinas ("Use for MR"): HW / MES-1, parada do volante. Fora do escopo MRL.
- Circuito de fechaduras: GS1 (porta de cabina), 1DS, 2DS e nDS (portas de pavimento), com o bypass S2. Rede 131, 132, 133 e 134 para as entradas X26, X28 e X27 do CN2; a cadeia de segurança chega à entrada X25.
Itens que o texto de apoio trouxe e o desenho NÃO confirma: BFS1 = carro e BFS2 = contrapeso (a palavra "counterweight" só aparece em CWSG e OS-G; a folha /48 do poço rotula apenas "Buffer 1" e "Buffer 2"); "a cadeia abre e desenergiza os contatores de marcha e freio" (o desenho só mostra a cadeia chegando ao CN2; a falha correspondente no manual é Err41, "Safety circuit disconnected").

## 5. Fora de escopo
Parâmetros do inversor (cap. 11), diagnóstico de falhas (cap. 13), montagem e fiação do quadro (caps. 3 e 4), normas em detalhe (cap. 14), NR-12, chave de afrouxamento de cabos, resgate por desbalanço.

## 6. Figuras previstas (SVG, legenda e fonte em todas)
1. Diagrama em blocos do elevador MRL.
2. Cadeia de segurança em série, do poço ao quadro, com cores funcionais só no desenho.
3. Fluxo de bloqueio e etiquetagem do quadro, passo a passo.

## 7. Alertas obrigatórios (antes do passo perigoso)
- Perigo: tensão presente no quadro e no barramento CC após desligar. Espera mínima de 10 minutos após desligar, manual NICE3000new "Safety Instructions", pág. PDF 20 e 21 (lido e confirmado em 14/11/2026). O manual também exige aterramento confiável, nunca ligar a rede nos bornes U, V, W e pulseira antiestática.
- Atenção: bypass de porta ou de segurança esquecido ligado.
- Cuidado: descarga eletrostática ao manusear placas, se o manual afirmar.

## 8. Perguntas de verificação (o leitor responde depois de ler)
1. Qual contato abre se alguém abrir a porta de um pavimento com a cabina em movimento, e o que o inversor faz?
2. Em que sequência se desenergiza e se bloqueia o quadro antes de abrir o inversor?
3. Quanto tempo se espera antes de tocar nos bornes de potência, e de onde vem esse valor?
4. O que o bypass de porta liga e quando é permitido usá-lo?
5. Por que a cadeia usa contatos NF e não NA?

## 9. Testes do capítulo (a implementar em `tests/`)
- Nenhum selo de trabalho (`[Certeza]`, `[Provável]`, `[Chute]`, `PREENCHER`).
- Toda tabela e figura com `Fonte:` e página.
- Todo passo perigoso com alerta antes.
- Todo termo técnico no `GLOSSARY.md`.
- Nenhuma citação de norma sem trecho fornecido.

## 10. Dependências do Gelson
- Fornecer o texto ou os itens da NR-10 e da NBR 16858 que tratam de bloqueio, etiquetagem e cadeia de segurança.
- Confirmar o elevador de referência (3 paradas, 1 porta, sem pesagem) e quais contatos da cadeia ele realmente tem.
- A assinatura é do departamento "Qualidade" (sem nome de pessoa).
