# Spec: Capítulo 3, Componentes do quadro de comando

Status: SPEC (14/11/2026). Capítulo com assinatura da Qualidade. Parte II, O quadro de comando.
Substitui, no Rev. 12, as seções 1 a 8 do Rev. 11 (inversor, KCB e PCB-D1, resgate, botoeira, disjuntores, contatores, bornes, trafo). O Rev. 11 serve de mapa, não de fonte (RULES.md).

## 1. Objetivo pedagógico
Ao terminar, o leitor reconhece cada componente do quadro de comando de 7,5 kW / 380 V, sabe a função dele, quais bornes e conectores ele tem e para onde cada um vai, e sabe localizá-lo no quadro real.

## 2. Leitor e pré-requisitos
Montador de quadro e técnico de campo. Pré-requisito: Capítulo 1 (cadeia de segurança) e Capítulo 2 (visão do sistema).

## 3. Conteúdo previsto
1. 3.1 Visão do quadro e layout em zonas (Z1 a Z6 do Rev. 11, a validar com as fotos): figura em SVG com callouts e foto "como deve ficar".
2. 3.2 Inversor NICE3000new com a placa MCB-C3: modelo de 7,5 kW / 380 V, bornes de potência (R, S, T, U, V, W, (+), PB, PE), conectores CN2 e CN3, flat de 40 vias.
3. 3.3 Placa de interface KCB-B4A: conectores KY1 a KY13, POW1, AA, AB, BA, BB, BC, BD, BE, HW, MT, OS, AC; fusíveis; plugues S1 e S2; entradas e saídas (X e Y).
4. 3.4 Placa fonte do freio PCB-D1: conectores J2, J3, J4; saídas de 24 V e 110 V.
5. 3.5 Resgate elétrico ERB-A1: bornes, indicadores e botões (a operação e o teste ficam no capítulo 13).
6. 3.6 Botoeira de inspeção (handle KKB4-1C-02): CIS, CIU E, CID E e MES.
7. 3.7 Proteção e alimentação: QF, QFB1, QFB2, QFB3, QFB4 e trafo TRF.
8. 3.8 Contatores de potência: SW (marcha), BY (freio) e FX (curto das fases U, V e W).
9. 3.9 Bornes, tomada e terra: XA, TA, XB, SZ (bornes em 5 pares, segundo o responsável técnico), CZ e XPE.
10. 3.10 Quadro "Se o seu elevador tiver…": variantes de 15 kW e de 220 V (só remissão ao adendo), QFB4 e iluminação.

## 4. Fontes permitidas
- Esquema Vitinho 19061867-ZL (decisão do responsável técnico, 14/11/2026): folhas /7 a /17, /21, /22, /23 (PDF pág. 9 a 19, 23 a 25).
- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`, cap. 1 e 2 (terminais, especificações).
- Manual do resgate elétrico: `Manual_Dispositivo_Resgate_Eletrico_ERB-A1_EN.pdf`.
- Fotos do quadro (24, 12 e 13/11/2026), com rostos e números de série cobertos antes de entrar.
- Resultados da auditoria (`AUDITORIA_REV11.md` e `auditoria/`).
- Não entram: códigos de BOM da produção, selos do Rev. 11, a lista de fios como base.

## 5. Fora de escopo
Fiação interna fio a fio e ordem de montagem (capítulo 4), testes (capítulo 5), qualidade do acabamento (em espera), parâmetros (capítulo 12), operação do resgate (capítulo 13), variantes 220 V (adendo), caixa de teto e cabos de campo (capítulos 8, 10 e 11).

## 6. Figuras previstas
1. Layout do quadro em zonas (SVG), a partir das fotos e do desenho de furação.
2. Mapa dos conectores da KCB-B4A (SVG) com pinos conferidos na folha /21.
3. Diagrama em blocos da alimentação e proteção (QF, QFB, trafo, bornes).
4. Esquema de potência (QF, inversor, contatores, motor) simplificado.

## 7. Alertas obrigatórios
Espera de 10 minutos após desligar, aterramento e pulseira antiestática (manual NICE3000new, pág. PDF 20 e 21); nunca ligar a rede em U, V e W; cuidado com o resistor e a carcaça quentes.

## 8. Perguntas de verificação
1. Em quais bornes do inversor entra a rede e de quais sai a potência do motor?
2. Qual é a função de cada contator (SW, BY e FX)?
3. O que a placa PCB-D1 alimenta e a partir de quê?
4. Quais conectores da KCB levam a cadeia de segurança e as fechaduras?
5. Onde fica cada componente no quadro?

## 9. Dependências do Gelson
- Aprovar a divisão em seções.
- Confirmar a posição real dos componentes nas zonas do quadro (as fotos mostram, mas o Rev. 11 diz "posição a confirmar" para a PCB-D1).
- Etiquetas dos contatores e do trafo recebidos (pendências P3 e P6).
