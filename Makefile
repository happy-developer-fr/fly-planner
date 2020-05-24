default: init test

init:
	pip install -r requirements.txt

test:
	pytest

freeze:
	pip freeze | grep -v "pkg-resources" > requirements.txt
