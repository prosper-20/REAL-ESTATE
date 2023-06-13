from django.contrib.auth.base_user import BaseUserManager
import unicodedata

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_username(username)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def normalize_username(self, username):
        return (
            unicodedata.normalize("NFKC", username)
            if isinstance(username, str)
            else username
        )

    def create_staffuser(self, email, username, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            
            email,
            username,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


