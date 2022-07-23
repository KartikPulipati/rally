# Base Template for my django projects

### How to use this repository!
###### *This is done with Mac commands*

1. Make sure to have python installed in your computer
2. Click Use this template
3. Make your own repository using this
4. Make folder for this project and *cd* into it
5. Clone that repository into that folder(I personally use Github Desktop cause it is so much easier!)
```
git clone https://github.com/<Username>/<Name of Repo>.git>
```
6. Create a venv and activate it
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
7. Install all project dependencies
```
pip install -r requirements.txt
```
8. Be sure to add your own Secret Key and Email credentials in Settings.py
9. Create the database
```
python manage.py migrate
```
10. Create a superuser and fill out the prompts, the password will be blank(it is for security)
```
python manage.py createsuperuser
```

 
