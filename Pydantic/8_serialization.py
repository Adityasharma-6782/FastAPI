from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str 
    pin: str

class Patient(BaseModel):
    name: str
    gender: str
    age: int
    address: Address



address_dict = {'city': "jaipur", "state": "RAJ", 'pin': '1234'}

address1 = Address(**address_dict)

patient_dict = {'name': "Aditya", 'gender': 'Male', 'age': 20, 'address': address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump()  # export in the form of dictionary
temp = patient1.model_dump(include=['name'])  # export only name in dictionary
# include ==> for export in dict
# exclude ==> for not export in dict

temp = patient1.model_dump(exclude={'adress':['city']})  # not export only city in dictionary
temp = patient1.model_dump_json()  # export in the form of json
print(temp)
print(type(temp))


# exclude_unset=True  ==> read self by you