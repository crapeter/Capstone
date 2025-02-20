# TTU-CS-4366

An automatic TA/grader assignment system, given the instructor of each course and a group of TA/graders (some master’s graders (20 hrs per week) and some ph.d. TAs (10 hrs or 20 hrs per week) with their experiences and preferences

## Necessary Technologies

### Python

This project requirest python 3.x.x. If you do not have python installed you can go to this [website](https://www.python.org/downloads/).

### Creating the Virtual Environment

To create the venv you can copy and paste this command: `python -m venv venv`

After creating the virtual environment, you can run the following commands to activate the virtual environment.

- Windows

  `venv\Scripts\activate`

- Mac/Linux

  `source venv/vin/activate`

### Installing Dependecies

Run the following command to install dependencies from **_requirements.txt_**

`pip install -r requirements.txt`

### Environment Variables

After installing the requirements, the venv will have python-dotenv installed. Python-dotenv is used to create the environment variables used in this project, mainly the paths to the files. To create the environment variables create a `.env` file and then put the paths there, it should look like this `variable_name=path_to_file`.

To read the environment variables you will need to import the os package, `import os` and import the dotenv package, `from dotenv import load_dotenv` and add `load_dotenv()` to the top of your python file, but below the imports. After those have been added you can access the variables by inputing `os.getenv('variable_name')`

### Usage

After setting up the environment, you can run the project using:

`python main.py`
