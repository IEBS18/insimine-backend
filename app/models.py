from django.db import models

# Create your models here.

# class Blog(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     image = models.ImageField(upload_to='blog_images/',null=True,blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
def content_block_image_upload_to(instance, filename):
    if instance.blog:
        return os.path.join('blog_images/', filename)
    elif instance.case_study:
        return os.path.join('case_study_images/', filename)
    return os.path.join('other_images/', filename)

class Blog(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CaseStudy(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ContentBlock(models.Model):
    TEXT = 'text'
    IMAGE = 'image'

    BLOCK_TYPE_CHOICES = [
        (TEXT, 'Text'),
        (IMAGE, 'Image'),
    ]

    blog = models.ForeignKey(Blog, related_name='content_blocks', on_delete=models.CASCADE, null=True, blank=True)
    case_study = models.ForeignKey(CaseStudy, related_name='content_blocks', on_delete=models.CASCADE, null=True, blank=True)
    block_type = models.CharField(max_length=10, choices=BLOCK_TYPE_CHOICES)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=content_block_image_upload_to, null=True, blank=True)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.blog.title if self.blog else self.case_study.title} - {self.get_block_type_display()}'


class FormData(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    country = models.CharField(max_length=30,default='USA')
    # additional_info = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class TechStack(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='tech_images/', null=True, blank=True)

    def __str__(self):
        return self.name

class WhitePaper(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='whitepaper_images/', null=True, blank=True)
    description = models.TextField()
    pdf = models.FileField(upload_to='whitepapers/', null=True, blank=True)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='client_images/', null=True, blank=True)

    def __str__(self):
        return self.name
