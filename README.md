<div align="center">
  <img width="256" height="256" alt="Logo Sarbil com Garota e Libras" src="https://github.com/user-attachments/assets/b8902123-742b-4477-899b-8df812ca7783" style="border-radius: 52px;" />
</div>

<h1 align="center"><b>Sarbil</b></h1>

O projeto tem como conceito fazer a detecção de sinais de **Libras**, posteriormente a isso, entregar a tradução da língua em português. Ao mesmo tempo, também haverá a realização de tradução de português para Libras com um avatar realizando os movimentos dos sinais e expressões. 

# Fluxo de Funcionamento 

1. **Identificação:** O sistema reconhece a mão e a expressão facial.
2. **Início:** O usuário começa a realizar a sinalização em Libras.
3. **Processamento:** O sistema aguarda o término para definir a estrutura da frase (**afirmativa**, **interrogativa** ou **negativa**).
4. **Finalização:** A sinalização é concluída.
5. **Tradução:** A mensagem traduzida em Português é exibida na tela.

# Diagrama de Caso de Uso 

_Em produção..._


# Diagrama de Classe 

_Em produção..._

# Processos e Desafios

O maior desafio da Libras é a sua estrutura própria. Tendo em vista que muitos desconhecem o seu verdadeiro funcionamento, alguns acreditam que Libras é somente a soletração, ou como também chamada, datilologia. Os sinais a serem realizados possuem a possibilidade de execução em cinco parâmetros da Libras: **configuração de mão, movimento, orientação, ponto de articulação e expressão corporal ou facial**. 
Identificar as minúcias dessa língua por detecção facial e corporal, além do treinamento com inteligência artificial é muito complexo porque, ao mesmo tempo, caso a frase seja interrogativa, não existe um ponto de interrogação próprio na Libras, geralmente é utilizada em contrapartida a expressão facial, ou seja, uma arqueada de sobrancelha, no caso da negação, um movimento negativo de cabeça. 
A idealização para a execução do projeto de maneira mais correta e dentro do contexto da Libras é utilizar um treinamento com inteligência artificial para colocar na memória as letras do alfabeto em Libras, mas em vez de gravar somente sinais isolados, gravar frases para um treinamento de reconhecimento de padrões. 


# Linguagem de Programação e Ferramentas

* Python (_3.12.5_)
  * _Mediapipe_
  * _Opencv_ 


