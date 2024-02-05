from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organisations(models.Model):
    name = models.CharField("название", max_length=255)
    director = models.ForeignKey(
        User, models.RESTRICT, "organisations_directors", verbose_name="Директор"
    )

    employees = models.ManyToManyField(
        User,
        "organisations_employees",
        verbose_name="Сотрудники",
        blank=True,
    )

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ("name",)
