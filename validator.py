from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import json
import jwt
import re
import bcrypt
from . import common
from health_monitor import settings
from django.http import JsonResponse

def validate(data,rules):
	message = []
	temp = ""
	for rule in rules:
		column = rule
		rule = rules[rule].split("|")
		for r in rule:
			try:
				req_data = json.loads(data.decode(encoding='utf-8'))
				table = r.split(":")
				if table[0] == "exists":
					temp_column = column
					condition = table[1].split(",")
					table = condition[0]
					if len(condition) > 1:
						column = condition[1]

					for key in req_data:
						if key == temp_column:
							temp = req_data[temp_column]
					if not temp:
						message.append(['invalid field '+column])
						return (400,message)
					query = "SELECT * FROM "+table+" where "+column+" = '"+str(temp)+"'"
					user = common.fetchRows(query)
					if not user:
						message.append(["invalid "+str(column)+" in the "+table+" table"])
						return (400,message)
				elif table[0] == "email":
					pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
					for key in req_data:
						if key == column:
							temp = req_data[column]
					if not temp:
						message.append(['invalid field '+column])
						return (400,message)

					if not re.match(pattern,temp):
						message.append(["invalid email format"])
						return (400,message)

				elif table[0] == "required":
					temp = 0;
					for key in req_data:
						if key == column:
							temp = 1
					if temp == 0:
						message.append([column+" field is required"])
						return (400,message)

				elif table[0] == "required-imp":
					temp = "";
					for key in req_data:
						if key == column:
							temp = req_data[key]
					if temp == " " or not temp:
						message.append([column+" field is required"])
						return (400,message)

				elif table[0] == "numeric":
					for key in req_data:
						if key == column:
							temp = req_data[column]
					if not temp:
						message.append([column+" field is required"])
						return (400,message)

					else:
						temp = str(temp)
						if not temp.isdigit():
							message.append([column+" must be numeric"])
							return (400,message)

				elif table[0] == "unique":
					exclude_id = 0
					exclude_condition=""
					start_table = table
					condition = table[1].split(",")
					table = condition[0]
					if len(start_table)>2:
						x = start_table[2].split(",")
						if len(x)>1:
							if x[0] == "exclude":
								exclude_id = x[1]
					if len(condition) > 1:
						column = condition[1]
					for key in req_data:
						if key == column:
							temp = req_data[column]
					if not temp:
						message.append(['invalid field '+column])
						return (400,message)
					if exclude_id != 0:
						exclude_condition = " and id != "+str(exclude_id)

					query = "SELECT * FROM "+table+" where "+column+" = '"+str(temp)+"'"+exclude_condition
					user = common.fetchRows(query)
					if user:
						message.append([column+" already taken"])
						return (400,message)

				elif table[0] == "in":
					if req_data[column] not in table[1]:
						message.append([column+" must be in "+str(table[1])])
						return (400,message)

				elif table[0] == "min-len":
					print(table[1])
					
					if int(len(req_data[column])) <= int(table[1]):
						message.append([column+" length must be in minimum "+str(table[1])+" digits"])
						return (400,message)

				elif table[0] == "max-len":
					print(table[1])
					if int(len(req_data[column])) > int(table[1]):
						message.append([column+" length must be in less then "+str(table[1])+" digits"])
						return (400,message)

				elif table[0] == "min":
					if int(req_data[column]) < int(table[1]):
						message.append([column+" value must be in minimum "+str(table[1])])
						return (400,message)

				elif table[0] == "max":
					if int(req_data[column]) > int(table[1]):
						message.append([column+" value must be in less then "+str(table[1])])
						return (400,message)

			except Exception as e:
				return (400,e)
	return (200,'')