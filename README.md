# JatYam_bookstore

## An django ecommerce app

**JatYam bookstore** is a bookstore that made from django

The project has some basic ecommerce features:

- Display products list
  - has two types of listing the products (nav-grid, nav-list)
- Cart (easy for user to trace what they want to buy)
  - cart saved in session
- Wishlist (allow user to trace the price of the product)
  - compare old price (when user put to wishlist) with new price
- Coupons system (admin can give discount to users with coupon code)

## Technolody Stack

- [Python](https://www.python.org/) 3.6.x / 3.7.x
- [Django Web Framework](https://www.djangoproject.com/) 2.2.x
- [PostgreSQL](https://www.postgresql.org/)
- [jQuery](https://api.jquery.com/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

### Get started:

Install python 3.7.x and PostgreSQL in your machine.

Install pipenv:

```bash
  pip install pipenv
```

cd to folder with /manage.py file, then install package from pipenv

```bash
  pipenv install --ignore-pipfile
```

create new database in your PostgreSQL, edit the settings.py in folder Jatyam_bookstore:

```python
  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': '{your-db-name}',
          'USER': '{your-db-user}',
          'PASSWORD': '{your-db-password}',
      }
  }
```

migrate model to database:

```bash
  python manage.py migrate
```
