# Spec: Capítulo 9, Operador de porta (interface do quadro e exemplo AD30/NICE900 com máquina J4210)

Status: SPEC (15/11/2026). Parte III, Instalação em campo. Aguarda aprovação do Gelson antes do rascunho.

## 1. Objetivo pedagógico
Ao terminar, o leitor sabe o que é o operador de porta e como ele conversa com a caixa de teto e o quadro; liga o controlador AD30/NICE900 (potência, encoder, entradas e saídas); ajusta e confere a parte mecânica da máquina J4210; configura o motor e o encoder, faz os dois autoajustes (motor e largura da porta); e corrige o sentido invertido.

## 2. Leitor e pré-requisito
Montador e técnico de campo. Pré-requisito: capítulos 2 e 8 (caixa de teto, bornes DEN1/DC1/DP).

## 2.1 Decisão do responsável técnico (15/11/2026)
O quadro de comando conversa com **muitos operadores de porta**, não com um só. Por isso o capítulo se organiza em duas camadas: (a) a **interface do quadro** com qualquer operador (alimentação, comandos de abrir e fechar, limites, cortina, fechamento forçado, proteção térmica), que vale para todos; (b) o **AD30/NICE900 com a máquina J4210** como **exemplo trabalhado**, porque é o único com documentação completa na base. Para outros operadores, o leitor segue o manual do fabricante, e o livro indica o que conferir na interface. Q107 deixa de pedir "qual é o operador" e passa a pedir só "qual é o operador do elevador de referência", se houver.

## 3. Conteúdo
1. 9.1 O que você vai aprender e alerta de segurança (desligar, esperar descarga, porta livre).
2. 9.2 O que é o operador de porta: máquina (motor síncrono de ímã permanente com encoder, polias, correia/cabo de aço, faca da porta) e controlador. Estrutura da máquina J4210 (Figura 1 do manual J4210).
3. 9.3 O controlador AD30/NICE900: três blocos de ligação (potência da rede, motor, encoder), entradas digitais DI1 a DI8 e saídas a relé; padrão de fábrica (DI1 abrir, DI2 fechar, DI3 cortina de luz, DI4 fechamento forçado; DO1/TC1 limite de porta aberta, DO2/TC2 limite de porta fechada, DO3 fechamento impedido, DO4 falha). Tabela terminal a terminal e figura de ligação.
4. 9.4 Ligação com a caixa de teto: DC1 (207, 208, PE) alimenta L, N, PE; DEN1 (B1, B2, B3, BM, X3, X5, 301) comanda e lê limites. Marcar como correspondência de função onde a fonte não documenta (ver Q108).
5. 9.5 Instalação mecânica da máquina J4210: fixação do controlador, distância de 32 mm da placa traseira à borda da cabina, abertura lateral (X = PL + 20), roldana superior (folga de 0,2 a 0,5 mm), faca de acionamento (folga do gancho de 0,3 a 1 mm), folga entre faca e rolete (10 ± 1 mm), folga painel e soleira (3 a 5 mm).
6. 9.6 Antes de parametrizar: anotar parâmetros, restaurar o padrão de fábrica (FP-01 igual a 1), conferir se a porta corre livre, painel de operação (teclas).
7. 9.7 Parâmetros do motor e do encoder (tipo de encoder, pulsos, tipo de motor, potência, tensão, corrente, frequência, rotação) e onde está a placa do motor.
8. 9.8 Autoajuste do motor e da largura da porta, pelos dois métodos das fontes: boletim AD30 (PRG + seta para a direita, TUNE1 e TUNE2) e manual de comissionamento NICE900 (F116, tecla ENTER, TUNE, teste a 5 Hz; autoajuste da largura por F600 e F601, leitura em F602 e F603). Cada um com sua notação, lado a lado.
9. 9.9 Sentido de abertura e fechamento invertido.
10. 9.10 Problemas comuns de mecânica (J4210, seção 5): batida ao fechar, limite de abertura por resistência, faca que não solta, lubrificante na guia, porta que rebate (1 a 2 mm).
11. 9.11 Manutenção (J4210, seção 6) em lista curta.
12. 9.12 O que é igual e o que muda entre operadores (interface comum: alimentação, abrir, fechar, limites, obstrução, fechamento forçado, falha; muda a numeração de parâmetros, o autoajuste e o painel). Se o seu elevador tiver outra configuração (duas portas, com pesagem, outro operador).
13. 9.13 Teste o que você aprendeu.

## 4. Fontes permitidas
- Boletim "Parametrização de Controlador de Porta NICE900" (`Parametrização do AD30 (Motor Síncrono).pdf`, 5 págs.).
- `Manual_Comissionamento_NICE900_VerticalParts.pdf` (12 págs., versão 1.0, fevereiro de 2026).
- `Manual_Instrucoes_Operador_de_Porta_J4210-T2.pdf` (16 págs., 22/03/2024, em inglês).
- Manual da caixa de teto CTW-B3 e esquema Vitinho 19061867-ZL, só para a interface DEN1/DC1/DP (já lida no capítulo 8).
- Catálogo `Catalogo_Operadores_de_Porta_BST_2019.pdf`, só se o Gelson confirmar que o operador é da BST (Q107).

