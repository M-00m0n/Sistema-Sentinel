# 🌑 SENTINEL - Central Operational System (V2.3)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Estável-green.svg" alt="Status">
</p>

O **Sentinel** é um sistema de gerenciamento de dados via terminal (CLI) desenvolvido em Python. O objetivo central é fornecer uma interface rápida e eficiente para o armazenamento e manipulação de dossiês operacionais, utilizando persistência em arquivos JSON locais.

---

## 📋 Sumário
1. [Sobre o Projeto](#sobre-o-projeto)
2. [Funcionalidades Principais](#funcionalidades-principais)
3. [Arquitetura do Sistema](#arquitetura-do-sistema)
4. [Instalação e Configuração](#instalação-e-configuração)
5. [Como Utilizar](#como-utilizar)
6. [Segurança e Dados](#segurança-e-dados)
7. [Contribuições](#contribuições)
8. [Licença](#licença)

---

## 📖 Sobre o Projeto
O Sentinel foi idealizado para ser uma central de controle leve. Diferente de sistemas complexos que dependem de bancos de dados robustos (SQL/NoSQL), este projeto utiliza a **simplicidade dos arquivos JSON** para garantir portabilidade e rapidez extrema na execução.

## ⚙️ Funcionalidades Principais
* **Cadastro Automatizado:** Criação de dossiês individuais com diretórios segregados.
* **Persistência Inteligente:** Salvamento de dados em formato estruturado (JSON).
* **Interface CLI Minimalista:** Navegação intuitiva via terminal.
* **Sistema de Edição:** Capacidade de atualizar registros existentes sem perda de dados históricos.
* **Auto-Gestão de Diretórios:** O sistema cria a estrutura necessária automaticamente caso não exista.

---

## 🏗 Arquitetura do Sistema
O sistema opera seguindo uma lógica de *Data Segregation*:
1. **Pasta Raiz:** Onde reside o arquivo `sentinel.py`.
2. **Pasta `/alvos/`:** Repositório principal de armazenamento.
3. **Estrutura JSON:** Cada alvo possui seu próprio arquivo `data.json` contendo chaves como CPF, RG, Endereço, etc.

## 🚀 Instalação e Configuração

### Pré-requisitos
* Python 3.6+ instalado.
* Sistema operacional compatível com terminal (Linux, Windows, macOS).

### Clonagem do Repositório
```bash
git clone [https://github.com/SEU_USUARIO/SENTINEL.git](https://github.com/SEU_USUARIO/SENTINEL.git)
cd SENTINEL
