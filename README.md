# NeuroPsic API

## Visão geral
Este projeto Django foi refatorado para usar **Supabase Postgres** como banco principal e expor uma API REST via **Django REST Framework**.

API = neuropsic

## Configuração rápida
1. Ative arquivo venv e crie um ambiente virtual
   ```bash
   source venv/bin/activate
   python3 -m venv venv
   ```
2. Instale dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Rode migrações:
   ```bash
   cd neuropsic
   python manage.py migrate
   ```
4. Rode servidor:
   ```bash
   python manage.py runserver
   ```

## Endpoints principais
- `GET /api/users/` — lista usuários
- `POST /api/users/` — cria usuário
- `PATCH /api/users/{id}/` — atualiza parcialmente
