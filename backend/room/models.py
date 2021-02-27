import uuid

from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """ Team model. Expansion for User model """

    LEAGUES = (
        ('super', 'Super'),
        ('high', 'High'),
        ('first', 'First'),
        ('second', 'Second'),
        ('student', 'Student'),
    )
    GANDERS = (
        ('M', 'Male'),
        ('W', 'Women'),
    )

    user = models.OneToOneField(User, verbose_name="Власник профілю", on_delete=models.CASCADE, default=None)
    name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False,)
    league = models.CharField(max_length=7, choices=LEAGUES, default='super')
    gender = models.CharField(max_length=1, choices=GANDERS, default='M')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Player(models.Model):
    """ Team player """

    ROLES = (
        ('OS', 'Діагональний'),
        ('OH', 'Догравальний'),
        ('ST', 'Пасуючий'),
        ('MB', 'Центральний блокуючий'),
        ('LB', 'Ліберо'),
    )

    # team = models.ForeignKey(Team, verbose_name='Команда', default=None, on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, default=None)
    # team_id = models.PositiveIntegerField(verbose_name="ID Команди",  validators=[MaxValueValidator(99999)])
    number = models.PositiveIntegerField(verbose_name='Номер футболки', validators=[MaxValueValidator(99)], unique=True)
    first_name = models.CharField(verbose_name='Ім`я', max_length=64)
    last_name = models.CharField(verbose_name='Призвіще', max_length=64)
    middle_name = models.CharField(verbose_name='По-батькові', max_length=64)
    role = models.CharField(verbose_name='Амплуа', max_length=2, choices=ROLES, default='OS')
    birthday = models.DateField()
    weight = models.PositiveIntegerField(verbose_name='Вага',  validators=[MaxValueValidator(9999)])
    height = models.PositiveIntegerField(verbose_name='Висота в см',  validators=[MaxValueValidator(9999)])
    attack = models.PositiveIntegerField(verbose_name='Висота атаки',  validators=[MaxValueValidator(9999)])
    block = models.PositiveIntegerField(verbose_name='Висота блоку',  validators=[MaxValueValidator(9999)])
    born_at = models.CharField(verbose_name='Місце народження', max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_cap = models.BooleanField(default=False)
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    team_uuid = models.CharField(verbose_name="uuid команди", max_length=36, null=True)

    def __str__(self):
        return f'№ {self.number} {self.first_name}'


class Coach(models.Model):
    """ Тренер """
    #team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(verbose_name='Ім`я', max_length=64)
    last_name = models.CharField(verbose_name='Призвіще', max_length=64)
    middle_name = models.CharField(verbose_name='По-батькові', max_length=64)
    birthday = models.DateField()
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    born_at = models.CharField(verbose_name='Місце народження', max_length=255)
    phone = models.IntegerField(verbose_name="Номер телефону")
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    team_uuid = models.CharField(verbose_name="uuid команди", max_length=36, null=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.first_name, self.is_main

