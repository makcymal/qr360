# qr
## setup:
1. create vurtual environment

	`python -m venv venv`
	
2. acivate venv

	`.\venv\Scripts\activate`
	
3. install python requirements

	`pip install -r requirements.txt`
	
4. install npm requirements
	
	`cd frontend`
	`npm install`
	`cd ..`

5. run backend at localhost:8000

	`python backend/manage.py runserver`

6. run frontend at localhost:8080

	`npm run --prefix frontend serve`
