import uuid

from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User


class Team(models.Model):
    """User profile"""

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

    user = models.OneToOneField(User, verbose_name="Власник профілю", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Назва команди", max_length=255)
    create_date = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    league = models.CharField(max_length=7, choices=LEAGUES, default='super')
    gender = models.CharField(max_length=1, choices=GANDERS, default='M')
    is_active = models.BooleanField(default=True)


class Player(models.Model):
    """ Team player """

    team = models.ForeignKey(Team, verbose_name='Команда', on_delete=models.CASCADE)
    number = models.PositiveIntegerField(verbose_name='Номер футболки', validators=[MaxValueValidator(99)])
    first_name = models.CharField(verbose_name='Ім`я', max_length=64)
    last_name = models.CharField(verbose_name='Призвіще', max_length=64)
    middle_name = models.CharField(verbose_name='По-батькові', max_length=64)
    birthday = models.DateField()
    weight = models.PositiveIntegerField(verbose_name='Вага',  validators=[MaxValueValidator(9999)])
    height = models.PositiveIntegerField(verbose_name='Висота в см',  validators=[MaxValueValidator(9999)])
    attack = models.PositiveIntegerField(verbose_name='Висота атаки',  validators=[MaxValueValidator(9999)])
    block = models.PositiveIntegerField(verbose_name='Висота блоку',  validators=[MaxValueValidator(9999)])
    born_at = models.CharField(verbose_name='Місце народження', max_length=255)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
