version:
	@printf "Currently using executable: python\n"
	python --version

venv:
	[ -d .venv ] || python -m venv .venv
	@printf "Now activate the Python virtual environment.\n"
	@printf "On Unix and Mac, do:\n"
	@printf ". .venv/bin/activate\n"
	@printf "On Windows (bash terminal), do:\n"
	@printf ". .venv/Scripts/activate\n"
	@printf "Type 'deactivate' to deactivate.\n

install:
	python -m pip install -r requirements.txt

installed:
	python -m pip list

clean:
	@$(call MESSAGE,$@)
	rm -f .coverage *.pyc
	rm -rf __pycache__
	rm -rf htmlcov

clean-doc: clean
	@$(call MESSAGE,$@)
	rm -rf doc

clean-all: clean clean-doc
	@$(call MESSAGE,$@)
	rm -rf .venv

pylint:
	@$(call MESSAGE,$@)
	python -m pylint *.py

flake8:
	@$(call MESSAGE,$@)
	-flake8

lint: flake8 pylint


black:
	@$(call MESSAGE,$@)
	 python -m black Pig/ test/

codestyle: black

unittest:
	@$(call MESSAGE,$@)
	 python -m unittest test/test_*

coverage:
	@$(call MESSAGE,$@)
	coverage run -m unittest test/test_*
	coverage html
	coverage report -m

test: lint coverage

