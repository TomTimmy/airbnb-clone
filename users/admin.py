from django.contrib import admin
from . import models  # ? from . 뜻: admin.py 즉, 지금 이 파일이 있는 폴더에서...


@admin.register(models.User)  # ! Decorator 는 이렇게 calss 위에 써야 작동한다.
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    list_display = ("username", "gender", "language", "currency", "superhost")
    list_filter = ("superhost", "language")


# admin.site.register(models.User, CustomUserAdmin)
