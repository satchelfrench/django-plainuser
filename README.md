# Django PlainUser

User login systems are a big part of most sites nowadays and django is a great framework for modern development, but sometimes you want a user to login with their email, or perhaps provide less information then required by the stock django user model.
Django-plainuser is a compliant user model that removes the bloat attributes of the stock user model. Requires only an email and password, provided as an abstract model to accommodate any customizations.

# Usage

This package is not available under PyPi, because it is assumed this will be wanted in the project folder and not the virtualenv installed packages folder.

* (1) Simply copy this repo into your applications directory.
* (2) Add to settings.py
* (3) Add AUTH_USER_MODEL
* (4) Reference the [django documentation](https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model).

# LICENSE

Open Source through BSD-3 (same as django)
