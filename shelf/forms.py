from django import forms
from .models import Treasure, File_Treasure, Site_Style, Treasure_Ultra

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
        model = Site_Style
        fields = ('font_color','background_color', 'background_image',)

class Treasure_UltraForm(forms.ModelForm):
    class Meta:
        model = Treasure_Ultra
        fields = ('title','story','date_thrown_away','foreground_image','border_color','font_color','treasure_height','treasure_width', 'background_color', 'background_image',)



