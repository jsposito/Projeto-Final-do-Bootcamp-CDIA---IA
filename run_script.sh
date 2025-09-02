#!/bin/bash

# Script de execução facilitada para o projeto Bootcamp ML
# Autor: Bootcamp CDIA
# Data: Setembro 2025

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Banner do projeto
show_banner() {
    echo -e "${CYAN}"
    echo "╔══════════════════════════════════════════════════════════════╗"
    echo "║              🤖 SISTEMA DE MANUTENÇÃO PREDITIVA             ║"
    echo "║                     Bootcamp CDIA 2025                      ║"
    echo "╚══════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

# Funções para mensagens
print_step() {
    echo -e "${BLUE}[PASSO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[✅ SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[⚠️  WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[❌ ERROR]${NC} $1"
}

print_info() {
    echo -e "${PURPLE}[ℹ️  INFO]${NC} $1"
}

# Menu principal
show_menu() {
    echo ""
    echo -e "${CYAN}Escolha uma opção:${NC}"
    echo "1. 🚀 Setup Completo (primeira vez)"
    echo "2. 🔄 Executar Jupyter Notebook"
    echo "3. 🌐 Executar API REST"
    echo "4. 🎯 Executar Treinamento"
    echo "5. 📊 Ver Status dos Containers"
    echo "6. 📝 Ver Logs"
    echo "7. 🛠️  Acessar Shell do Container"
    echo "8. 🧹 Limpeza Completa"
    echo "9. ❓ Ajuda"
    echo "0. 🚪 Sair"
    echo ""
    echo -n "Digite sua escolha [0-9]: "
}

# Verificar pré-requisitos
check_prerequisites() {
    print_step "Verificando pré-requisitos..."
    
    # Docker
    if ! command -v docker &> /dev/null; then
        print_error "Docker não encontrado!"
        echo "Instale em: https://docs.docker.com/get-docker/"
        exit 1
    fi
    
    # Docker Compose
    if ! command -v docker-compose &> /dev/null; then
        print_error "Docker Compose não encontrado!"
        echo "Instale em: https://docs.docker.com/compose/install/"
        exit 1
    fi
    
    print_success "Pré-requisitos OK"
}

# Setup completo
setup_complete() {
    print_step "Executando setup completo..."
    
    # Criar diretórios
    mkdir -p data models outputs visualizations notebooks
    print_success "Diretórios criados"
    
    # Verificar dados
    if [ ! -f "data/bootcamp_train.csv" ]; then
        print_warning "Arquivo 'data/bootcamp_train.csv' não encontrado!"
        echo "Por favor, coloque o arquivo na pasta 'data/' e execute novamente."
        read -p "Pressione Enter após colocar o arquivo..."
    fi
    
    # Build
    print_step "Construindo imagem Docker..."
    if docker-compose build; then
        print_success "Imagem construída com sucesso!"
    else
        print_error "Falha na construção da imagem"
        return 1
    fi
    
    # Executar
    print_step "Iniciando containers..."
    docker-compose up -d
    
    print_success "Setup completo finalizado!"
    echo ""
    print_info "Jupyter Notebook: http://localhost:8888"
    print_info "Para API REST, escolha opção 3 no menu"
}

# Executar Jupyter
run_jupyter() {
    print_step "Iniciando Jupyter Notebook..."
    
    if docker-compose ps | grep -q "bootcamp_jupyter.*Up"; then
        print_info "Jupyter já está executando!"
    else
        docker-compose up -d jupyter
        print_success "Jupyter iniciado!"
    fi
    
    echo ""
    print_info "📖 Acesse: http://localhost:8888"
    print_info "🔧 Para parar: docker-compose stop jupyter"
}

# Executar API
run_api() {
    print_step "Iniciando API REST..."
    
    # Verificar se modelo existe
    if [ ! -f "models/modelo_otimizado.pkl" ]; then
        print_warning "Modelo não encontrado! Execute o treinamento primeiro."
        echo "Deseja treinar agora? (y/n)"
        read -r response
        if [[ "$response" == "y" || "$response" == "Y" ]]; then
            run_training
        else
            return 1
        fi
    fi
    
    if docker-compose -f docker-compose-full.yml ps | grep -q "bootcamp_api.*Up"; then
        print_info "API já está executando!"
    else
        docker-compose -f docker-compose-full.yml up -d api
        print_success "API iniciada!"
    fi
    
    echo ""
    print_info "🌐 API: http://localhost:8000"
    print_info "📚 Docs: http://localhost:8000/docs"
    print_info "🔧 Para parar: docker-compose -f docker-compose-full.yml stop api"
}

# Executar treinamento
run_training() {
    print_step "Executando treinamento do modelo..."
    
    # Verificar dados
    if [ ! -f "data/bootcamp_train.csv" ]; then
        print_error "Arquivo 'data/bootcamp_train.csv' não encontrado!"
        echo "Coloque o arquivo na pasta 'data/' e tente novamente."
        return 1
    fi
    
    print_info "Dados encontrados. Iniciando treinamento..."
    print_warning "Este processo pode levar alguns minutos..."
    
    # Executar treinamento
    if docker-compose -f docker-compose-full.yml --profile training up trainer; then
        print_success "Treinamento concluído!"
        
        # Verificar se modelo foi criado
        if [ -f "models/modelo_otimizado.pkl" ]; then
            print_success "Modelo salvo em models/modelo_otimizado.pkl"
        fi
        
        # Verificar outputs
        if [ -f "outputs/submission.csv" ]; then
            print_success "Arquivo de submissão gerado: outputs/submission.csv"
        fi
        
    else
        print_error "Falha no treinamento"
        return 1
    fi
}

# Ver status
show_status() {
    print_step "Verificando status dos containers..."
    echo ""
    
    # Status geral
    echo -e "${CYAN}Status dos Containers:${NC}"
    docker-compose ps
    
    echo ""
    echo -e "${CYAN}Uso de Recursos:${NC}"
    docker stats --no-stream --format "table {{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}" 2>/dev/null || echo "Nenhum container executando"
    
    echo ""
    echo -e "${CYAN}Arquivos Importantes:${NC}"
    [ -f "data/bootcamp_train.csv" ] && echo "✅ Dados de treino" || echo "❌ Dados de treino"
    [ -f "data/bootcamp_test.csv" ] && echo "✅ Dados de teste" || echo "⚠️  Dados de teste (opcional)"
    [ -f "models/modelo_otimizado.pkl" ] && echo "✅ Modelo treinado" || echo "❌ Modelo treinado"
    [ -f "outputs/submission.csv" ] && echo "✅ Submissão gerada" || echo "❌ Submissão gerada"
}

# Ver logs
show_logs() {
    echo -e "${CYAN}Escolha o serviço para ver logs:${NC}"
    echo "1. Todos os serviços"
    echo "2. Jupyter"
    echo "3. API"
    echo "4. Voltar"
    echo ""
    echo -n "Digite sua escolha [1-4]: "
    read -r choice
    
    case $choice in
        1)
            print_info "Mostrando logs de todos os serviços..."
            docker-compose logs --tail=50 -f
            ;;
        2)
            print_info "Mostrando logs do Jupyter..."
            docker-compose logs jupyter --tail=50 -f
            ;;
        3)
            print_info "Mostrando logs da API..."
            docker-compose -f docker-compose-full.yml logs api --tail=50 -f
            ;;
        4)
            return
            ;;
        *)
            print_error "Opção inválida!"
            ;;
    esac
}

