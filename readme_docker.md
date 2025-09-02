# 🤖 Sistema de Manutenção Preditiva - Bootcamp CDIA

Este projeto implementa um sistema inteligente de manutenção preditiva para identificar falhas em máquinas industriais usando Machine Learning. O sistema utiliza Random Forest com otimização de hiperparâmetros para classificação multirrótulo de 5 tipos diferentes de falhas.

## 📋 Visão Geral do Projeto

### Objetivo
Desenvolver um sistema capaz de:
- Identificar falhas em máquinas industriais
- Classificar o tipo específico da falha
- Retornar probabilidades associadas às predições
- Fornecer insights através de visualizações

### Tipos de Falhas Detectadas
1. **FDF** - Falha Desgaste Ferramenta
2. **FDC** - Falha Dissipação Calor  
3. **FP** - Falha Potência
4. **FTE** - Falha Tensão Excessiva
5. **FA** - Falha Aleatória

## 🏗️ Arquitetura do Sistema

### 📄 Arquivos Principais
| Arquivo | Descrição | Tipo |
|---------|-----------|------|
| `main.py` | Script Python principal com classe ManutencaoPreditiva | 🐍 Core |
| `RandomForest.ipynb` | Notebook Jupyter original | 📓 Notebook |
| `api.py` | API REST com FastAPI | 🌐 Bonus |
| `config.py` | Configurações centralizadas | ⚙️ Config |

### 🐋 Arquivos Docker
| Arquivo | Descrição | Uso |
|---------|-----------|-----|
| `Dockerfile` | Configuração do container | Build da imagem |
| `docker-compose.yml` | Orquestração básica (Jupyter) | Desenvolvimento |
| `docker-compose-full.yml` | Versão completa (Jupyter + API) | Produção |
| `.dockerignore` | Arquivos ignorados pelo Docker | Otimização |

### 🛠️ Automação e Configuração  
| Arquivo | Descrição | Funcionalidade |
|---------|-----------|----------------|
| `setup.sh` | Script de configuração inicial | Setup automático |
| `run.sh` | Script de execução interativa | Menu facilitado |
| `Makefile` | Comandos automatizados | Automação avançada |
| `requirements.txt` | Dependências Python | Gestão de pacotes |
| `.env` | Variáveis de ambiente | Configuração runtime |

## 🚀 Guia de Início Rápido

### 🎯 **Método 1: Script Interativo (Mais Fácil)**
```bash
# Dar permissão e executar
chmod +x run.sh
./run.sh

# Menu interativo aparecerá:
# 1. 🚀 Setup Completo (primeira vez)
# 2. 🔄 Executar Jupyter Notebook  
# 3. 🌐 Executar API REST
# etc...
```

### 🎯 **Método 2: Setup Automático**
```bash
# Setup completo em um comando
chmod +x setup.sh
./setup.sh

# Colocar dados
cp bootcamp_train.csv data/

# Executar
make quick-start
```

### 🎯 **Método 3: Manual Tradicional**
```bash
# Estrutura básica
mkdir -p data models outputs visualizations

# Colocar dados
cp bootcamp_train.csv data/

# Docker
docker-compose up --build
```

### Pré-requisitos
- Docker instalado
- Docker Compose instalado

### Estrutura do Projeto
```
projeto/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── main.py
├── RandomForest.ipynb
├── data/
│   ├── bootcamp_train.csv
│   └── bootcamp_test.csv (opcional)
├── models/
├── outputs/
├── visualizations/
└── notebooks/
```

## 📁 Estrutura Completa do Projeto

