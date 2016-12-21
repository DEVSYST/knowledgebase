<h1>Steps:</h1>

1. clone repository rpi.buildout
2. checkout current branch
3. create virtualenv </br>
command: virtual [env_name] </br>
(creates isolated environment) </br>
then: source [env_name]/bin/activate </br>
4. pip install zc.buildout </br>
   pip install lxml
5. pyhon bootstrap.py
(create project structure)
6. ./bin/buildout
(build project dependencies)
7. ./bin/manage.py makemigrations </br>
./bin/manage.py migrate
