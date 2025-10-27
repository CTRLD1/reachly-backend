from django.contrib import admin
from .models import Challenge, UserChallenge, Reflection

# Register your models here.
admin.site.register(Challenge)
admin.site.register(UserChallenge)
admin.site.register(Reflection)