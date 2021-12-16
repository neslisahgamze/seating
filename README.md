# Seating Algorithm

  

**# Getting Started**

  

- First clone the repository from Github and switch to the new directory:

  

`$ git clone git@github.com:neslisahgamze/seating.git`

`$ cd ticket`

  

### Run with virtualenv

  

- Activate the [virtualenv](https://docs.python.org/3/library/venv.html) for your project.

- Install project dependencies:

	`$ pip install -r requirements.txt`

- Then simply apply the migrations:

	`$ python manage.py migrate`

- You can now run the development server:

	`$ python manage.py runserver`

- You can create a superuser:

	`$ python manage.py createsuperuser`

  
### Run with Docker

The projects' Makefiles should provide the following commands, if applicable:

  

 - ### `make build`

	  Building your app.

- ### `make up`

  	Up the containers

- ### `make start`
	Run the program.

- ### `make down`
	Kill all container.

- ### `make migrate`

  	Run all migrations.

 - ### `make makemigrations`

  	Run makemigrations for the app.

 - ### `test`

  	Run all tests.
