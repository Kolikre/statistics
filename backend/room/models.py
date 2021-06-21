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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,)
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
    number = models.PositiveIntegerField(null=True, verbose_name='Номер футболки', validators=[MaxValueValidator(99)], unique=True)
    first_name = models.CharField(null=True, verbose_name='Ім`я', max_length=64)
    last_name = models.CharField(null=True, verbose_name='Призвіще', max_length=64)
    middle_name = models.CharField(null=True, verbose_name='По-батькові', max_length=64)
    role = models.CharField(null=True, verbose_name='Амплуа', max_length=2, choices=ROLES, default='OS')
    birthday = models.DateField(null=True)
    weight = models.PositiveIntegerField(null=True, verbose_name='Вага',  validators=[MaxValueValidator(9999)])
    height = models.PositiveIntegerField(null=True, verbose_name='Висота в см',  validators=[MaxValueValidator(9999)])
    attack = models.PositiveIntegerField(null=True, verbose_name='Висота атаки',  validators=[MaxValueValidator(9999)])
    block = models.PositiveIntegerField(null=True, verbose_name='Висота блоку',  validators=[MaxValueValidator(9999)])
    born_at = models.CharField(null=True, verbose_name='Місце народження', max_length=255)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True)
    is_cap = models.BooleanField(default=False)
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    team_uuid = models.CharField(verbose_name="uuid команди", max_length=36, null=True)
    zone = models.PositiveIntegerField(default=0, verbose_name='Зона на майданчику',  validators=[MaxValueValidator(18)], null=True)
    negative_attack = models.IntegerField(verbose_name='Коефіцієнт атаки', default=0)
    negative_block = models.IntegerField(verbose_name='Коефіцієнт блок', default=0)
    negative_set = models.IntegerField(verbose_name='Коефіцієнт передачі', default=0)
    negative_serve = models.IntegerField(verbose_name='Коефіцієнт подачі', default=0)
    negative_dig = models.IntegerField(verbose_name='Коефіцієнт прийому', default=0)
    negative_rc = models.IntegerField(verbose_name='Прийом ідеал', default=0)
    positive_attack = models.PositiveIntegerField(verbose_name='Кількість атак за матч', default=0)
    positive_block = models.PositiveIntegerField(verbose_name='Кількість блоків за матч', default=0)
    positive_set = models.PositiveIntegerField(verbose_name='Кількість передач за матч', default=0)
    positive_serve = models.PositiveIntegerField(verbose_name='Кількість подач за матч', default=0)
    positive_dig = models.PositiveIntegerField(verbose_name='Кількість прийомів за матч', default=0)
    positive_rc = models.PositiveIntegerField(verbose_name='Кількість ідеальних прийомів за матч', default=0)
    total_attack = models.PositiveIntegerField(verbose_name='Кількість атак за матч', default=0)
    total_block = models.PositiveIntegerField(verbose_name='Кількість блоків за матч', default=0)
    total_set = models.PositiveIntegerField(verbose_name='Кількість передач за матч', default=0)
    total_serve = models.PositiveIntegerField(verbose_name='Кількість подач за матч', default=0)
    total_dig = models.PositiveIntegerField(verbose_name='Кількість прийомів за матч', default=0)
    total_rc = models.PositiveIntegerField(verbose_name='Кількість ідеальних прийомів за матч', default=0)
    index_attack = models.IntegerField(verbose_name='Коефіцієнт атаки', default=0)
    index_block = models.IntegerField(verbose_name='Коефіцієнт блок', default=0)
    index_set = models.IntegerField(verbose_name='Коефіцієнт передачі', default=0)
    index_serve = models.IntegerField(verbose_name='Коефіцієнт подачі', default=0)
    index_dig = models.IntegerField(verbose_name='Коефіцієнт прийому', default=0)
    index_rc = models.IntegerField(verbose_name='Прийом ідеал', default=0)

    def __str__(self):
        return f'№ {self.number} {self.first_name}'


class Coach(models.Model):
    """ Тренер """

    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, null=True)
    first_name = models.CharField(verbose_name='Ім`я', max_length=64)
    last_name = models.CharField(verbose_name='Призвіще', max_length=64)
    middle_name = models.CharField(verbose_name='По-батькові', max_length=64)
    birthday = models.DateField()
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
        ('dig+', 'Прийом +'),
        ('dig/', 'Прийом в ігрі'),
        ('dig-', 'Прийом -'),
        ('team+', 'Забила команда'),
        ('team-', 'Командна помилка')
    )

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, verbose_name="Власник профілю", on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(auto_now_add=True, blank=True)
    team_name = models.CharField(verbose_name="Назва команди", max_length=255, null=True)
    opponent_name = models.CharField(verbose_name="Назва команди суперника", max_length=255, null=True)
    set_number = models.PositiveIntegerField(verbose_name='Номер партії',  validators=[MaxValueValidator(5)], default=1)
    team_points = models.IntegerField(verbose_name="Очки команди")
    opponent_points = models.IntegerField(verbose_name="Очки суперників")
    player_name = models.CharField(verbose_name="Ім`я гравця", max_length=64)
    player_uuid = models.CharField(verbose_name='uuid Гравця', max_length=64)
    action = models.CharField(max_length=7, choices=ACTIONS)
    action_time = models.DateTimeField(blank=True, null=True)
