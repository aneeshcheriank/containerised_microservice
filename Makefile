install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
	python -m textblob.download_corpora

test:
	python -m pytest -vv --cov=nlplogic test_corenlp.py
	# --cov specify the root folder for 

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test