# Spec: Capítulo 12, Energização, parâmetros e autoajuste

Status: SPEC (14/11/2026). Parte IV, Comissionamento. Capítulo com assinatura da Qualidade (segurança).

## 1. Objetivo pedagógico
Ao terminar, o leitor sabe energizar o quadro de comando pela primeira vez com segurança, verificar o estado do controlador, comissionar em velocidade de inspeção (autoajuste do motor e do poço) e em velocidade normal, e ajustar o conforto de viagem, seguindo a sequência do fabricante e os parâmetros do projeto.

## 2. Leitor e pré-requisitos
Técnico de campo. Pré-requisitos: capítulos 1, 3 e 4 (cadeia de segurança, componentes e montagem), 5 (testes de bancada) e 7 (motor, freio e encoder).

## 3. Conteúdo
1. 12.1 Ferramentas de comissionamento: teclado da MCB, painel de operação e comissionamento por celular (manual cap. 4).
2. 12.2 Guia de comissionamento (manual 5.1) e verificação de segurança e do circuito (5.2).
3. 12.3 Energização e verificação do estado do controlador (5.3).
4. 12.4 Comissionamento em velocidade de inspeção: autoajuste do motor e do poço (5.4).
5. 12.5 Comissionamento em velocidade normal (5.5).
6. 12.6 Ajuste do conforto de viagem (5.6).
7. 12.7 Parâmetros do projeto: a lista de parâmetros e as instruções de ajuste do esquema Vitinho (folhas /5 e /6).
8. 12.8 Quadro "Se o seu elevador tiver…": motor assíncrono, outras velocidades e mais pavimentos.

## 4. Fontes permitidas
- Manual NICE3000new, `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`, capítulos 4 e 5 (págs. impressas 133 a 176; PDF 134 a 177).
- Esquema Vitinho 19061867-ZL, folhas /5 (lista de parâmetros) e /6 (instruções de ajuste), págs. PDF 7 e 8.
- Extratos em `sources/cap12_*.md`.

## 5. Fora de escopo
Tabela completa de parâmetros F0 a FP (apêndice próprio, a fazer), falhas (capítulo 13), resgate elétrico (capítulo 14 do plano, hoje capítulo 12 do índice provisório), normas.

## 6. Figuras previstas (SVG)
1. Fluxo geral do comissionamento, da verificação de segurança ao conforto de viagem.
2. Sequência do autoajuste do motor.
3. Sequência do autoajuste do poço.

## 7. Alertas obrigatórios
Espera de 10 minutos e desenergização antes de qualquer verificação nos bornes; conferência da cadeia de segurança e dos jumpers de bancada antes de energizar (capítulos 1 e 4); manter a cabina livre e sem passageiros durante o comissionamento; nunca ponteie a cadeia de segurança nem as fechaduras para "ajudar" o autoajuste.

## 8. Perguntas de verificação
1. O que se verifica no quadro antes da primeira energização?
2. Em que ordem se faz o autoajuste do motor e o do poço?
3. Em que velocidade ocorre o autoajuste do poço?
4. Que falha o controlador mostra se o autoajuste do poço falha?
5. Que parâmetros definem a velocidade de inspeção e a de operação de emergência?

## 9. Dependências do Gelson
Dados do motor da máquina de referência (placa), parâmetros F1 do projeto, velocidade nominal e altura entre pavimentos do elevador de referência; aprovação do texto traduzido.
