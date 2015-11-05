PROJECT=rechan

develop: setup-git
	pip install -r requirements.txt

setup-git:
	git config branch.autosetuprebase always
	cd .git/hooks && ln -sf ../../hooks/* ./

install-test-requirements:
	pip install -r requirements.txt

test: install-test-requirements test-python
