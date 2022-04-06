from django.contrib import admin
from .models import Blogmodel,commentmodel,Profile

admin.site.register(Blogmodel)
admin.site.register(commentmodel)
admin.site.register(Profile)
