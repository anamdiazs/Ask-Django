from django.contrib import admin
from .models import *

admin.site.register(Usuario)
admin.site.register(Categories)
admin.site.register(create_question)
admin.site.register(create_answer)

# Register your models here.
