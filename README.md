
# CRM-system for managers API (DRF)



## AUTH


I **SendActivationEmail**: sending an email to the user with a token to activate the account

II **ActivationManager**: allows the activation of a user's account

III **RecoveryPasswordRequest**: send a request to reset password

IV **RecoveryPassword**: resets the password using the token

V **CrateActivationTokenForManager**: create activation token for manager


## ORDERS

I **OrderViewSet**: 
- show all orders (/api/orders/list/)
- show order by specific id (/api/orders/list/1/)
- export filtered (or non filtered) orders to excel file (/api/orders/list/export_to_excel/)

II **UpdateOrder**: manager can update order by id

III **GeneralOrdersStatistics**: admin can view general statistics on orders

IV **OrderStatisticsByManager**: admin can view general statistics on orders by each manager


## USERS

I **ListCreateManager**: create new user

II **ManagerBan**: blocks the Manager

III **ManagerUnban**: unlocks the Manager

IV  **GetMe**: get info about me (authenticated )


## GROUPS

I **CreateListGroup**: create grooup or list all groups

II **RetrieveGroup**: get order by id


## COMMENTS

I **CommentOrderCreate**: manager can leave a comment under order


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






