all: test

test:
	python3 -m doctest imbaedit/main.py

upload:
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*

clean:
	rm -rf imbaedit.egg-info
	rm -rf imbaedit/__pycache__
	rm -rf dist
	rm -rf build
	rm -rf setuptools