```
bootcamp_ml_project/
│
├── 📚 DOCUMENTAÇÃO
│   ├── README.md                    # Este arquivo - guia completo
│   └── .env                         # Variáveis de ambiente
│
├── 🐋 DOCKER & CONTAINERIZAÇÃO
│   ├── Dockerfile                   # Definição da imagem
│   ├── docker-compose.yml           # Orquestração básica  
│   ├── docker-compose-full.yml      # Versão completa (Jupyter + API)
│   └── .dockerignore               # Exclusões do build
│
├── 🐍 CÓDIGO PYTHON
│   ├── main.py                      # ⭐ Script principal - Classe ManutencaoPreditiva
│   ├── api.py                       # 🌐 API REST com FastAPI (BONUS)
│   ├── config.py                    # ⚙️ Configurações centralizadas
│   └── RandomForest.ipynb           # 📓 Notebook Jupyter original
│
├── 📊 DADOS
│   └── data/
│       ├── bootcamp_train.csv       # 📈 Dados de treinamento
│       └── bootcamp_test.csv        # 🧪 Dados de teste (opcional)
│
├── 🤖 MODELOS TREINADOS  
│   └── models/
│       ├── modelo_otimizado.pkl     # 🎯 Modelo final otimizado
│       └── modelo_basico.pkl        # 🔧 Modelo básico (backup)
│
├── 📈 RESULTADOS & OUTPUTS
│   └── outputs/
│       ├── submission.csv           # 📝 Arquivo final de submissão
│       └── metricas.json           # 📊 Métricas de performance
│
├── 🎨 VISUALIZAÇÕES
│   └── visualizations/
│       ├── analise_exploratoria.png # 📊 Gráficos EDA
│       └── confusion_matrices.png   # 🎯 Matrizes de confusão
│
├── 📓 NOTEBOOKS (desenvolvimento)
│   └── notebooks/
│       └── (seus notebooks adicionais)
│
└── 🛠️ AUTOMAÇÃO & SCRIPTS
    ├── setup.sh                    # 🚀 Configuração inicial automática
    ├── run.sh                      # 🎮 Menu interativo de execução
    ├── Makefile                    # ⚡ Comandos automatizados
    └── requirements.txt            # 📦 Dependências Python
```

## 🎮 Scripts de Execução Facilitada

### 🚀 **setup.sh** - Configuração Inicial
Script que automatiza todo o setup inicial:
```bash
chmod +x setup.sh
./setup.sh
```

**O que faz:**
- ✅ Verifica instalação Docker/Docker Compose
- ✅ Cria estrutura de diretórios
- ✅ Valida arquivos necessários  
- ✅ Constrói imagem Docker
- ✅ Fornece instruções de próximos passos

### 🎮 **run.sh** - Menu Interativo
Script com menu amigável para todas as operações:
```bash
chmod +x run.sh
./run.sh
```

**Menu disponível:**
```
1. 🚀 Setup Completo (primeira vez)
2. 🔄 Executar Jupyter Notebook
3. 🌐 Executar API REST  
4. 🎯 Executar Treinamento
5. 📊 Ver Status dos Containers
6. 📝 Ver Logs
7. 🛠️ Acessar Shell do Container
8. 🧹 Limpeza Completa
9. ❓ Ajuda
0. 🚪 Sair
```

### ⚡ **Makefile** - Comandos Automatizados
Comandos rápidos para operações comuns:
```bash
make help           # 📖 Ver todos os comandos
make quick-start    # 🚀 Setup + build + run automático  
make setup          # 📁 Criar estrutura de pastas
make build          # 🔨 Construir imagem Docker
make run            # ▶️ Executar containers
make train          # 🎯 Executar treinamento
make stop           # ⏹️ Parar containers
make clean          # 🧹 Limpeza completa
make logs           # 📝 Ver logs em tempo real
make shell          # 🐚 Acessar bash do container
make status         # 📊 Status dos containers
make backup-models  # 💾 Backup dos modelos
``` Fácil)
```bash
# Setup completo automático
make quick-start

# Ou passo a passo
make setup        # Criar pastas
make build        # Construir imagem  
make run          # Executar containers
```

#### 🎯 Opção 2: Docker Compose Básico
```bash
# Apenas Jupyter
docker-compose up --build

# Em background
docker-compose up -d --build
```

#### 🎯 Opção 3: Docker Compose Completo (com API)
```bash
# Jupyter + API REST
docker-compose -f docker-compose-full.yml up --build

# Apenas treinar modelo
docker-compose -f docker-compose-full.yml --profile training up trainer
```

#### 🎯 Opção 4: Docker Direto
```bash
# Construir imagem
docker build -t bootcamp-ml .

# Executar container
docker run -p 8888:8888 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/outputs:/app/outputs \
  bootcamp-ml
```

## 🌐 Acessando os Serviços

### Jupyter Notebook
- **URL:** http://localhost:8888
- **Token:** Não necessário (acesso direto configurado)
- **Função:** Desenvolvimento e análise interativa

### API REST (Bonus)
- **URL:** http://localhost:8000
- **Documentação:** http://localhost:8000/docs (Swagger UI)
- **Função:** Servir modelo via API

