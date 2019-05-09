# kredivo_python

## POST /api/contact

*Request(application/x-www-form-urlencoded):*
```bash
{
  "phone_number": "08123232",
  "name": "Test",
  "email": "email@mail.com",
  "photo": "photo.jpg"
}
```
*Response:*

```bash
{
  "id": 1,
  "phone_number": "08123232",
  "name": "Test",
  "email": "email@mail.com",
  "photo": "photo.jpg"
}
```

## GET /api/contacts

*Response:*

```bash
[
  {
    "id": 1,
    "phone_number": "08123232",
    "name": "Test",
    "email": "email@mail.com",
    "photo": "photo.jpg"
  },
  {
    "id": 2,
    "phone_number": "08123232",
    "name": "Test2",
    "email": "email2@mail.com",
    "photo": "photo2.jpg"
  }
]
```


## GET /api/contact/1

*Response:*

```bash
{
  "id": 1,
  "phone_number": "08123232",
  "name": "Test",
  "email": "email@mail.com",
  "photo": "photo.jpg"
}
```


## PUT /api/contact/1

*Request(application/x-www-form-urlencoded):*
```bash
{
  "phone_number": "08123232",
  "name": "Test123",
  "email": "email123@mail.com",
  "photo": "photo.jpg"
}
```
*Response:*

```bash
{
  "id": 1,
  "phone_number": "08123232",
  "name": "Test123",
  "email": "email123@mail.com",
  "photo": "photo.jpg"
}
```


## DELETE /api/contact/1
*Response:*

```bash
Has been deleted
```
