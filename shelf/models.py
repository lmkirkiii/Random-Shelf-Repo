from django.db import models


class Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    img_url = models.TextField()

    def __str__(self):
        return self.title


class File_Treasure(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    file_path = models.FileField(upload_to="documents/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Site_Style(models.Model):
    font_color = models.CharField(max_length=1000)
    background_color = models.CharField(max_length=1000)
    background_image = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.title

class Treasure_Ultra(models.Model):
    title = models.CharField(max_length=1000)
    story = models.CharField(max_length=1000)
    date_thrown_away = models.DateTimeField()
    foreground_image = models.TextField()
    border_color = models.CharField(max_length=1000)
    font_color = models.CharField(max_length=1000)
    treasure_height = models.CharField(max_length=1000)
    treasure_width = models.CharField(max_length=1000)
    background_color = models.CharField(max_length=1000)
    background_image = models.TextField()
    
    def __str__(self):
        return self.title