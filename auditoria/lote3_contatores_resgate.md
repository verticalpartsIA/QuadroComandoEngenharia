# Auditoria do lote 3: contatores BY/FX/SW, placa de resgate ERB e placa fonte do freio

Esquema usado como base: Inovance 19061867-ZL (Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT)), 51 páginas. Página do PDF = folha do carimbo + 2.
Folhas lidas: /8 (PDF 10), /9 (PDF 11), /10 (PDF 12), /13 (PDF 15), /16 (PDF 18), /17 (PDF 19), /23 (PDF 25).
Esquema secundário (19060918-ZL, Verticalparts): só conferida a página PDF 16 (circuito de resgate), que repete exatamente o desenho da /23 do principal. O manual da ERB não foi consultado.
Lista auditada: 32 fios (lote3_contatores_resgate.txt). Nenhum arquivo existente foi alterado.

## Observações gerais de leitura

1. Contatores: no esquema, SW, BY e FX têm bobina A1 ligada ao KY2 da KCB (Y1, Y2, Y3) e A2 comum na rede 102 (/17). Os contatos de retorno SW 11-12, BY 11-12 e FX 13-14 têm o lado 12/12/14 unido na rede 301 (/17).
2. A rede 102 vem do MCB-C3 CN2:6 (XCM2), conforme /16.
3. Rotas de freio (/13): BK1+ (PCB-D1 J3/2) vai a SW 54; SW 53 vai ao nó ZQ1+ da KCB. BK2+ (J3/3) vai a SW 74; SW 73 vai ao nó ZQ2+. BK- (J3/1) vai a BY 1; BY 6 vai aos nós ZQ1- e ZQ2- (unidos).
4. Resgate (/23): L e N da ERB vêm das redes 501 e 502. ZQ+ da ERB vai ao pino 5 do plugue MT1 (nó ZQ1+), ZQ- vai ao pino 12 (nó ZQ2-). MS+ e MS- seguem as redes 133 e 131.
5. O desenho da ERB não tem borne PE. Os pinos do conector SZ vão só de 1 a 9: 1=101B, 6=101, 4=302, 9=302, 5=FL1, 3=DC12, 8=T02, 2=133, 7=131.
6. Bitola: nenhum desenho (/9, /13, /17, /23) indica seção de condutor. A coluna mm2 da lista (0,75, 2,5 e 6) não pôde ser confrontada com o esquema.
7. Nomes "DQFB1" e "DQFB3" da lista não existem no esquema (aparecem como QFB1 e QFB3). Tratei o "D" como prefixo de rótulo. É inconsistência de nome, não de ligação.

## Tabela

