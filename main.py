from pytube import YouTube 
import os
import string

#link of the video to be downloaded 
link=["https://www.youtube.com/watch?v=2PTsyeOkukM",
    ]

def verifica_letra(letra):
    caracteres = "áÁàÀéÉèÈíÍìÌóÓòÒúÚùÙãÃõÕâÂêÊîÎôÔûÛçÇ-_[]}{()"
    if letra in string.ascii_letters or letra in string.digits or letra == " " or letra in caracteres:
        return True
    else:
        return False


def limpa_espaco(titulo):
    titulo_sem_espaco = ''
    for indice in range(0, len(titulo), 1):
        try:
            if titulo[indice] == " " and titulo[indice+1] == " ":
                pass
            else:
                titulo_sem_espaco += "".join(titulo[indice])
        except:
            titulo_sem_espaco += ""

    return titulo_sem_espaco



for i in link: 
    try: 
          
        # object creation using YouTube
        # which was imported in the beginning 
        yt = YouTube(i) 

        nome = yt.title

        nome_arquivo = ''.join(char for char in nome if verifica_letra(char))

        nome_arquivo_sem_espaco = limpa_espaco(nome_arquivo)

        local_base = os.getcwd()

        nome_arquivo_mp4 = "{}.mp4".format(nome_arquivo_sem_espaco)
        print(nome_arquivo)
        nome_arquivo_mp3 = "{}.mp3".format(nome_arquivo_sem_espaco)

        print(nome_arquivo)
        
        os.system("pytube {} -a".format(i))
        os.rename("{}\{}.mp4".format(local_base, nome_arquivo), "{}\{}".format(local_base, nome_arquivo_mp4))
        os.system("ffmpeg -i \"{}\{}\" -b:a 192K -vn \"{}\{}\"".format(local_base, nome_arquivo_mp4, local_base, nome_arquivo_mp3))
        os.remove("{}\{}".format(local_base, nome_arquivo_mp4))
    except Exception as e: 
        print("Ocorreu algum erro. {}".format(e)) 
      