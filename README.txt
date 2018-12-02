# PyKernel


[ Sobre ]

    Esse é um programa simples que tem por finalidade realizar o download da
    última versão estável do Kernel Linux (https://kernel.org) através de um
    comando no terminal.

    O programa poderá ter atualizações, para isso tem o arquivo "CHANGELOG.md"
    no qual você pode estar acompanhando essas atualizações.

[ Perguntas ]

    1 - Qual a finalidade desse programa?

    R:- Caso o usuário seja um 'sysadmin' que trabalhe apenas com terminal
        em uma máquina sem interface gráfica, e queira realizar o download
        do Kernel Linux estável para instalar na máquina, ele pode fazer
        isso com o PyKernel.

    2 - Por que criou esse programa?

    R:- Esse projeto (v1.0.0) foi realizado para a conclusão do curso
        "Aprenda a programar em Python com facilidade do zero" na Udemy
        (https://www.udemy.com) ministrado por Ivan Lourenço Gomes
        (https://www.udemy.com/user/ivan-lourenco-gomes/).

[ Dependências ]

  * Git
  * Python3
  * pip3

  Modulos externos:
    * pathlib
    * requests
    * tqdm

[ Instalação ]

    $ pip3 install --user virtualenv
    $ git clone https://github.com/williamcanin/pykernel.git pykernel
    $ cd pykernel
    $ virtualenv ENV
    $ source ENV/bin/activate
    $ pip install requests tqdm pathlib

[ Usando ]

    > Linux / OS X

        $ chmod +x pykernel.py
        $ ./pykernel.py download --path "$HOME/Downloads"

    > Windows

        Mesmo que você consiga executar o PyKernel no Windows, ele foi
        desenvolvido para atender uma necessidade em sistemas operacionais Linux.

    Nota1 : Se você não especificar o argumento --path, ele realizará o
            download na pasta raiz do usuário. Ex: ./pykernel.py download
    Nota 2: Se a pasta que você especificar para o download
            tiver permissão apenas para usuário root, o download não irá ser
            feito por questões de permissão.

    Para mais informações de comandos, use: ./pykernel.py --help


[ Demo ]

  Acesse o link abaixo para ver uma demonstração de instalação e usabilidade
  do PyKernel:

  https://raw.githubusercontent.com/williamcanin/pykernel/trinket/demo.gif

[ Licença ]

    MIT License (MIT) https://opensource.org/licenses/MIT


Projeto Oficial em: https://github.com/williamcanin/pykernel

© PyKernel. William C. Canin. All rights reserved. ®
