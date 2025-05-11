
# CRM-system for managers API (DRF)



## AUTH


I **SendActivationEmail**: sending an email to the user with a token to activate the account

II **ActivationManager**: allows the activation of a user's account

III **RecoveryPasswordRequest**: send a request to reset password

IV **RecoveryPassword**: resets the password using the token

## ORDERS

I **OrderList**: show all orders

II **GetMyOrders**: manager can review their own orders

III **UpdateOrder**: manager can update order by id

IV **GeneralOrdersStatistics**: admin can view general statistics on orders

V **OrderStatisticsByManager**: admin can view general statistics on orders by each manager


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
    
