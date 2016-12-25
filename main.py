from hospital_manager import HospitalManager


def main():
    hospital_name = input("hospital name:> ")
    hospital = HospitalManager(hospital_name)
    hospital.run_interface()


if __name__ == '__main__':
    main()
