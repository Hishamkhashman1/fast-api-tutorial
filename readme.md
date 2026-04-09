Instructions for Linx

Inititate a venv , I highly recommend doing it this way
 python3 -m venv venv
 source venv/bin/activate
 pip install fastapi uvicorn

To run app

 uvicorn main:app --reload

 terminal will indicate local server running app


curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'
curl -X GET http://127.0.0.1:8000/items/0
