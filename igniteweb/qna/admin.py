from django.contrib import admin
from .models import question_bank,hint
# Register your models here.

admin.site.register(question_bank)
admin.site.register(hint)