| Fio | Ligação listada | Evidência no esquema | Resultado | Confiança | Observação |
|---|---|---|---|---|---|
| 1 | BY 2 a BY 4 | /13 (PDF 15): contatos principais do BY em série; ponte do 2 para o 4 | CONFERE | alta | Confirmado também pela legenda de bornes da /17 (1-2, 4-3, 5-6) |
| 2 | BY 3 a BY 5 | /13 (PDF 15): ponte do 3 para o 5 | CONFERE | alta | Idem |
| 14 | DQFB1 2 (101B) a SZ 1 | /23 (PDF 25): SZ 1 = 101B. /10 (PDF 12): 101B sai do jumper "Short when used for MR" ligado à rede 101, que sai do QFB1 pino 2 | CONFERE | média | Precisou seguir traço na /10. O disjuntor aparece como QFB1, sem o "D" |
| 20 | DQFB3 2 (501) a ERB N | /8 (PDF 10): QFB3 pino 2 = 501 (fase, vinda de L1). /23 (PDF 25): 501 entra no borne L da ERB | DIVERGE | alta | Desenho: 501 vai a L. Lista: 501 vai a N. Ligação trocada com o fio 94. O secundário (PDF 16) mostra o mesmo (501 em L) |
| 21 | FX A2 a BY A2 | /17 (PDF 19): A2 de SW, BY e FX ligam todos à rede 102 (linha inferior) | CONFERE | média | Rede comum, sem fio direto desenhado entre os dois A2 |
| 22 | FX 31 a FX 21 | /9 (PDF 11): 21 e 31 do FX unidos por jumper | CONFERE | alta | Confirmado em ampliação |
| 23 | FX A2 a SW A2 (102) | /17 (PDF 19): A2 de SW e FX na rede 102 | CONFERE | média | Rede comum |
| 26 | FX 14 a SW 12 | /17 (PDF 19): 12 do SW e 14 do FX ligados à mesma linha (rede 301) | CONFERE | média | Mesma rede 301, sem fio direto desenhado |
| 27 | FX 14 a BY 12 | /17 (PDF 19): 12 do BY e 14 do FX na rede 301 | CONFERE | média | Idem |
| 28 | ERB PE a chapa da botoeira PE | /23 (PDF 25): a ERB não tem borne PE nem símbolo de terra | NÃO VERIFICÁVEL | baixa | Chapa da botoeira não aparece no desenho |
| 29 | ERB ZQ+ a SZ 4 | /23 (PDF 25): ZQ+ da ERB vai ao pino 5 do MT1 (nó ZQ1+). SZ 4 = rede 302, que não é ZQ+ | DIVERGE | alta | Desenho: ZQ+ não passa pelo SZ. SZ 4 é 302. Secundário (PDF 16) igual |
| 30 | ERB ZQ+ a SW 73 | /23 (PDF 25) e /13 (PDF 15): ZQ+ da ERB está no nó ZQ1+, que liga a SW 53. SW 73 é o nó ZQ2+ (MT 6), sem ligação desenhada à ERB | DIVERGE | média | Desenho leva ERB ZQ+ ao lado de SW 53, não de SW 73. Precisou seguir traço (MT1 5 e 12) |
| 31 | ERB ZQ- a BY 6 | /23 (PDF 25): ZQ- da ERB vai ao MT1 12 (nó ZQ2-). /13 (PDF 15): ZQ2- está unido a ZQ1- e a BY 6 | CONFERE | média | Mesma rede ZQ-, passando pela KCB |
| 74 | MCB-C3 CN2/6 a SW A2 (102) | /16 (PDF 18): CN2:6 (XCM2) = rede 102, que segue para /17.2:E. /17 (PDF 19): A2 do SW na 102 | CONFERE | alta | |
| 75 | PCB-D1 J3/1 (BK-) a BY 1 | /13 (PDF 15): J3/1 BK- liga ao BY 1 | CONFERE | alta | |
| 77 | PCB-D1 PE a MCB-C2 PE | /10 (PDF 12): PCB-D1 tem PE em J3/8 com símbolo de terra. Não há MCB-C2 no esquema (a placa é MCB-C3) e nenhum ponto de PE do MCB | NÃO VERIFICÁVEL | baixa | Só símbolo de terra |
| 78 | PCB-D1 J3/2 (BK1+) a SW 54 | /13 (PDF 15): J3/2 BK1+ liga ao SW 54 | CONFERE | alta | |
| 79 | PCB-D1 J3/3 (BK2+) a SW 74 | /13 (PDF 15): J3/3 BK2+ liga ao SW 74 | CONFERE | alta | |
| 80 | NICE3000 U a SW 1 | /9 (PDF 11): U do inversor ao pino 1 do SW | CONFERE | alta | Desenho não informa bitola (lista: 6 mm2) |
| 81 | NICE3000 V a SW 3 | /9 (PDF 11): V ao pino 3 | CONFERE | alta | Idem |
| 82 | NICE3000 W a SW 5 | /9 (PDF 11): W ao pino 5 | CONFERE | alta | Idem |
| 94 | QFB3 4 (502) a ERB L | /8 (PDF 10): QFB3 pino 4 = 502 (neutro, vindo de N). /23 (PDF 25): 502 entra no borne N da ERB | DIVERGE | alta | Desenho: 502 vai a N. Lista: 502 vai a L. Troca com o fio 20. Secundário igual ao principal |
| 97 | SW 2 a FX 22 | /9 (PDF 11), ampliado: FX 22 liga à linha do SW 2 (fase U) | CONFERE | alta | Desenho não informa bitola (lista: 2,5 mm2) |
| 98 | SW 4 a FX 32 | /9 (PDF 11): FX 32 liga à linha do SW 4 (V) | CONFERE | alta | Idem |
| 99 | SW 6 a FX 21 | /9 (PDF 11): FX 21 (unido ao 31) liga à linha do SW 6 (W) | CONFERE | alta | Idem |
| 100 | SW 2 a TA U | /9 (PDF 11): saída 2 do SW desce à borneira TA, U | CONFERE | alta | Lista: 6 mm2, sem indicação no desenho |
| 101 | SW 4 a TA V | /9 (PDF 11): saída 4 à TA V | CONFERE | alta | Idem |
| 102 | SW 6 a TA W | /9 (PDF 11): saída 6 à TA W | CONFERE | alta | Idem |
| 107 | SZ 14 a ERB MS+ | /23 (PDF 25): MS+ da ERB segue a rede 133, que chega ao pino SZ 2. O SZ só tem pinos 1 a 9 | DIVERGE | média | Desenho: MS+ em SZ 2. Lista: "SZ 14", pino que não existe. Pode ser notação de outro conector, mas não bate com o esquema |
| 108 | SZ 24 a ERB MS- | /23 (PDF 25): MS- da ERB segue a rede 131, pino SZ 7 | DIVERGE | média | Desenho: MS- em SZ 7. Lista: "SZ 24", inexistente |
| 109 | SZ 3 (ZQ1+) a SW 53 | /23 (PDF 25): SZ 3 = DC12, não ZQ1+. /13 (PDF 15): SW 53 vai ao nó ZQ1+ da KCB (MT 5) | DIVERGE | alta | Desenho: ZQ1+ chega por MT, não pelo SZ. O destino SW 53 está correto, a origem SZ 3 não |
| 122 | XPE PE a ERB PE | /23 (PDF 25): a ERB não tem borne PE. /8 (PDF 10) mostra a entrada PE (+EX-PE) só como terra | NÃO VERIFICÁVEL | baixa | Sem ponto de ligação explícito na ERB |

