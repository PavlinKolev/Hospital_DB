import os
from hospital_data_base import HospitalDB


def populate_hospital(hospital):
    if type(hospital) is not HospitalDB:
        raise TypeError("Type of hospitalital must be hospitalitalDB")

    hospital.add_doctor("Dr. Georgiev", "Georgiev1", 35, 'Allergist')  # id=1
    hospital.add_doctor("Dr. Slavcheva", "Slavcheva1", 34, 'Oncologist')  # id=2
    hospital.add_doctor("Dr. Radeva", "Radeva11", 45, 'Gynecologist')  # id=3
    hospital.add_doctor("Dr. Petrov", "Petrov11", 38, 'Pediatrician')  # id=4
    hospital.add_doctor("Dr. Martinov", "Martinov1", 29, 'Urologist')  # id=5

    hospital.add_patient("Rositsa", "Rositsa1", 20, 1)  # id=6
    hospital.add_patient("Ivanka", "Ivanka11", 25, 2)  # id=7
    hospital.add_patient("Pesho Georgiev", "Georgiev1", 19, 3)  # id=8
    hospital.add_patient("Bojko Petrov", "Petrov11", 22, 4)  # id=9
    hospital.add_patient("Petq Hristova", "Hristova1", 23, 5)  # id=10
    hospital.add_patient("Martin Georgiev", "Georgiev1", 20, 1)  # id=11
    hospital.add_patient("Baba Zlata", "BabaZlata1", 85, 2)  # id=12
    hospital.add_patient("Dqdo Ioco", "DqdoIoco1", 89, 3)  # id=13
    hospital.add_patient("Lelq Goshka", "LelqGoshka1", 45, 4)  # id=14
    hospital.add_patient("Bat Georgi", "BatGeorgi1", 28, 5)  # id=15

    hospital.add_hospital_stay("2016-12-16", 105, 6, "Cancer", "2016-12-20")
    hospital.add_hospital_stay("2017-01-05", 155, 7, "Leukemia", "2017-01-20")
    hospital.add_hospital_stay("2016-12-14", 222, 8, "Diabetes", "2016-12-22")
    hospital.add_hospital_stay("2016-12-15", 308, 9, "Eczema", "2017-01-10")
    hospital.add_hospital_stay("2016-12-23", 404, 10, "Epilepsy", "2016-12-27")
    hospital.add_hospital_stay("2016-12-16", 105, 11, "Cancer", "2016-12-26")
    hospital.add_hospital_stay("2016-12-22", 105, 12, "Leukemia", "2016-12-25")
    hospital.add_hospital_stay("2016-12-10", 222, 13, "Lupus", "2016-12-15")
    hospital.add_hospital_stay("2016-12-31", 777, 14, "Hepatitis", "2017-12-20")
    hospital.add_hospital_stay("2016-12-06", 355, 15, "Laryngitis", "2016-12-22")

    hospital.add_visitation(1, "2016-12-31 12:00")
    hospital.add_visitation(1, "2016-12-31 13:00")
    hospital.add_visitation(1, "2016-12-31 14:00")
    hospital.add_visitation(2, "2016-12-31 12:00")
    hospital.add_visitation(2, "2016-12-31 13:00")
    hospital.add_visitation(2, "2016-12-31 14:00")
    hospital.add_visitation(3, "2016-12-31 12:00")
    hospital.add_visitation(3, "2016-12-31 13:00")
    hospital.add_visitation(3, "2016-12-31 14:00")
    hospital.add_visitation(4, "2016-12-31 12:00")
    hospital.add_visitation(4, "2016-12-31 13:00")
    hospital.add_visitation(4, "2016-12-31 14:00")
    hospital.add_visitation(5, "2016-12-31 12:00")
    hospital.add_visitation(5, "2016-12-31 13:00")
    hospital.add_visitation(5, "2016-12-31 14:00")


def is_hospital_existing(hospital_name):
    file_path = os.getcwd() + '/' + hospital_name + '.db'
    if os.path.isfile(file_path):
        return True
    return False
