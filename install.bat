@echo off
echo Creating python environment...
python -m venv venv

echo Entering python environment...
call venv/Scripts/activate

echo Installing requirements...
pip install setuptools wheel
pip install -r requirements.txt

echo Building mod2win...
rm -rf build/* && python setup.py sdist bdist_wheel && python setup.py build && python setup.py install && python setup.py develop

echo Cleanup...
scrub
@echo on
