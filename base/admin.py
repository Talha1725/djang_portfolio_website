from django.contrib import admin
from .models import Home,About,Profile,Category,Portfolio,Skills

# Register your models here.

#Home
admin.site.register(Home)

#Portfolio
admin.site.register(Portfolio)

#About
class Profile_inline(admin.TabularInline):
    model=Profile
    extra=1


@admin.register(About)
class About_Admin(admin.ModelAdmin):
    inlines=[
        Profile_inline,
        ]

#Skills
class Skilss_inline(admin.TabularInline):
    model=Skills
    extra = 2

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    inlines=[
        Skilss_inline,
    ]
