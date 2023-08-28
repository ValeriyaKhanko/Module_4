from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.utils import timezone
from django.contrib.auth import get_user_model


User = get_user_model()


class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    prise = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateField('Дата создания', auto_now_add=True)
    updated_at = models.DateField('Дата изменения', auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField('Изображение', upload_to='advertisements/', null=True, blank=True)

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at == timezone.now().date():
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', self.created_at)
        return self.created_at
    
    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.created_at == timezone.now().date():
            return format_html(
                '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', self.created_at)
        return self.created_at

    @admin.display(description='Фото')
    def html_image(self):
        if self.image:
            return format_html(
                '<img src="{url}" style="max-width: 80px; max-height: 80px;"', url=self.image.url
            )
        return self.created_at

    def __str__(self):
        return f"Advertsementi(id={self.id}, title={self.title}, prise={self.prise})"
    
    class Meta:
        db_table = "advertisements"