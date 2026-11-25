# TVs — site no GitHub (https://llz-qualidade.github.io/galeria-gifs/)

## Implantação (uma vez só)

1. Abra https://github.com/llz-qualidade/galeria-gifs → **Add file → Upload files**.
2. **Descompacte o zip antes** e arraste os 3 arquivos (não o .zip): `index.html`, `admin.html`, `playlist.js` → **Commit changes**.
   (O `index.html` antigo é substituído. As imagens que já estão lá continuam sendo usadas.)
3. Espere ~10 minutos (o GitHub demora para trocar a versão do site).
4. Em cada TV, **atualize a página uma última vez** (ou desligue e ligue a TV). Aperte **OK** no controle para tela cheia.
   A partir daí, nunca mais precisa mexer nas TVs.

## Dia a dia — direto no GitHub (mais simples)

- **Colocar imagem:** Adicionar arquivo → Upload files → arraste a imagem → Confirmar alterações.
  Ela entra no fim da sequência sozinha (automação do GitHub) e aparece nas TVs em ~2 minutos.
- **Tirar imagem:** clique na imagem no GitHub → menu **⋯** (canto direito) → **Excluir arquivo** → Confirmar alterações.
- Prefira nomes sem espaço/símbolos: `campanha-natal.png`.

## Ajustes finos (ordem, tempo, datas) — pelo painel

1. Abra https://llz-qualidade.github.io/galeria-gifs/admin.html — ele já mostra o que está no ar.
2. Adicione/remova artes, ajuste ordem, tempo e datas ("Exibir até" tira a arte do ar sozinha).
3. **Publicar nas TVs** → na 1ª vez, escolha uma pasta do seu computador (ex.: `Área de Trabalho\TV publicar`).
   O painel grava ali o `playlist.js` e a pasta `imagens` com as artes novas.
4. **Abrir envio no GitHub** → arraste tudo o que está nessa pasta → **Commit changes**.
5. Em 1 a 2 minutos todas as TVs mostram a nova sequência.

> Não edite mais o `index.html` à mão — a lista agora fica no `playlist.js`, gerado pelo painel.
> Para checar uma TV: `https://llz-qualidade.github.io/galeria-gifs/?debug`.

## Atenção — site público

Tudo em `llz-qualidade.github.io/galeria-gifs` pode ser aberto por qualquer pessoa com o link (fotos de colaboradores,
resultados e metas). Recomendado avaliar com Tecnologia/Jurídico (LGPD) a migração para um endereço interno.
O sistema funciona igual em servidor interno — muda só o lugar onde os arquivos ficam.
