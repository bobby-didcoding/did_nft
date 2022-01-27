from .import utils
from .models import NoneFungibleToken
from PIL import Image
from django.conf import settings
from random import randint
from io import BytesIO
from django.core.files.uploadedfile import File

from celery import shared_task
from celery.utils.log import get_task_logger
logger = get_task_logger(__name__)

def randomise():
    return str(randint(1,4))

@shared_task(bind=True)
def create_nft(self, quantity):
    base_dict = utils.createBaseDict()
    body_dict = utils.createBodyDict()
    hair_dict = utils.createHairDict()
    top_dict = utils.createTopDict()
    pants_dict = utils.createPantsDict()
    prop_dict = utils.createPropDict()
    bling_dict = utils.createBlingDict()

    for nft in range(quantity):
        nft_attributes = {}

        base_key = randomise()
        base = Image.open(f'{settings.STATIC_ROOT}/base/{base_key}.png')
        nft_attributes["base"] = base_dict[int(base_key)]

        body_key = randomise()
        body = Image.open(f'{settings.STATIC_ROOT}/body/{body_key}.png')
        nft_attributes["body"] = body_dict[int(body_key)]

        hair_key = randomise()
        hair = Image.open(f'{settings.STATIC_ROOT}/hair/{hair_key}.png')
        nft_attributes["hair"] = hair_dict[int(hair_key)]

        top_key = randomise()
        top = Image.open(f'{settings.STATIC_ROOT}/top/{top_key}.png')
        nft_attributes["top"] = top_dict[int(top_key)]

        pants_key = randomise()
        pants = Image.open(f'{settings.STATIC_ROOT}/pants/{pants_key}.png')
        nft_attributes["pants"] = pants_dict[int(pants_key)]

        prop_key = randomise()
        prop = Image.open(f'{settings.STATIC_ROOT}/prop/{prop_key}.png')
        nft_attributes["prop"] = prop_dict[int(prop_key)]

        bling_key = randomise()
        bling = Image.open(f'{settings.STATIC_ROOT}/bling/{bling_key}.png')
        nft_attributes["bling"] = bling_dict[int(bling_key)]

        # Paste/Merge Required PNGs, as layers on base
        base.paste(body, (0, 0), body)
        base.paste(hair, (0, 0), hair)
        base.paste(top, (0, 0), top)
        base.paste(pants, (0, 0), pants)
        base.paste(prop, (0, 0), prop)
        base.paste(bling, (0, 0), bling)

        #create a new NFT object in db - with json attributes
        new_nft = NoneFungibleToken()
        new_nft.nft_attributes = nft_attributes
        new_nft.save()

        #Resize image to OpenSea market recommended size - "Resample Nearest" to retain resolution
        resized_img = base.resize((300, 300), resample=Image.NEAREST)
        image_io = BytesIO()

        resized_img.save(image_io, "PNG")
        name = f'Did Coding NFT #{new_nft.id}'
        slug = f'didcoding-{new_nft.id}'
        file_name = f'didcoding-{new_nft.id}.png'
        image = File(image_io, name=file_name)
        
        new_nft.image = image
        new_nft.name = name
        new_nft.slug = slug
        new_nft.save()

