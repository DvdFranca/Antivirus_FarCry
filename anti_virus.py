import os

path = '.'

for f in os.listdir(path):
    arquivo = os.path.join(path, f)

    if os.path.isdir(arquivo):
        continue

    if os.path.basename(arquivo) == os.path.basename(__file__):# não escaneia a si mesmo
        continue

    try:
        with open(arquivo, "rb") as f:# abre o arquivo em modo de leitura
            conteudo = f.read()

            if b'\x46\x61\x72\x43\x72\x79\x20\x4D\x61\x6C\x77\x61\x72\x65' in conteudo:# se no conteúdo conter a sequência em bytes 
                print('Malware FarCry Removido...!!')
                os.remove(arquivo)  # Remove o arquivo
    except Exception as e:
        print(f"Erro ao processar o arquivo {arquivo}: {e}")


                
    


