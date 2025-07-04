# 📘 README – Visualizador de PLD Horário por Submercado


### 🧾 Descrição

Este projeto é uma aplicação web interativa desenvolvida em Python com Streamlit que permite visualizar a média diária do Preço de Liquidação das Diferenças (PLD) horário para diferentes submercados e anos no Brasil.

Os dados são lidos de arquivos .csv disponibilizados pelo ONS/CCEE e processados para construção de gráficos dinâmicos com Plotly.

### 🛠️ Funcionalidade

Seleção de ano (ex: 2023, 2024, 2025)

Seleção de submercado (ex: NORDESTE, SUDESTE, etc.)

Geração de gráfico de PLD médio diário

Interface web simples com Streamlit

### 🖼️ Exemplo de visualização

Um gráfico de linha mostrando a evolução diária do PLD médio por submercado.

O usuário seleciona o ano e o submercado e visualiza a curva gerada dinamicamente.

### 🧼 Limpeza e melhorias futuras (ideias)

Melhor tratamento de erros de leitura de arquivos

Inclusão de mais anos ou fonte automatizada dos dados

Exportação dos gráficos em Excel ou PNG

Filtro por meses específicos

Dashboard interativo com múltiplas métricas

# 🚀 Rode a aplicação

bash
Copiar
Editar
python -m streamlit run scripts/dashboard_pld.py
O navegador será aberto automaticamente em http://localhost:8501. 

### 📜 Licença

Este projeto é livre para uso educacional e pessoal. Para fins comerciais, verifique a licença de uso dos dados da CCEE/ONS.

