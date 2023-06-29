# Starting from scratch

```shell
pip3 install django
django-admin startproject pyshop . # name the project as pyshop
python3 manage.py runserver
```

```shell
python3 manage.py startapp products # run another app and called it "products"
```

- register 'products.apps.ProductsConfig' in INSTALLED_APPS in pyshop/settings.py

```shell
python3 manage.py makemigrations
# run this command after creating a new class in products/models.py
# will generate products/migrations/0001_initial.py
```

```shell
python3 manage.py migrate
```

- add admin.site.register(Product) in products/admin.py to manage products

## Notes

- pyshop/urls.py: defining all routes
- products/urls.py: defining routes for /products
