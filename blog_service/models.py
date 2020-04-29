import random
import time
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class Category(models.Model):
    name = models.CharField('类别', max_length=30)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('标签', max_length=16)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


def user_directory_path(_, filename):
    ext = filename.split('.')[-1]
    filename = time.strftime('%Y%m%d%H%M%S')
    filename = filename + '_%d' % random.randint(0, 100)
    filepath = 'Cover_map/' + time.strftime('%Y/%m/')
    return filepath + '{0}.{1}'.format(filename, ext)


class Blog(models.Model):
    title = models.CharField('标题', max_length=32)
    Cover_map = models.ImageField('封面', upload_to=user_directory_path, blank=True)
    author = models.CharField('作者', max_length=16)
    content = HTMLField()
    pub = models.DateTimeField('发布时间', auto_now_add=True)
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)  # 多对一（博客--类别）
    tag = models.ManyToManyField(Tag, verbose_name='标签')  # (多对多）
    views = models.PositiveIntegerField('阅读量', default=0)

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])


class Comment(models.Model):
    blog = models.ForeignKey(Blog, verbose_name='博客', on_delete=models.CASCADE)  # (博客--评论:一对多)
    name = models.CharField('昵称', max_length=16)
    email = models.EmailField('邮箱')
    content = models.CharField('内容', max_length=240)
    pub = models.DateTimeField('发布时间', auto_now_add=True)
    floor = models.PositiveIntegerField('楼层', default=0)

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content


class Custom(models.Model):
    name = models.CharField('变量名', max_length=28)
    values = models.CharField('内容', max_length=240)

    class Meta:
        verbose_name = "自定义变量"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
