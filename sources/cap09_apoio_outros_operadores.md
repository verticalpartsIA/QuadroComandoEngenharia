# Capítulo 9: apoio sobre outros operadores de porta (15/11/2026)

Material de **apoio de conhecimento** (não é fonte do elevador de referência). Útil para a camada "interface do quadro com qualquer operador" (spec, seção 2.1). Só vira fonte se o operador de um elevador for desses modelos.

## 1. BST BG201 (`444060259-Gearless-JSA07910E-AA-BST-BG201-adjust-manual-pdf.pdf`, 33 págs., inglês)
Controlador de porta para motor síncrono BST (47 W, 125 V, 0,42 A, 2,3 N·m), encoder ABZ, entrada monofásica de 180 a 264 V CA.
- Entradas (isoladas por optoacoplador): abrir, fechar, "nudging" (fechamento forçado) e uma reservada. Prioridade: nudging, abrir, fechar, reservada.
- Saídas a relé: limite de abertura, limite de fechamento (comum entre os dois), obstrução e falha (contato de 250 V CA / 2 A).
- Modos: IO, painel e demonstração (P01.00 igual a 0, 1 ou 4). Em modo painel o comando externo é ignorado e P01.00 deve voltar a 0.
- Passos: confirmar fiação do motor e do encoder; autoajuste do motor (P03.02 = 2); autoajuste da largura da porta (P03.02 = 1: fecha, abre, fecha; leitura em P03.03 e P03.04); depois ajustar velocidades, distâncias de desaceleração e torque de manutenção (grupos P04, P05, P06).
- Padrão de fábrica de parâmetros: P01.14 = 21 (preserva a largura da porta).
- Teclado: senha inicial 1234; teclas esquerda e direita abrem e fecham em modo painel.

## 2. BST BG101 (`278035405-BST-BG101-Door-Controler.pdf`, 22 págs., inglês e chinês)
Controlador de porta para motor assíncrono (0,4 kW ou 0,2 kW; versão síncrona "em desenvolvimento" no texto), encoder Hall-ABZ de 4 fios, entrada monofásica de 180 a 264 V CA, comunicação RS-485 (CAN opcional). Mesma lógica de entradas e saídas do BG201 (abrir, fechar, nudging, reservada; limites, obstrução, falha). Pede cabo blindado no encoder, par trançado blindado (passo de 20 a 30 mm) na comunicação e não permite teste de tensão aplicada no controlador.

## 3. Brochura J5801 + AlphaBox (`872156811-202308151647354735.pdf`, 10 págs., chinês)
Sistema em que a caixa de teto e o operador de porta formam um só conjunto e **dispensa o controlador de porta separado** (menos fiação, instalação modular). Entrada de 200 a 240 V CA, saída de 1,1 A (um operador) ou 1,1 A + 1,1 A (dois), 200 W por motor, encoder ABZ ou SPI. Tradução feita por mim a partir do texto extraído, sem tradutor nativo: tratar como indicativo.

## 4. O que isso confirma para o livro
- O quadro conversa com operadores de famílias diferentes (AD30/NICE900, BST BG101/BG201, J5801 integrado), mas o **contrato de interface é o mesmo**: alimentação monofásica de 200 a 240 V, comando de abrir e fechar, limites de abertura e fechamento, obstrução ou cortina, fechamento forçado e falha.
- O que **muda** entre famílias é a numeração de parâmetros, o modo de autoajuste e as teclas do painel. Isso justifica o capítulo em duas camadas.
- Em todos os manuais, o autoajuste tem duas partes: motor (reconhecimento dos polos) e largura da porta.
