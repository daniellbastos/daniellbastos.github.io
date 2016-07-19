:title: Primeira contribuição com projeto Open-source
:date: 2016-07-19 08:00
:category: open-source
:tags: python, open-source, bottle
:slug: primeira-contribuicao-com-projeto-open-source
:author: Daniel Bastos
:illustration: primeira-contribuicao.png


Fala pessoal, beleza??

Hoje acordei, abri meu e-mail e estava lá: **meu primeiro pull request foi
aceito.**

Sei que pra muitas pessoas isso já faz parte do dia-a-dia, e pode achar até
engraçado alguém comemorar algo tão banal.
Mas eu realmente quis fazer esse post porque acredito que deve ter mais gente,
assim como eu, que nunca contribui com projetos *open-source*, mas gostariam,
então resolvi fazer o meu breve relato.

Por que contrinuir?
-------------------

Sempre achei nobre a atitude das pessoas que disponibilizam seus projetos
para o quem quiser usar. Sempre trabalhei com tecnologias *open-source* e devo
minha carreira à essas pessoas.

Como a minha carreira foi alicerceada em tecnologias *open-source*, sempre quis
retribuir de alguma forma (financeiramente não rola ainda :/).
Por isso quis contribuir com projetos *open-source*. Mas qual projeto? Como?

Cosse a propria cosseira
------------------------

Com o questionamento na cabeça (qual projeto posso ajudar?), fiquei muito tempo
sem resposta e parei de tentar responde-la. A ideia acabou ficando em segundo
plano, e segui tocando a vida.

Eis que um dia criei um projeto pra brincar com a API do Facebook. Normalmente
costumo tentar resolver tudo com Python 3 (pra já ir me familiarizando com as
mudanças, já que hoje no meu trabalho ainda uso o Python 2.7 com Django).

Brincando com a API do Facebook, usei Python 3 e MongoDB para consumir
os dados da API, e agora chegou a hora de criar um site pra visualiza-los melhor.
Então para expor os dados, usei o Bottle com a *lib* `BottleCBV <https://github.com/techchunks/bottleCBV>`_.
Sempre gostei muito do micro-framework Bottle pela sua simplicidade, e sempre
achei que um dia poderia contribuir com ele, pela sua simplicidade.

E foi nessa brincadeira que descobri que a *lib* BottleCBV não havia sido portada
para o Python 3, e estava dando alguns erros de retorno que foram modificados
no Python 3

Logo pensei: **Achei o que precisava para colaborar com projetos *open-source*!!**

Como se tratava de uma *lib* simples, assim como o Bottle, são apenas
um arquivo Python. Então não tinha mais desculpas para não colaborar.

E foi o que eu fiz, mandei meu `pull request <https://github.com/techchunks/bottleCBV/pull/7>`_.

Foi muito legal ter tido a experiência em colaborar com projetos *open-source*,
mesmo que a minha colaboração não tenha sido nada de muito relevante, foi
adicionando/modificando meia-dúzia de linhas.
Mas pra mim já serviu para resolver o meu problema, e espero que de outras
pessoas também.

Isso me motivou ainda mais em querer continuar contribuindo com projetos
*open-source*.

Resumindo a história
--------------------

Acredito que qualquer um pode colaborar com projetos *open-source* (se eu consigo,
qualquer um consegui hehehe), basta buscar algo que você use, conheça, e logo
conseguirá contribuir.

Minha dica é: comece com projetos/*libs* que você usa no seu dia-a-dia, e se for
um projeto pequeno, melhor ainda.. mais fácil de compreender todo o projeto.


Próximos passos
---------------

Como esse meu projeto lúdico ainda esta em processo de desenvolvimento, logo
vou precisar de mais algumas funcionalidades, dentre elas um sistema de autenticação.
Vi por cima que o **Thiago Avelino** tem uma *lib* pra isso o `bottle-auth <https://github.com/avelino/bottle-auth>`_,
logo vou incorporar essa *lib* no meu projeto, e pretendo contribuir com o Bottle
Authentication.
