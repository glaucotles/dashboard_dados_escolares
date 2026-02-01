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
    'LunchType': 'tipo_de_almoco',
    'TestPrep': 'preparacao_teste',
    'ParentMaritalStatus': 'estado_civil_parental',
    'PracticeSport': 'pratica_esportiva',
    'IsFirstChild': 'e_primeiro_filho',
    'NrSiblings': 'número_de_irmaos', # tem nan
    'TransportMeans': 'meio_de_transporte', 
    'WklyStudyHours': 'horas_de_estudo_semanais', # tem nan
    'MathScore': 'pontuacao_matematica',
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

escolaridade_parental_disponiveis = { # tem nan
    "some high school": "ensino_medio_incompleto",
    "high school": "ensino_medio",
    "some college": "ensino_superior_incompleto",
    "associate's degree": "tecnologo",
    "bachelor's degree": "bacharelado",
    "master's degree": "mestrado",
}

tipo_de_almoco = {
    "standard": "padrao",
    "free/reduced": "gratuito_ou_reduzido"
}

preparacao_teste_disponiveis = { # tem nan
    "none": "nenhum",
    "completed": "completado"
}

estado_civil_parental = { # tem nan
    "married": "casado",
    "single": "solteiro",
    "divorced": "divorciado",
    "widowed": "viuvo"
}

pratica_esportiva = { # tem nan
    "sometimes": "as_vezes",
    "regularly": "regularmente",
    "never": "nunca"
}

e_primeiro_filho = { # tem nan
    "yes": "sim",
    "no": "nao"
}

meio_de_transporte = { # tem nan
    "school_bus": "transporte_escolar",
    "private": "privado"
}

# Aplicando alteração em nomes das categorias

df["genero"] = df["genero"].replace(genero)
df["grupo_etnico"] = df["grupo_etnico"].replace(grupo_etnico)
df["escolaridade_parental"] = df["escolaridade_parental"].replace(escolaridade_parental_disponiveis)
df["tipo_de_almoco"] = df["tipo_de_almoco"].replace(tipo_de_almoco)
df["preparacao_teste"] = df["preparacao_teste"].replace(preparacao_teste_disponiveis)
df["estado_civil_parental"] = df["estado_civil_parental"].replace(estado_civil_parental)
df["pratica_esportiva"] = df["pratica_esportiva"].replace(pratica_esportiva)
df["e_primeiro_filho"] = df["e_primeiro_filho"].replace(e_primeiro_filho)
df["meio_de_transporte"] = df["meio_de_transporte"].replace(meio_de_transporte)

# Trocar os nan por "Não Informado"

df["grupo_etnico"] = df["grupo_etnico"].fillna("nao_informado")
df["escolaridade_parental"] = df["escolaridade_parental"].fillna("nao_informado")
df["preparacao_teste"] = df["preparacao_teste"].fillna("nao_informado")
df["estado_civil_parental"] = df["estado_civil_parental"].fillna("nao_informado")
df["pratica_esportiva"] = df["pratica_esportiva"].fillna("nao_informado")
df["e_primeiro_filho"] = df["e_primeiro_filho"].fillna("nao_informado")
df["número_de_irmaos"] = df["número_de_irmaos"].fillna("nao_informado")
df["meio_de_transporte"] = df["meio_de_transporte"].fillna("nao_informado")
df["horas_de_estudo_semanais"] = df["horas_de_estudo_semanais"].fillna("nao_informado")

# Configurar pagina do streamlit

