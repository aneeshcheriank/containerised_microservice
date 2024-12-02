install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=./src ./test/test_engine.py

format:
	black *.py src/*.py

lint:
	pylint --disable=R,C *.py

all: install format lint test