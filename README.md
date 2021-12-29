# InstaWork Home Assignment

The following project implements a simple team member management application. It provides basic features such as, adding, editing and deleting a team member.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.txt.

```bash
pip install -r requirements.txt
```

## How to run the project

```bash
python manage.py runserver
```
Once the server starts, the application can be accessed at the following url: (http://127.0.0.1:8000/user/).

## Overview

The project implements the features of managing team members by providing functionalities of adding, editing and deleting a team member. This is implemented using Django's ModelForms to minimize boiler plate code

The landing page shows the list page which displays all the team members.

## Features
- Add a team member (basic form validations are implemented and advanced validations such as verifying email as an unique user identifier)
- Edit existing info of team member
- Delete a team member

-- The application has three pages : List page, add page, edit page.

The List page shows all the team members basic info , the number of team members, and if the team member is an admin or not. From this page , you can either edit the info of the team member by clicking the edit button or add a new team member.

When adding a user, the applications checks if the user already exists in the database by checking for the uniqueness of the email. 

The edit page will show the pre existing info of the member to make it easier for the user to edit information.

Deletion, addition and change of info -  all the three actions will take user back to list page.


------------
I have not focused too much on css and styling as it was written in the problem statement to focus more on the usage of Django and its functionalities. 
Since there is no login page to the application, its impossible to identify if the user logged in is an admin or regular , hence for now the user can delete any user. Future scope for the application would be to implement an authorization and authentication layer.
