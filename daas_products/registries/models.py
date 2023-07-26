from django.db import models

class Salutation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class EducationLevel(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Specialisation(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='zones')

    class Meta:
        unique_together = ('name', 'region',)

    def __str__(self):
        return self.name


class Woreda(models.Model):
    name = models.CharField(max_length=255)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name='woredas')

    class Meta:
        unique_together = ('name', 'zone',)

    def __str__(self):
        return self.name


class Kebele(models.Model):
    name = models.CharField(max_length=255)
    woreda = models.ForeignKey(Woreda, on_delete=models.CASCADE, related_name='kebeles')
    class Meta:
        unique_together = ('name', 'woreda',)

    def __str__(self):
        return self.name


class DevelopmentAgent(models.Model):
    salutation = models.ForeignKey(Salutation, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    name = models.TextField()
    father_name = models.TextField()
    grand_father_name = models.TextField()
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    birth_month = models.IntegerField()
    birth_year = models.IntegerField()
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    phone_number = models.TextField()
    telegram_phone_number = models.TextField(null=True, blank=True)
    alternate_phone_number = models.TextField(null=True, blank=True)
    email = models.TextField()
    education_level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    specialization = models.TextField(null=True)
    specialization_other = models.TextField(null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    employment_month = models.IntegerField()
    employment_year = models.IntegerField()
    assignment_month = models.IntegerField()
    assignment_year = models.IntegerField()
    pension_number = models.TextField()
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    woreda = models.ForeignKey(Woreda, on_delete=models.SET_NULL, null=True, related_name='development_agents')
    kebele = models.ForeignKey(Kebele, on_delete=models.SET_NULL, null=True, related_name='development_agents')

    def __str__(self):
        return self.name


    class Meta:
        db_table = 'development_agent'

