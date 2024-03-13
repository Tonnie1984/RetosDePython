"""/*
 * Crea un programa que se encargue de calcular el aspect ratio de una
 * imagen a partir de una url.
 * - Url de ejemplo:
 *  https://avatars.githubusercontent.com/u/17043402?v=4
 * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
 *   imagen de 1920*1080px.
 */
"""

import requests
from PIL import Image
from io import BytesIO
from fractions import Fraction

URL = "https://previews.123rf.com/images/patterndesign/patterndesign1706/patterndesign170600928/80149009-fondo-de-imagen-abstracto-16-9-relaci%C3%B3n-de-aspecto-en-el-estilo-de-arte-digital-tiras-azules.jpg"


def calcular_ratio(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        alto = image.height
        ancho = image.width
        fraccion = Fraction(alto, ancho)
        fraccion = Fraction.as_integer_ratio(fraccion)
        print(fraccion)
        # (f"La relacion de aspecto es de {fraccion.denominator}:{fraccion.numerator}")


calcular_ratio(URL)
