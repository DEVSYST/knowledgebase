##### There was an issue while 1st instalation of the buidout - explain the issue and describe steps

Buildout invalid  version of uwsgi==2.0.14 error (buildout build procecss failed)
Steps how to deal with the issue: 
* **clean install (optional in virtualenv)**
```
virtualenv env
source env/bin/activate
pip install zc.buildout
python bootstrap.py
.bin/buildout

```
