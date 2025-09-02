#!/usr/bin/env python3
"""
Arquivo de Configuração do Sistema de Manutenção Preditiva
Centraliza todas as configurações do projeto
"""

import os
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict, Any

@dataclass
class ConfiguracaoProjeto:
    """Classe de configuração centralizada"""
    
    # Informações do Projeto
    NOME_PROJETO: str = "Sistema de Manutenção Preditiva"
    VERSAO: str = "1.0.0"
    AUTOR: str = "Bootcamp CDIA"
    DATA_CRIACAO: str = "Setembro 2025"
    
    # Caminhos de Dados
    CAMINHO_DADOS_TREINO: str = "data/bootcamp_train.csv"
    CAMINHO_DADOS_TESTE: str = "data/bootcamp_test.csv"
    CAMINHO_SUBMISSION: str = "outputs/submission.csv"
    CAMINHO_MODELO: str = "models/modelo_otimizado.pkl"
    CAMINHO_METRICAS: str = "outputs/metricas.json"
    
    # Diretórios
    DIR_DADOS: str = "data"
    DIR_MODELOS: str = "models"
    DIR_OUTPUTS: str = "outputs"
    DIR_VISUALIZACOES: str = "visualizations"
    DIR_NOTEBOOKS: str = "notebooks"
    
    # Features do Modelo
    FEATURES: List[str] = None
    FEATURES_NUMERICAS: List[str] = None
    FEATURES_CATEGORICAS: List[str] = None
    COLUNAS_TARGET: List[str] = None
    
    # Parâmetros do Modelo
    RANDOM_STATE: int = 42
    TEST_SIZE: float = 0.2
    CV_FOLDS: int = 3
    N_JOBS: int = -1
    
    # Grid de Hiperparâmetros
    PARAM_GRID: Dict[str, List] = None
    
    # Configurações da API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_RELOAD: bool = True
    
    # Configurações do Jupyter
    JUPYTER_PORT: int = 8888
    JUPYTER_HOST: str = "0.0.0.0"
    
    def __post_init__(self):
        """Inicializar configurações após criação da instância"""
        
        # Definir features
        self.FEATURES = [
            'tipo', 'temperatura_ar', 'temperatura_processo', 
            'velocidade_rotacional', 'torque', 'desgaste_da_ferramenta'
        ]
        
        self.FEATURES_NUMERICAS = [
            'temperatura_ar', 'temperatura_processo', 
            'velocidade_rotacional', 'torque', 'desgaste_da_ferramenta'
        ]
        
        self.FEATURES_CATEGORICAS = ['tipo']
        
        self.COLUNAS_TARGET = [
            'FDF (Falha Desgaste Ferramenta)',
            'FDC (Falha Dissipacao Calor)',
            'FP (Falha Potencia)',
            'FTE (Falha Tensao Excessiva)',
            'FA (Falha Aleatoria)'
        ]
        
        # Grid de hiperparâmetros
        self.PARAM_GRID = {
            'classifier__estimator__n_estimators': [100, 150, 200],
            'classifier__estimator__max_depth': [10, 20, 30],
            'classifier__estimator__min_samples_leaf': [5, 10, 15],
            'classifier__estimator__min_samples_split': [10, 20],
            'classifier__estimator__max_features': ['sqrt', 'log2']
        }
        
        # Criar diretórios se não existirem
        self._criar_diretorios()
    
    def _criar_diretorios(self):
        """Criar diretórios necessários"""
        diretorios = [
            self.DIR_DADOS, self.DIR_MODELOS, 
            self.DIR_OUTPUTS, self.DIR_VISUALIZACOES, self.DIR_NOTEBOOKS
        ]
        
        for diretorio in diretorios:
            Path(diretorio).mkdir(exist_ok=True)
    
    def validar_ambiente(self) -> Dict[str, bool]:
        """Validar se o ambiente está configurado corretamente"""
        validacoes = {
            'dados_treino_existe': os.path.exists(self.CAMINHO_DADOS_TREINO),
            'dados_teste_existe': os.path.exists(self.CAMINHO_DADOS_TESTE),
            'modelo_existe': os.path.exists(self.CAMINHO_MODELO),
            'dir_dados_existe': os.path.exists(self.DIR_DADOS),
            'dir_modelos_existe': os.path.exists(self.DIR_MODELOS),
            'dir_outputs_existe': os.path.exists(self.DIR_OUTPUTS)
        }
        
        return validacoes
    
    def imprimir_configuracao(self):
        """Imprimir configuração atual"""
        print(f"📋 {self.NOME_PROJETO} v{self.VERSAO}")
        print(f"👤 {self.AUTOR} - {self.DATA_CRIACAO}")
        print("-" * 50)
        
        print("📁 Caminhos:")
        print(f"  Treino: {self.CAMINHO_DADOS_TREINO}")
        print(f"  Teste:  {self.CAMINHO_DADOS_TESTE}")
        print(f"  Modelo: {self.CAMINHO_MODELO}")
        
        print(f"\n🎯 Features ({len(self.FEATURES)}):")
        for feature in self.FEATURES:
            print(f"  - {feature}")
        
        print(f"\n🎯 Targets ({len(self.COLUNAS_TARGET)}):")
        for target in self.COLUNAS_TARGET:
            print(f"  - {target}")
        
        print(f"\n⚙️ Parâmetros:")
        print(f"  Random State: {self.RANDOM_STATE}")
        print(f"  Test Size: {self.TEST_SIZE}")
        print(f"  CV Folds: {self.CV_FOLDS}")