## 🔧 Comandos Úteis do Makefile

```bash
make help           # Ver todos os comandos disponíveis
make setup          # Criar estrutura de pastas
make build          # Construir imagem Docker  
make run            # Executar containers
make stop           # Parar containers
make restart        # Reiniciar containers
make logs           # Ver logs em tempo real
make shell          # Acessar shell do container
make train          # Executar treinamento do modelo
make clean          # Limpar containers e imagens
make status         # Ver status dos containers
make quick-start    # Setup + build + run automático
make backup-models  # Backup dos modelos treinados
```

## 🐍 Executando o Script Python Principal

### Dentro do Container
```bash
# Entrar no container
docker exec -it bootcamp_jupyter bash

# Executar pipeline completo
python main.py
```

### Diretamente (se Python instalado)
```bash
pip install -r requirements.txt
python main.py
```

## 📊 Funcionalidades do Sistema

### Classe ManutencaoPreditiva (main.py)

#### Métodos Principais:
- `carregar_dados()` - Carrega datasets de treino e teste
- `diagnostico_dados()` - Análise completa dos dados
- `limpar_dados()` - Limpeza e pré-processamento
- `analise_exploratoria()` - EDA com visualizações
- `preparar_dados()` - Preparação para ML
- `treinar_modelo()` - Treinamento com otimização
- `avaliar_modelo()` - Métricas de performance
- `gerar_predicoes()` - Predições para teste
- `executar_pipeline_completo()` - Pipeline end-to-end

### API REST Endpoints (api.py)

#### Principais Rotas:
- `GET /` - Status da API
- `GET /health` - Health check
- `POST /predizer` - Predição individual
- `POST /predizer_lote` - Predição em lote (CSV)
- `GET /modelo/info` - Informações do modelo
- `POST /retreinar` - Retreinar modelo
- `GET /metrics` - Métricas de performance

### Exemplo de Uso da API:
```python
import requests

# Predição individual
data = {
    "tipo": "M",
    "temperatura_ar": 300.0,
    "temperatura_processo": 310.0,
    "velocidade_rotacional": 1500.0,
    "torque": 40.0,
    "desgaste_da_ferramenta": 200.0
}

response = requests.post("http://localhost:8000/predizer", json=data)
print(response.json())
```

## 📁 Estrutura Completa do Projeto

```
bootcamp_ml_project/
├── 📝 Documentação
│   ├── README.md
│   └── .env
│
├── 🐋 Docker
│   ├── Dockerfile
│   ├── docker-compose.yml
│   ├── docker-compose-full.yml
│   └── .dockerignore
│
├── 🐍 Código Python
│   ├── main.py                    # Script principal
│   ├── api.py                     # API REST (bonus)
│   └── RandomForest.ipynb         # Notebook original
│
├── 📊 Dados
│   └── data/
│       ├── bootcamp_train.csv     # Dados de treino
│       └── bootcamp_test.csv      # Dados de teste (opcional)
│
├── 🤖 Modelos
│   └── models/
│       └── modelo_otimizado.pkl   # Modelo treinado
│
├── 📈 Outputs
│   └── outputs/
│       ├── submission.csv         # Submissão final
│       └── metricas.json          # Métricas do modelo
│
├── 🎨 Visualizações
│   └── visualizations/
│       ├── analise_exploratoria.png
│       └── confusion_matrices.png
│
└── 🛠️ Automação
    ├── Makefile                   # Comandos facilitados
    ├── setup.sh                   # Script de configuração
    └── requirements.txt           # Dependências Python
```

## 🔍 Detalhamento dos Arquivos

### 📄 **Dockerfile**
- Imagem base: Python 3.9-slim
- Instala dependências do sistema (gcc, g++)
- Configura ambiente Jupyter
- Expõe porta 8888

### 📄 **docker-compose.yml** (Básico)
- Serviço único: Jupyter Notebook
- Volumes para persistência
- Rede isolada

### 📄 **docker-compose-full.yml** (Completo)
- **jupyter:** Desenvolvimento interativo
- **api:** Servidor FastAPI  
- **trainer:** Execução de treinamento
- Profiles para controle seletivo

