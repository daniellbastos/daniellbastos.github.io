Title: Usando as ferramentas disponíveis: xargs
Date: 2021-03-14 18:00
Slug: usando-as-ferramentas-disponiveis-xargs
Author: daniellbastos
Tags: linux, script
Og_image: static/img/usando-as-ferramentas-disponiveis-xargs.jpg


É comum no dia-a-dia de quem trabalha desenvolvendo softwares, lidarmos com algumas tarefas repetitivas e
manuais. No mundo ideal, essas tarefas todas seriam automatizadas e teriam interfaces bonitinhas para que um
usuário não dependa de um programador para executar essa rotina. Mas ainda temos que lidar com o famoso:
"Pede para o Automático executar a
rotina X". E o "Automático" é você!

![Você](static/img/usando-as-ferramentas-disponiveis-xargs-voce.jpg)

Como vivemos no mundo real, isso faz parte da realidade do nosso trabalho. E é por isso que decidi voltar a
estudar um pouco mais sobre Linux, já que frequentemente eu esqueço alguns comandos e preciso recorrer ao
google muitas vezes (shame).

Hoje vou criar o seguinte cenário hipotético para ajudar a compreender as vantagens de conhecer melhor as
ferramentas que estão disponíveis no seu sistema operacional

## Cenário hipotético

Devido a urgência de lançar o MVP, uma empresa decidiu que muitas das funcionalidades menos prioritárias seriam deixadas de lado. Uma
delas foi a feature de recuperação da senha do usuário. Por ser um "caso raro", ficou combinado que a equipe de atendimento reuniria
os identificadores dos usuários comproblemas na senhas, e os colocaria no mesmo ticket de chamado para a
equipe de suporte.

Dado o cenário, optou-se por criar um endpoint simples para isso. Ao fazer uma requisição para esse nosso endpoint,
a API vai atualizar a senha usando 6 dígitos aleatórios e retornar no payload essa string.

A pessoa responsável por atender esse chamado vai pegar o retorno da API e colocar como resposta do ticket,
indentificando o ID do usuário e a sua nova senha. Então o atendimento segue o seu trabalho para informar a
cada usuário sua nova senha.

Com esse cenário, uma dentre as mil formas de se "automatizar" essa rotina, poderia ser criando um
script python. Esse script irá receber um **único parâmetro** e fazer o request para o endpoint. Depois disso, ele deve
"cuspir" no terminal as informações no formato: `ID:senha`.

Por que um único ID por vez? Sabendo que vamos precisar rodar o script para uma série de IDs, por que já não
deixar o script preparado para receber uma lista de IDs?

Simples! Esse é o motivo: **ser simples!**

Vamos fazer um script python bem simples e usar os recursos disponíveis no sistema operacional (Unix)  para
reutilizar esse script python quantas vezes for necessário.

O script python ficaria mais ou menos asism:

```
# reset_password.py
import random
import string
import sys

PASSWORD_SIZE = 6
user_id = sys.argv[1]


def make_request(user_id):
    """
    Simulate a request in API.
    """
    allowed_chars = string.ascii_uppercase + string.digits
    random_string = ''.join([random.choice(allowed_chars) for _ in range(PASSWOD_SIZE)])
    return {'password': random_string}

response = make_request(user_id)
print('{}:{}'.format(user_id, response['password']))
```

Com pouco mais de dez linhas de código, temos um script python que faz exatamente o que esperamos! E podemos chamar
ele de uma forma extremamente simples:

```
$ python reset_password.py 42
```

E vamos ter como retorno:

```
42:850BBH
```

Pronto! Com esse script python e um pouco de conhecimento em shell, vamos resolver o problema que frequentemente
nos atormenta.

Agora, para repetir essa rotina de uma forma simples, vamos criar um arquivo de texto com todos os IDs que o
atendimento põem no ticket, colocando um ID de usuário por linha. E vamos usar esse arquivo como input do
nosso script python.

Para juntar o script python com o arquivo de IDs, vamos usar o comando [xargs][0]{:target="blank"} do Unix.
Onde a sua definição é:
`xargs - build and execute command lines from standard input.`

Com essa definição bonitona, vamos conseguir chamar o nosso script python "N" vezes, passando diferentes inputs
de uma forma simples. Tipo assim:

```
$ xargs -l python reset_passwod.py < arquivo_com_os_ids
```

Desta forma, o `xargs` vai pegar cada linha do arquivo e executar o comando (`python reset_password.py`) passando o
conteúdo da linha como parâmeto de entrada. Então, ao executar o comando acima, vamos ter o seguinte resultado:

```
10:GB5HL4
20:X4K23M
111:R4KGYN
9000:E5D389
19:XM2HTH
92:NFJFL5
3:H85MJV
1:S1O326
89:8KHZ4U
```

O que achou? Você também usa bastante os recursos que o seu sistema operacional oferece no seu dia-a-dia?
Comenta aí.


[0]: https://man7.org/linux/man-pages/man1/xargs.1.html
