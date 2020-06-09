from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField, HStoreField

# Create your models here.


class User(models.Model):
    

    username = models.CharField(verbose_name="用户名称", max_length=64)
    sex = models.BooleanField(verbose_name="性别", null=True)
    intro = models.CharField(verbose_name="签名", max_length=1024, null=True)
    avatar = models.CharField(verbose_name="头像URL", max_length=126)
    create_time = models.DateTimeField('创建时间', auto_now_add=True)

    class Meta:
        db_table = 'user'


class Story(models.Model):
    
    title = models.CharField(verbose_name="故事标题", max_length=126)
    song_name = models.CharField(verbose_name="歌曲名称", max_length=64)
    image_url = models.CharField(verbose_name="图片URL", max_length=126)
    content = JSONField(verbose_name="故事内容", default={})
    comment_num = models.IntegerField(verbose_name="评论数")
    like_num = models.IntegerField(verbose_name="点赞数")
    view_num = models.IntegerField(verbose_name="浏览数")
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    user = models.ForeignKey(User, null=True, verbose_name=u"创建人", on_delete=models.CASCADE)

    class Meta:
        db_table = 'story'
