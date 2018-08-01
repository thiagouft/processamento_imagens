#!/usr/bin/env python3
# -*- coding: utf-8 -*

from PIL import Image

if __name__ == '__main__':
    print("Processamento de Imagens.")
    img = Image.open("img/Root_Beer_Guy_At_Typewriter.png")
    img.show()
    print("Fim execução!!")
   