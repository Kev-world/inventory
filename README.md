# Overview
Inventory is a sub-service that allow user to create a product and manage their inventory. It is connected via redis stream with another sub-service 'payment', when the user makes the order the payment service will push an event and our Inventory service will pick it up and 
update the inventory detail of the product.

## Features

-   [x] Create Product
-   [x] Query Products
-   [x] Query a Product
-   [x] Delete Product

## Endpoints

### Get Products

```bash
POST /products
```
#### Request Body
```json
{
    "name": "Gummt",
    "price": 20.0,
    "quantity": 25
}
```

#### Response

```json
{
    "pk": "01HK4JGGF59RNGVRJ14QXKCMWM",
    "name": "Gummt",
    "price": 20.0,
    "quantity": 25
}
```

```bash
GET /products
```
#### Response

```json
[
    {
        "id": "01HK445Y6TVJNHW242Q0NJSBDQ",
        "name": "Pluffy",
        "price": 20.0,
        "quantity": 5
    }
]
```

### Get Product by Primary Key

```bash
GET /products/{pk}
```
#### Param
```bash
pk: String
```
#### Response
```json
{
    "pk": "01HK4JGGF59RNGVRJ14QXKCMWM",
    "name": "Gummt",
    "price": 20.0,
    "quantity": 25
}
```

### Delete Product by Primary Key

```bash
Delete /products/{pk}
```
#### Param
```bash
pk: String
```
#### Response
```json
{
  1: 'Success',
  0: 'Fail'
}
```
