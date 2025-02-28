
# CRM-system for managers API (DRF)



## AUTH


I SendActivationEmail: sending an email to the user with a token to activate the account

II ActivationManager: allows the activation of a user's account

III RecoveryPasswordRequest: send a request to reset password

IV RecoveryPassword: resets the password using the token
## Orders

I OrderList: show all orders
## USERS

I ListCreateManager: create new user

II ManagerBan: blocks the Manager

III ManagerUnban: unlocks the Manager


## Installation

Install project 

```bash
  https://github.com/mist258/CRM_system

  poetry install

  docker compose up --build 

  docker compose run --rm app sh

 ./manage.py makemigrations
 ./manage.py migrate
 ./manage.py createsuperuser

```
    
