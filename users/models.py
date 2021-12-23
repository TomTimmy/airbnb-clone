from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom User Model"""  # ? Doc String.

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),  # ? 첫번째 값 GENDER_MALE 는 database 로 갈꺼고,
        (GENDER_FEMALE, "Female"),  # ? 두번째 값 "Male" 은 admin 패널의 form 으로 갈꺼다.
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "kr"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "English"),
        (LANGUAGE_KOREAN, "Korean"),
    )

    CURRENCY_USD = "usd"
    CURRENCY_KRW = "krw"

    CURRENCY_CHOICES = (
        (CURRENCY_USD, "usd"),
        (CURRENCY_KRW, "krw"),
    )

    bio = models.TextField(
        default="", blank=True
    )  # ? bio 값이 비어있을때, database 가 기본적으로 대입할 값.
    # ? 또는, 비어있는 필드를 이용할 수도 있다. bio = models.TextField(null=True)
    # ! default OR null.

    avatar = models.ImageField(
        null=True, blank=True
    )  # ? null 은 database 가 사용하는 것이고, blank 는 form 이 사용하는 것이다.
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True
    )
    # ? TextField 와 CharField 의 차이점:
    # ?  TextField 는 글자수 제한이 없고, 줄이 여러개다.
    # ?  CharField 는 글자수 제한이 있고, 입력란이 한 줄이다.
    # ? 또한, CharField 는 약간의 수정(커스터마이징)도 가능하다!

    birthdate = models.DateField(null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, null=True, blank=True
    )
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, null=True, blank=True
    )
    superhost = models.BooleanField(default=False)


# # #? Inheritance(상속) 짧게 복습
# class Dog:s
#     legs = 4
#     eyes = 2


# class JindoDog(Dog):
#     color = "yellow"

# JindoDog.
