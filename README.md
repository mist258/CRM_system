
# CRM-system for managers API (DRF)



## AUTH


I SendActivationEmail: sending an email to the user with a token to activate the account

II ActivationManager: allows the activation of a user's account

III RecoveryPasswordRequest: send a request to reset password

IV RecoveryPassword: resets the password using the token
## Orders

I OrderList: show all orders

II AssignedOrderToManager: manager can take the order to work 

III GetMyOrders: manager can review their own orders

IV CommentOrderCreate: manager can leave a comment under order

V CreateListGroup: create grooup or list all groups

VI RetrieveGroup: get order by id

VII UpdateOrder: manager can update order by id

VIII GeneralOrdersStatistics: admin can view general statistics on orders

IX OrderStatisticsByManager: admin can view general statistics on orders by each manager


## USERS

I ListCreateManager: create new user

II ManagerBan: blocks the Manager

III ManagerUnban: unlocks the Manager

IV  GetMe: get info about me (authenticated )


## Installation

Install project 

```bash
  https://github.com/mist258/CRM_system.git

  poetry install

  docker compose up --build 

  docker compose run --rm app sh

 ./manage.py makemigrations
 ./manage.py migrate
 ./manage.py createsuperuser

```
    
