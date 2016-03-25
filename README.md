## import
`python manage.py --file-xml /tmp/test.xml`

## DEV
```bash
pep8 --max-line-length=120 --exclude=migrations .
```

## install
```bash
pip install git+https://github.com/vir-mir/test_kudago
```

add `settings.py`
```python
INSTALLED_APPS = [
    ....
    'test_kudago_import'
]
```

```bash
python manage.py migrate
```