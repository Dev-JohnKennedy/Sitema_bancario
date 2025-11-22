# 💰 Sistema Bancário em Python (Console)

Um sistema bancário simples desenvolvido em Python, utilizando funções, validações de entrada e organização por camadas lógicas.  
Este projeto simula as operações essenciais de um banco: criação de usuários, contas, depósitos, saques e emissão de extrato.

---

## 📌 Funcionalidades Implementadas

### 👤 Gestão de Usuários
- Criar usuário com:
  - CPF (apenas números — 11 dígitos, validação incluída)
  - Nome completo (somente letras)
  - Data de nascimento (formato flexível aceitando `ddmmyyyy`, `dd/mm/yyyy`, etc.)
  - Endereço completo (formato livre)
- Impede duplicação de usuários pelo CPF.
- Busca de usuário por CPF ao criar contas.

---

### 🏦 Gestão de Contas Correntes
- Criação de contas vinculadas a usuários existentes.
- Cada conta recebe:
  - Agência (fixa: `0001`)
  - Número da conta sequencial (1, 2, 3...)
  - Objeto usuário vinculado

- Listagem de todas as contas cadastradas com:
  - Agência
  - Número da conta
  - Nome do titular
  - CPF
  - Data de nascimento
  - Endereço

---

### 💸 Operações Financeiras

#### ✔ Depósito
- Aceita apenas valores positivos.
- Atualiza saldo e extrato.

#### ✔ Saque
- Regras de negócio implementadas:
  - Máximo de **3 saques por sessão**
  - Limite máximo de **R$ 500 por saque**
  - Verifica saldo insuficiente
  - Não aceita valores inválidos (negativos ou zero)
- Atualiza saldo, extrato e contador de saques.

#### ✔ Extrato
Mostra:
- Lista de depósitos e saques realizados
- Saldo atual
- Caso não haja movimentações, exibe mensagem específica

---

## 🧠 Estrutura Lógica do Sistema

### 🔍 Filtragem de Usuário
```python
filtrar_usuario(cpf, usuarios)

🧑‍💼 Criar Usuário
criar_usuario(usuarios)


Inclui validações completas de CPF, nome e data de nascimento.

🏦 Criar Conta Corrente
criar_conta_corrente(agencia, numero_conta, usuarios)


A conta só é criada se o CPF informado existir no sistema.

💰 Depósito
depositar(saldo, valor, extrato, /)


Usa parâmetros posicionais-only.

💵 Saque
sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)


Usa parâmetros nomeados-only e aplica validações.

📄 Extrato
exibir_extrato(saldo, /, *, extrato)

🖥️ Menu Principal

O sistema é totalmente interativo via terminal, com o menu:

==================== MENU ====================
[d]  Depositar
[s]  Sacar
[e]  Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q]  Sair
==============================================
