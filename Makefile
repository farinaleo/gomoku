run: venv/bin/activate
	./venv/bin/python3 main.py

setup: requirements/requirements.txt
	pip3 install -r requirements/requirements.txt

venv/bin/activate: requirements/requirements.txt
	python3 -m venv venv
	./venv/bin/pip install -r requirements/requirements.txt

clean:
	rm -rf venv
	rm -rf __pycache__

.PHONY: run setup clean
