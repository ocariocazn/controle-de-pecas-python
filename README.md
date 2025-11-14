Sistema de Controle de Peças – Python

Este projeto implementa um sistema simples de controle de qualidade e organização de peças industriais, utilizando apenas conteúdos básicos estudados na disciplina de Algoritmos e Lógica de Programação.

O sistema funciona no terminal e oferece um menu interativo para cadastro, listagem, remoção e análise das peças.

Funcionalidades

Cadastro de peças
Avaliação automática da qualidade
Armazenamento das peças aprovadas em caixas de 10 unidades
Listagem de todas as peças cadastradas
Remoção de peças
Listagem de caixas fechadas
Geração de relatório final consolidado

Regras de Qualidade

Uma peça é considerada APROVADA se:

Peso entre 95g e 105g
Cor azul ou verde
Comprimento entre 10cm e 20cm
Se qualquer uma dessas condições não for atendida, a peça é REPROVADA e recebe o motivo correspondente.
Lógica de Organização das Caixas
Apenas peças aprovadas entram nas caixas
Cada caixa comporta 10 peças
Quando a caixa atinge a capacidade máxima, ela é fechada
O sistema recalcula as caixas automaticamente sempre que peças são cadastradas ou removidas

📂 Estrutura do Projeto
controle-pecas/
│
├── main.py
├── README.md

Como Executar

No terminal, execute:
python avaliacao.py

O menu interativo aparecerá com as opções:

1 - Cadastrar peça
2 - Listar peças
3 - Remover peça
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair

Tecnologias e Conteúdos Utilizados

Python básico
Variáveis
Estruturas condicionais (if / elif / else)
Funções
Listas e dicionários

Laços de repetição (while)

Organização simples de código
