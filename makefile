copyfiles:
	cp $(filepath) .

run-two-towers:
	python3 towers.py $(input) $(output)

list-two-towers:
	ls towers.py

show-two-towers:
	@echo 'Showing python file towers.py'
	cat towers.py
