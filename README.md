### installation
```
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ sudo setcap 'cap_net_raw,cap_net_admin+eip' env/lib/python3.7/site-packages/$ bluepy/bluepy-helper
$ copy .env.template .env
$ vim .env
```

### execution
```
$ python3 main.py
```