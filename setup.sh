#!/bin/bash

# Script de inicialização do projeto WorkoutAPI

echo "🏋️  Iniciando configuração do WorkoutAPI..."

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não está instalado. Por favor, instale Python 3.10+"
    exit 1
fi

# Verificar se Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker não está instalado. Por favor, instale Docker"
    exit 1
fi

# Verificar se Docker Compose está instalado
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose não está instalado. Por favor, instale Docker Compose"
    exit 1
fi

echo "✅ Pré-requisitos verificados!"

# Criar ambiente virtual se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv .venv
fi

# Ativar ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source .venv/bin/activate

# Instalar dependências
echo "📚 Instalando dependências..."
pip install --upgrade pip
pip install -r workout_api/requirements.txt

# Criar arquivo .env se não existir
if [ ! -f ".env" ]; then
    echo "⚙️  Criando arquivo de configuração..."
    cp .env.example .env
fi

# Iniciar banco de dados
echo "🗃️  Iniciando banco de dados..."
docker-compose up -d

# Aguardar o banco inicializar
echo "⏳ Aguardando banco de dados inicializar..."
sleep 10

# Executar migrações
echo "🔄 Executando migrações..."
make run-migrations

echo ""
echo "🎉 Configuração concluída!"
echo ""
echo "Para iniciar a aplicação, execute:"
echo "  make run"
echo ""
echo "A API estará disponível em: http://localhost:8000"
echo "Documentação Swagger: http://localhost:8000/docs"
echo ""
