
# CRM-system for managers API (DRF)

**Python version** - 3.10

**Database** - PostgreSQL


## AUTH

**/api/auth**: login user (for registered users)

**/api/auth/refresh**: get refresh token 

**/api/auth/<int:pk>/email**: sending an email to the user with a token to activate the account (for superuser)

**/api/auth/activate/<str:token>**: activate manager's account (for superuser)

**/api/auth/managers/recovery_request**: send request email for recoovery password (for registered users)

**/api/auth/managers/change_password/<str:token>**: change password (for registered users)

**/api/auth/managers/<int:pk>/activation_token**: superuser can create activation token for users (for superuser)


## ORDERS

**/api/orders/list/**:  show all orders 

**/api/orders/list/1/**: show order by specific id

**/api/orders/list/orders_to_excel/**: export filtered (or non filtered) orders to excel file

**/api/orders/general_statistic**: statistic by orders

**/api/orders//<int:pk>/orders**:  manager can update order


## USERS

**/api/users/managers**: create new user

**/api/users/managers/<int:pk>/ban**: blocks the Manager

**/api/users/managers/<int:pk>/unban**: unlocks the Manager

**/api/useers/managers/info**: get info about me (authenticated )


## GROUPS

**/api/groups**: create grooup or list all groups

**/api/groups/<int:pk>**: get order by id


## COMMENTS

**/api/comments/<int:pk>/comments**: manager can leave a comment under order


## Installation

**Install project** 

```bash
  https://github.com/mist258/CRM_system.git

  poetry install

  docker compose up --build 

  docker compose run --rm app sh

 ./manage.py makemigrations
 ./manage.py migrate
 ./manage.py createsuperuser

```






