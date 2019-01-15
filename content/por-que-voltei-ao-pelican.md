Title: Por que voltei ao Pelican?
Date: 2019-01-15 07:33
Slug: por-que-voltei-ao-pelican
Author: Daniel Bastos
Tags: cotidiano


Depois de muito tempo tendo abandonado o meu blog (que nunca foi muito ativo também) resolvi reativar ele.
Há alguns anos atrás, esse blog era feito em Pelican, e com o passar do tempo ele acabou se perdendo. Recentemente
quis voltar a escrever, porém queria algo que não demandasse muito trabalho e migrei meus posts para o Wordpress.

Isso resolveu um problema, e criou outro. Agora eu precisava ter um local para hospedar o blog.
Minha primeira iniciativa foi usar o plano free do Heroku. Sei que não é o ideal, mas não queria ter custos
para manter o blog no ar.

Como não haviam muitos posts, foi tranquilo migrar o conteúdo. Porém, assim que fui
escrever meu primeiro post no Wordpress, **comecei a torcer o nariz**.

Primeiro, era necessário acessar a área restrita do blog para começar a escrever (não gosto de ter rascunhos
em arquivos do LibreOffice ou Google Driver). Com a ajuda do alza (alzaimer), foi aind amais frustrante.
Não fazia uma semana que eu havia configurado o Wordpress e já havia esquecido da senha.

OK, passado o lapso de memória, escrevi o primeiro post direto no Wordpress. Anexei uma imagem e... pimba!
A imagem sumia do post cada vez que o dyno era resetado (óbvio)!

Logo me veio aquela lembrança: **"Eu só quero escrever um post. Sem grandes dificuldades nem custos"**

"Garrei" um certo ódio de mim mesmo!

Foi então de decidi, de uma vez por todas, retornar ao Pelican. Dentre os motivos, os principais foram:

* Não vou ter custo de hospedagem (GitHub Pages está ai para isso);
* Não preciso acessar um painel para começar a escrever;
* É em Python. Não queria lidar com `gems` ou algo do tipo;

Os motivos parecem ser bobos, mas o fato de eu só precisar ter o terminal para criar meus arquivos `.md` ou
`.rst` para sair escrevendo, me pareceu ser uma grande vantagem. Sem falar que não precisaria mais me preocupar
em manter um infraestrutura (por menor que seja) para hospedar um blog em Wordpress.

Mas o mundo é uma caixinha de surpresas e nem tudo são flores. Voltamos ao problema de ter que reconfigurar
o Pelican na minha máquina.

Eu tenho uma certa preguiça em mexer com algumas ferramentas, e o Pelican era uma dessas. Como quero hospedar
meu blog no GitHub, o conteúdo do branch `master` tem que ser os HTML's gerados pelo Pelican. Ao mesmo tempo,
preciso versionar o código-fonte com meus arquivos `.md` e `.rst`.

**É aqui que começa a preguiça.**

Para não perder muito tempo, deixei a estrutura versionada pelo branch `pelican` da seguinte forma:

```
.
├── content/
├── Makefile
├── output/ (esta pasta é ignorada)
├── pelicanconf.py
├── publishconf.py
├── requirements.txt
└── tasks.py
```

Ok, o versionamento do código-fonte "está resolvido".

Agora preciso ter o controle dos arquivos HTML. Então dentro da pasta `output` eu faço o
versionamento dos arquivos para meu branch `master`. Mesmo sabendo que não é a melhor forma, foi assim que
resolvi meu ranço com o Pelican + GitHub Pages.


Sei que esse post não trouxe tanta novidade nem algo surpreendente, mas quero usar esse meu espaço como uma espécie
de diário. Mesmo coisas banais vão acabar virando post, pois quero criar em mim a disciplina de escrever constantemente
e compartilhar as coisas que venho vivenciando no meu dia-a-dia de trabalho. Assim como os assuntos relacionados
a carreira e reflexões de leituras vão virar material para esse blog.

Enfim, se você leu até aqui... Parabéns, você merece um prêmio por sua paciência.
Esse é um texto que saiu sem qualquer planejamento/pauta, apenas queria estrear o blog com algum texto novo.


Um forte abraço!!
