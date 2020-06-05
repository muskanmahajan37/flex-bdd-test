SHELL = bash.exe
run-test:
	source .env.test && pytest -s -v