### 📄 **main.py** (Script Principal)
```python
# Classe principal
class ManutencaoPreditiva:
    - diagnostico_dados()      # Análise dos dados
    - limpar_dados()          # Pré-processamento  
    - analise_exploratoria()  # EDA com gráficos
    - treinar_modelo()        # ML com otimização
    - avaliar_modelo()        # Métricas de performance
    - gerar_predicoes()       # Predições finais
```

### 📄 **api.py** (API REST)
```python
# Endpoints principais
POST /predizer              # Predição individual
POST /predizer_lote         # Predição em lote (CSV)
GET  /modelo/info          # Info do modelo
POST /retreinar            # Retreinar modelo
GET  /metrics              # Métricas de performance
```

### 📄 **setup.sh** (Configuração Automática)
- Verifica instalação Docker/Docker Compose
- Cria estrutura de diretórios
- Valida arquivos necessários
- Constrói imagem Docker
- Fornece instruções de uso

### 📄 **Makefile** (Automação)
- `make quick-start` - Setup completo automático
- `make build/run/stop` - Gestão de containers
- `make train` - Execução de treinamento
- `make shell/logs` - Debugging e monitoramento

## 🚀 Guia de Início Rápido

### 1. **Setup Automático (Recomendado)**
```bash
# Clone/baixe todos os arquivos
git clone <seu-repositorio>
cd bootcamp_ml_project

# Execute setup automático
chmod +x setup.sh
./setup.sh

# Coloque seus dados
cp /caminho/para/bootcamp_train.csv data/

# Inicie tudo
make quick-start
```

### 2. **Setup Manual**
```bash
# Criar estrutura
mkdir -p data models outputs visualizations notebooks

# Colocar dados
cp bootcamp_train.csv data/
cp bootcamp_test.csv data/  # (opcional)

# Construir e executar
docker-compose up --build
```

### 3. **Execução Seletiva**
```bash
# Apenas Jupyter
docker-compose up jupyter

# Apenas API
docker-compose -f docker-compose-full.yml up api

# Apenas treinamento
docker-compose -f docker-compose-full.yml --profile training up trainer
```

## 🎯 Cenários de Uso

### 👨‍💻 **Desenvolvimento/Análise**
```bash
make run          # Inicia Jupyter
# Acesse: http://localhost:8888
# Use: RandomForest.ipynb ou crie novos notebooks
```

### 🤖 **Treinamento Automatizado**
```bash
make train        # Executa main.py completo
# Ou
python main.py    # Se dentro do container
```

### 🌐 **Servir Modelo via API**
```bash
# Iniciar API
docker-compose -f docker-compose-full.yml up api

# Testar API
curl -X POST "http://localhost:8000/predizer" \
  -H "Content-Type: application/json" \
  -d '{
    "tipo": "M",
    "temperatura_ar": 300.0,
    "temperatura_processo": 310.0,
    "velocidade_rotacional": 1500.0,
    "torque": 40.0,
    "desgaste_da_ferramenta": 200.0
  }'
```

### 📊 **Análise de Dados**
```bash
# Executar apenas diagnóstico
docker exec -it bootcamp_jupyter python -c "
from main import ManutencaoPreditiva
sistema = ManutencaoPreditiva()
sistema.carregar_dados()
sistema.diagnostico_dados()
"
```

## 🛠️ Configuração e Personalização

### Variáveis de Ambiente (.env)
```bash
# Portas
JUPYTER_PORT=8888
API_PORT=8000

# Caminhos
MODEL_PATH=models/modelo_otimizado.pkl
TRAIN_DATA_PATH=data/bootcamp_train.csv

# Configurações do modelo
RANDOM_STATE=42
```

### Modificar Hiperparâmetros
Edite em `main.py`:
```python
param_grid = {
    'classifier__estimator__n_estimators': [100, 150, 200],
    'classifier__estimator__max_depth': [10, 20, 30],
    'classifier__estimator__min_samples_leaf': [5, 10, 15]
}
```

### Adicionar Novas Dependências
1. Edite `requirements.txt`
2. Reconstrua: `make build`

### Customizar Portas
Edite `docker-compose.yml`:
```yaml
ports:
  - "9999:8888"  # Jupyter na porta 9999
  - "8001:8000"  # API na porta 8001
```

## 📈 Outputs e Resultados

### Arquivos Gerados
- `models/modelo_otimizado.pkl` - Modelo treinado com melhores parâmetros
- `outputs/submission.csv` - Arquivo final de submissão
- `outputs/metricas.json` - Métricas de performance
- `visualizations/analise_exploratoria.png` - Gráficos EDA
- `visualizations/confusion_matrices.png` - Matrizes de confusão

