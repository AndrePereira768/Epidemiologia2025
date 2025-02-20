# Simulação do Crescimento Bacteriano

Este repositório contém um **modelo de autômato celular baseado em Python** para simular o crescimento e controle bacteriano sob diversas condições ambientais. 
O estudo foca em como as populações bacterianas reagem a diferentes intervenções, incluindo tratamento com antibióticos, desenvolvimento de resistência e limitações de recursos.

##  **Visão Geral**
A simulação explora:
- **Propagação bacteriana** ao longo do tempo.
- **Efeitos dos antibióticos** na sobrevivência bacteriana.
- **Emergência da resistência aos antibióticos**.
- **Papel das barreiras físicas e restrições de recursos** no controle bacteriano.

## **Artigo Científico**
Um artigo **detalhado** explicando a metodologia e os resultados desta simulação está disponível. Você pode acessá-lo aqui:

 **[Simulação do Crescimento Bacteriano - Relatório Científico](https://drive.google.com/YOUR-LINK-HERE)**

Alternativamente, o artigo também está disponível neste repositório no arquivo: [`bacterial_growth_article.pdf`](./bacterial_growth_article.pdf)

## **Como Executar a Simulação**
Para executar o modelo de crescimento bacteriano, siga estes passos:

### 1 **Clone o Repositório**
```bash
git clone https://github.com/YOUR-USERNAME/bacterial-growth-simulation.git
cd bacterial-growth-simulation
```

### 2️ **Instale as Dependências**
Certifique-se de que o Python está instalado. Depois, instale as bibliotecas necessárias:
```bash
pip install numpy matplotlib
```

### 3️ **Execute a Simulação**
Execute o script Python para visualizar a dinâmica de crescimento e controle bacteriano:
```bash
python simulation.py
```
Isso gerará imagens exibindo a propagação bacteriana ao longo do tempo.

## **Saídas Geradas**
Após a execução da simulação, os seguintes arquivos de imagem serão salvos:
- **`estado_inicial.png`** - Distribuição inicial das bactérias.
- **`propagacao_bacteriana.png`** - Propagação bacteriana ao longo das iterações.
- **`comparacao_antibioticos.png`** - Comparação do crescimento com e sem antibióticos.

## **Informações Científicas**
Este modelo destaca conceitos epidemiológicos importantes:
- **Mecanismos de resistência a antibióticos** e seu impacto no controle de infecções.
- **Barreiras e limitações de recursos** como estratégias de contenção.
- **Previsão da propagação bacteriana** em diferentes ambientes.

## **Referências**
1. Schiff, J. L. (2008). *Cellular Automata: A Discrete View of the World*. Wiley.
2. Wolfram, S. (2002). *A New Kind of Science*. Wolfram Media.
3. Murray, J. D. (2002). *Mathematical Biology*. Springer.

## 🤝 **Contribuindo**
Sinta-se à vontade para fazer um fork deste repositório, sugerir melhorias ou relatar problemas!

**Contato:** andre.amaro@ufrpe.br

