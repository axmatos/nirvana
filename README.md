# Nirvana Take Home Project

- Clone the project and `cd` into its folder
- Create a Python 3.10 virtual environment and activate it
- Install requirements (`pip install -r requirements.txt`)
- Check if the project is working (`./manage.py check`)
- Apply db migrations (`./manage.py migrate`)
- Run the test suite (`./manage.py test`)
- Run the dev server (`./manage.py runserver 9090`)
- Open the URL in your browser (http://127.0.0.1:9090/api/?member_id=1)

There are four available URL endpoints:

- http://127.0.0.1:9090/api1/?member_id=1
- http://127.0.0.1:9090/api2/?member_id=1
- http://127.0.0.1:9090/api3/?member_id=1
- http://127.0.0.1:9090/api/?member_id=1

The last URL returns the coalesced values from the other three according to the selected strategy. There are 3 available strategies and the average is used by default.
