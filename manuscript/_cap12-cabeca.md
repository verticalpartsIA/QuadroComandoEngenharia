# Capítulo 12. Energização, parâmetros e autoajuste

> RASCUNHO v0.1 de 14/11/2026. Aguarda aprovação do Gelson e assinatura da Qualidade. O texto das seções 12.1 a 12.7 é tradução fiel do capítulo 4 e das seções 5.1 a 5.6 do manual do controlador; as seções 12.8 em diante usam o esquema Vitinho. Este arquivo é montado por `build/monta_cap12.py`; edite os arquivos de origem em `sources/` e `manuscript/_cap12-*.md`.

**Parte IV. Comissionamento**

## 12.0 O que você vai aprender

Ao terminar este capítulo você será capaz de:

1. Verificar a segurança e os circuitos do quadro de comando antes da primeira energização.
2. Energizar o controlador e ler o estado dele.
3. Comissionar em velocidade de inspeção, incluindo o autoajuste do motor.
4. Fazer o autoajuste do poço e comissionar em velocidade normal.
5. Ajustar o conforto de viagem e a precisão de nivelamento.
6. Saber quais parâmetros do projeto aparecem no esquema.

> **PERIGO.** Antes de qualquer verificação nos bornes, desligue toda a alimentação e espere no mínimo 10 minutos. Mantenha a cabina livre e sem passageiros durante todo o comissionamento. Antes de energizar, confira que os jumpers de bancada (fios 62 a 66 da lista de fios) foram removidos e que a cadeia de segurança e as fechaduras estão ligadas de verdade (capítulos 1 e 4). Nunca ponteie a cadeia de segurança nem as fechaduras para "ajudar" um autoajuste. Fonte: manual NICE3000new, págs. PDF 20 e 21; esquema Vitinho, folha /19.

> **NOTA.** Os dados do motor da máquina de referência (potência, tensão, corrente, frequência e rotação nominais), o tipo e os pulsos do encoder, a velocidade nominal e a altura entre pavimentos não constam em nenhum documento do projeto. Onde o procedimento pede esses valores, o texto remete à placa do motor e à do encoder. O elevador de referência tem máquina síncrona de ímã permanente e encoder SIN/COS (EI53C9.25-2048), e por isso valem os procedimentos de motor síncrono.
