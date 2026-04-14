# 📰 Jornal Online - Projeto Django

Este projeto é uma aplicação web desenvolvida em Django que simula um jornal digital. O objetivo é permitir a publicação de notícias e a interação dos leitores através de comentários, servindo como avaliação para o uso de Git/GitHub e controlo de versões.

## 🚀 Funcionalidades

- **Página Principal:** Listagem de todos os títulos das notícias publicadas.
- **Página do Artigo:** Visualização individual de cada notícia (título e corpo de texto).
- **Sistema de Comentários:** Página dedicada para ler comentários existentes e publicar novos comentários por artigo.
- **Painel de Administração:** Gestão de conteúdos (Artigos e Comentários) através do Django Admin.

## 📋 Requisitos do Trabalho

- [x] Repositório Git local e remoto (GitHub).
- [x] Histórico de desenvolvimento com um mínimo de 4 commits.
- [x] Página pública com lista de títulos clicáveis para navegação.
- [x] Página de detalhe com botão de redirecionamento para comentários.
- [x] Funcionalidade de submissão de comentários com gravação na base de dados.

## 🛠️ Tecnologias Utilizadas

- **Python 3.13**
- **Django** (Framework Web)
- **SQLite** (Base de dados local)
- **Git & GitHub** (Controlo de versões)

## 🔧 Como instalar e correr o projeto

Para testar este projeto localmente, segue os passos abaixo:

1. **Clonar o repositório:**
    ``git clone [https://github.com/O-TEU-UTILIZADOR/O-TEU-REPOSITORIO.git](https://github.com/O-TEU-UTILIZADOR/O-TEU-REPOSITORIO.git)``
    ``cd jornal``

2. **Criar e ativar o ambiente virtual:**

   ``python -m venv venv``

   # No Windows:

   ``venv\Scripts\activate``

   # No Linux/Mac:

   ``source venv/bin/activate``

3. **Instalar o Django**
    ``pip install django``

4. **Executar as migrações (configurar a base de dados):**
    ``python manage.py migrate``

5. **Criar um superutilizador (para gerir o jornal):**
    ``python manage.py createsuperuser``

6. **Iniciar o servidor de desenvolvimento:**
    ``python manage.py runserver``

7. **Aceder no browser:**
    Website: http://127.0.0.1:8000/
    Administração: http://127.0.0.1:8000/admin

## 👥 Autor
### **Tomás Matos**

*Trabalho prático para a UC de ASII - Abril 2026*
