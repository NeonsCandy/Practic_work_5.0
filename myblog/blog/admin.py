from django.contrib import admin
from .models import Post

@admin.register(Post)  # Використовуємо декоратор для реєстрації
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status'] # Поля, що відображаються у списку [cite: 229]
    list_filter = ['status', 'created', 'publish', 'author']     # Додає фільтрацію [cite: 230]
    search_fields = ['title', 'body']                          # Додає поле пошуку [cite: 231]
    prepopulated_fields = {'slug': ('title',)}                 # Автоматично заповнює slug з title [cite: 232]
    raw_id_fields = ['author']                               # Покращує вибір автора [cite: 233]
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']