# Acessar shell
access_shell() {
    print_step "Acessando shell do container..."
    
    if docker-compose ps | grep -q "bootcamp_jupyter.*Up"; then
        print_info "Entrando no container Jupyter..."
        docker exec -it bootcamp_jupyter bash
    else
        print_warning "Container Jupyter não está executando."
        echo "Deseja iniciar? (y/n)"
        read -r response
        if [[ "$response" == "y" || "$response" == "Y" ]]; then
            docker-compose up -d jupyter
            docker exec -it bootcamp_jupyter bash
        fi
    fi
}

# Limpeza completa
clean_all() {
    print_warning "⚠️  ATENÇÃO: Isso removerá todos os containers, imagens e volumes!"
    echo "Tem certeza? (y/N)"
    read -r response
    
    if [[ "$response" == "y" || "$response" == "Y" ]]; then
        print_step "Executando limpeza completa..."
        
        # Parar containers
        docker-compose down
        docker-compose -f docker-compose-full.yml down
        
        # Remover imagens
        docker rmi bootcamp-ml 2>/dev/null || true
        
        # Limpeza geral
        docker system prune -f
        
        print_success "Limpeza concluída!"
    else
        print_info "Limpeza cancelada."
    fi
}

# Mostrar ajuda
show_help() {
    echo -e "${CYAN}📖 Guia de Ajuda${NC}"
    echo ""
    echo -e "${YELLOW}Arquivos Principais:${NC}"
    echo "  main.py              - Script Python principal"
    echo "  api.py               - API REST (bonus)"
    echo "  RandomForest.ipynb   - Notebook original"
    echo "  Dockerfile           - Configuração do container"
    echo "  docker-compose.yml   - Orquestração básica"
    echo ""
    echo -e "${YELLOW}Comandos Make Úteis:${NC}"
    echo "  make help            - Ver comandos disponíveis"
    echo "  make quick-start     - Setup + build + run"
    echo "  make train           - Executar treinamento"
    echo "  make shell           - Acessar shell"
    echo "  make clean           - Limpeza completa"
    echo ""
    echo -e "${YELLOW}URLs Importantes:${NC}"
    echo "  http://localhost:8888     - Jupyter Notebook"
    echo "  http://localhost:8000     - API REST"
    echo "  http://localhost:8000/docs - Documentação da API"
    echo ""
    echo -e "${YELLOW}Estrutura de Pastas:${NC}"
    echo "  data/           - Arquivos CSV"
    echo "  models/         - Modelos treinados"
    echo "  outputs/        - Resultados finais"
    echo "  visualizations/ - Gráficos gerados"
    echo ""
}

# Loop principal
main() {
    show_banner
    check_prerequisites
    
    while true; do
        show_menu
        read -r choice
        
        case $choice in
            1)
                echo ""
                setup_complete
                ;;
            2)
                echo ""
                run_jupyter
                ;;
            3)
                echo ""
                run_api
                ;;
            4)
                echo ""
                run_training
                ;;
            5)
                echo ""
                show_status
                ;;
            6)
                echo ""
                show_logs
                ;;
            7)
                echo ""
                access_shell
                ;;
            8)
                echo ""
                clean_all
                ;;
            9)
                echo ""
                show_help
                ;;
            0)
                echo ""
                print_success "Saindo... Obrigado por usar o sistema!"
                break
                ;;
            *)
                print_error "Opção inválida! Digite um número de 0 a 9."
                ;;
        esac
        
        echo ""
        echo -e "${CYAN}Pressione Enter para continuar...${NC}"
        read -r
    done
}

# Verificar se é execução direta
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi