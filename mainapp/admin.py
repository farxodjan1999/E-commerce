from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin


from .models import *

class SmartphoneAdminForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if not instance.sd:
            self.fields['sd_volume'].widget.attrs.update({
                'readonly': True, 'style': 'background: grey'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume'] = None
        return self.cleaned_data


# class NotebookAdminForm(ModelForm):
#
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['image'].help_text = mark_safe('<span style="color:red; font-size:14px;">Загружайте изображениея с минимальным разрешением {}x{}</span>'.format(
#                 *Product.MIN_RESOLUTION
#             )
#         )
#
#     def clean_image(self):
#         image = self.cleaned_data['image']
#         img = Image.open(image)
#         min_height, min_width = Product.MIN_RESOLUTION
#         max_height, max_width = Product.MAX_RESOLUTION
#         if image.size > Product.MAX_IMAGE_SIZE:
#             raise ValidationError('Размер изображения не должен превышать 3 МВ!')
#         if img.height < min_height or img.width < min_width:
#             raise ValidationError('Разрешение изображения меньше минимального!')
#         if img.height > max_height or img.width > max_width:
#             raise ValidationError('Разрешение изображения больше максимального!')
#         return image



class NotebookAdmin(admin.ModelAdmin):

    # form = NotebookAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebook'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

    change_form_template = 'mainapp/admin.html'
    form = SmartphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphone'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)




