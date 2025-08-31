# DBank

Sistema bancário simples desenvolvido em Django e Django REST Framework.

## Requisitos

- Python 3.10+
- pip
- (Recomendado) Ambiente virtual: venv ou virtualenv

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd DBank/DBank
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Realize as migrações do banco de dados:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Crie um superusuário para acessar o admin:

   ```bash
   python manage.py createsuperuser
   ```

6. Rode o servidor de desenvolvimento:
   ```bash
   python manage.py runserver
   ```

## Endpoints principais

- `/api/v1/users/` - Listar e criar usuários
- `/api/v1/accounts/` - Listar e criar contas bancárias
- `/api/v1/transactions/` - Listar e criar transações
- `/api/v1/transfers/` - Listar e criar transferências
- `/api/v1/api-token-auth/` - Obter token de autenticação
- `/admin/` - Admin do Django

## Autenticação

A maioria dos endpoints exige autenticação por token. Obtenha um token em `/api/v1/api-token-auth/` enviando `username` e `password` via POST.

Inclua o token no header das requisições:

```
Authorization: Token <seu_token>
```

## Testes

Para rodar os testes (se existirem):

```bash
python manage.py test
```

## Observações

- O projeto utiliza Django REST Framework para a API.
- O arquivo `requirements.txt` lista todas as dependências necessárias.
- Para customizações, edite os arquivos em `banking/`.

---

Sinta-se à vontade para contribuir!
