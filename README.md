# Very Easy Selenium
SELENIUM, BUT EASY.

Obrigado por estar utilizando este projeto.

Se possível contribua para o nosso desenvolvimento, submeta atualizações!


Requisitos para o projeto.

Firefox Browser
https://www.mozilla.org/pt-BR/firefox/new/

Geckodriver
https://github.com/mozilla/geckodriver/releases



Biblioteca selenium

pip install selenium

===

PYTHON 3

===

Uso.


1- Primeiro você precisa chamar o Navegador, e para isso temos o seguinte comando.
==

my_agent_007 = Browser(log = True) # Os logs mostraram xpath não encontrados. Deixe ativo.


Agora com seu "agente" criado, vamos manipula-lo.

Vamos acessar uma URL, pode ser o google.com

my_agent_007.Access_Url("https://www.google.com")
==

Fácil, não ?

E para finalizar o seu agente. 

my_agent_007.Close()
==




Confira todas as funções; Não podem ser chamadas diretamente!

Access_Url(url) # Acessa uma URL

Get_Url() # Pega a URL atual em que o browser está

Read_Xpath(xpath) # Lê o texto de um Xpath

Get_Url_Xpath_Href(xpath) # Lê o atributo 'HREF' de um XPATH / <a href="Python.com">Python</a> 

Write_Xpath(xpath, text) # Escreve em um Xpath / o parametro text é str / text = "Python free" 

Click_Xpath(xpath) # Clica em um Xpath / Conveniente para buttons

Clear_Input(xpath) # Limpa o valor de uma Input /

Close() # Finaliza o agente / Navegador

Free_Select_Xpath(xpath) # Seleção free de xpath / você pode utilizar diretamente as funções do Selenium; Ex: agente.Free_Select_Xpath(xpath = '/html/body/div[4]').click()
