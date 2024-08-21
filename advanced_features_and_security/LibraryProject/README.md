# Django Application - Groups and Permissions

## Overview
This Django application implements a detailed access control system using custom groups and permissions. This setup enhances the security and functionality of the application by restricting access to certain actions based on user roles.

## Custom Permissions
Custom permissions have been added to the `MyModel` model to control actions such as viewing, creating, editing, and deleting instances. These permissions are:

- `can_view`: Allows viewing instances of `MyModel`.
- `can_create`: Allows creating new instances of `MyModel`.
- `can_edit`: Allows editing existing instances of `MyModel`.
- `can_delete`: Allows deleting instances of `MyModel`.

### Adding Custom Permissions to Models
The following permissions were added in the `models.py` file:
```python
class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view", "Can view model"),
            ("can_create", "Can create model"),
            ("can_edit", "Can edit model"),
            ("can_delete", "Can delete model"),
        ]
