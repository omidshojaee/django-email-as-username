# Introduction

By default, Django's User model uses **Username** as the primary identifier for authentication and **Email** is optional.
To change that, we need to:

- Subclass `BaseUserManager` (models.py)
- Create custom `User Model` (models.py)
- Substitue `User Model` (settings.py)
- Customize `Admin site` (admin.py)
---
# Warning

You need to do this **BEFORE FIRST MIGRATION**. Switching user model in the middle of the project generates lots of errors and you have to modify previous migrations of **User** model manually and apply them again.
