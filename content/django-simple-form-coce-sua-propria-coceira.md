Title: Django simple form: Coce a sua própria coceira
Date: 2019-07-03 11:00
Slug: django-simple-form-coce-sua-propria-coceira
Author: daniellbastos
Tags: django, python
Og_image: static/img/back-end-vs-front-end.png


## "Coce a sua própria coceira"

> "Se algo te incomoda, vá lá e resolva e não espere que alguém resolva o problema que **É SEU**."

Sempre gostei muito do conceito de código *open-source*, por dar a possibilidade para que muitas
pessoas se beneficiem de um trabalho que foi feito para resolver o problema de uma pessoa apenas.
Já que a "dor" de um, pode ser a "dor" de muitas outras pessoas.


Como eu trabalho muito com projetos web com Django, uma constante do meu trabalho envolve a construção de
interfaces para que os usuários possam interagir com o sistema, consumindo ou fornecendo dados.

Nesse trabalho de codificação de telas para *input* de dados, o Django oferece muitos recursos que auxiliam no
desenvolvimento de interfaces. Porém sempre é necessário algum tipo de customização na hora de apresentar um
formulário web. Principalmente se você trabalha com algum framework front-end (Bootstrap, Foundation, etc).

Foi exatamente para essa "coceira" que eu criei o [Django simple form][0]. Atualmente, nos meus projetos Django
eu já tenho um "modelo" que utilizo para fazer a padronização dos meus formulários. Agora decidi criar uma
biblioteca *open-source* e espero que outras pessoas possam se beneficiar desse código também.

## A motivação

Tive uma resistência inicial em criar algo público, pois pensava se tratar algo muito exclusivo do meu modo de
trabalhar, e não seria algo "útil" para a comunidade.
Porém agora, trabalhando em projetos com diferentes tipos de interface, notei que estava tendo muito retrabalho
em gerir esse "pacote" e acabava movendo arquivos de um projeto para o outro.

Então para facilitar **a minha vida**, resolvi criar a biblioteca.

Os detalhes de como instalar e como usar está descrito no README do projeto, está aqui [https://github.com/daniellbastos/django-simple-form/][0]

[0]: https://github.com/daniellbastos/django-simple-form/
