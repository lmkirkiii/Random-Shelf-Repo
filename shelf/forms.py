from django import forms
from .models import Treasure, File_Treasure, Site_Style

class TreasureForm(forms.ModelForm):

    class Meta:
        model = Treasure
        fields = ('title', 'img_url', 'description',)

class File_TreasureForm(forms.ModelForm):
    class Meta:
        model = File_Treasure
        fields = ('title','description', 'file_path',)

class Site_StyleForm(forms.ModelForm):
    class Meta:
        model = Site_StyleForm
        fields = ('font_color','background_color', 'background_image',)