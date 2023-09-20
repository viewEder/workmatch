from django.contrib import admin
from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts

# Register your models here.
admin.site.register(Academy)
admin.site.register(ProjectDev)
admin.site.register(Skills)
admin.site.register(Stack)
admin.site.register(EmploymentHistory)
admin.site.register(HobbiesExtras)
admin.site.register(Facts)

