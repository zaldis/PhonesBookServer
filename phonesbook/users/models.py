from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import Count


class UserManager(BaseUserManager):
    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.annotate(_contacts_count = Count('contacts'))
        return qs


class User(AbstractUser):
    objects = UserManager()

    @property
    def contacts_count(self) -> int:
        # return self.contacts.count()
        return self._contacts_count

