# Projeto-Final-do-Bootcamp-CDIA---IA
Projeto Final do Bootcamp CDIA da etapa bootcamp residencia em IA

🤖 Sistema de Manutenção Preditiva
Sistema inteligente para detecção de falhas em máquinas industriais usando Machine Learning.
📋 O que faz?

Analisa dados de sensores IoT de máquinas industriais
Prediz 5 tipos de falhas diferentes
Retorna probabilidades de cada tipo de falha
Gera visualizações dos dados e resultados

🎯 Tipos de Falhas Detectadas

FDF - Falha Desgaste Ferramenta
FDC - Falha Dissipação Calor
FP - Falha Potência
FTE - Falha Tensão Excessiva
FA - Falha Aleatória

🚀 Como usar?
Método 1: Script Automático (Mais Fácil)
bash# 1. Executar menu interativo
chmod +x run.sh
./run.sh

# 2. Escolher "1. Setup Completo"
# 3. Colocar arquivo bootcamp_train.csv na pasta data/
# 4. Acessar http://localhost:8888
Método 2: Docker Manual
bash# 1. Colocar dados
mkdir data
cp bootcamp_train.csv data/

# 2. Executar
docker-compose up --build

# 3. Acessar http://localhost:8888
📁 Estrutura
projeto/
├── data/
│   └── bootcamp_train.csv     # Seus dados aqui
├── models/                    # Modelos treinados
├── outputs/                   # Resultados finais
├── main.py                    # Script principal
├── api.py                     # API REST (bonus)
└── RandomForest.ipynb         # Notebook original
🔧 Comandos Úteis
bashmake quick-start    # Setup + execução automática
make train          # Treinar modelo
make logs           # Ver logs
make shell          # Acessar container
🌐 Funcionalidades

Jupyter Notebook: http://localhost:8888
API REST: http://localhost:8000 (bonus)
Documentação API: http://localhost:8000/docs

📊 Outputs

models/modelo_otimizado.pkl - Modelo treinado
outputs/submission.csv - Arquivo de submissão
visualizations/ - Gráficos gerados

🛠️ Tecnologias

Python + Pandas + Scikit-learn
Random Forest com otimização de hiperparâmetros
Docker para containerização
FastAPI para API REST (bonus)
Jupyter para análise interativa


Desenvolvido para o Bootcamp de Ciência de Dados e IA - Setembro 2025
