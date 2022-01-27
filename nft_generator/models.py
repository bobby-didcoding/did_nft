from django.db import models
from django_extensions.db.models import TimeStampedModel
from PIL import Image

class NoneFungibleToken(TimeStampedModel,models.Model):

    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(default='blank.png', upload_to='nfts')
    slug = models.SlugField(null=True, blank=True)
    nft_attributes = models.JSONField(default=dict)


    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return f"/nft/{self.slug}"

    def all_nfts(self):
        all_nfts = NoneFungibleToken.objects.all()
        return all_nfts.count()

    @property
    def base_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__base = self.nft_attributes["base"]).count()
        return format(nft_qty / self.all_nfts(), '.2%')

    @property
    def body_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__body = self.nft_attributes["body"]).count()
        return format(nft_qty / self.all_nfts(), '.2%')

    @property
    def hair_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__hair = self.nft_attributes["hair"]).count()
        return format(nft_qty /self.all_nfts(), '.2%')

    @property
    def pants_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__pants = self.nft_attributes["pants"]).count()
        return format(nft_qty /self.all_nfts(), '.2%')

    @property
    def top_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__top = self.nft_attributes["top"]).count()
        return format(nft_qty /self.all_nfts(), '.2%')

    @property
    def prop_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__prop = self.nft_attributes["prop"]).count()
        return format(nft_qty /self.all_nfts(), '.2%')

    @property
    def bling_rarity(self):
        nft_qty = NoneFungibleToken.objects.filter(nft_attributes__bling = self.nft_attributes["bling"]).count()
        return format(nft_qty /self.all_nfts(), '.2%')

    @property
    def overall_rarity(self):
        base_qty = NoneFungibleToken.objects.filter(nft_attributes__base = self.nft_attributes["base"]).count()
        body_qty = NoneFungibleToken.objects.filter(nft_attributes__body = self.nft_attributes["body"]).count()
        hair_qty = NoneFungibleToken.objects.filter(nft_attributes__hair = self.nft_attributes["hair"]).count()
        top_qty = NoneFungibleToken.objects.filter(nft_attributes__top = self.nft_attributes["top"]).count()
        pants_qty = NoneFungibleToken.objects.filter(nft_attributes__pants = self.nft_attributes["pants"]).count()
        prop_qty = NoneFungibleToken.objects.filter(nft_attributes__prop = self.nft_attributes["prop"]).count()
        bling_qty = NoneFungibleToken.objects.filter(nft_attributes__bling = self.nft_attributes["bling"]).count()
        
        total_traits = base_qty + body_qty + hair_qty + top_qty + pants_qty + prop_qty + bling_qty
        total_nfts = self.all_nfts() * 7
        return format(total_traits /total_nfts, '.2%')

