import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.sidebar.header('**Cúrriculo Interativo**') 

opcoes = ['Informações Gerais', 
		  'Projetos Acadêmicos e Científicos']

pagina = st.sidebar.selectbox('Navegue pelo meu currículo:', opcoes)

if pagina == 'Informações Gerais':
	st.title('Bem-vindos ao meu portfólio')

	st.header('Caio César Caldas Santos')
	st.write("""### **Informações Pessoais**
	Nascimento: 26/06/1996
	Telefone: 75 99199 4295
	Email: caldas.ccs@gmail.com
	Nacionalidade: Brasileira
	""")

	st.write("""### **Educação**
	2011 - 2013:  Ensino Médio, Colégio Santo Antônio de Jesus
	2015 - Atual: Bacharelado em Estatística, Universidade Federal da Bahia.
		      Expectativa de graduação: julho/2021.

	""")

	st.write("""### **Experiências Profissionais**
	Jul/2018 - Jul/2019 :  Estagiário no Tribunal Regional Eleitoral da Bahia - TRE-BA.
	Jul/2019 - Ago/2019:   Estagiário na empresa Cielo.
	Set/2019 - Dez/2019 :  Estagiário no Serviço Nacional de Aprendizagem Rural - SENAR 
			       BAHIA.
	""")

	st.write("""### **Projetos Científicos**
	Ago/2016 - Jul/2017 :  Estudo do perfil dos alunos que ingressaram no período de 2004 
			       a 2012  do curso de Estatística de Universidade Federal da Bahia.
	Ago/2017 - Jul/2018:   Estudo do tempo de permanência no curso de Estatística da UFBA
	                       no período de 2004 a 2012: uma abordagem de análise de sobre-
	                       vivência.
	Set/2020 - Atual:      Modelos de regressão estendidos para eventos recorrentes em análise 
			       de sobrevivência.
	""")

	st.write("""### **Habilidades**
	Pacote Office Intermediário (Word, Excel e PowerPoint);
	LaTeX;
	Linguagem de Programação R;
	Inglês avançado;
	SPSS Básico;
	Experiência com análise de dados e planejamento estratégico.
	""")

	st.write("""Segue as redes sociais. Fique à vontade para entrar em contato!""")
	col1, col2 = st.beta_columns(2)
 
	col1.markdown('[![alt text](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/linkedin.png)](https://www.linkedin.com/in/caio-cesar-caldas-santos-a74625160/)')  
	col2.markdown('[![alt text](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/instagram.png)](https://www.instagram.com/caioccaldas/)')

else:
	st.write("""
	# Produção Acadêmica e Científica  
	
	:star: Caio César Caldas Santos, Denise Nunes Viola. 
	**Estudo da incidência da sífilis em gestantes no ano de 2012**  
	2017.  
	[https://drive.google.com/file/d/1Pbku46Yc9OG4jxzy5KQzMIGh2YSxKWrY/view?usp=sharing](https://drive.google.com/file/d/1Pbku46Yc9OG4jxzy5KQzMIGh2YSxKWrY/view?usp=sharing).
	
	:star: Caio César Caldas Santos, Suzana de Lima Santos da Silva, Denise Nunes Viola. 
	**Estudo da meningite no espaço-tempo durante os anos de 2007 a 2014.**  
	2017.   
	[https://drive.google.com/file/d/1zdF3OSCcG53-pCfLOJaOvbeflJM1UruN/view?usp=sharing](https://drive.google.com/file/d/1zdF3OSCcG53-pCfLOJaOvbeflJM1UruN/view?usp=sharing).

	:star: Caio César Caldas Santos, Giovana Oliveira Silva. 
	**Estudo do perfil dos alunos que ingressaram no período de 2004 a 2012 do curso de Estatística da Universidade Federal da Bahia**  
	_Projeto de iniciação científica_, 2017.  
	[https://drive.google.com/file/d/1tXMyD_Revdlclpmr-BCXAd3tSVfc9Wa-/view?usp=sharing](https://drive.google.com/file/d/1tXMyD_Revdlclpmr-BCXAd3tSVfc9Wa-/view?usp=sharing).

	:star: Caio César Caldas Santos, Giovana Oliveira Silva. 
	**Comparação entre Análise Discriminante e Regressão Logística como método de melhor resultado na verificação de fatores que influenciam a evasão de alunos do curso de Estatística da UFBA no período de 2004 a 2012**  
	_Projeto de iniciação científica_, 2018.  
	[https://drive.google.com/file/d/1_nmQn-KcXw_UHRH8xPrhl1tSx99-R2ng/view?usp=sharing](https://drive.google.com/file/d/1_nmQn-KcXw_UHRH8xPrhl1tSx99-R2ng/view?usp=sharing).

	:star: Caio César Caldas Santos, Kézia Alves Mustafa, Rafael Toledo Costa de Almeida. 
	**Experimento com redes neurais utilizando uma base de dados referente às vendas globais da 7ª e 8ª gerações de console.**  
	2020.  
	[https://colab.research.google.com/drive/1fem-98vUpZKxf_dozUVgpr4e-Tu9Vy4M?usp=sharing](https://colab.research.google.com/drive/1fem-98vUpZKxf_dozUVgpr4e-Tu9Vy4M?usp=sharing).
	
	Para mais informações, por favor, acesse meu currículo lattes para ver os demais itens de minha produção científica.
 
	[![Foo](https://raw.githubusercontent.com/ricardorocha86/StreamlitCV/main/lattes.png)](http://lattes.cnpq.br/1446699755071943)
 
    """) 
	st.markdown('---')