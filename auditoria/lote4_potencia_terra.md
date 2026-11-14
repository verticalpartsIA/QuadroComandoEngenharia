# Auditoria do lote 4: potência, alimentação de comando e terra

Esquema usado como base de verdade: Inovance 19061867-ZL (Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf, 51 páginas). Folha /N = PDF pág. N+2. Folhas lidas: /7 (pág. 9), /8 (pág. 10), /9 (pág. 11), /10 (pág. 12), /11 (pág. 13), /12 (pág. 14), /46 (pág. 48). O esquema secundário (19060918-ZL) não foi usado.

## O que o esquema mostra (fatos gerais)

- Não existem no esquema os componentes DQFB1, DQFB2, DQFB3, XPE nem o bloco MCTC-MCB-C2 (nenhuma etiqueta encontrada nas folhas lidas). Existem QF, QFB1, QFB2, QFB3, QFB4, TRF, CZ, XA e XB.
- XA (R, S, T, N) aparece só na folha /8 (MRL, pág. 10), com círculos de borne sobre as linhas L1, L2, L3, N, antes do QF. Na folha /7 (MR) as mesmas linhas entram direto, sem XA.
- Entre o QF e a saída de potência há o filtro EMC (L1, L2, L3, N para R, S, T, N). A saída R, S, T, N vai para a folha /9 (borne TA R, S, T, N), e de TA para o inversor R, S, T.
- Redes 201 e 202: saem de QFB2 e vão para KY5 1 e KY5 5 da placa MCTC-KCB-B4A (folha /10, pág. 12) e para as setas 22.2:A e 22.4:A. QFB2 é alimentado por +CC-R e +CC-N, que vêm da folha /9 (borne TA, R e N, depois do filtro EMC). O desenho não mostra a origem da fase R além disso.
- Redes 501 e 502: saem de QFB3 (RCD do topo da cabina), bornes 2 e 4 (folhas /7 e /8). QFB3 é alimentado pelo ramal antes do QF (fase R no borne 1 e neutro N no borne 3). Seguem para a folha /11 (pág. 13), placa KCB-B4A POW1 1 e 2 (com fusível F2 na 501), e para os consumos 11.2:A (iluminação do quadro). Nada de DQFB.
- Neutro N: sai de XA N (folha /8) antes do QF 7; uma derivação alimenta QFB3 3 e a outra segue pelo QF 7 e filtro EMC até TA N, que gera +CC-N para QFB2 (folha /9).
- Trafo TRF (folha /10, pág. 12): bornes 220V e 0P no primário, 125V e 0S no secundário. A etiqueta é "0P" (zero P), não "OP". Primário alimentado por 207 e 208 (KY8 1 e 2, da placa KCB-B4A, originadas de 201/202 via proteção OVP). O texto do desenho: 50 Hz, 63 VA (3,7 a 22 kW) / 110 VA (30 a 37 kW). A tensão do secundário aparece como 125V, não 110V. O desenho mostra símbolo de PE na blindagem entre os enrolamentos e na linha 0S.
- CZ (tomada fêmea): nas folhas /7 e /8 é alimentada por QFB4 (RCD da iluminação de caixa, bornes 2 e 4), com PE em símbolo. Não é ligada a QFB3, 501 ou 502.
- QFB1 (folha /10): disjuntor 1P+N 10 A, bornes N e 1 embaixo, N e 2 em cima (rótulos do desenho; não há borne 3). 125V do trafo vai ao borne 1 de baixo; 0S vai ao borne N de baixo; borne 2 de cima vai à rede 101 (KY5 7, fusível F3) e 102.

## Tabela

