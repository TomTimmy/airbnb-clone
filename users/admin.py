from django.contrib import admin
from . import models  # ? from . 뜻: admin.py 즉, 지금 이 파일이 있는 폴더에서...


@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass
