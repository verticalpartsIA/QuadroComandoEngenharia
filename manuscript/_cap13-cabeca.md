# Capítulo 13. Diagnóstico de falhas

> RASCUNHO v0.1 de 14/11/2026. Aguarda aprovação do Gelson e assinatura da Qualidade. A tabela de falhas é tradução fiel do capítulo 7 do manual do controlador; a revisão técnica final é do responsável técnico e da Qualidade. Este arquivo é montado por `build/monta_cap13.py`; edite os arquivos de origem.

**Parte IV. Comissionamento**

## 13.1 O que você vai aprender

Ao terminar este capítulo você será capaz de:

1. Ler um código de falha no teclado da placa MCB e no painel de operação.
2. Dizer o que cada nível de falha faz com o elevador.
3. Reiniciar o controlador depois de uma falha do jeito que a falha exige.
4. Encontrar, para um código, a causa possível e o que o manual manda verificar.

> **PERIGO.** Antes de abrir o quadro de comando ou tocar em qualquer borne para diagnosticar uma falha, desligue toda a alimentação e espere no mínimo 10 minutos. Nunca ponteie a cadeia de segurança nem as fechaduras para testar uma falha: isso anula a proteção (capítulo 1). Fonte: manual NICE3000new, págs. PDF 20 e 21.

## 13.2 Como a falha aparece

Quando o controlador detecta uma falha, ele avisa e registra as informações dela.

- **No teclado da placa MCB** aparecem o código e o subcódigo da falha atual, por exemplo **E22-101**.
- **No painel de operação**, quando ele está ligado, aparece o código da falha atual, por exemplo **Err22**.
- Com o parâmetro **F-2 igual a 2** no teclado, ele mostra as últimas 10 falhas, com código, subcódigo e hora.
- O controlador grava informação detalhada das últimas 10 falhas e informação simples de 50 grupos de falhas. Os detalhes estão nos grupos de parâmetros E0 a E9 e nos parâmetros FC-11 a FC-210.

O código aparece então em dois formatos para a mesma falha: "E22-101" no teclado e "Err22" no painel. Neste livro, a tabela usa o formato "Err" e o texto cita o subcódigo quando ele existe.

Fonte: manual NICE3000new, seção 7.1, pág. PDF 265 (impressa 264), figuras 7-1 e 7-2.

## 13.3 Como reiniciar depois da falha

| Etapa | O que fazer |
|---|---|
| Quando a falha ocorre | Com F-2 igual a 2 no teclado, veja as últimas 10 falhas (código, subcódigo e hora). |
| Antes de reiniciar | Identifique a causa pelo código no painel de operação e elimine-a conforme a seção 13.5. |
| Reinício automático | Em algumas falhas, depois de eliminada a causa, o controlador reinicia sozinho quando as condições de reinício são atendidas. |
| Reinício manual | Algumas falhas exigem reinício manual: pressione a tecla vermelha STOP/RES do painel de operação ou ajuste F-2 para 1 no teclado. |
| Reinício desligando | Algumas falhas exigem desligar a alimentação do controlador e ligar de novo depois de eliminar a causa. |

Fonte: manual NICE3000new, seção 7.2, pág. PDF 266 (impressa 265).

## 13.4 Os cinco níveis de falha

O NICE3000new tem quase 70 informações de alarme e funções de proteção. Elas são classificadas em cinco níveis, de acordo com a gravidade. O que o controlador faz depende do nível.

| Nível | O que o controlador faz | Subníveis |
|---|---|---|
| 1 | Mostra o código da falha e aciona o comando do relé de falha | 1A: a marcha do elevador não é afetada em nenhuma condição |
| 2 | Mostra o código, aciona o relé de falha e o elevador continua a marcha normal | 2A: a função de operação em paralelo ou em grupo é desabilitada. 2B: a função de abertura antecipada da porta e de renivelamento é desabilitada |
| 3 | Mostra o código, aciona o relé de falha, para a saída e aplica o freio logo depois da parada | 3A: em baixa velocidade, o elevador para com taxa especial de desaceleração e não pode reiniciar. 3B: em baixa velocidade o elevador não para; em velocidade normal ele para e depois pode partir em baixa velocidade, após 3 s |
| 4 | Mostra o código e aciona o relé de falha; no controle por distância o elevador desacelera até parar e não pode andar de novo | 4A: em baixa velocidade, para com taxa especial de desaceleração e não pode reiniciar. 4B: em baixa velocidade não para; em velocidade normal para e depois pode partir em baixa velocidade, após 3 s. 4C: o manual dá para o 4C o mesmo texto do 4B |
| 5 | Mostra o código, aciona o relé de falha e o elevador para imediatamente | 5A: em baixa velocidade, para imediatamente e não pode reiniciar. 5B: em baixa velocidade não para; em velocidade normal para e depois pode partir em baixa velocidade, após 3 s |

Fonte: manual NICE3000new, seção 7.3, Tabela 7-1, pág. PDF 267 (impressa 266).

## 13.5 Como usar a tabela de falhas

Para cada código a tabela traz o nome da falha em português e o original em inglês, o nível, o subcódigo (quando existe) e as causas possíveis, cada uma com o que verificar ou fazer. O livro traduz o que o manual diz e não acrescenta causa nem solução. Onde o texto do manual ficou ambíguo, a tabela mantém o original entre aspas e manda ver a página.

Os códigos Err01, Err63 e Err68 não constam na tabela do manual. Alguns códigos são "Reserved" (reservados) e o manual manda contatar o agente ou a Inovance. As notas do manual depois da tabela aparecem junto do código a que se referem.

Fonte: manual NICE3000new, seção 7.4, págs. PDF 268 a 289 (impressas 267 a 288).

## 13.6 Tabela de falhas
