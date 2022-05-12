from text import Text
from config import Config, Icon
from image import Image

def main():
    config = Config()
    text = Text()
    
    passage = text.get_passage(0, 0, 0, 0)

    Image(passage, config)

    tweet_text = passage.Attribution() + ' #Bible #KJV'

    config.api_context.update_status_with_media(filename='Twitterbot/output/card.png', status=tweet_text)


if __name__ == '__main__':
    main()