Title: Como organizar suas virtualenvs
Date: 2019-01-18 17:00
Slug: como-organizar-suas-virtualenvs
Author: daniellbastos
Tags: python
Og_image: static/img/como-organizar-suas-virtualenvs.jpg

Nesse post não vou trazer grandes novidades nem dicas maravilhosas, daquelas que as pessoas costumam guardar
apenas para si.
Minha ideia é oferecer um caminho simples e prático para quem está iniciando seus projetos em Python e ainda
tem dúvidas de como organizar as suas virtualenvs.

> Não pretende expor aqui a forma definitiva de como os tuas virtualenvs devem estar organizadas, apenas vou
> compartilhar como EU organizo meus projetos em Python.

**Vaaamos lá!**

Eu utilizo uma biblioteca chamada [Virtualenvwrapper][0].
Ela é uma espécie de extensão do virtualenv (daqui pra frente vou usar só **venv**) que nos ajuda a organizar
melhor nossas venvs e e toda nos oferendo alguns comandos bem legais.


Para instalar, basta rodar o comando:
```
sudo pip install virtualenvwrapper
```

Detalhe, eu rodo o `pip` sem nenhuma venv ativada para que o virtualenvwrapper fique disponível diretamente
no OS.

Depois disso, crie uma pasta onde você deseja por todas tuas venvs:

```
mkdir ~/.virtualenvs
```

Com o diretório criado, adicione o seguinte código no final do seu `.bash_profile` ou `.bashrc`:

```
# virtualenvwrapper
source /usr/local/bin/virtualenvwrapper.sh
export WORKON_HOME=$HOME/.virtualenvs
```

Agora feche seu terminal e abra-o novamente para que ele carregue essas configurações.
Se tudo estiver OK, estamos pronto para usar o nosso amigo `virtualenvwrapper`.


### Conhecendo alguns do novos comandos

1) **mkvirtualenv**

Cria uma nova venv. Esse comando possui alguns parâmetros bem bacanas:
```
mkdir teste
mkvirtualenv teste -a teste/ -p ~/.pyenv/versions/3.6.7/bin/python
```

Entendendo os parâmetros:

* **teste**: nome da venv;
* **-a teste/:** define o diretório do projeto. Toda vez que ativar a venv (já já mostra como), você será levado
diretamente para esse diretório;
* **-p ~/.pyenv/versions/3.6.7/bin/python:** Esse parâmetro é opcional, mas costumo sempre passar ele para definir
o interpretador python da venv.
> Como da pra notar, estou utilizando o Python 3.6.7 do meu `pyenv`, um dia eu comento
como configurar e usar o `pyenv`

2) **lsvirtualenv**

Lista todas venvs.
```
$ lsvirtualenv
teste
=====
```

3) **workon**

Ativa uma venv.
```
$ workon teste
```

4) **rmvirtualenv**

Remove uma venv.
```
$ rmvirtualenv teste
```

5) **cdsitepackages**

Com uma venv ativada, o comando te leva até o diretório onde ficam todas as libs instaladas via comando pip.
É muito útil pra quem quer entender o funcionamento das libs para além da documentação.


6) **cdproject**

Com uma venv ativada, o comando te leva de volta ao diretório do projeto (aquele que tu definiu na criação da
venv com o parâmetro `-a`).
Caso não tenha informado o diretório quando você criou a venv, não se preocupe. Basta criar um arquivo `.project`
na raiz da pasta da venv com o caminho para o projeto. Assim:

```
$ cd teste/
$ pwd > ~/.virtualenvs/test/.project
```


Enfim, como eu havia prometido no início, não são dicas extraordinárias nem nada parecido.
Mas talvez possa ajudar quem acha confuso e gerenciar muitas venvs.

E você, como organiza os teus projetos? Não concordou com algo do texto?

Comenta aí!

[0]: https://virtualenvwrapper.readthedocs.io/en/latest/
