'''
Why Pydantic use ==> 1. Type validation
                     2. Data validation
'''



def insert_patient_data(name: str, age: int): 

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("Inserted into database")
    else:
        raise TypeError('Incorrect data type')

def update_patient_data(name: str, age: int): 

    if type(name)==str and type(age)==int:
        print(name)
        print(age)
        print("Update into database")
    else:
        raise TypeError('Incorrect data type')

insert_patient_data('Aditya', 12)
update_patient_data('Aditya', 12)