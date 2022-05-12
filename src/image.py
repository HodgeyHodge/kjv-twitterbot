import os
import random
import PIL.Image, PIL.ImageFont, PIL.ImageDraw

class Image:
    def __init__(self, passage, config, **kwargs):
        icon = kwargs.get('icon', random.choice(config.icons))
        font_name = kwargs.get('font', random.choice(config.fonts))
        font_colour = kwargs.get('font_colour', self._random_colour(upper=config.dark))
        background_colour = kwargs.get('colour', self._random_colour(lower=config.light))
        
        image_icon = PIL.Image.open(os.path.join('Twitterbot/assets/icons/', icon.Filename)).convert('RGBA')
        image_font_attribution = PIL.ImageFont.truetype(os.path.join('Twitterbot/assets/fonts/', font_name), 25)
        image_font_passage = PIL.ImageFont.truetype(os.path.join('Twitterbot/assets/fonts/', font_name), 40)

        WIDTH = 1024

        img = PIL.Image.new('RGBA', (WIDTH, 2096), background_colour)
        drawcontext = PIL.ImageDraw.Draw(img)
        
        passage_size = drawcontext.multiline_textsize(text=passage.Passage(50), font=image_font_passage, spacing=15)
        attribution_size = drawcontext.textsize(text=passage.Attribution(), font=image_font_attribution)
        margin = (WIDTH - passage_size[0])//2
        image_height = margin + passage_size[1] + margin + icon.Height + 30 + attribution_size[1] + 80 #top to bottom
    
        drawcontext.multiline_text(
            xy=(margin, margin),
            text=passage.Passage(50),
            fill=font_colour,
            font=image_font_passage,
            spacing=15,
            align='center')
                           
        drawcontext.text(
            xy=(
                (WIDTH - attribution_size[0])//2,
                margin + passage_size[1] + margin + icon.Height + 30),
            text=passage.Attribution(),
            fill=font_colour,
            font=image_font_attribution)
    
        self._add_border(drawcontext, WIDTH, image_height, 14, font_colour)
        self._add_border(drawcontext, WIDTH, image_height, 10, font_colour)
    
        Xbg = PIL.Image.new('RGBA', (WIDTH, image_height))
        Xbg.paste(
            image_icon,
            box=(
                (WIDTH - icon.Width)//2,
                margin + passage_size[1] + margin))
    
        img = PIL.Image.composite(Xbg, img, Xbg)
        img.crop((0, 0, WIDTH, image_height)).save(os.path.join('Twitterbot/output/', 'card.png'), 'png')

        self.img = img


    def _random_colour(self, lower=0, upper=255):
        r = random.randint(lower, upper)
        g = random.randint(lower, upper)
        b = random.randint(lower, upper)
        return (r, g, b)

    def _add_border(self, drawcontext, width, height, margin, colour):
        drawcontext.line((margin, margin, width - margin, margin), fill=colour)
        drawcontext.line((margin, height - margin, width - margin, height - margin), fill=colour)
        drawcontext.line((margin, margin, margin, height - margin), fill=colour)
        drawcontext.line((width - margin, margin, width - margin, height - margin), fill=colour)