import requests
import docx
from PIL import Image, ImageDraw, ImageFont

taco_recipe_one = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
taco_recipe_two = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()
taco_recipe_three = requests.get('https://taco-1150.herokuapp.com/random/?full_taco=true').json()


image = Image.open('christine-siracusa-vzX2rgUbQXM-unsplash.jpg')
img_draw = ImageDraw.Draw(image)
font = ImageFont.truetype('DejaVuSans.ttf', 300)
img_draw.text([250, 1500], 'Random Taco Cookbook', fill='darkslateblue', font=font)
image.thumbnail((800, 800))
image.show()
image.save('random_taco_cookbook.jpg')

document = docx.Document()
document.add_paragraph('Random Taco Cookbook', 'Title')
document.add_picture('random_taco_cookbook.jpg', width=docx.shared.Inches(4), height=docx.shared.Inches(6))
document.add_paragraph('Credits', 'Heading 1')
document.add_paragraph('Image: Christine Siracusa on Unsplash')
document.add_paragraph('Recipes from: https://taco-1150.herokuapp.com/random/?full_taco=true')
document.add_paragraph('Code by: Quinn Daniel')
document.add_page_break()

def taco(recipe):
    base_layer = recipe['base_layer']['name']
    seasoning = recipe['seasoning']['name']
    mixin = recipe['mixin']['name']
    condiment = recipe['condiment']['name']
    shell = recipe['shell']['name']
    base_layer_recipe = recipe['base_layer']['recipe']
    seasoning_recipe = recipe['seasoning']['recipe']
    mixin_recipe = recipe['mixin']['recipe']
    condiment_recip = recipe['condiment']['recipe']
    shell_recipe = recipe['shell']['recipe']
    document.add_paragraph(f'{base_layer} with {mixin}, {seasoning} and {condiment} in {shell}', 'Title')
    document.add_paragraph(f'{base_layer}', 'Heading 1')
    document.add_paragraph(f'{base_layer_recipe}')
    document.add_paragraph(f'{mixin}', 'Heading 1')
    document.add_paragraph(f'{mixin_recipe}')
    document.add_paragraph(f'{seasoning}', 'Heading 1')
    document.add_paragraph(f'{seasoning_recipe}')
    document.add_paragraph(f'{condiment}', 'Heading 1')
    document.add_paragraph(f'{condiment_recip}')
    document.add_paragraph(f'{shell}', 'Heading 1')
    document.add_paragraph(f'{shell_recipe}')
    document.add_page_break()
    return
taco(taco_recipe_one)
taco(taco_recipe_two)
taco(taco_recipe_three)

document.save('random_taco_test.docx')











