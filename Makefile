clean:
	rm -rf venv

install:
	make clean
	virtualenv --python=python3.7 venv
	source venv/bin/activate && pip install -r requirements.txt

run:
	venv/bin/python3 -m service.app customer1.us.ca.sfo