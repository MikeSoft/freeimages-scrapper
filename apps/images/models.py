from django.db import models


class Search(models.Model):
    query = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    max_results = models.IntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Image(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ImageTag(models.Model):
    class Meta:
        verbose_name = "Image Tag"
        verbose_name_plural = "Image Tags"
        unique_together = ('image', 'tag')
        indexes = [
            models.Index(fields=['image', 'tag'])
        ]

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image.title} - {self.tag.name}"
