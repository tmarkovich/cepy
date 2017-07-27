.phony: test

PIP := pip
PY := python

FILES=cepy tests setup.py

help:
	@echo "    build-dep"
	@echo "         Builds all the python dependencies using pip via pip."
	@echo "    setup"
	@echo "         Installs cepy using the develop instruction"
	@echo "    test-style"
	@echo "         Check style with flake8."
	@echo "    test"
	@echo "         Run cepy tests including benchmarks"
	@echo "    tests"
	@echo "         Run all cepy tests, including doctests and coverage"
	@echo "    test-coverage"
	@echo "         Tests the unit-test coverage of the test-suite"
	@echo "    test-doc"
	@echo "         Checks for documentation build warnings"
	@echo "    test-doctest"
	@echo "         Runs the unit tests for the doctests"
	@echo "    clean-pyc"
	@echo "         Remove python artifacts."
	@echo "    clean-build"
	@echo "         Remove build artifacts."
	@echo "    clean"
	@echo "         Removes all build and python artifacts"
	@echo "     "
	@echo " VARIABLES: "
	@echo "         PY_VERSION    The version of python to use (2 or 3). Defaults to 2.7"
	@echo "         PY            Which python to use. Defaults to the one present in the virtualenv"
	@echo "         PIP           Which pip to use. Defaults to the one present in the python"

build-dep:
	$(PIP) install -r requirements.txt
	$(PIP) install -r requirements-test.txt

setup:
	$(PY) setup.py develop

test-style:
	find ${FILES} -type f -name \*.py -print0 | xargs -0 flake8

test-coverage:
	py.test -v --cov=cepy --benchmark-skip  tests/

test-doctest:
	# py.test fails if no tests are found, so uncomment when doctests exist
	# py.test --benchmark-skip --doctest-modules --ignore=setup.py cepy/

test-doc:
	sphinx-build -a -n -W -b html docs/ build/sphinx/html/

test:
	py.test -v --benchmark-skip tests/

benchmark:
	py.test --benchmark-only --benchmark-autosave tests/

benchmark-compare:
	py.test --benchmark-only --benchmark-autosave --benchmark-compare tests/

tests: test-style test-doctest test-coverage

clean-pyc:
	rm -f cepy/_cephes.{c,o,so}
	find ${FILES} -name '*.pyc' -exec rm -f {} +
	find ${FILES} -name '*.pyo' -exec rm -f {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info

clean: clean-build clean-pyc

all: clean build-dep setup tests

.DEFAULT_GOAL := all
