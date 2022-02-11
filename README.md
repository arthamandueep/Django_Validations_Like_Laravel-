# Django_Validations_Like_Laravel-

## How to use
```bash
  from validator import PayloadValidation
```

## Validation examples
django validation which is similar to laravel rule validation
```bash
  #example required
        rules={
            "equipment_type":"required",
            "status":"required",
            "receiver_email":"required-imp",
            "repeat_time":"required"
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```
#example min and max values
```bash
        rules={
                "count":"required-imp|min:6000000000|max:9999999999",
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```
here min and max are number ranges not lengths for strings

#example min and max lengths
```bash
        rules={
                "string_title":"required-imp|min-len:2|max-len:3",
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```
#example for IN
```bash
        rules={
                "status":"required|in:['pending']"
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```

#example for Array validation
```bash
        rules={
                "ids":"required|array"
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```

#example for Boolean validation
```bash
        rules={
                "status":"required|bool"
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```
