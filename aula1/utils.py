def popularListaArquivo(lista, nomeArquivo):
        with open(nomeArquivo, "w", encoding='utf8') as escritor:
            escritor.writelines(str(lista))

def lerArquivoLista(nomeArquivo):
    with open(nomeArquivo, 'r', encoding='uft8') as leitor:
         for linha in leitor:
            linha.replace('\n', '\0')
            lista.append(linha.strip())