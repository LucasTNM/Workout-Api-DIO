# 🏋️ WorkoutAPI

Uma API REST moderna desenvolvida com FastAPI para gerenciamento de atletas, categorias e centros de treinamento.

## 🚀 Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido para Python
- **SQLAlchemy** - ORM para Python com suporte assíncrono
- **Alembic** - Ferramenta de migração de banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Docker** - Containerização da aplicação
- **Pydantic** - Validação de dados e serialização
- **Uvicorn** - Servidor ASGI de alta performance

## 📋 Funcionalidades

### 🏃‍♀️ Atletas
- ✅ Criar novo atleta
- ✅ Listar todos os atletas
- ✅ Buscar atleta por ID
- ✅ Atualizar dados do atleta
- ✅ Deletar atleta

### 🏷️ Categorias
- ✅ Criar nova categoria
- ✅ Listar todas as categorias
- ✅ Buscar categoria por ID
- ✅ Atualizar categoria
- ✅ Deletar categoria

### 🏢 Centros de Treinamento
- ✅ Criar novo centro de treinamento
- ✅ Listar todos os centros
- ✅ Buscar centro por ID
- ✅ Atualizar centro de treinamento
- ✅ Deletar centro de treinamento

## 🛠️ Instalação e Configuração

### Pré-requisitos

- Python 3.10+
- Docker e Docker Compose
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/workout-api.git
cd workout-api
```

### 2. Configure o ambiente

```bash
# Crie um ambiente virtual
python -m venv .venv

# Ative o ambiente virtual
# No Linux/Mac:
source .venv/bin/activate
# No Windows:
.venv\Scripts\activate

# Instale as dependências
pip install -r workout_api/requirements.txt
```

### 3. Configure o banco de dados

```bash
# Inicie o PostgreSQL com Docker
docker-compose up -d

# Execute as migrações
make run-migrations
```

### 4. Inicie a aplicação

```bash
# Usando o Makefile
make run

# Ou diretamente
uvicorn workout_api.main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📖 Documentação da API

Após iniciar a aplicação, acesse:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🗃️ Estrutura do Projeto

```
workout_api/
├── alembic/                    # Migrações do banco de dados
│   ├── versions/
│   ├── env.py
│   └── script.py.mako
├── workout_api/               # Código principal da aplicação
│   ├── atleta/               # Módulo de atletas
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── categorias/           # Módulo de categorias
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── centro_treinamento/   # Módulo de centros de treinamento
│   │   ├── controller.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── config/               # Configurações
│   │   ├── database.py
│   │   └── settings.py
│   ├── contrib/              # Utilitários compartilhados
│   │   ├── dependencies.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── main.py              # Ponto de entrada da aplicação
│   ├── router.py            # Configuração das rotas
│   └── requirements.txt     # Dependências Python
├── docker-compose.yml        # Configuração do Docker
├── Makefile                 # Comandos úteis
├── alembic.ini             # Configuração do Alembic
└── README.md               # Este arquivo
```

## 🔧 Comandos Úteis

```bash
# Iniciar a aplicação
make run

# Criar nova migração
make create-migrations d="descrição_da_migração"

# Executar migrações
make run-migrations

# Iniciar apenas o banco de dados
docker-compose up -d

# Parar todos os serviços
docker-compose down
```

## 📊 Modelos de Dados

### Atleta
```json
{
  "id": "uuid4",
  "nome": "string",
  "cpf": "string",
  "idade": "integer",
  "peso": "float",
  "altura": "float",
  "sexo": "string",
  "categoria": {
    "nome": "string"
  },
  "centro_treinamento": {
    "nome": "string"
  }
}
```

### Categoria
```json
{
  "id": "uuid4",
  "nome": "string"
}
```

### Centro de Treinamento
```json
{
  "id": "uuid4",
  "nome": "string",
  "endereco": "string",
  "proprietario": "string"
}
```

## 🧪 Exemplos de Uso

### Criar um atleta

```bash
curl -X POST "http://localhost:8000/atletas/" \
  -H "Content-Type: application/json" \
  -d '{
    "nome": "João Silva",
    "cpf": "12345678901",
    "idade": 25,
    "peso": 75.5,
    "altura": 1.75,
    "sexo": "M",
    "categoria": {"nome": "Scale"},
    "centro_treinamento": {"nome": "CT King"}
  }'
```

### Listar todos os atletas

```bash
curl -X GET "http://localhost:8000/atletas/"
```

### Buscar atleta por ID

```bash
curl -X GET "http://localhost:8000/atletas/f7350a7c-5358-4d23-ba1f-1944564b25c7"
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 👨‍💻 Autor

**Lucas Tony**
- GitHub: [@LucasTNM](https://github.com/LucasTNM/)
- LinkedIn: [Lucas Tony](https://www.linkedin.com/in/lucas-tony-6899b6336/)

## 🙏 Agradecimentos

- FastAPI pela excelente documentação
- SQLAlchemy pela robustez do ORM
- Comunidade Python pelo suporte contínuo

---

⭐ Não esqueça de dar uma estrela se este projeto te ajudou!
