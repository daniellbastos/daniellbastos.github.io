Title: O hack do hack: Controle suas contas
Date: 2019-02-05 09:00
Slug: o-hack-do-hack-controle-suas-contas
Author: daniellbastos
Tags: hack, finanças
Og_image: static/img/o-hack-do-hack-controle-suas-contas.jpg

Quem aqui já deixou de controlar os gastos por não ter paciência de "planilhar" tudo?

Quem aqui sabe, exatamente, para onde vai a maior parte do seu dinheiro?

Quem aqui aqui quer mudar essa confusão financeira que suas contas viraram?

Se a sua resposta foi: **Sim, Não, Sim**. Então esse post vai te ajudar.


Eu não tenho a pretensão de ensinar o que você deve, ou não deve, fazer com seu dinheiro. Mas de tanto sofrer
posso dizer com certeza que você **deve** ter o mínimo de controle dos seus gastos. Eu digo *deve*, não porque eu
sou um exemplo, mas porque posso ser um contra-exemplo.

Não tenho dívidas no meu nome e não estou "matando cachorro" a grito, mas faz muito tempo que não me sinto
confortável com minhas finanças. E esse desconforto vem justamente por não ter esse controle das finanças.

Então vou mostrar como eu estou **começando** a resolver esse problema. Sim, o problema ainda existe, mas estou
caminhando para resolver essa situação.

## Hackeie sua preguiça

Toda iniciativa que eu fiz, de ter as finanças da casa em controle, foi frustrada pela minha enorme preguiça
de preencher planilhas. Então a ideia aqui é mostrar alguns *hacks* para facilitar esse trabalho. Talvez não
resolva todo o problema, mas diminiu o tamanho do obstáculo.

O termo **hack**, para quem não está familiarizado, é um análogo a "**hackear algo**". É forçar um sistema a fazer
algo diferente daquilo qual ele foi concebido. Isso não é, necessariamente, igual aquelas cenas de filmes onde
um nerd (não geek) fica trancado em seu porão e quebra o sistema de segurança de um banco.

Aqui, o termo **hack** está mais para: "**Criar meios para que o sistema resolva as minhas necessidades com o
menor esforço possível.**"

Nesse caso, o "sistema/fluxo/rotina" que eu quero "hacker" é a rotina de preencher valores em uma planilha,
com o menor esforço possível.


## O hack

Após um longo tempo conversando sobre a necessidade de ter o controle dos gastos, o meu amigo Augusto Goulart,
compartilhou o seu hack para "burlar" o sistema de preenchimento de planilhas.

Basicamente consistem em criar um grupo no Whatsapp com a esposa (ou os membros da família) e usar esse grupo
**apenas** para anotar os gastos. Esse grupo irá receber mensagens com o seguinte padrão: `Mercado,120`,
`Farmácia,150.36`, etc.

Inicialmente parece dar o mesmo trabalho de anotar em um planilha, mas a ideia é anotar os gastos do jeito mais
prático possível, para não precisar ter que, ao final do dia, pegar notinha por notinha e passar a limpo na
planilha.

Uma vez que os valores estão salvos nesse grupo do Whatsapp, você só precisa pegar um dia e usar o
recurso de exportar mensagens do grupo. O Whatsapp cria um arquivo no formato de texto (`nome-do-arquivo.txt`),
como você padronizou as mensagens separadas por `,`, basta mudar a extensão do arquivo para `.csv` e importar o
conteúdo na sua planilha.


## O hack do hack

Realmente, não há escapatória para o trabalho de anotar todos os gastos. Porém eu queria evitar
esse último passo, de exportar o histórico de conversa do grupo para importar na planilha.

Pensando nisso, fui pesquisar se não teria como criar uma automação nessa etapa do processo. Foi quando eu
lembrei que poderia criar um bot no **Telegram** para fazer isso.


O Telegram para quem não conhece, é um aplicativo de mensagem similar ao Whatsapp, porém é possível criar
diversas integrações com ele.

Eu nunca havia criado um bot ou qualquer tipo de automação usando o Telegram, mas desconfiava que isso era
possível. Já na primeira pesquisada no Google, encontrei um tutorial para fazer **exatamente** o que eu queria.

[>> Confira o tutorial <<][0]

Segui o tutorial e fiz apenas uma adaptação na função `doPost`:
```
function doPost(e) {
  var data = JSON.parse(e.postData.contents);
  var text = data.message.text;
  var name = data.message.chat.first_name;
  var kind = text.split(',')[0];
  var value = text.split(',')[1];
  SpreadsheetApp.openById(ssId).getSheets()[0].appendRow([new Date(),name,kind,value]);
}
```

Agora basta postar a mensagem no bot, seguindo o padrão `<Tipo-do-gasto>,<Valor>` que automaticamente o gasto
vai para a planilha.


## Conclusão

Use a preguiça a seu favor e não deixe de fazer o dever de casa.


E ai, o que achou?

Comenta ai sua opinião e como você faz para controlar seus gastos.

[0]: https://www.youtube.com/watch?v=mKSXd_od4Lg
