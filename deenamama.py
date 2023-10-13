import pyfiglet
import random
def get_random_font_style():
    font_styles=pyfiglet.FigletFont.getFonts()
    return random.choice(font_styles)
def wishes():
    random_font_style=get_random_font_style()
    font=pyfiglet.Figlet(font=random_font_style)
    print(font.renderText("Happy Birthday Deena Mama :)"))
    print(font.renderText("Enjoy Your Day!"))
    print(font.renderText("Party Hard"))
wishes()