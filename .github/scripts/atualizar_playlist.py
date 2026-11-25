"""
Mantém o playlist.js em sincronia com as imagens do repositório.
- Imagem ADICIONADA no push  -> entra no fim da sequência das TVs.
- Imagem EXCLUÍDA no push    -> sai da sequência.
- Imagem RENOMEADA           -> continua no mesmo lugar, com o nome novo.
Itens retirados pelo painel (admin.html) não voltam sozinhos: só imagens novas entram.
Uso: python atualizar_playlist.py <sha_antes> <sha_depois>
"""
import datetime, json, re, subprocess, sys

EXT = re.compile(r'\.(png|jpe?g|webp|gif|mp4|webm)$', re.I)
ARQ = 'playlist.js'

def git(*a):
    return subprocess.run(['git', *a], check=True, capture_output=True, text=True).stdout

def mudancas(antes, depois):
    if not antes or set(antes) == {'0'}:
        return []
    out = git('-c', 'core.quotepath=false', 'diff', '--name-status', '-M', antes, depois)
    return [l.split('\t') for l in out.splitlines() if l.strip()]

def main():
    antes, depois = sys.argv[1], sys.argv[2]
    txt = open(ARQ, encoding='utf-8').read()
    pl = json.loads(txt[txt.index('{'):txt.rindex('}') + 1])
    itens = pl['itens']
    nomes = [i['arquivo'] for i in itens]
    alterou = []

    for m in mudancas(antes, depois):
        st = m[0][0]
        if st == 'A' and EXT.search(m[1]) and m[1] not in nomes:
            itens.append({'arquivo': m[1], 'titulo': m[1].rsplit('/', 1)[-1].rsplit('.', 1)[0]})
            nomes.append(m[1]); alterou.append('+ ' + m[1])
        elif st == 'D' and m[1] in nomes:
            itens[:] = [i for i in itens if i['arquivo'] != m[1]]
            nomes.remove(m[1]); alterou.append('- ' + m[1])
        elif st == 'R' and EXT.search(m[2]):
            velho, novo = m[1], m[2]
            if velho in nomes:
                for i in itens:
                    if i['arquivo'] == velho: i['arquivo'] = novo
                nomes[nomes.index(velho)] = novo; alterou.append(f'~ {velho} -> {novo}')
            elif novo not in nomes:
                itens.append({'arquivo': novo, 'titulo': novo.rsplit('/', 1)[-1].rsplit('.', 1)[0]})
                nomes.append(novo); alterou.append('+ ' + novo)

    if not alterou:
        print('Nenhuma imagem adicionada ou removida — playlist.js mantido.')
        return
    agora = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-3)))
    pl['versao'] = agora.isoformat(timespec='seconds')
    pl['geradoEm'] = agora.strftime('%d/%m/%Y %H:%M:%S') + ' (automático)'
    open(ARQ, 'w', encoding='utf-8').write(
        '// Gerado automaticamente em ' + pl['geradoEm'] + ' — não edite à mão.\n'
        'window.TV_PLAYLIST = ' + json.dumps(pl, indent=2, ensure_ascii=False) + ';\n')
    print('\n'.join(alterou))

if __name__ == '__main__':
    main()
