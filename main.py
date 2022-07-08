from sys import argv
from pathlib import Path

from converte_pdf.jpg import converte_jpg_pdf

ARGS = argv[1:]


def main():
    arquivos_jpg = [Path(arq) for arq in ARGS if Path(arq).suffix.lower() == ".jpg"]
    for jpg in arquivos_jpg:
        print(f"Convertendo arquivo {jpg.name} em PDF...")
        ok = converte_jpg_pdf(jpg)
        if not ok:
            print(f"Erro ao tentar converter o arquivo {jpg.name} em PDF.")


if __name__ == "__main__":
    main()
