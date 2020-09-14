import re

def _validate_required(payload_variable, req_data, condition=""):
    temp = 0
    if payload_variable in req_data:
        temp = 1
    if temp == 0:
        message = "{} field is required".format(payload_variable)
        return False, message
    return True, "passed"


def _validate_required_imp(payload_variable, req_data, condition=""):
    temp = None
    if payload_variable in req_data:
        temp = req_data[payload_variable]
    if temp is None and not isinstance(temp, bool):
        message = "{} field is required".format(payload_variable)
        return False, message
    return True, "passed"


def _validate_numeric(payload_variable, req_data, condition=""):
    temp = None
    if payload_variable in req_data:
        temp = req_data[payload_variable]
    if temp is None and not isinstance(temp, bool):
        message = "{} field is required".format(payload_variable)
        return False, message
    else:
        temp = str(temp)
        if not temp.isdigit():
            message = "{} must be numeric".format(payload_variable)
            return False, message
    return True, "passed"


def _validate_in(payload_variable, req_data, condition):
    if req_data[payload_variable] not in condition:
        message = "{} must be in {}".format(payload_variable,str(condition))
        return False, message
    return True, "passed"


def _validate_min_len(payload_variable, req_data, condition):
    if int(len(req_data[payload_variable])) <= int(condition):
        message = "{} length must be in minimum {} digits".format(payload_variable,str(condition))
        return False, message
    return True, "passed"


def _validate_max_len(payload_variable, req_data, condition):
    if int(len(req_data[payload_variable])) > int(condition):
        message = "{} length must be in less then {} digits".format(payload_variable,str(condition))
        return False, message
    return True, "passed"


def _validate_min(payload_variable, req_data, condition):
    if int(req_data[payload_variable]) < int(condition):
        message = "{} value must be in minimum {}".format(payload_variable,str(condition))
        return False, message
    return True, "passed"


def _validate_max(payload_variable, req_data, condition):
    if int(req_data[payload_variable]) > int(condition):
        message = "{} value must be in less then {}".format(payload_variable,str(condition))
        return False, message
    return True, "passed"


def _validate_array(payload_variable, req_data, condition=""):
    if not isinstance(req_data[payload_variable], list):
        message = "{} should be an array".format(payload_variable)
        return False, message
    return True, "passed"


def _validate_boolean(payload_variable, req_data, condition=""):
    if not isinstance(req_data[payload_variable], bool):
        message = "{} should be an boolean".format(payload_variable)
        return False, message
    return True, "passed"


class PayloadValidation:
    def __init__(self):
        pass

    _get_validator_method = {
        "email": _validate_email,
        "required": _validate_required,
        "required-imp": _validate_required_imp,
        "in": _validate_in,
        "numeric": _validate_numeric,
        "min-len": _validate_min_len,
        "max-len": _validate_max_len,
        "min": _validate_min,
        "max": _validate_max,
        "array": _validate_array,
        "bool": _validate_boolean
    }

    @staticmethod
    def validate(data, rules):
        for rule in rules:
            payload_variable = rule
            rule = rules[rule].split("|")
            for r in rule:
                req_data = data
                condition = r.split(":")
                validation_function = PayloadValidation._get_validator_method[condition[0]]
                if callable(validation_function):
                    if len(condition) > 1:
                        response = validation_function(payload_variable, req_data, condition[1])
                    else:
                        response = validation_function(payload_variable, req_data, condition)
                    if not response[0]:
                        return response
                else:
                    return False, "no validation rule found"
        return True, 'success'
