# Introduction

By default, Django's User model uses **Username** as the primary identifier for authentication and **Email** is optional.
To change that, we need to:

- Create a custom `User Model` (models.py)
- Subclass `BaseUserManager` (models.py)
- Substitue `User Model` (settings.py)
- Customize `Admin site` (admin.py)
---
# Warning

You need to do this **BEFORE FIRST MIGRATION**. Switching user model in the middle of the project generates lots of errors and you have to modify all previous migrations manually and apply them again.
