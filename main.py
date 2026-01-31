import streamlit as st
import pandas as pd
import plotly.express as px

# Carregamento de dados
df = pd.read_csv("https://raw.githubusercontent.com/glaucotles/dashboard_dados_escolares/refs/heads/main/dados_escolares.csv")

# Renomear colunas para português
novos_nomes = {
    'Unnamed: 0': 'id',
    'Gender': 'genero',
    'EthnicGroup': 'grupo_etnico',
    'ParentEduc': 'escolaridade_parental',
    'LunchType': 'tipo_de_almoço',
    'TestPrep': 'preparacao_teste',
    'ParentMaritalStatus': 'estado_civil_parental',
    'PracticeSport': 'pratica_esportiva',
    'IsFirstChild': 'e_primeiro_filho',
    'NrSiblings': 'número_de_irmaos',
    'TransportMeans': 'meio_de_transporte',
    'WklyStudyHours': 'horas_de_estudo_semanais',
    'MathScore': 'pontuacao_matemática',
    'ReadingScore': 'pontuacao_leitura',
    'WritingScore': 'pontuacao_escrita'
}

# Aplicando renomeação das colunas
df.rename(columns=novos_nomes, inplace=True)

# Modificando o nome das categorias

genero = {
    "female": "feminino",
    "male": "masculino"
}

grupo_etnico = { # tem nan
    "group A": "grupo_a",
    "group B": "grupo_b",
    "group C": "grupo_c",
    "group D": "grupo_d",
    "group E": "grupo_e"
}

escolaridade_parental = { # tem nan
    "some high school": "ensino_medio_incompleto",
    "high school": "ensino_medio",
    "some college": "ensino_superior_incompleto",
    "associate's degree": "tecnologo",
    "bachelor's degree": "bacharelado",
    "master's degree": "mestrado",
}

tipo_de_almoço = {
    "standard": "padrao",
    "free/reduced": "gratuito_ou_reduzido"
}

preparacao_teste = { # tem nan
    "none": "nenhum",
    "completed": "completado"
}


df["genero"] = df["genero"].replace(genero)
df["grupo_etnico"] = df["grupo_etnico"].replace(grupo_etnico)
df["escolaridade_parental"] = df["escolaridade_parental"].replace(escolaridade_parental)
df["tipo_de_almoço"] = df["tipo_de_almoço"].replace(tipo_de_almoço)
df["preparacao_teste"] = df["preparacao_teste"].replace(preparacao_teste)