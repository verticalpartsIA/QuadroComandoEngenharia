# HARNESS.md: como o agente trabalha neste projeto

## Antes de qualquer tarefa
1. Ler `RULES.md` e `GLOSSARY.md`.
2. Ler a spec do capítulo em `specs/` e a lista de perguntas de verificação dela.
3. Usar só o que está em `sources/` (extratos com página) ou nos PDFs originais listados na spec.

## Proibições
- Não inventar pino, parâmetro, código de falha, valor de norma, bitola ou fórmula. Sem fonte, a frase não entra: registrar a lacuna na spec e perguntar ao Gelson.
- Não usar o livro interno Rev. 11 como fonte de verdade técnica sem conferir no esquema ou no manual; ele traz selos de dúvida.
- Não copiar texto de norma. Explicar com palavras próprias e citar o item.
- Não usar termos fora de `GLOSSARY.md`.
- Não incluir códigos de BOM, pendências internas ou nomes de colaboradores.
- Não alterar o aviso legal sem aprovação.

## Fontes autorizadas (em `C:\dev\SitesProjetos\Conhecimento_Claude\PDF`, salvo indicação; os arquivos foram renomeados para nomes em português em 14/11/2026, o conteúdo do manual de 368 páginas é o mesmo, hash conferido)
- Manual NICE3000new, 368 páginas: `Manual_Usuario_Controlador_NICE3000new_Completo.pdf`.
- Esquemas: `Diagrama Completo Vitinho NICE3000-B&W-B4A(GBT).pdf` (19061867-ZL) e `Esquema Elétrico Elevadores Verticalparts.pdf` (19060918-ZL). São revisões diferentes: citar qual.
- Caixa de teto: `Manual_Caixa_de_Teto_MCTC-CTW-B3_EN.pdf`.
- Resgate elétrico: `Manual_Dispositivo_Resgate_Eletrico_ERB-A1_EN.pdf`.
- Encoder: `Manual_Encoder_Seno_Cosseno_EI53C9.25-2048.pdf`.
- Porta: `Manual_Comissionamento_NICE900_VerticalParts.pdf`, `Parametrização do AD30 (Motor Síncrono).pdf`.
- Resgate de passageiros: `VerticalParts_Manual_de_Resgate-2.pdf` (aprovação pendente do Gelson).
- Conceitos: `665594883-Treinamento-Villarta-Monarch-V5-0-apostila.pdf`.
- Fotos: `Fotos do quadro\` (24 imagens, 12 e 13/11/2026).
- Livro interno (apoio, não fonte): `Livro_Quadro_de_Comando_NICE3000_VerticalParts_Rev11.pdf`.

## Fluxo de um capítulo
1. Spec em `specs/capNN-*.spec.md` (público, pré-requisitos, fontes permitidas, o que é escopo e o que não é, figuras, perguntas de verificação).
2. Extratos novos vão para `sources/`, com documento e página.
3. Rascunho em `manuscript/capNN-*.md`.
4. Testes de `tests/` (a implementar): sem selos de trabalho, `Fonte:` em tabelas e figuras, termos no glossário, alerta antes de passo perigoso, parâmetros e falhas existentes no manual, links e figuras íntegros.
5. Gelson aprova. Capítulos 1, 3, 4, 5, 12 e 14 vão para a assinatura da Qualidade.
6. Só então o próximo capítulo.

## Build
- Markdown de `manuscript/` vira HTML modular; `build/tokens.css` e o CSS de impressão geram o PDF com marcadores e links.
- Cabeçalho e rodapé com logotipo de `assets/logos/`.
