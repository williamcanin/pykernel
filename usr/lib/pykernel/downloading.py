import modules.imports as app_import
import modules.message_colors as color_msg


# Function using 'tqdm'
def package(app_version, app_down_dir):
    # Url completa do kernel Linux.
    urlDownload = 'https://cdn.kernel.org/pub/linux/kernel/v' + \
                  app_version.split(".")[0] + '.x/linux-' + \
                  app_version + '.tar.xz'
    chunk_size = 1024
    # Servidor não suporta solicitação de intervalo, por isso o verify=True,
    # não suporta continuação de download. Caso suportação, poderia deixar
    # verify=False que o download continuava de onde parou.
    r = app_import.requests.get(urlDownload,
                                headers={'Range': 'bytes=StartPos-StopPos'},
                                stream=True, verify=True, allow_redirects=True
                                )
    # Faz a contagem total do tamanho do arquivo.
    total_size = int(r.headers['Content-Length'])
    # Pega url completa do kernel e realiza um split através do /.
    filename = urlDownload.split('/')[-1]

    # Escreve o arquivo fisico.
    with open(app_down_dir + '/' + filename, 'wb') as f:
        # Realiza a animação da biblioteca tqdm.
        color_msg.Message.print_color(
                            color_msg.Message._header,
                            '> Realizando o download do "Kernel Linux Stable \
'+app_version+'" ...')
        for data in app_import.tqdm(
                                iterable=r.iter_content(chunk_size=chunk_size),
                                total=total_size / chunk_size, unit='KB'):
            f.write(data)
        # Após completa downlod, printa mensagem de conclusão.
        color_msg.Message.print_color(
                    color_msg.Message._okgree,
                    '> Download concluído!')
