from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения информации об авторе.
    """

    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    email = models.EmailField(max_length=50, verbose_name="Email")
    github_link = models.URLField(verbose_name="Github")
    resume_link = models.URLField(verbose_name="Резюме")

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    def __str__(self) -> str:
        return f'Автор (id={self.pk}) {self.get_full_name()}'

    def get_full_name(self) -> str:
        return f'{self.first_name} {self.last_name}'