| Fio | Ligação listada | Evidência no esquema (folha, pág.) | Resultado | Confiança | Observação |
|---|---|---|---|---|---|
| 15 | DQFB1 1 para QFB1 2 | /10 pág. 12: QFB1 2 (cima) liga à rede 101 (KY5 7) e 102; DQFB1 não existe no desenho | NÃO VERIFICÁVEL | média | O lado QFB1 2 existe, mas o DQFB1 não está no esquema. |
| 18 | 501: DQFB3 2 para CZ 2 | /7 pág. 9 e /8 pág. 10: CZ 1 e 2 ligam a QFB4 2 e 4; 501 sai de QFB3 2 e vai a 7.4:F/8.4:E. DQFB3 ausente | DIVERGE | média | O esquema não liga a tomada CZ à rede 501 nem ao QFB3; liga ao QFB4. |
| 83 | QF 2 para NICE3000 R | /8 pág. 10 e /9 pág. 11: QF 2 vai a EMC L1, sai em R, entra no TA R e no inversor R | CONFERE | média | O desenho passa pelo filtro EMC e pelo borne TA; seguiu-se o traço. A lista não cita o filtro. |
| 84 | QF 4 para NICE3000 S | idem, linha S | CONFERE | média | Mesmo comentário do fio 83. |
| 85 | QF 6 para NICE3000 T | idem, linha T | CONFERE | média | Mesmo comentário do fio 83. |
| 86 | R: QF 2 para QFB2 1 | /9 pág. 11: +CC-R vem do TA R; /10 pág. 12: QFB2 1 recebe +CC-R | CONFERE | média | Origem real é QF 2 via filtro EMC e TA R. Borne 1 de QFB2 confere. |
| 87 | QF 1 para QFB3 1 | /8 pág. 10: derivação da linha R antes do QF 1 vai ao borne 1 do QFB3 (nota CAUTION confirma alimentação antes do QF) | CONFERE | alta | Ligação a montante do QF no mesmo nó do QF 1. |
| 88 | 201: QFB2 2 para DQFB2 1 | /10 pág. 12: 201 sai do borne 3 de QFB2 e vai a KY5 1 e 22.2:A; DQFB2 ausente | DIVERGE | média | Rede 201 confere, mas no desenho o borne de saída é 3 (o borne 2 de QFB2 é a entrada N). DQFB2 não existe. |
| 90 | 202: QFB2 4 para XB 202 | /10 pág. 12: 202 sai do borne 4 de QFB2 e vai a KY5 5 e 22.4:A; XB não aparece nessa folha | NÃO VERIFICÁVEL | média | Borne 4 e rede 202 conferem; o borne XB 202 não está desenhado. |
| 91 | 502: QFB3 4 para CZ 1 | /7 pág. 9 e /8 pág. 10: 502 sai de QFB3 4 e vai a 7.4:F e 11.2:A/POW1 2; CZ 1 ligado a QFB4 2 | DIVERGE | média | QFB3 4 = 502 confere; o destino CZ 1 não bate. |
| 92 | 501: QFB3 2 para DQFB3 1 | /8 pág. 10 e /11 pág. 13: QFB3 2 = 501, vai a POW1 1 (via F2); DQFB3 ausente | NÃO VERIFICÁVEL | média | Origem confere; o DQFB3 não está no esquema. |
| 112 | TRF 125V para QFB1 1 | /10 pág. 12 (recorte ampliado): 125V desce e vai ao borne 1 de baixo do QFB1 | CONFERE | média | Seguiu-se o traço. Secundário rotulado 125V (BOM diz 110 V). |
| 113 | TRF 0S para QFB1 3 | /10 pág. 12: 0S vai ao borne N de baixo do QFB1; não há borne 3 | CONFERE | média | Ligação a N confere; o rótulo do desenho é N e não 3. Se "3" for a numeração do componente real, não dá para conferir pelo desenho. |
| 114 | TRF 0S para XPE PE | /10 pág. 12: linha 0S tem derivação para um símbolo PE; XPE não existe | NÃO VERIFICÁVEL | baixa | O desenho aterra o 0S só como símbolo; não há ponto explícito. |
| 115 | XA R para QF 1 | /8 pág. 10: XA R desce direto ao QF 1 | CONFERE | alta | Só na folha /8 (MRL). |
| 116 | XA S para QF 3 | /8 pág. 10 | CONFERE | alta | |
| 117 | XA T para QF 5 | /8 pág. 10 | CONFERE | alta | |
| 118 | N: XA N para QFB2 3 | /8 pág. 10 e /9 pág. 11; /10 pág. 12: neutro chega a QFB2 via +CC-N no borne 2 (cima) | DIVERGE | média | O neutro de QFB2 entra no borne 2, não no 3; além disso passa por QF 7, EMC e TA N, e não direto de XA N. |
| 119 | N: XA N para QFB3 3 | /8 pág. 10: derivação de XA N (antes do QF 7) vai ao borne 3 de QFB3 | CONFERE | alta | |
| 120 | 202: XB 202 para XB 202 | Nenhuma folha lida mostra borne XB 202 | NÃO VERIFICÁVEL | baixa | Jumper interno do borne; desenho não mostra. |
| 121 | XPE PE para CZ PE | /7 pág. 9 e /8 pág. 10: CZ PE com símbolo de terra | NÃO VERIFICÁVEL | baixa | Só símbolo de terra; XPE ausente. |
| 123 | XPE PE para MCTC-MCB-C2 PE | MCB-C2 não encontrada nas folhas lidas (KCB-B4A tem PE em +CC-PE, /10 e /11) | NÃO VERIFICÁVEL | baixa | |
| 124 | XPE PE para NICE3000 PE | /9 pág. 11: inversor PE com símbolos de terra | NÃO VERIFICÁVEL | baixa | |
| 125 | XPE PE para TRF PE | /10 pág. 12: símbolos PE na blindagem do trafo | NÃO VERIFICÁVEL | baixa | |