# Configurações específicas para diferentes ambientes
class ConfiguracaoDesenvolvimento(ConfiguracaoProjeto):
    """Configuração para ambiente de desenvolvimento"""
    
    def __post_init__(self):
        super().__post_init__()
        self.API_RELOAD = True
        
        # Grid menor para desenvolvimento rápido
        self.PARAM_GRID = {
            'classifier__estimator__n_estimators': [50, 100],
            'classifier__estimator__max_depth': [10, 20],
            'classifier__estimator__min_samples_leaf': [5, 10]
        }


class ConfiguracaoProducao(ConfiguracaoProjeto):
    """Configuração para ambiente de produção"""
    
    def __post_init__(self):
        super().__post_init__()
        self.API_RELOAD = False
        
        # Grid mais extenso para produção
        self.PARAM_GRID = {
            'classifier__estimator__n_estimators': [100, 150, 200, 250],
            'classifier__estimator__max_depth': [10, 20, 30, None],
            'classifier__estimator__min_samples_leaf': [1, 5, 10, 15],
            'classifier__estimator__min_samples_split': [2, 10, 20],
            'classifier__estimator__max_features': ['sqrt', 'log2', None]
        }


# Factory para obter configuração baseada no ambiente
def obter_configuracao(ambiente: str = None) -> ConfiguracaoProjeto:
    """Obter configuração baseada no ambiente"""
    
    if ambiente is None:
        ambiente = os.getenv('AMBIENTE', 'desenvolvimento')
    
    if ambiente.lower() == 'producao':
        return ConfiguracaoProducao()
    else:
        return ConfiguracaoDesenvolvimento()


# Instância global da configuração
config = obter_configuracao()

# Funções utilitárias
def imprimir_status_ambiente():
    """Imprimir status do ambiente atual"""
    config.imprimir_configuracao()
    
    print("\n🔍 Validação do Ambiente:")
    validacoes = config.validar_ambiente()
    
    for nome, status in validacoes.items():
        emoji = "✅" if status else "❌"
        print(f"  {emoji} {nome.replace('_', ' ').title()}")


def obter_variaveis_ambiente() -> Dict[str, Any]:
    """Obter variáveis de ambiente para Docker"""
    return {
        'PROJECT_NAME': config.NOME_PROJETO,
        'VERSION': config.VERSAO,
        'JUPYTER_PORT': config.JUPYTER_PORT,
        'API_PORT': config.API_PORT,
        'RANDOM_STATE': config.RANDOM_STATE,
        'MODEL_PATH': config.CAMINHO_MODELO,
        'TRAIN_DATA_PATH': config.CAMINHO_DADOS_TREINO,
        'TEST_DATA_PATH': config.CAMINHO_DADOS_TESTE
    }


if __name__ == "__main__":
    print("🔧 Configuração do Sistema de Manutenção Preditiva")
    print("=" * 55)
    imprimir_status_ambiente()