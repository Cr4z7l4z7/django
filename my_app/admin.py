from django.contrib import admin
from my_app.models import Topic, AccessRecord, WebPage, User

admin.site.register(Topic)
admin.site.register(WebPage)
admin.site.register(AccessRecord)
admin.site.register(User)


# Register your models here.
