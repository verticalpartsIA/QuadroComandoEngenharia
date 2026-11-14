# STANDBY.md: itens em espera (decisão do Gelson, 14/11/2026)

Nada daqui entra no ebook até o Gelson reativar o item.

| Item | Assunto | Situação |
|---|---|---|
| NR-12 | Entra ou não no capítulo de normas | Em espera. Fora do ebook por enquanto. |
| Registro | CREA ou CFT do responsável técnico (verso da folha de rosto) | Não informado. Marcador `PENDENTE-REGISTRO` bloqueia o build de lançamento. |
| Q47 | Texto da NR-10, NBR 16858 e EN 81-20 para o capítulo 1 | Em espera. Sem texto, o capítulo não cita norma. |
| Q49 | Posição do capítulo de qualidade (nova numeração) | Em espera. |
| Q50 | Definição de "qualidade do equipamento" e "qualidade dos acabamentos" (proposta: equipamento = quadro como produto; acabamentos = mão de obra visível) | Gelson concordou com a divisão; capítulo fica em espera. |
| Q51 | Origem dos critérios de aceite da Qualidade (POP-ISO-PCP 6.1.13 diz "definidos pela empresa") | Em espera. |
| Q52 | Fotos de acabamento conforme e não conforme | Em espera. |
| SVG do logotipo | Só PNG no `009_DesignSystem` | O Gelson envia se for necessário. |
| Q54 | O elevador de referência tem RCS, CWSG e OS-G (contrapeso)? | Sem resposta. Marcado com o selo `PREENCHER [Q54]` nos rascunhos; bloqueia o lançamento. |
| Q56 | BFS1 e BFS2: qual é do carro e qual é do contrapeso | O esquema VerticalParts 19060918-ZL (pág. 30) diz BFS1 = carro, BFS2 = contrapeso. Texto provisório "chave do amortecedor 1/2" até o Gelson confirmar. |
| Q59 | Função de cada chave da cadeia (o que detecta e por que existe) | Sem fonte lida. Selo `PREENCHER [Q59]` no capítulo 1. |
| Q60 | MES-1 ("Motor emg. stop button") existe no MRL de referência? Aparece na cadeia fora do bloco "Use for MR" | Sem resposta. Selo `PREENCHER [Q60]`. |
| 220 V | Adendo (etiquetas reais do inversor, trafo, origem dos 220 V, bitola) | Depois do ebook 380 V. |
| Manual de Resgate da VerticalParts | Confirmar que está aprovado | Pendente. |
| Encoder | Confirmar EI53C9.25-2048 no motor real | Pendente. |

## Respostas registradas em 14/11/2026 (auditoria da lista de fios)
| Item | Resposta do Gelson | Ressalva |
|---|---|---|
| Q69 limitador | AC 220 V | A folha /22 traz as duas versões (AC 220 V e DC 24 V); a escolha vem do Gelson e é coerente com a lista (201 e 202 até XB 203 e 205). |
| Q70 SZ | Bornes pequenos em 5 pares (1-2, 3-4, 13-14, 23-24, 33-34) no lugar da tomada de 9 pinos do esquema | Coerente com o desenho (1-2 = plugue SZ1 normal; 33-34 = ligação DC12 a T02). Pares com origem na lista e no Rev. 11. |
| Q71 jumpers 62 a 66 | Só de bancada; saem quando os cabos de campo (BA, BD, BE, HW, AA) são ligados | Indicação baseada na pendência P8 do Rev. 11, marcada [Provável] lá; sem confirmação visual em campo. Os jumpers 61 (BA/8-9) e 67 (AA/14-6) o próprio esquema prevê para elevador de PORTA ÚNICA ("single door, connect…"), então ficam no campo no elevador de referência (1 porta). |

## Perguntas abertas do Capítulo 3 (14/11/2026), cada uma com selo no rascunho
| Selo | Pergunta |
|---|---|
| Q79 | O inversor entregue é o NICE-L-C-4007 (o esquema só diz "40XX")? |
| Q80 | Qual resistor de frenagem está instalado (ohm e watt)? |
| Q81 | Qual a função de DQFB1, DQFB2 e DQFB3 (aparecem na foto, não no esquema)? |
| Q82 | Corrente nominal, poder de corte e tipo do QF e dos QFB3 e QFB4 (C ou D); qual proteção diferencial o projeto adota (o manual pede tipo B)? |
| Q83 | Pares de pinos do plugue S2 (as folhas /14, /16 e /19 divergem) e posição de cada jumper |
| Q84 | Valores de B0-00, B0-01 e B0-02 e tensão e corrente da bobina do freio da máquina de referência |
| Q85 | Posição no quadro real da PCB-D1, do QFB4, de XA, TA, XB, SZ, CZ e XPE; o que cada polo do barramento de terra recebe |
| Q86 | O ERB do quadro é o A1 (com bateria) ou o A2? |
| Q87 | Qual rótulo da botoeira vale (12/11 amarelo ou 13/11 branco)? |
| Q88 | Marca, corrente (AC-3), tensão de bobina e tipo dos auxiliares de SW, BY e FX |
