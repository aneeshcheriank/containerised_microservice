install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=nlplogic test_corenlp.py
	# --cov specify the root folder for 

format:
	black *.py src/*.py

lint:
	pylint --disable=R,C *.py

all: install lint test