## Resumo

- CONFERE: 22
- DIVERGE: 7
- NÃO VERIFICÁVEL: 3
- Total: 32

### Divergências

1. Fios 20 e 94: L e N da ERB estão trocados na lista. O esquema (principal e secundário) liga 501 (QFB3 pino 2, fase) ao borne L e 502 (QFB3 pino 4, neutro) ao borne N. A lista faz o contrário.
2. Fios 29 e 109: a lista passa ZQ+ pelo conector SZ (pinos 4 e 3). No esquema SZ 4 é 302 e SZ 3 é DC12; ZQ+ e ZQ1+ chegam à ERB pelo plugue MT1 (pino 5), não pelo SZ.
3. Fio 30: ERB ZQ+ listado para SW 73. No desenho a ERB está no nó ZQ1+ (SW 53); SW 73 é o nó ZQ2+ e não tem ligação à ERB desenhada.
4. Fios 107 e 108: SZ 14 e SZ 24 não existem no desenho (SZ vai de 1 a 9). MS+ está em SZ 2 (rede 133) e MS- em SZ 7 (rede 131).

Possível causa das divergências 2 a 4: o painel real pode usar outra topologia de resgate (ZQ pelo SZ) que o esquema não mostra. É hipótese, não leitura.

### Não verificáveis

- Fio 28: a ERB e a chapa da botoeira não têm ponto de PE desenhado.
- Fio 77: MCB-C2 não existe no esquema; só há PE da PCB-D1 como símbolo de terra.
- Fio 122: a ERB não tem borne PE no desenho.

### Bitolas (mm2)

O esquema não registra seção de condutor nos pontos lidos. Nada a registrar sobre 2,5 mm2 ou 6 mm2.

### Fios conferidos por rede comum (confiança média)

Fios 21, 23, 26, 27 e 31 batem porque as duas pontas estão na mesma rede (102, 301, ZQ-), sem fio direto desenhado entre elas.
