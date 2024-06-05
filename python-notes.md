# Virtual Environments
## Basic commands 
- Create virtual environment: `python3 -m venv env` - where `env` is the name of the virtual environment (I think `env` as a name is standard)

- Activate virtual environmet: `source env/bin/activate`

- Deactivate virtual environment: `deactivate`

- List packages in virtual environment: `pip list`

- Install packages: `pip install requests` - installs requests package and each of its dependencies

- Save all required versions of packages for environment (eg to be used by someone else): `pip freeze > requirements.txt`

- Install packages from a file (eg you're that someone else now): `pip install -r requirements.txt`)

## Common Practices
- Create virtual environment in same folder as where the project exists

- Virtual environment folder created - don't put project files in there - only for storing things related to virtual environment

# Jupyter Notebook
- Install cli tool to work with jupyter notebooks: `pip install jupyter`

- Start localhost server session creating a jupyter notebook: `jupyter notebook`

- Convert jupyter notebook to python script: `jupyter nbconvert --to=script notebook-name.ipynb`

