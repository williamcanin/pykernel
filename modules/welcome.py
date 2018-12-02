import modules.message_colors as color_msg


# Método apenas para printar um welcome.
# Nota: A escrita do texto foi usando o pacote "figlet" no Linux.
# $ sudo apt install figlet
# $ figlet PyKernel
def message(scrip_name, app_name):

    print(f'''
=================================================
 ____        _  __                    _
|  _ \ _   _| |/ /___ _ __ _ __   ___| |
| |_) | | | | ' // _ \ '__| '_ \ / _ \ |
|  __/| |_| | . \  __/ |  | | | |  __/ |
|_|    \__, |_|\_\___|_|  |_| |_|\___|_|
       |___/
=================================================
Para cancelar, digite Ctrl+C.
''')
    color_msg.Message.print_color(
                            color_msg.Message._header,
                            '> Coletando última versão estável do '
                            + app_name + ' ...')
