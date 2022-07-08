from pathlib import Path

from PIL import Image


def converte_jpg_pdf(imagem: Path) -> bool:
    """Tenta determinar a resolução de um arquivo .JPG. Retorna None
    caso não consiga."""

    _res: tuple[int, int]
    _img = Image.open(imagem)

    # Define a resolução do JPG.
    try:
        _res = _img.info["jfif_density"]
    except KeyError:
        try:
            for k in _img.info.keys():
                if k == "photoshop":
                    _res = (
                        int(_img.info[k][1005]["XResolution"]),
                        int(_img.info[k][1005]["YResolution"]),
                    )
        except KeyError as erro:
            print(erro)
            return False

    # Converte o JPG em PDF.
    _pdf = imagem.parent / (imagem.stem + ".pdf")
    _img.convert("RGB")
    _img.save(_pdf, format="PDF", resolution=_res[0])

    return True
