from django.db import models

SKILL_LEVEL = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

PROJECT_TAGS = (
    ('Jogos', 'jogos'),
    ('web', 'web'),
    ('FrontEnd', 'frontend'),
    ('BackEnd', 'backend'),
    ('Data Base', 'db'),
    ('Python', 'python'),
    ('C#', 'csharp'),
    ('Unity', 'unity')
)


# Home Model
class Gabriel(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    picture = models.ImageField(upload_to='picture/')
    #save last modified
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


# skills and levels
class Skills(models.Model):
    skillName = models.CharField(max_length=30)
    level = models.CharField(default='1', max_length=1, choices=SKILL_LEVEL)
    skillLevelDescription = models.CharField(max_length=100)
    skillIcon = models.ImageField(upload_to='picture/')

    def __str__(self):
        return self.skillName


class Profile(models.Model):
    about = models.ForeignKey(Gabriel, on_delete=models.CASCADE)
    Icon = models.ImageField(upload_to='picture/')
    social_name = models.CharField(max_length=10)
    link = models.URLField(max_length=200)



class Portifolio(models.Model):
    projectName = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='portifolio/')
    link = models.URLField(max_length=200)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return f'Project {self.projectName}'