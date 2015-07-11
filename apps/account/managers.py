from django.contrib.auth.models import UserManager


class AuthUserManager(UserManager):

    def create_user(self, username, first_name,  password=None, place=None, lat=None, lng=None):
        # self._validate_unique()
        user = super(AuthUserManager, self).create_user(username=username, password=password, **{
            'first_name': first_name,
            'lat': lat,
            'lng': lng,
        })
        return user
  
    def create_superuser(self, username, password, email):
        user = super(AuthUserManager, self).create_superuser(username, email, password)
        user.save(using=self._db)
        return user

    def _validate_unique(self, email, username):
        self._check_unique_email(email)
        self._check_unique_username(username)

    def _check_unique_email(self, email):
        try:
          self.get_queryset().get(email=email)
          raise ValueError("This email is already registered")
        except self.model.DoesNotExist:
          return True

    def _check_unique_username(self, username):
        try:
          self.get_queryset().get(username=username)
          raise ValueError("Mobile is already taken. Please try another.")
        except self.model.DoesNotExist:
          return True
