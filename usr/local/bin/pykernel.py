#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2018 - William C. Canin Copyright Holder All Rights Reserved.

# import modules.imports as app_import
# import modules.welcome as welcome
# import modules.version as version
# import modules.downloading as download
# import modules.menu as menu
# import modules.message_colors as color_msg

# app_import.sys.path.append('modules')

import requests
import sys
from argparse import ArgumentParser
from pathlib import Path
import json
from tqdm import tqdm
from modules import *


class PyKernel():
    # Cria um dicionário contendo as principais informações para a passagem de
    # parametro no script.
    def __init__(self):
        config = {
            'scripName': 'PyKernel',
            'appName': 'Kernel Linux',
            'appSite': 'https://www.kernel.org/',
            'jsonFilename': 'releases.json'
        }

        # Variável que armazena os argumentos passado.
        args = menu.arguments(config['scripName'], app_import.Path.home())
        # Faz uma comparação se o argumento obtido em "command" é igual a
        # download.
        # O "command" é o argumento obrigatório na passagem de parametro.
        if args.command == 'download':
            # Se "command" for igual a "download", então tudo se inicia,
            # mostrando
            # primeiramente o "Welcome".
            welcome.Welcome(config['scripName'], config['appName'])
            try:
                # Armazena a última versão estável do kernel através do metodo
                # number no arquivo version.py.
                latestVersion = version.number(
                                config['appSite'],
                                config['jsonFilename'],
                                config['appName'])
                color_msg.Message.print_color(
                            color_msg.Message._okgreen,
                            '> Última versão: ' + latestVersion)
                download.package(latestVersion, args.path)

            except Exception as err:
                print(f'\nErro ao prosseguir com o \
                {config["scripName"]}.', err)
                exit(1)
            # Caso o usuário cancele o processo, irá exibir essa excessão de
            # interrupção.
            except KeyboardInterrupt as keI:
                print('\n\n> Processo interrompido pelo usuário.', keI)
                exit(0)
        # Se o parametro obrigatório for diferente de "download", então mostra
        # a mensagem abaixo.
        else:
            color_msg.Message.print_color(
                            color_msg.Message._fail,
                            'Erro de parametro no ' + config["scripName"] +
                            '.')
            color_msg.Message.print_color(
                            color_msg.Message._warning,
                            '> Use: "' + config["scripName"].lower() + '.py --help" para obter mais \
        informações.')


if __name__ == '__main__':
    PyKernel()