## Resumo

Contagem (24 fios): CONFERE 11, DIVERGE 4, NÃO VERIFICÁVEL 9.

Divergências:
- Fio 18 (501, DQFB3 2 para CZ 2) e fio 91 (502, QFB3 4 para CZ 1): no esquema a tomada CZ é alimentada pelo QFB4 (iluminação de caixa), não pelas redes 501/502 do QFB3. DQFB3 não existe no desenho.
- Fio 88 (201, QFB2 2 para DQFB2 1): no desenho 201 sai do borne 3 do QFB2 e não há DQFB2.
- Fio 118 (N, XA N para QFB2 3): no desenho o neutro entra no borne 2 do QFB2 e chega via QF 7, filtro EMC e borne TA N (+CC-N), não direto de XA N.
- Observação de numeração: em QFB2 o desenho numera 1 e 2 em cima (R e N) e 3 e 4 embaixo (201 e 202); a lista usa 1 e 3 como entradas e 2 e 4 como saídas. A topologia R para 201 e N para 202 é a mesma; pode ser só diferença de numeração do componente real.

Não verificáveis:
- 15, 88/92 (lado DQFB), 90 e 120 (XB 202 não desenhado), 92: DQFB1, DQFB2, DQFB3 e XB não aparecem nas folhas lidas.
- 114, 121, 123, 124, 125: fios de terra; o desenho só traz símbolos de PE, sem barramento XPE nem MCB-C2.

Registro pedido (sem concluir sobre a variante 220 V):
- 201 e 202: saem de QFB2 (bornes 3 e 4 no desenho), que é alimentado por +CC-R e +CC-N vindos da folha /9 (borne TA, depois do filtro EMC). Seguem para KY5 1 e 5 da KCB-B4A e para 22.2:A e 22.4:A.
- 501 e 502: saem de QFB3 (bornes 2 e 4), alimentado antes do QF (R no 1, N no 3), e vão a POW1 1 e 2 da KCB-B4A (501 via fusível F2) e a 11.2:A.
- Neutro N: derivado de XA N antes do QF (alimenta QFB3 3); outro ramo passa por QF 7, filtro EMC e TA N e gera +CC-N para QFB2.
- Trafo: bornes 220V e 0P (primário, ligados a 207 e 208) e 125V e 0S (secundário); o desenho diz 125V, não 110 V. A lista usa "OP", e a etiqueta do desenho é "0P". O 125V vai ao QFB1 1 e o 0S ao N do QFB1; 0S tem símbolo de PE.
- Limitações: filtro EMC e borne TA do esquema não constam da lista; o esquema secundário não foi consultado.
