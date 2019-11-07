# Django_Validations_Like_Laravel-

## How to use
```bash
  from xyz import validator
```

dejango validation which is similar to laravel rule validation
```bash
  #example required
        rules={
            "equipment_type":"required",
            "status":"required",
            "receiver_email":"required-imp",
            "repeat_time":"required"
        }
        validation = validator.validate(request.body,rules)
```
in above example required means it will accept null but variable should exist . required-imp means it will not accept nulls
#example Unique
```bash
        rules={
                "type":"required-imp|unique:Boxes,type",
                "count":"required-imp|numeric",
        }
validation = validator.validate(request.body,rules)
```

#example Unique excluding given id
```bash
        rules={
                "id":"required-imp|exists:Boxes",
                "type":"required-imp|unique:Boxes,type:exclude,"+str(req_data['id']),
                "count":"required-imp|numeric"
        }
        validation = validator.validate(request.body,rules)
```
#example min and max values
```bash
        rules={
                "mobile_number":"required-imp|unique:Sims|min:6000000000|max:9999999999",
        }
        validation = validator.validate(request.body,rules)
```
here min and max are number ranges not lengths for strings

#example min and max lengths
```bash
        rules={
                "name":"required-imp|unique:DeviceType,DeviceType",
                "equip_type":"required-imp|min-len:2|max-len:3",
                "equipment_name":"required-imp"
        }
        validation = validator.validate(request.body,rules)
```
#example for IN
```bash
        rules={
                "status":"required|in:['pending']"
        }
        validation = validator.validate(request.body,rules)
```
This is used check wheather item exstis in given values or not

