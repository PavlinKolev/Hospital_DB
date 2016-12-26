## Hospital Manager

On Wednesday we create a simple hospital database for patients, doctors and hospital stays.

But one hospital cannot be managed only with this information.

Our task for today is to create a working system, which can be used by both doctors and patients.

First we need a Base user, which will be inherited by the doctor and patient. Our user need to have username, password and age.

The hard part here is to create the relation between the different users.

#### Hint
Implement method, which will promote a baseuser to doctor or patient.

```python
def promote_to_doctor(baseuser):
    pass

def promote_to_patient(baseuser, doctor=None):
    pass
```

Doctors themselves need additional information, such as academic title.

For the patients we don't need more data, for now.

We have a table for the hospital stay with the information for the room, start and end date, injury and patient.

But the patients can come to the hospital on a visitation. For this reason we need new table, which will collect the data.

Each doctor can have several hours for visitations in one day. One hour is for one visitation, so we need to know the start hour of it.

Now its time to create add the new tables and try to keep the current data from database.

Once we have the whole schema done, we need to provide a good command line interface to our users.

#### Abilities of the users:

- Doctor:
  - Register
  - Log into the system
  - can list all of his/hers patients
  - can add hours for visitation
  - can delete free hours of visitation
  - has the ability to see the room and the duration of hospital stays per each of his patients

- Patient:
  - Register
  - Log into the system
  - can reserve hour for visitation
  - can see the free hours of his/hers doctor
  - can stay at the hospital for an injury
  - can see the academic title of his doctor

### Examples:

```
Welcome to Hospital Manager!
Choose:
1 to Log into the system,
2 to register as a new user,
3 for help main,
4 to exit the system.
```

#### Log in as a patient

```
> 1
> username:
Rositsa Zlateva
> Password:

Hi, Rositsa Zlateva,
You are a patient in Hospital Manager.
You have the abilities to:
1) see the free hours of your doctor
2) reserve hour for visitation
3) stay at the hospital for an injury
4) see the academic title of his doctor
5) list your hospital stays
6) change your doctor
7) change your username and/or age
8) log out
>
```

#### Log in as a doctor

```
> 1
> username:
Dr. Albena Bachvarova
> Password:

Hi, Dr. Albena Bachvarova,
You are a oncologist doctor in Hospital Manager.
You have the abilities to:
1) list all of your patients
2) add hours for visitation
3) delete free hours of visitation
4) see the room and the duration of hospital stays per each of your patients
5) change your username and/or age
6) raise into the hospital hierarchy
5) log out
>
```

#### Register as a doctor

```
> 2
> username:
Dr. Yordanka Yordanova
> password:

> password(again):

> age:
35
> academic title:
surgeon

Hi, Dr. Yordanka Yordanova,
You are a surgeon doctor in Hospital Manager.
You have the abilities to:
1) list all of your patients
2) add hours for visitation
3) delete free hours of visitation
4) see the room and the duration of hospital stays per each of your patients
5) change your username and/or age
6) raise into the hospital hierarchy
5) log out
>
```


#### Register as a patient

```
> 2
> username:
Mariq Ignatova
> password:

> password(again):

> age:
35
> choose a doctor to cure your diseases:
  1) Dr. Albena Bachvarova, oncologist
  2) Dr. Pavlina Zdravkova, surgeon
> 2

Hi, Mariq Ignatova,
You are a patient in Hospital Manager.
You have the abilities to:
1) see the free hours of your doctor
2) reserve hour for visitation
3) stay at the hospital for an injury
4) see the academic title of his doctor
5) list your hospital stays
6) change your doctor
7) change your username and/or age
8) log out
>
```

## Important

- Decide how to log in and out your users
- Validate user password!

  Password constraints:
   - At least one uppercase letter
   - At least one lowercase letter
   - One digit
   - Length greater than 7


- On registration hash the password!
- Hide the user password! (use `getpass` library)
- All settings in settings.py
- All queries in outer file
- If you have requirements, put them in requirement.txt

