# 🤖 Sistema de Manutenção Preditiva

Sistema inteligente para detecção de falhas em máquinas industriais usando Machine Learning.

## 📋 O que faz?

- Analisa dados de sensores IoT de máquinas industriais
- Prediz 5 tipos de falhas diferentes
- Retorna probabilidades de cada tipo de falha
- Gera visualizações dos dados e resultados

## 🎯 Tipos de Falhas Detectadas

1. **FDF** - Falha Desgaste Ferramenta
2. **FDC** - Falha Dissipação Calor
3. **FP** - Falha Potência
4. **FTE** - Falha Tensão Excessiva  
5. **FA** - Falha Aleatória

## 🚀 Como usar?

### Método 1: Google Colab
```bash
# 1. Colocar o arquivo RandomForest.ipynb
no google colab

# 2. Executar
cada celular observando os resultados

# 3. gereação do arquvo submission.csv com o resutado final.
```

### Método 2: Script Automático (Mais Fácil)
```bash
# 1. Executar menu interativo
chmod +x run.sh
./run.sh

# 2. Escolher "1. Setup Completo"
# 3. Colocar arquivo bootcamp_train.csv na pasta data/
# 4. Acessar http://localhost:8888
```

### Método 3: Docker Manual
```bash
# 1. Colocar dados
mkdir data
cp bootcamp_train.csv data/

# 2. Executar
docker-compose up --build

# 3. Acessar http://localhost:8888
```

## 📁 Estrutura

```
projeto/
├── data/
│   └── bootcamp_train.csv     # Seus dados aqui
├── models/                    # Modelos treinados
├── outputs/                   # Resultados finais
├── main.py                    # Script principal
├── api.py                     # API REST (bonus)
└── RandomForest.ipynb         # Notebook original
```

## 🔧 Comandos Úteis

```bash
make quick-start    # Setup + execução automática
make train          # Treinar modelo
make logs           # Ver logs
make shell          # Acessar container
```

## 🌐 Funcionalidades

- **Jupyter Notebook:** http://localhost:8888
- **API REST:** http://localhost:8000 (bonus)
- **Documentação API:** http://localhost:8000/docs

## 📊 Outputs

- `models/modelo_otimizado.pkl` - Modelo treinado
- `outputs/submission.csv` - Arquivo de submissão
- `visualizations/` - Gráficos gerados

## 🛠️ Tecnologias

- **Python** + Pandas + Scikit-learn
- **Random Forest** com otimização de hiperparâmetros
- **Docker** para containerização
- **FastAPI** para API REST (bonus)
- **Jupyter** para análise interativa

---

**Desenvolvido para o Bootcamp de Ciência de Dados e IA - Setembro 2025**
