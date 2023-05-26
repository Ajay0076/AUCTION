from django.contrib import admin
from .models import *



from django.contrib import admin
from .models import auction

from django.contrib import admin
from django.utils.html import mark_safe
from .models import auction

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_display', 'deadline', 'status', 'end')
    readonly_fields = ('image_display',)

    def image_display(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url.url}" width="100" height="100">')
        else:
            return '(No image)'

    image_display.short_description = 'Image'

admin.site.register(auction, AuctionAdmin)

from django.contrib import admin
from .models import Player

from django.contrib import admin
from django.utils.html import mark_safe
from .models import Player

class PlayerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobilenumber', 'currentclub', 'Age', 'position', 'base', 'image_display')
    readonly_fields = ('image_display',)

    def image_display(self, obj):
        if obj.image_url:
            return mark_safe(f'<img src="{obj.image_url.url}" width="100" height="100">')
        else:
            return '(No image)'

    image_display.short_description = 'Image'

admin.site.register(Player, PlayerAdmin)


from django.contrib import admin
from .models import Club

from django.contrib import admin
from django.utils.html import mark_safe
from .models import Club

class ClubAdmin(admin.ModelAdmin):
    list_display = ('clubname', 'email', 'contactNo', 'manager', 'place', 'logo_display')
    readonly_fields = ('logo_display',)

    def logo_display(self, obj):
        if obj.logo:
            return mark_safe(f'<img src="{obj.logo.url}" width="100" height="100">')
        else:
            return '(No logo)'

    logo_display.short_description = 'Logo'

admin.site.register(Club, ClubAdmin)


from django.contrib import admin
from .models import auctionreg

class AuctionRegAdmin(admin.ModelAdmin):
    list_display = ('auction', 'clubname', 'playername', 'status')

admin.site.register(auctionreg, AuctionRegAdmin)

from django.contrib import admin
from .models import bidplayer

class BidPlayerAdmin(admin.ModelAdmin):
    list_display = ('auction', 'clubname', 'playername', 'amount')

admin.site.register(bidplayer, BidPlayerAdmin)
from django.contrib import admin
from .models import Acceptdeal

class AcceptDealAdmin(admin.ModelAdmin):
    list_display = ('clubname', 'playername', 'status')

admin.site.register(Acceptdeal, AcceptDealAdmin)
