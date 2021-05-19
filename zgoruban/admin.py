from django.contrib import admin
from zgoruban.models import*

class blogimgModel(admin.StackedInline):
    model = CAMPparticipants

class blogModel(admin.ModelAdmin):
    inlines = [blogimgModel]

admin.site.register(demo_images)
admin.site.register(Go_Ruban_Motive)
admin.site.register(Camps,blogModel)
admin.site.register(About)
admin.site.register(Team)
admin.site.register(GALLERY)
admin.site.register(BLOGS)
admin.site.register(TESTIMONY)
admin.site.register(EVENTSS)
admin.site.register(NEWSS)
admin.site.register(BANNER_ABOUT)
admin.site.register(BANNER_CAMPS)
admin.site.register(BANNER_ANANTMANDI)
admin.site.register(BANNER_STORE)
admin.site.register(EMAIL_LETTERS)
admin.site.register(Oppurtunities)
admin.site.register(TERMS_CONDITIONSs)
admin.site.register(PRIVACY_POLICYs)
admin.site.register(PAYMENT_PROCEDUREs)
admin.site.register(Contact)
admin.site.register(EMIMG)