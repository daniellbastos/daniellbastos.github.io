Title: Iniciando um projeto Django
Date: 2016-04-04 15:00
Category: django
Tags: django, python
Slug: iniciando-um-projeto-django
Author: Daniel Bastos
Illustration: como-me-tornei-programador-python.png


Ao contrário do que o título do post sugeri, esse não é um artigo introdutório
para quem esta aprendendo Django e quer saber os primeiros passos com o framework.

Nesse artigo eu vou mostrar como eu faço para iniciar novos projetos usando Django
a partir de uma estrutura de projeto base. Espero mostrar para vocês que vale a
pena parar um tempinho para criar a sua estrutura base de projeto e junto
definir suas libs favoritas.

Sabendo que para iniciar um projeto Django temos que fazer diversos passos e
configurações, para só depois começarmos de fato a pensar nas funcionalidades
do projeto que devemos implementar.

Dentre esses passos estão:

* Configurar settings para lidar com os arquivos estáticos, media e templates
* Configurar ambiente para que seja criado os testes
* Instalar libs básicas que são frequentemente utilizadas
* Etc.

Além disso, eu costumo fazer os seguintes passos a mais (cada louco com suas
manias hehe):

* Criar um pacote de settings
* Separar os requirements
* Isolar minhas apps dentro de um diretório
* Costumo usar uma app chamada core para dar início ao projeto (e aos poucos ir desmembrando em novas apps)
* Configurar rotas para a app core

Depois de tudo isso feito, eu então começava a pensar no projeto de fato.

Não foi um ou dois projetos que iniciei e fiz isso manualmente, mas em cada projeto
eu ia modificando algo procurando melhorar a estrutura.. E acredito que agora
cheguei em um modelo que me agradou muito.

Então, como eu agilizo esse processo? **Criando um projeto template**.

O Django tem esse recurso, e por muito tempo eu o ignorei (eu não tinha um modelo
de projeto qual eu dissesse: É ESSE!), e depois de algum tempo me incomodando
com a burocracia para iniciar meus novos projetos do zero, e cada um com estrutura
diferente.. Decidi parar com a putaria e criar o meu modelo.

Talvez não esteja da melhor forma, mas vou manter essa estrutura sempre atualizada,
assim garanto que sempre vou ter alguma referência para iniciar um novo projeto.

Por enquanto criei apenas para o Django 1.8 (que é uma versão LTS) e já adicionei
algumas libs que costumo usar em quase todos os projetos.

Agora para iniciar meus projetos, primeiro é necessário instalar o Django (com
a versão 1.8):

    pip install django==1.8

Depois disso é só executar:

    django-admin startproject project_name --template=https://github.com/daniellbastos/templatedjango18/archive/master.zip
    cd project_name
    pip install -r requirements/dev.txt -U

Agora o próprio Django se encarrega de baixar e descompactar os arquivos e o
projeto já arrancada com a estrutura definida pelo template.

Bom pessoal, acho que era isso, não é nada técnico, mas gostaria de compartilhar isso..
Porque mesmo trabalhando com Django há algum tempo, somente agora decidi criar
meu projeto template, e talvez haja mais pessoas que também estão ignorando esse recurso.

Para saber mais sobre a estrutura, basta acessar o repositório no [GitHub][0].

Abraço à todos!!


[0]: [https://github.com/daniellbastos/templatedjango18/]
