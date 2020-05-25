default: init test lint

init:
	pip install -r requirements.txt

test:
	pytest

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt

flake8:
	flake8 flyplanner/

lint:
	pylint --rcfile standard.rc flyplanner/
