from django.db import models
from django.forms import ModelForm

# Create your models here.
class update_book(models.Model):

    host = models.CharField(max_length=128, default='')
    local = models.CharField(max_length=128, default='')
    project = models.CharField(max_length=128)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now_add=True)
    patch_file = models.CharField(max_length=128)
    new_version = models.CharField(max_length=128, default='')
    last_version = models.CharField(max_length=128, default='')

    def __str__(self):
        return str(self.c_time)

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "发布工单"
        verbose_name_plural = "发布工单"


class host(models.Model):
    
    name = models.CharField(max_length=128, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now_add=True)
    ip = models.CharField(max_length=20, unique=True)
    host_local = models.ForeignKey('local', on_delete=models.CASCADE)
    ssh_user_name = models.CharField(max_length=30, default='')
    ssh_passwd = models.CharField(max_length=20, default='')
    ssh_port = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "主机"
        verbose_name_plural = "主机"

class project(models.Model):
    
    name = models.CharField(max_length=128, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now_add=True)
    alias_name = models.CharField(max_length=128, default='')
    release_version = models.CharField(max_length=128, unique=True)
    release_path = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "应用"
        verbose_name_plural = "应用"


class local(models.Model):
    
    name = models.CharField(max_length=128, unique=True)
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now_add=True)
    alias_name = models.CharField(max_length=128, default='')
    project = models.ManyToManyField(
        'project',
        through='local_project_ship',
        through_fields=('local_name', 'project_name'),
        )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["id"]
        verbose_name = "驻地"
        verbose_name_plural = "驻地"


class local_project_ship(models.Model):  # 这就是具体的中间表模型
    local_name = models.ForeignKey('local', on_delete=models.CASCADE)
    project_name = models.ForeignKey('project',on_delete=models.CASCADE)
    last_version = models.CharField(max_length=128)
    path = models.CharField(max_length=128)
    backup_path = models.CharField(max_length=128,default='')
    c_time = models.DateTimeField(auto_now_add=True)
    u_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.local_name)+str(self.project_name)

    class Meta:
        ordering = ["id"]
        verbose_name = "驻地项目关系"
        verbose_name_plural = "驻地项目关系"


class history_version(models.Model): 
    version = models.CharField(max_length=128, default='')
    local_project_ship =  models.ForeignKey('project',on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)
    local_project = models.CharField(max_length=128, default='')


    def __str__(self):
        return str(self.local_project)+str(self.version)

    class Meta:
        ordering = ["id"]
        verbose_name = "历史版本"
        verbose_name_plural = "历史版本"

class update_type(models.Model):
    kind = (
        ('hotfix',"热更新"),
        ('patch',"小版本"),
        ('package',"大版本")
    )
    update_type = models.CharField(max_length=10,choices=kind, default='hotfix')
    

    def __str__(self):
        return str(self.update_type )

    class Meta:
        ordering = ["id"]
        verbose_name = "发布类型"
        verbose_name_plural = "发布类型"


class localForm(ModelForm):
    class Meta:
        model = local
        fields = ['name']

class projectForm(ModelForm):
    class Meta:
        model = project
        fields = ['name','release_version','release_path']