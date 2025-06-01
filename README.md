
# CRM-system for managers API (DRF)



## AUTH


I **SendActivationEmail**: sending an email to the user with a token to activate the account

II **ActivationManager**: allows the activation of a user's account

III **RecoveryPasswordRequest**: send a request to reset password

IV **RecoveryPassword**: resets the password using the token

V **CrateActivationTokenForManager**: create activation token for manager


## ORDERS

I **OrderList**: show all orders

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
## Tools

![image](https://github.com/user-attachments/assets/df1e2918-97c2-4b6a-aa15-01d612065489)
![image](https://github.com/user-attachments/assets/f0ce8bfd-378f-4e5a-9acc-80051c7853a5)
![image](https://github.com/user-attachments/assets/67a9b7ab-c894-459b-af88-7493556eabce)
![image](https://github.com/user-attachments/assets/9b866fdd-6f74-4f6c-b5fb-1add118260f3)
![image](https://github.com/user-attachments/assets/d5315227-4dbe-452a-ad2d-8d11f6d0590d)
![image](https://github.com/user-attachments/assets/4a0efb83-40f9-4769-87ca-9aa9b836ed6e)






