<h1>Description how to setup rpi.buildout project </h1>


<h2>Problem description:</h2>
Missing Python libraries

<h2>System prerequisites:</h2>
libraries: lxml, pyodbc 

<h2>Steps how to setup project:</h2>


1. clone repository rpi.buildout
2. checkout current branch
3. create virtualenv </br>
command: virtual [env_name] </br>
(creates isolated environment) </br>
then: source [env_name]/bin/activate </br>
4. pip install zc.buildout </br>
5. pyhon bootstrap.py
(create project structure)
6. ./bin/buildout
(build project dependencies)
7. ./bin/manage.py makemigrations </br>
./bin/manage.py migrate
