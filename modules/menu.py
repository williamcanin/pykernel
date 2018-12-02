import modules.imports as app_import
import modules.message_colors as color_msg


def arguments(script_name, path_default):

    try:
        parser = app_import.ArgumentParser(prog=script_name,
                                           usage=script_name.lower() +
                                           '.py' + ' <command> [arguments]',
                                           description='The ' + script_name +
                                           ' downloads the Linux kernel.',
                                           epilog='See you later!!')
        parser.add_argument('command', action='store', metavar='download',
                            type=str, default='download')
        parser.add_argument('-p', '--path', action='store', type=str,
                            dest='path', default=str(path_default),
                            help='Enter the absolute path where the download \
                                    will be saved.')
        args = parser.parse_args()
        return args

    except Exception as err:
        color_msg.Message.print_color(
                    color_msg.Message._fail,
                    'Err! Erro na passagem de argumentos.', err)
