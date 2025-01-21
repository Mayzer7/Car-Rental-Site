from django.contrib import admin
# from carts.admin import CartTabAdmin
# from orders.admin import OrderTabulareAdmin

from users.models import User

# admin.site.register(User) - нельзя внести изменения в админку, поэтому плохой способ регистрации. Ниже прописан более гибкий способ

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "email",]
    search_fields = ["username", "first_name", "last_name", "email",]

    # inlines = [CartTabAdmin, OrderTabulareAdmin, ]