# Django_Validations_Like_Laravel-

## How to use
```bash
  from validator import PayloadValidation
```

## Validation examples
dejango validation which is similar to laravel rule validation
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
in above example required means it will accept null but variable should exist . required-imp means it will not accept nulls
#example Unique
```bash
        rules={
                "type":"required-imp|unique:Boxes,type",
                "count":"required-imp|numeric",
        }
      validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```

#example Unique excluding given id
```bash
        rules={
                "id":"required-imp|exists:Boxes",
                "type":"required-imp|unique:Boxes,type:exclude,"+str(req_data['id']),
                "count":"required-imp|numeric"
        }
        validation = PayloadValidation.validate(request.data, rules)
        if not validation[0]:
            response = [validation[1]]
            raise ValidationError(response)
```
#example min and max values
```bash
        rules={
                "mobile_number":"required-imp|unique:Sims|min:6000000000|max:9999999999",
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
                "name":"required-imp|unique:DeviceType,DeviceType",
                "equip_type":"required-imp|min-len:2|max-len:3",
                "equipment_name":"required-imp"
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
This is used check wheather item exstis in given values or not

