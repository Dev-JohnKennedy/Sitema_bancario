🏦 Sistema Bancário em Python (v1.0 - Modularizado)
Este é um projeto de simulação de um sistema bancário simples desenvolvido em Python. O objetivo principal é praticar a modularização do código utilizando funções (def), gerenciamento de estado (listas e variáveis) e a aplicação de boas práticas, como o uso de argumentos posicionais e nomeados, e validação de dados de entrada.

✨ Funcionalidades
O sistema oferece as seguintes operações básicas:

1. Operações de Transação
Depósito ([d]): Permite depositar valores positivos.

  Saque ([s]):

  Limitado a 3 saques diários.

  Limitado a R$ 500,00 por saque.

  Requer saldo suficiente.

  Extrato ([e]): Exibe todas as movimentações e o saldo atual.

2. Gerenciamento de Clientes e Contas
Novo Usuário ([nu]): Cadastra um cliente (pessoa física).

  Validação de CPF: Deve ter exatamente 11 dígitos numéricos e ser único no sistema.

  Validação de Nome: Deve conter apenas letras.

  Formatação de Dados: Nome, data de nascimento e endereço são formatados automaticamente.

  Nova Conta Corrente ([nc]): Abre uma conta e a vincula a um usuário existente através do CPF.

  Agência Fixa: 0001

Número da Conta: Sequencial (inicia em 1).

Listar Contas ([lc]): Exibe todas as contas cadastradas com os dados completos do titular.

💻 Como Rodar o Projeto
Pré-requisitos
O projeto é escrito em Python puro.

Python 3.x

Execução
1. Salve o Código: Salve todo o código do sistema em um arquivo chamado, por exemplo, banco.py.

2. Abra o Terminal: Navegue até o diretório onde o arquivo foi salvo.

3. Execute: Utilize o comando abaixo para iniciar o sistema:

Bash

python banco.py

Comandos de Menu
Ao rodar o script, o menu principal será exibido:

<img width="207" height="212" alt="image" src="https://github.com/user-attachments/assets/24ee5a8f-b4cd-4f09-b1e5-1b2a3c6123b3" />


⚙️ Estrutura do Código (Modularização)
O código é dividido em funções para isolar a lógica de cada operação, conforme as boas práticas de modularização.

<img width="523" height="394" alt="image" src="https://github.com/user-attachments/assets/447109c1-bed5-46d2-913b-c6b3fab72474" />
