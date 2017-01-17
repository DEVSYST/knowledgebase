<h1>Description how to setup rpi.buildout project </h1>


<h2>Problem description:</h2>
Missing Python libraries

<h2>System prerequisites:</h2>
libraries: lxml, pyodbc 

<h2>Steps how to setup project:</h2>


1. clone repository rpi.buildout
2. checkout current branch
3. create virtualenv </br>
command: virtualenv [env_name] </br>
(creates isolated environment) </br>
then: source [env_name]/bin/activate </br>
4. pip install zc.buildout </br>
5. python bootstrap.py --setuptools-version=32
(create project structure)
6. ./bin/buildout
(build project dependencies)
7. ./bin/manage.py makemigrations </br>
./bin/manage.py migrate

Adding python exectuable to virtualenv enviroment
add2virtualenv omelette/
