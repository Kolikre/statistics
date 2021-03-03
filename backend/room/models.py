import uuid
from django.contrib.postgres.fields import ArrayField

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

    # def __str__(self):
    #     return self.name


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
    zone = models.PositiveIntegerField(default=0, verbose_name='Зона на майданчику',  validators=[MaxValueValidator(18)], null=True)
    cof_attack = models.IntegerField(verbose_name='Коефіцієнт атаки', default=0)
    cof_block = models.IntegerField(verbose_name='Коефіцієнт блок', default=0)
    cof_set = models.IntegerField(verbose_name='Коефіцієнт передачі', default=0)
    cof_serve = models.IntegerField(verbose_name='Коефіцієнт подачі', default=0)
    cof_dig = models.IntegerField(verbose_name='Коефіцієнт прийому', default=0)
    cof_rc = models.IntegerField(verbose_name='Прийом ідеал', default=0)
    total_attack = models.PositiveIntegerField(verbose_name='Кількість атак за матч', default=0)
    total_block = models.PositiveIntegerField(verbose_name='Кількість блоків за матч', default=0)
    total_set = models.PositiveIntegerField(verbose_name='Кількість передач за матч', default=0)
    total_serve = models.PositiveIntegerField(verbose_name='Кількість подач за матч', default=0)
    total_dig = models.PositiveIntegerField(verbose_name='Кількість прийомів за матч', default=0)
    total_rc = models.PositiveIntegerField(verbose_name='Кількість ідеальних прийомів за матч', default=0)


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
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    born_at = models.CharField(verbose_name='Місце народження', max_length=255)
    phone = models.IntegerField(verbose_name="Номер телефону")
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    team_uuid = models.CharField(verbose_name="uuid команди", max_length=36, null=True)

    def __str__(self):
        return self.first_name


class Game(models.Model):
    """ Модель гри """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, null=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True)
    players = models.ManyToManyField(Player, verbose_name="Гравці", null=True)
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    opponent_name = models.CharField(verbose_name="Назва команди суперника", max_length=255, null=True)
    # action = models.CharField(verbose_name="Дія ", max_length=255, null=True)


class Set(models.Model):
    """ Модель партії """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    game = models.ForeignKey(Game, verbose_name="Модель гри", on_delete=models.CASCADE, null=True)
    team_points = models.PositiveIntegerField(default=0, verbose_name='Очки команд',
                                              validators=[MaxValueValidator(150)])
    opponent_points = models.PositiveIntegerField(default=0, verbose_name='Очки суперника',
                                                  validators=[MaxValueValidator(150)])
    number = models.PositiveIntegerField(verbose_name='Номер партії', default=0)


class Action(models.Model):
    """ Модель дії гравця """

    ACTIONS = (
        ('set+', 'Пас +'),
        ('set/', 'Пас в ігрі'),
        ('set-', 'Пас -'),
        ('serve+', 'Подача +'),
        ('serve/', 'Подача в ігрі'),
        ('serve-', 'Подача -'),
        ('attack+', 'Атака +'),
        ('attack/', 'Атака в ігрі'),
        ('attack-', 'Атака -'),
        ('rc+', 'Доводка +'),
        ('rc/', 'Доводка в ігрі'),
        ('rc-', 'Доводка -'),
        ('LB', 'Прийом +'),
        ('LB', 'Прийом в ігрі'),
        ('LB', 'Прийом -'),
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, null=True)
    set = models.ForeignKey(Set, verbose_name="Партія", on_delete=models.CASCADE, null=True)
    player = models.PositiveIntegerField(verbose_name="гравець", validators=[MaxValueValidator(150)], null=True)
    eavent = models.CharField(verbose_name='Подія', max_length=7, choices=ACTIONS, null=True)