st.set_page_config(
    page_title="Dashboard de Desempenho em Provas",
    page_icon="🏫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Barra lateral de filtros
st.sidebar.header("🔍 Filtros")

# Filtro de generos
generos_disponiveis = sorted(df["genero"].unique())
generos_selecionados = st.sidebar.multiselect(
    "Generos", generos_disponiveis, default=generos_disponiveis
    )

# Filtro de nível de escolaridade dos pais
escolaridade_parental_disponiveis = sorted(df["escolaridade_parental"].unique())
escolaridade_parental_selecionados = st.sidebar.multiselect(
    "Escolaridade Parental", escolaridade_parental_disponiveis, default=escolaridade_parental_disponiveis
    )

# Filtro de status de curso preparatorio
preparacao_teste_disponiveis = sorted(df["preparacao_teste"].unique())
preparacao_teste_selecionados = st.sidebar.multiselect(
    "Status de Curso Preparatorio", preparacao_teste_disponiveis, default=preparacao_teste_disponiveis
)

# Filtro de horas de estudo
horas_de_estudo_semanais_disponiveis = sorted(df["horas_de_estudo_semanais"].unique())
horas_de_estudo_semanais_selecionados = st.sidebar.multiselect(
    "Horas de estudo semanais", horas_de_estudo_semanais_disponiveis, default=horas_de_estudo_semanais_disponiveis
)

# Filtro de tipo de almoço
tipo_de_almoco_disponiveis = sorted(df["tipo_de_almoco"].unique())
tipo_de_almoco_selecionados = st.sidebar.multiselect(
    "Tipo de almoço", tipo_de_almoco_disponiveis, default=tipo_de_almoco_disponiveis
)

# Filtragem do dataframe baseado nas selecoes da barra lateral
df_filtrado = df[
    (df["genero"].isin(generos_selecionados)) &
    (df["escolaridade_parental"].isin(escolaridade_parental_selecionados)) &
    (df["preparacao_teste"].isin(preparacao_teste_selecionados)) &
    (df["horas_de_estudo_semanais"].isin(horas_de_estudo_semanais_selecionados)) &
    (df["tipo_de_almoco"].isin(tipo_de_almoco_selecionados))
]

# Titulo e markdown
st.title("Dashboard de Desempenho em Provas")
st.markdown("Explore dados sobre o desempenho dos alunos em provas")

# KPI's principais
st.subheader("Métricas gerais:")

if not df_filtrado.empty:
    # 1. Cálculos das Métricas
    total_alunos = len(df_filtrado)
    media_mat = df_filtrado["pontuacao_matematica"].mean()
    media_leitura = df_filtrado["pontuacao_leitura"].mean()
    media_escrita = df_filtrado["pontuacao_escrita"].mean()

    # Exibição dos KPIs em colunas
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total de Alunos", total_alunos)
    col2.metric("Média Matemática", f"{media_mat:.1f}")
    col3.metric("Média Leitura", f"{media_leitura:.1f}")
    col4.metric("Média Escrita", f"{media_escrita:.1f}")

    st.divider()

    # Gráficos | Linha 1
    col_esq, col_dir = st.columns(2)

    with col_esq:
        st.subheader("Desempenho por Escolaridade Parental")
        # Calculando a média por grupo
        df_escolaridade = df_filtrado.groupby("escolaridade_parental")[["pontuacao_matematica", "pontuacao_leitura", "pontuacao_escrita"]].mean().reset_index()
        fig_escolaridade = px.bar(
            df_escolaridade, 
            x="escolaridade_parental", 
            y=["pontuacao_matematica", "pontuacao_leitura", "pontuacao_escrita"],
            barmode="group",
            labels={"value": "Pontuação Média", "variable": "Matéria"},
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(fig_escolaridade, use_container_width=True)

    with col_dir:
        st.subheader("Distribuição de Gênero")
        fig_pie = px.pie(
            df_filtrado, 
            names="genero", 
            hole=0.4,
            color_discrete_sequence=["#636EFA", "#EF553B"]
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # Gráficos | Linha 2
    st.subheader("Relação: Horas de Estudo vs Notas")
    
    # Criando uma nota média global para facilitar a visão
    df_filtrado["nota_geral"] = df_filtrado[["pontuacao_matematica", "pontuacao_leitura", "pontuacao_escrita"]].mean(axis=1)
    
    fig_hist = px.histogram(
    df_filtrado, 
    x="nota_geral", 
    nbins=30,  # Define a quantidade de barras
    color="genero",  # Permite ver a distribuição comparada entre gêneros
    marginal="rug",  # Adiciona marcações individuais no rodapé do gráfico
    title="Frequência das Notas Gerais dos Alunos",
    labels={"nota_geral": "Nota Média Final", "count": "Quantidade de Alunos"},
    color_discrete_sequence=px.colors.qualitative.Safe,
    opacity=0.75,
    barmode='overlay' # Sobrepõe as cores para facilitar a comparação
        )

    fig_hist.update_layout(
        xaxis_title="Nota Geral (0 - 100)",
        yaxis_title="Número de Alunos",
        bargap=0.05
        )

    st.plotly_chart(fig_hist, use_container_width=True)

    # 4. Tabela de Dados (Opcional)
    with st.expander("Ver dados brutos filtrados"):
        st.dataframe(df_filtrado)

else:
    st.error("⚠️ Nenhum dado encontrado para os filtros selecionados. Ajuste os filtros na barra lateral.")