### Métricas Avaliadas
- **Precision, Recall, F1-Score** por tipo de falha
- **AUC-ROC Score** médio ponderado
- **Confusion Matrix** para cada classificador
- **Support** (quantidade de amostras por classe)

## 🔧 Comandos de Manutenção

### Logs e Debugging
```bash
make logs                    # Ver logs em tempo real
make shell                   # Acessar bash do container
docker-compose logs jupyter  # Logs específicos do Jupyter
docker-compose logs api      # Logs específicos da API
```

### Limpeza e Reset
```bash
make clean                   # Remove containers e imagens
make stop                    # Para containers
docker system prune -f       # Limpeza geral do Docker
```

### Backup e Restore
```bash
make backup-models           # Backup automático dos modelos
# Restore manual: copie .pkl para models/
```

## 🐛 Troubleshooting

### Problemas Comuns

**🔴 Porta já em uso**
```bash
# Verificar portas em uso
netstat -tulpn | grep :8888

# Usar porta diferente
docker run -p 8889:8888 bootcamp-ml
# Ou editar docker-compose.yml
```

**🔴 Permissões de arquivo (Linux/Mac)**
```bash
# Ajustar proprietário das pastas
sudo chown -R $USER:$USER ./data ./outputs ./models

# Ou executar com sudo
sudo docker-compose up
```

**🔴 Falta de memória**
```bash
# Limitar recursos do container
docker run -m 2g --cpus="1.0" bootcamp-ml

# Ou adicionar em docker-compose.yml:
deploy:
  resources:
    limits:
      memory: 2G
      cpus: '1.0'
```

**🔴 Erro de importação de bibliotecas**
```bash
# Reconstruir imagem sem cache
docker-compose build --no-cache

# Verificar requirements.txt
make shell
pip list
```

**🔴 Dados não encontrados**
```bash
# Verificar se dados estão na pasta correta
ls -la data/

# Verificar volumes montados
docker inspect bootcamp_jupyter | grep Mounts -A 10
```

### Debugging Avançado

**🔍 Acessar logs detalhados**
```bash
# Logs de todos os serviços
docker-compose logs --tail=100

# Logs de serviço específico
docker-compose logs jupyter --follow

# Debug do container
docker exec -it bootcamp_jupyter bash
python -c "import pandas; print('OK')"
```

**🔍 Verificar recursos**
```bash
# Stats do container
docker stats bootcamp_jupyter

# Espaço em disco
docker system df
```

## 🎓 Desenvolvimento e Extensão

### Modificar Jupyter para JupyterLab
Edite `Dockerfile`:
```dockerfile
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
```

### Adicionar Streamlit Dashboard
1. Adicione ao `requirements.txt`:
```
streamlit==1.25.0
```

2. Crie `dashboard.py`
3. Adicione serviço ao `docker-compose-full.yml`:
```yaml
dashboard:
  build: .
  ports:
    - "8501:8501"
  command: ["streamlit", "run", "dashboard.py", "--server.address=0.0.0.0"]
```

### Deploy em Produção
```bash
# Build para produção
docker build -t bootcamp-ml:prod --target production .

# Push para registry
docker tag bootcamp-ml:prod seu-registry/bootcamp-ml:latest
docker push seu-registry/bootcamp-ml:latest
```

## 📚 Recursos Adicionais

### Documentação
- [Docker Documentation](https://docs.docker.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Scikit-learn Documentation](https://scikit-learn.org/)

### Melhorias Sugeridas
- [ ] CI/CD com GitHub Actions
- [ ] Monitoramento com Prometheus
- [ ] Dashboard com Streamlit/Dash
- [ ] Deploy na nuvem (AWS/GCP/Azure)
- [ ] MLOps com MLflow
- [ ] Testes automatizados
- [ ] Cache de predições
- [ ] Balanceador de carga

---

## 👥 Contribuição

Este projeto foi desenvolvido como parte do **Bootcamp de Ciência de Dados e IA**.

**Autor:** Juliano Spósito Galdino  
**Data:** Setembro 2025  
**Versão:** 1.0.0

---

## 📄 Licença

Este projeto é desenvolvido para fins educacionais como parte do Bootcamp CDIA.
