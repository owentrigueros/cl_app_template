build:
	python setup.py build sdist

install: 
	find dist/ -name *.tar.gz -exec pip install --user {} \;

clean:
	rm -rf build/ dist/ *.egg-info/
