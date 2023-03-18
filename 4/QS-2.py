'''the patient is stored in a list. The details of the medical specialities
 are stored in a dictionary as follows: {"p": "Pediatrics", "0": "Orthopedics", "E":"ENT}

Write a function to find the medical speciality visited by
the maximum number of patients and return the name of the speciality.

Note: 1.Assume that there is always only one medical speciality which
is visited by maximum number of patients. 2.
Perform case sensitive string comparison wherever necessary

[101,P,102,0,302,P,305,P]                              Pediatrics

[101,0,102,0,302, P, 305, E, 401,0,656,0]             ENT

[101,0,102, E, 302, P, 305, P, 401, E,656,0,987,E]    Orthopedics
'''
def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    P= patient_medical_speciality_list.count('P')
    E= patient_medical_speciality_list.count('O')
    O= patient_medical_speciality_list.count('E')
    if P>E and P>O:
        speciality = medical_speciality['P']
    elif E>O:
        speciality = medical_speciality['E']
    else:
        speciality = medical_speciality['O']
    return speciality
patient_medical_speciality_list=[101,"O",102, "P", 302, "P", 305, "P", 401, "E",656,0,987,"E"]
medical_speciality={"P": "Pediatrics", "O": "Orthopedics", "E":"ENT"}
print(max_visited_speciality(patient_medical_speciality_list,medical_speciality))
