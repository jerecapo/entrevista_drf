# entrevista_drf
Repo para entrevista DRF

----
## Login - Get Token:

URL:
http://jeremiascuta.pythonanywhere.com/token/

METHOD: POST

BODY:
{
    "username": "entrevista",
    "password": "fefe2020"
}

----

## GET ALL PRODUCTS:
URLS:
http://jeremiascuta.pythonanywhere.com/core/products/

METHOD: GET

HEADER:
Authorization: jwt [LoginToken]

----

## GET A PRODUCT:
URLS:
http://jeremiascuta.pythonanywhere.com/core/products/[PRODUCT_ID]/

METHOD: GET

HEADER:
Authorization: jwt [LoginToken]

----

## CREATE PRODUCT:
URLS:
http://jeremiascuta.pythonanywhere.com/core/products/

METHOD: POST

BODY:
{
    "name": "prueba",
    "price": 12.35,
    "stock": 10
}

HEADER:
Authorization: jwt [LoginToken]

----

## UPDATE A PRODUCT:
URLS:
http://jeremiascuta.pythonanywhere.com/core/products/[PRODUCT_ID]/

METHOD: PUT

BODY:
{
    "name": "prueba",
    "price": 12.35,
    "stock": 10
}

HEADER:
Authorization: jwt [LoginToken]

----

## UPDATE STOCK PRODUCT:
URLS:
http://jeremiascuta.pythonanywhere.com/core/products/[PRODUCT_ID]/stock

METHOD: PUT

BODY:
{
    "stock": 5
}

HEADER:
Authorization: jwt [LoginToken]

----

## DELETE PRODUCT:

URL:
http://jeremiascuta.pythonanywhere.com/core/products/[PRODUCT_ID]/

METHOD: DELETE

HEADER:
Authorization: jwt [LoginToken]

----

## GET ALL ORDERS:

URL:
http://jeremiascuta.pythonanywhere.com/core/orders/

METHOD: GET

HEADER:
Authorization: jwt [LoginToken]

----

## GET A ORDER:

URL:
http://jeremiascuta.pythonanywhere.com/core/orders/[ORDER_ID]/

METHOD: GET

HEADER:
Authorization: jwt [LoginToken]

----

## CREATE A ORDER:

URL:
http://jeremiascuta.pythonanywhere.com/core/orders/

METHOD: POST

BODY:
[
    {
        "quantity": 11,
        "product": 1
    }
]

HEADER:
Authorization: jwt [LoginToken]

----

## UPDATE A ORDER:

URL:
http://jeremiascuta.pythonanywhere.com/core/orders/[ORDER_ID]/

METHOD: PUT

BODY:
[
    {
        "quantity": 11,
        "product": 1
    }
]

HEADER:
Authorization: jwt [LoginToken]

----

## DELETE A ORDER:

URL:
http://jeremiascuta.pythonanywhere.com/core/orders/[ORDER_ID]/

METHOD: DELETE

HEADER:
Authorization: jwt [LoginToken]

