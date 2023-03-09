from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Модель пользователя."""
    currency = models.PositiveIntegerField('Баланс валюты', default=0)
    count_test = models.PositiveIntegerField(
        'Количество пройденных тестов',
        default=0,
    )

    class Meta:
        ordering = ('-count_test',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Transaction(models.Model):
    """Модель проведенных транзакций."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField('Количество транзакций', default=0)
    created_at = models.DateTimeField('Дата транзакции', auto_now_add=True)


class Test(models.Model):
    """Модель тестов."""
    title = models.CharField('Оглавнение теста', max_length=256, unique=True)
    description = models.TextField('Описание теста')
    slug = models.SlugField('Слаг', unique=True)
    create_date = models.DateTimeField('Дата создания', auto_now_add=True)
    change_date = models.DateTimeField('Дата изменения', auto_now=True)

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'

    def __str__(self):
        return self.title


class Question(models.Model):
    """Модель вопросов."""
    test = models.ForeignKey(
        Test,
        on_delete=models.DO_NOTHING,
        related_name='question',
    )
    text = models.CharField('Текст вопроса', max_length=256)
    correct_answer = models.CharField('Правильный ответ', max_length=256)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.text


class Choice(models.Model):
    """Модель вариантов ответа."""
    question = models.ForeignKey(
        Question,
        on_delete=models.DO_NOTHING,
        related_name='choice',
    )
    text = models.CharField('Текст варианта ответа', max_length=256)

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'

    def __str__(self):
        return self.text


class Color(models.Model):
    """Модель цветов."""
    user = models.ManyToManyField(
        User, related_name='color',
        verbose_name='Цвета'
    )
    name = models.CharField(max_length=256)
    price = models.PositiveIntegerField(
        'Цена',
        default=0,
    )
    rgb_code = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_available = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.name


# class Answer(models.Model):
#     """Модель ответа."""
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='answer',
#     )
#     question = models.ForeignKey(
#         Question,
#         on_delete=models.DO_NOTHING,
#         related_name='answer',
#     )
#     choice = models.ForeignKey(
#         Choice,
#         on_delete=models.DO_NOTHING,
#         related_name='answer',
#     )
#     date_create = models.DateTimeField('Дата создания', auto_now_add=True)
#     count_answers = models.PositiveIntegerField('Счетчик правильных', default=0)
#
#     class Meta:
#         verbose_name = 'Ответ пользователя'
#         verbose_name_plural = 'Ответы пользователя'
#
#     def __str__(self):
#         return self.choice.text
