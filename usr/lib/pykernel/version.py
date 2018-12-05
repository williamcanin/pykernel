import modules.imports as app_import


def number(app_site, json_filename, app_name):
    try:
        # Faz requisição da url.
        req = app_import.requests.get(app_site + json_filename)
        # Como a url é direcionada para um Json, então faz o load desse Json,
        # amarzenando em uma variável.
        releases = app_import.json.loads(req.text)
        # Navega até o Json pegando os valores "latest_stable" e "version".
        latest_version = releases['latest_stable']['version']
        # Retorna o valor obtido, no caso a versão estável do kernel.
        return latest_version
    except Exception as err:
        # Caso aconteça algum erro, me mostra a mensagem de erro,
        print(f'Erro ao capturar a versão do {app_name}!', err)
        return False
