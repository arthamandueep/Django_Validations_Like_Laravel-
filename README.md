# Django_Validations_Like_Laravel-
dejango validation which is similar to laravel rule validation
#example
```bash
        rules={
            "entity":"required",
            "airport":"required",
            "equipment_type":"required",
            "status":"required",
            "receiver_email":"required-imp",
            "repeat_time":"required"
        }
        validation = validator.validate(request.body,rules)
```
