#  NLP Matemático em Português

> Interprete linguagem natural em português e execute operações matemáticas.

---

## Sobre o projeto

Este é meu primeiro projeto pessoal, iniciado como um experimento: *será que consigo fazer o Python entender uma conta escrita em português?*

O **TokenizerCalc** é um interpretador de linguagem natural focado em operações aritméticas. Você digita algo como `"some 10 com 5 e depois tire 3"` e ele entende, tokeniza e calcula — sem precisar de sintaxe rígida.

Importante frisar que um dos fundamentos do projeto é se aproximar o maximo da linguagem humana e ignorando regras de procedência matemática.

O projeto está em desenvolvimento ativo desde o primeiro commit há 23 de Janeiro e já passou por várias rodadas de refatoração. Cada versão resolveu bugs reais e melhorou a arquitetura.


---

## Como funciona

O pipeline segue três etapas principais:

```
Entrada de texto
      ↓
  Validação  →  regex extrai números, módulo identifica operação
      ↓
 Tokenização →  cada palavra vira um token: NUM | OP | CON
      ↓
Processamento →  tokens são lidos em sequência, conectivos como
                 "de" invertem a ordem dos operandos quando necessário
      ↓
   Resultado
```

### Tipos de token

| Tipo | Significado | Exemplo |
|------|-------------|---------|
| `NUM` | Número operando | `10`, `1,5`, `-3` |
| `OP`  | Operação matemática | `mais`, `vezes`, `dividido` |
| `CON` | Conectivo semântico | `de`, `com` |

O conectivo `"de"` tem comportamento especial: ele sinaliza inversão de operandos, permitindo frases como *"30% de 200"* funcionarem corretamente.

---

## Estrutura do projeto

```
.
├── main.py               # Entrada, validação e pipeline principal
├── verificar_operacao.py # Detecta e mapeia operações a partir do texto
└── calculadora.py        # Executa os cálculos com os operandos resolvidos
```

---

## Exemplo de uso

```
Insira a conta que deseja fazer: some 15 com 7 e tire 4
→ 18.0

Insira a conta que deseja fazer: 30 porcento de 200
→ 60.0

Insira a conta que deseja fazer: multiplique 6 por 7
→ 42.0
```

---

## O que o validador cobre

Antes de processar, o sistema verifica:

-  Presença de ao menos dois números
-  Presença de ao menos uma operação reconhecida
-  Números com vírgula ou ponto decimal (`1,5` → `1.5`)
-  Números negativos (`-10`)

Se a entrada for inválida, uma mensagem de erro específica é exibida e o usuário pode tentar novamente.

---

## Histórico de desenvolvimento

O código original era baseado em índices e posições fixas — a lógica iterava sobre listas de valores e operações pelos seus índices numéricos, assumindo que tudo estaria na ordem certa. 

Na prática, qualquer variação na entrada quebrava o fluxo: um número fora do lugar, uma operação não detectada ou uma frase com estrutura diferente eram suficientes para produzir resultados errados ou travar a execução. Refatorar parecia arriscado — o código "funcionava" nos casos que eu testava, e mexer nele sem uma estrutura melhor em mente poderia quebrar tudo. 

Mesmo assim, tomei a decisão de abandonar a abordagem por posição e reescrever o processamento em torno de tokens com tipo e valor, onde cada elemento da frase carrega sua própria identidade independente da ordem em que aparece. 

---

## Limitações conhecidas (V1)

- Suporte a conectivos ainda limitado (`"de"`, `"com"`)
- Expressões com parênteses não são suportadas
- Apenas operações binárias (dois operandos por vez, encadeados)

---

## Próximos passos

- Ampliar vocabulário de conectivos e sinônimos de operação
-  Suporte a porcentagem como operação nativa (`"30% de 200"`)
-  Testes automatizados para cada caso de entrada
-  Interface simples via terminal com histórico de cálculos

---

## Tecnologias

- **Python 3.x**
- **Módulo `re`** — expressões regulares para extração de números
- Arquitetura modular com separação de responsabilidades

---

## Aprendizados

Este projeto me ensinou na prática:

- Como estruturar um pipeline de processamento de texto
- A diferença entre tokenizar e interpretar
- Por que casos de borda (zero, vírgula, inversão de operandos) importam mais do que o caso feliz
- Como refatorar código incremental sem perder o fio da lógica

---

*Primeiro projeto. Muito bugado no começo. Muito melhor agora. Ainda em construção.*
