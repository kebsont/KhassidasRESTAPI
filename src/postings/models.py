from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse as api_reverse
from django.db.models.signals import post_save
from django.utils.translation import ugettext as _
import subprocess

# Create your models here.
class KhassidaPost(models.Model):
    # pk aka id --> numbers
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title       = models.CharField(max_length=120, null=True, blank=True)
    file        = models.FileField(blank=False,null=False)
    coverImage  = models.ImageField(upload_to = 'media/cover/',blank = True,null = True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.file)

    def save(self):
        thumbnail = "media/cover/%s.png" % (self.timestamp,)
        self.thumbnail = thumbnail
        super(KhassidaPost, self).save()


    @property
    def owner(self):
        return self.user

    # def get_absolute_url(self):
    #     return reverse("api-postings:post-rud", kwargs={'pk': self.pk}) '/api/postings/1/'

    def get_api_url(self, request=None):
        return api_reverse("api-postings:post-rud", kwargs={'pk': self.pk}, request=request)

    # What to do after a PDF is saved
def book_post_save(sender, instance=False, **kwargs):
    """This post save function creates a thumbnail for the commentary PDF"""
    pdf = KhassidaPost.objects.get(pk=instance.pk)
    command = "convert -quality 95 -thumbnail 100 %s/%s[0] %s/cover/%s.png" % (settings.MEDIA_ROOT, pdf.file, settings.MEDIA_ROOT, pdf.file)
    # command = "convert -thumbnail 222 RapportSI.pdf[0] testQ.png"
    # params = ['convert', '-thumbnail 300 -resize 100x100', 'RapportSI.pdf', 'thumb.jpg']
    # subprocess.check_call(params)

    proc = subprocess.Popen(command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout_value,stderr_value = proc.communicate()
    print(stdout_value)
    print(stderr_value)

# Hook up the signal
post_save.connect(book_post_save, sender=KhassidaPost)
