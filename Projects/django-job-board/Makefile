## The Makefile includes instructions on environment setup and lint tests
# Each "command" runs exactly in different shell, so chain commands using &&
# setup: Create and activate a virtual environment
# Install: install dependencies in requirements.txt
# Lint: Dockerfile should pass hadolint, any code.py should pass pylint
 
# Targets
  
setup:
	# Create python virtualenv using  python builtin 'venv' module
	python3 -m venv ./django-venv
install:
	# This should be run from inside a virtualenv
	. ./django-venv/bin/activate &&\
	pip install --upgrade pip &&\
	pip install -r requirements.txt &&\
	sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v2.12.0/hadolint-Linux-x86_64 &&\
	sudo chmod +x /bin/hadolint
lint:
	# See local hadolint install instructions:   https://github.com/hadolint/hadolint
	# linter for Dockerfiles
	# linter for Python source code linter: https://www.pylint.org/
	. ./django-venv/bin/activate &&\
	hadolint Dockerfile &&\
	pylint --disable=R,C,W0611,E0401,E0402,E0611 --fail-under=7 ./**/*.py 
	# Pylint fails only if the score under 7

test:
	# Run Unit tests on Job application
	. ./django-venv/bin/activate &&\
	python3 manage.py test job/
run:
	# Run django server in background
	. ./django-venv/bin/activate &&\
	python manage.py runserver 0.0.0.0:8080 &

all: install lint test