- Manual de depuração da Glarie GKL-01 (`639728241-manual-de-programacion-de-glarie.pdf`): **apoio de conhecimento, não fonte**. Trata da placa principal GKL-01 e do inversor de tração; não traz o controlador de porta NICE900/AD30 nem o F215. Não se cita no livro.
- `403327582-New-monarch-nice-3000-pdf.pdf` (Scribd, 233 págs., inglês): edição mais antiga do manual do NICE3000new (Suzhou Monarch). **Apoio, não fonte**; não tem FA-63, F3-25 nem o código E22, que o manual da base (368 págs.) tem. Não traz o AD30/NICE900. Nele, F2-15 é parâmetro do laço de corrente de servo zero (NICE3000new), não inversão de sentido de porta.

- BST BG101 e BG201 (manuais de ajuste) e brochura J5801 + AlphaBox: **apoio**, resumidos em `sources/cap09_apoio_outros_operadores.md`. Servem para a tabela "o que é igual e o que muda entre operadores" e só viram fonte se o elevador usar esses modelos.

## 5. Fora de escopo
Instalação das portas de pavimento e da cabina (manuais GLORY J2240/T2240, em espera); falhas do AD30 (as fontes não trazem tabela de falhas do controlador de porta); parâmetros do AD30 além dos citados; resgate com porta (capítulo 14).

## 6. Pontos em que as fontes divergem (não resolver sozinho)
1. **Notação dos parâmetros.** O boletim usa F1-00 a F1-07 e FP-01; o manual de comissionamento usa F100 a F105, F214, F215 e FP01. Pulsos do encoder: F1-07 (boletim) e F214 (manual). Tipo de encoder: só no boletim (F1-06). Não se sabe se são o mesmo controlador com duas notações ou duas versões (Q106).
2. **Método de autoajuste.** O boletim usa PRG + seta para a direita (TUNE1 e TUNE2, até 3 aberturas); o manual usa F116 igual a 3 ou 4, ENTER e OPEN, ou OPEN e CLOSE juntos por cerca de 5 s, e ainda F600/F601 para a largura.
3. **Espera para descarga.** O manual NICE900 manda esperar 5 minutos; o manual do NICE3000new, 10 minutos. Para o quadro vale o maior tempo; para o controlador de porta o livro cita 5 minutos como o manual diz e remete ao alerta do capítulo 1 (Q110).
4. **Sentido invertido.** O manual diz que o método recomendado é trocar os cabos U e V, mas a mesma lista manda também inverter o valor de F215 (descrito como direção de rotação do motor na lista de parâmetros e do encoder na seção 5). Trocar U e V e mudar F215 ao mesmo tempo pode se anular; o manual não esclarece (Q111).
5. **Numeração das etapas do manual.** Pula da Etapa 4 para a Etapa 6 (não há Etapa 5 de autoajuste do motor).

## 7. Figuras previstas
1. Visão do operador de porta: máquina, controlador, caixa de teto, quadro (SVG).
2. Ligação elétrica do AD30 (potência, encoder, DI1 a DI8, DO1 a DO4) redesenhada a partir da Figura 1 do boletim.
3. Sequência do autoajuste (TUNE1, TUNE2) e do autoajuste da largura (cinco passos do manual).
4. Cotas críticas da faca e da roldana (tabela, sem desenho se a fonte não der cota legível).

## 8. Alertas obrigatórios
PERIGO: desligar e esperar a descarga antes de mexer em cabos do motor; ATENÇÃO: o autoajuste move a porta por completo, área livre; não tocar no motor nem na carga durante o autoajuste; nunca inverter 24 V e GND do encoder, nem PGA, PGB e PGZ; cabos de abrir/fechar com blindagem (J4210 6.2); só pessoal treinado abre à mão a porta de cabina ou de pavimento (J4210 1.2); não lubrificar a guia da máquina de porta (J4210 5.4).

## 9. Perguntas de verificação
1. Quais são os padrões de fábrica de DI1, DI2, TC1 e TC2?
2. O que o controlador faz em TUNE1 e em TUNE2?
3. Como se calcula a largura da porta a partir de F602 e F603?
4. Que folga leva o gancho da faca de acionamento?
5. Qual o primeiro passo antes de parametrizar o controlador pela primeira vez?

## 10. Perguntas abertas (viram selos e issues se confirmadas)
- **Q106** Notação de parâmetros que vale no controlador entregue (F1-01 ou F101?).
- **Q107** Qual operador de porta tem o elevador de referência, se houver um? (O capítulo vale para vários operadores; o AD30/J4210 é o exemplo.)
- **Q108** Ligação real DEN1 da caixa de teto com o AD30 (B1 a DI1, B2 a DI2, B3 a DI4, X3 a TC1, X5 a TC2, 301 a TA12 só por correspondência de função).
- **Q109** Dados do motor e do encoder da porta (placa do motor; tipo de encoder; pulsos).
- **Q110** Espera de descarga do controlador de porta.
- **Q111** Sentido invertido: trocar U e V ou mudar F215, ou os dois?

## 11. Respostas do responsável técnico em 15/11/2026
- Q106 (notação), Q110 (espera de descarga) e Q111 (sentido invertido, F215): **o responsável não sabe responder**. Ficam como selos e viram issues, a resolver com as fotos da etiqueta do controlador ou com o fabricante.
- Q107: o quadro serve a vários operadores (ver 2.1).
