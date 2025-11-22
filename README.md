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
Salve o Código: Salve todo o código do sistema em um arquivo chamado, por exemplo, banco.py.

Abra o Terminal: Navegue até o diretório onde o arquivo foi salvo.

Execute: Utilize o comando abaixo para iniciar o sistema:

Bash

python banco.py

Comandos de Menu
Ao rodar o script, o menu principal será exibido:

Comando,Descrição
d,Realizar Depósito
s,Realizar Saque
e,Exibir Extrato
nu,Cadastrar Novo Usuário
nc,Criar Nova Conta
lc,Listar Contas
q,Sair do sistema

⚙️ Estrutura do Código (Modularização)
O código é dividido em funções para isolar a lógica de cada operação, conforme as boas práticas de modularização.

Função,Tipo de Argumento,Retorno,Descrição
depositar,Posicional-only (/),"saldo, extrato",Adiciona valor ao saldo e registra no extrato.
sacar,Keyword-only (*),"saldo, extrato, numero_saques",Verifica limites de saldo/valor/saques antes de debitar.
exibir_extrato,Posicional e Keyword,Nenhum,Imprime as movimentações e o saldo.
filtrar_usuario,Posicional,usuario (dict),Busca um usuário por CPF.
criar_usuario,Posicional,Nenhum,Cadastra um novo cliente com validação rigorosa.
criar_conta_corrente,Posicional,conta (dict),Cria conta e a vincula ao cliente.
listar_contas,Posicional,Nenhum,Exibe lista de contas e dados dos titulares.
main,-,-,Função principal que gerencia o estado global (listas) e o loop de execução do menu.

➡️ Próximos Passos de Evolução
Para aprimorar este projeto, sugere-se a refatoração para o paradigma de Programação Orientada a Objetos (POO).

Classes: Criar classes como Cliente, Conta, e ContaCorrente para encapsular dados e comportamento.

Multi-Contas: Adaptar as funções de transação para operar em uma conta específica (passando o número da conta como parâmetro).
