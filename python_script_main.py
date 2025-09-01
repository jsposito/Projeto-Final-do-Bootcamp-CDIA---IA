#!/usr/bin/env python3
"""
Projeto Final - Bootcamp de Ciência de Dados e IA
Sistema de Manutenção Preditiva
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib
from pathlib import Path

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.multioutput import MultiOutputClassifier
from sklearn.metrics import classification_report, roc_auc_score, confusion_matrix

class ManutencaoPreditiva:
    """Classe principal para o sistema de manutenção preditiva"""
    
    def __init__(self):
        self.df_train = None
        self.df_test = None
        self.model_pipeline = None
        self.best_model = None
        
        # Definir colunas
        self.features = [
            'tipo', 'temperatura_ar', 'temperatura_processo', 
            'velocidade_rotacional', 'torque', 'desgaste_da_ferramenta'
        ]
        
        self.target_cols = [
            'FDF (Falha Desgaste Ferramenta)',
            'FDC (Falha Dissipacao Calor)',
            'FP (Falha Potencia)',
            'FTE (Falha Tensao Excessiva)',
            'FA (Falha Aleatoria)'
        ]
        
        self.numerical_features = [
            'temperatura_ar', 'temperatura_processo', 
            'velocidade_rotacional', 'torque', 'desgaste_da_ferramenta'
        ]
        
        self.categorical_features = ['tipo']
        
        # Criar diretórios necessários
        self._create_directories()
    
    def _create_directories(self):
        """Criar diretórios necessários para o projeto"""
        directories = ['data', 'models', 'outputs', 'visualizations']
        for directory in directories:
            Path(directory).mkdir(exist_ok=True)
    
    def carregar_dados(self, caminho_train="data/bootcamp_train.csv", caminho_test=None):
        """Carregar dados de treino e teste"""
        try:
            print("Carregando dados de treino...")
            self.df_train = pd.read_csv(caminho_train)
            print(f"Dados de treino carregados: {self.df_train.shape}")
            
            if caminho_test and os.path.exists(caminho_test):
                print("Carregando dados de teste...")
                self.df_test = pd.read_csv(caminho_test)
                print(f"Dados de teste carregados: {self.df_test.shape}")
                
        except FileNotFoundError as e:
            print(f"Erro ao carregar dados: {e}")
            print("Certifique-se de que os arquivos estão no diretório 'data/'")
    
    def diagnostico_dados(self):
        """Realizar diagnóstico completo dos dados"""
        if self.df_train is None:
            print("Erro: Dados de treino não carregados!")
            return
        
        print("Executando diagnóstico completo do arquivo de treino...")
        print("-" * 50)
        
        # 1. Formato dos dados
        print("Formato dos dados:")
        print(f" - df_train: {self.df_train.shape}")
        print()
        
        # 2. Nomes das colunas
        print("Colunas encontradas:")
        print(list(self.df_train.columns))
        print()
        
        # 3. Tipos de dados
        print("Tipos de dados por coluna:")
        print(self.df_train.dtypes.sort_index())
        print()
        
        # 4. Separação de colunas numéricas e categóricas
        num_cols = self.df_train.select_dtypes(include=np.number).columns.tolist()
        cat_cols = self.df_train.select_dtypes(exclude=np.number).columns.tolist()
        print(f"Colunas Numéricas ({len(num_cols)}): {num_cols}")
        print(f"Colunas Categóricas ({len(cat_cols)}): {cat_cols}")
        print()
        
        # 5. Valores ausentes
        print("Colunas com valores ausentes:")
        missing = self.df_train.isna().sum().sort_values(ascending=False)
        print(missing[missing > 0])
        print()
        
        # 6. Linhas duplicadas
        dup = int(self.df_train.duplicated().sum())
        print(f"Linhas duplicadas encontradas: {dup}")
        print()
        
        # 7. Estatísticas básicas
        print("Estatísticas das variáveis numéricas:")
        stats = self.df_train[self.numerical_features].describe().T[['mean','std','min','max']]
        print(stats)
        print()
        
        # 8. Análise das targets
        print("Análise das Colunas-Alvo:")
        present_targets = [c for c in self.target_cols if c in self.df_train.columns]
        
        if present_targets:
            print("Alvos encontrados:", present_targets)
            for t in present_targets:
                vc = self.df_train[t].value_counts(dropna=False)
                total = vc.sum()
                print(f"\n— Distribuição de '{t}':")
                for k, v in vc.items():
                    pct = 100.0 * v / total
                    print(f"    {str(k):<10}: {v:>6} ({pct:.2f}%)")
        
        print("-" * 50)
        print("Diagnóstico concluído.")
    
    def limpar_dados(self):
        """Limpar e preparar os dados"""
        if self.df_train is None:
            print("Erro: Dados de treino não carregados!")
            return
        
        print("Iniciando a limpeza dos dados de treino...")
        
        # Mapeamento para limpar colunas de falha
        mapa_valores = {
            'sim': 1, 'Sim': 1, 'y': 1, '1': 1, 1: 1, True: 1,
            'não': 0, 'Não': 0, 'N': 0, '0': 0, 0: 0, False: 0, 'n': 0
        }
        
        # Limpar colunas de falha
        colunas_para_limpar = ['falha_maquina'] + self.target_cols
        
        for col in colunas_para_limpar:
            if col in self.df_train.columns:
                self.df_train[col] = self.df_train[col].replace(mapa_valores)
                self.df_train[col] = pd.to_numeric(self.df_train[col], errors='coerce').fillna(0).astype(int)
        
        # Preencher valores faltantes nas features numéricas
        for col in self.numerical_features:
            if col in self.df_train.columns:
                mediana = self.df_train[col].median()
                self.df_train[col].fillna(mediana, inplace=True)
        
        print("Limpeza de dados concluída!")
        
        # Verificar resultado
        print("\nVerificando 'falha_maquina':")
        print(self.df_train['falha_maquina'].value_counts())
    
    def analise_exploratoria(self):
        """Realizar análise exploratória de dados"""
        if self.df_train is None:
            print("Erro: Dados não carregados!")
            return
        
        print("Iniciando a Análise Exploratória de Dados...")
        
        # 1. Distribuição da falha geral
        plt.figure(figsize=(12, 10))
        
        plt.subplot(2, 2, 1)
        falha_counts = self.df_train['falha_maquina'].value_counts()
        sns.barplot(x=falha_counts.index, y=falha_counts.values, palette='viridis')
        plt.title('Distribuição da Falha Geral da Máquina')
        plt.xticks([0, 1], ['Sem Falha', 'Com Falha'])
        
        # 2. Contagem por tipo específico de falha
        plt.subplot(2, 2, 2)
        falhas_especificas = self.df_train[self.target_cols].sum().sort_values(ascending=False)
        sns.barplot(x=range(len(falhas_especificas)), y=falhas_especificas.values, palette='crest')
        plt.title('Contagem de Cada Tipo de Falha Específica')
        plt.xticks(range(len(falhas_especificas)), falhas_especificas.index, rotation=45, ha='right')
        
        # 3. Distribuição das variáveis numéricas
        plt.subplot(2, 2, 3)
        self.df_train[self.numerical_features].hist(bins=20, ax=plt.gca())
        plt.title('Distribuição das Variáveis Numéricas')
        
        # 4. Matriz de correlação
        plt.subplot(2, 2, 4)
        cols_for_corr = self.numerical_features + ['falha_maquina']
        correlation_matrix = self.df_train[cols_for_corr].corr()
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', cbar=True)
        plt.title('Matriz de Correlação')
        
        plt.tight_layout()
        plt.savefig('visualizations/analise_exploratoria.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print("Análise exploratória concluída. Gráficos salvos em 'visualizations/'")
    
    def preparar_dados(self):
        """Preparar dados para treinamento"""
        if self.df_train is None:
            print("Erro: Dados não carregados!")
            return
        
        print("Preparando dados para treinamento...")
        
        # Definir X e y
        X = self.df_train[self.features]
        y = self.df_train[self.target_cols]
        
        # Criar preprocessador
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numerical_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_features)
            ]
        )
        
        # Dividir dados
        X_train, X_val, y_train, y_val = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=self.df_train['falha_maquina']
        )
        
        print(f"Conjunto de treino: {X_train.shape}")
        print(f"Conjunto de validação: {X_val.shape}")
        
        return X_train, X_val, y_train, y_val, preprocessor
    
    def treinar_modelo(self, X_train, y_train, preprocessor, otimizar=True):
        """Treinar modelo de machine learning"""
        print("Iniciando o treinamento do modelo...")
        
        # Modelo base
        base_classifier = RandomForestClassifier(random_state=42, class_weight='balanced')
        multi_output_model = MultiOutputClassifier(estimator=base_classifier, n_jobs=-1)
        
        # Pipeline
        pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', multi_output_model)
        ])
        
        if otimizar:
            print("Executando otimização de hiperparâmetros...")
            
            param_grid = {
                'classifier__estimator__n_estimators': [100, 150],
                'classifier__estimator__max_depth': [10, 20],
                'classifier__estimator__min_samples_leaf': [5, 10]
            }
            
            grid_search = GridSearchCV(
                estimator=pipeline,
                param_grid=param_grid,
                scoring='f1_weighted',
                cv=3,
                n_jobs=-1,
                verbose=1
            )
            
            grid_search.fit(X_train, y_train)
            
            print("\nMelhores parâmetros encontrados:")
            print(grid_search.best_params_)
            
            self.best_model = grid_search.best_estimator_
            
            # Salvar modelo
            joblib.dump(self.best_model, 'models/modelo_otimizado.pkl')
            print("Modelo salvo em 'models/modelo_otimizado.pkl'")
            
        else:
            pipeline.fit(X_train, y_train)
            self.best_model = pipeline
            joblib.dump(self.best_model, 'models/modelo_basico.pkl')
        
        print("Treinamento concluído!")
        return self.best_model
    
    def avaliar_modelo(self, X_val, y_val):
        """Avaliar desempenho do modelo"""
        if self.best_model is None:
            print("Erro: Modelo não treinado!")
            return
        
        print("Avaliando modelo no conjunto de validação...")
        
        # Previsões
        y_pred_val = self.best_model.predict(X_val)
        
        # Relatório de classificação
        print("\nRelatório de Classificação:")
        print(classification_report(y_val, y_pred_val, target_names=self.target_cols, zero_division=0))
        
        # Matrizes de confusão
        self._plot_confusion_matrices(y_val, y_pred_val)
        
        # Tentar calcular AUC-ROC
        try:
            y_proba_val = self.best_model.predict_proba(X_val)
            probabilities = []
            
            for p in y_proba_val:
                if p.shape[1] == 2:
                    probabilities.append(p[:, 1])
                else:
                    probabilities.append(np.zeros(p.shape[0]))
            
            y_proba_val_reformatted = np.array(probabilities).T
            auc_score = roc_auc_score(y_val, y_proba_val_reformatted, average='weighted')
            print(f"\nAUC-ROC Score (Média Ponderada): {auc_score:.4f}")
            
        except ValueError as e:
            print(f"\nNão foi possível calcular o AUC Score. Motivo: {e}")
    
    def _plot_confusion_matrices(self, y_val, y_pred_val):
        """Plotar matrizes de confusão"""
        fig, axes = plt.subplots(2, 3, figsize=(15, 8))
        axes = axes.flatten()
        
        for i, col in enumerate(self.target_cols):
            cm = confusion_matrix(y_val[col], y_pred_val[:, i])
            
            labels = [
                ['Verdadeiro Negativo\n'+str(cm[0,0]), 'Falso Positivo\n'+str(cm[0,1])],
                ['Falso Negativo\n'+str(cm[1,0]), 'Verdadeiro Positivo\n'+str(cm[1,1])]
            ]
            
            label_text = np.asarray(labels).reshape(2,2)
            sns.heatmap(cm, annot=label_text, fmt='', cmap='Blues', ax=axes[i], cbar=False)
            
            axes[i].set_title(col)
            axes[i].set_ylabel('Rótulo Verdadeiro')
            axes[i].set_xlabel('Rótulo Previsto')
        
        axes[5].axis('off')
        plt.tight_layout()
        plt.savefig('visualizations/confusion_matrices.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def gerar_predicoes(self, caminho_test="data/bootcamp_test.csv"):
        """Gerar predições para o conjunto de teste"""
        if self.best_model is None:
            print("Erro: Modelo não treinado!")
            return
        
        if self.df_test is None:
            if os.path.exists(caminho_test):
                self.df_test = pd.read_csv(caminho_test)
            else:
                print(f"Arquivo de teste não encontrado: {caminho_test}")
                return
        
        print("Gerando predições para o conjunto de teste...")
        
        # Limpar dados de teste
        df_test_clean = self.df_test.copy()
        for col in self.numerical_features:
            if col in df_test_clean.columns:
                mediana = self.df_train[col].median()  # Usar mediana do treino
                df_test_clean[col].fillna(mediana, inplace=True)
        
        # Fazer predições
        X_test = df_test_clean[self.features]
        test_probabilities = self.best_model.predict_proba(X_test)
        
        # Criar DataFrame de submissão
        submission_df = pd.DataFrame()
        submission_df['id'] = df_test_clean['id']
        
        probabilities_submission = []
        for p in test_probabilities:
            if p.shape[1] == 2:
                probabilities_submission.append(p[:, 1])
            else:
                probabilities_submission.append(np.zeros(p.shape[0]))
        
        for i, col in enumerate(self.target_cols):
            submission_df[col] = probabilities_submission[i]
        
        # Salvar arquivo
        submission_df.to_csv('outputs/submission.csv', index=False)
        print("Arquivo 'outputs/submission.csv' gerado com sucesso!")
        
        return submission_df
    
    def executar_pipeline_completo(self, otimizar_modelo=True):
        """Executar todo o pipeline do projeto"""
        print("=== EXECUTANDO PIPELINE COMPLETO ===")
        
        # 1. Carregar dados
        self.carregar_dados()
        
        # 2. Diagnóstico
        self.diagnostico_dados()
        
        # 3. Limpeza
        self.limpar_dados()
        
        # 4. Análise exploratória
        self.analise_exploratoria()
        
        # 5. Preparação
        X_train, X_val, y_train, y_val, preprocessor = self.preparar_dados()
        
        # 6. Treinamento
        self.treinar_modelo(X_train, y_train, preprocessor, otimizar=otimizar_modelo)
        
        # 7. Avaliação
        self.avaliar_modelo(X_val, y_val)
        
        # 8. Predições (se arquivo de teste existir)
        if os.path.exists('data/bootcamp_test.csv'):
            self.gerar_predicoes()
        
        print("\n=== PIPELINE COMPLETO EXECUTADO ===")


def main():
    """Função principal"""
    print("Sistema de Manutenção Preditiva - Bootcamp CDIA")
    print("=" * 50)
    
    # Criar instância do sistema
    sistema = ManutencaoPreditiva()
    
    # Executar pipeline completo
    sistema.executar_pipeline_completo(otimizar_modelo=True)


if __name__ == "__main__":
    main()