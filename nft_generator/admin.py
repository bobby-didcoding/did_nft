from django.contrib import admin

from .models import NoneFungibleToken

@admin.register(NoneFungibleToken)
class NoneFungibleToken(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'slug',
        'overall_rarity',
        'base_rarity',
        'body_rarity',
        'hair_rarity',
        'top_rarity',
        'pants_rarity',
        'prop_rarity',
        'bling_rarity',
        )
    readonly_fields = ('slug', )

