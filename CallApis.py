from flask import Flask, request,jsonify
from flask_restful import Resource, Api, reqparse
import requests
from json2xml import json2xml
from json2xml.utils import readfromurl, readfromstring, readfromjson
import json

app = Flask(__name__)
api = Api(app)


@api.representation('application/xml')
@app.get('/all')
def all_user():
   response = requests.get("https://reqres.in/api/users")
   print(request.headers.get('Content-Type'));
   print(response.status_code);
   print(response.json());
#   return response.json();
   if(request.headers.get('Content-Type')=='application/xml'):
      return json2xml.Json2xml(response.json()).to_xml();
   else:
      return response.json();   
      
      
@api.representation('application/xml')
@app.get('/single/<id>')
def single_user(id):
   response = requests.get("https://reqres.in/api/users/"+id)
   print(request.headers.get('Content-Type'));
   print(response.status_code);
   print(response.json());
#   return response.json();
   if(request.headers.get('Content-Type')=='application/xml'):
      return json2xml.Json2xml(response.json()).to_xml();
   else:
      return response.json();         
      
      
@api.representation('application/xml')
@app.post('/insert')
def insert_user():
   record = json.loads(request.data);   
   response = requests.post("https://reqres.in/api/users",json=record)
   print(request.headers.get('Content-Type'));
   print(response.status_code);
   print(response.json());
#   return response.json();
   if(request.headers.get('Content-Type')=='application/xml'):
      return json2xml.Json2xml(response.json()).to_xml();
   else:
      return response.json();               
   
   
@api.representation('application/xml')
@app.put('/update/<id>')
def update_user(id):
   record = json.loads(request.data);
   response = requests.put("https://reqres.in/api/users/"+id,json=record)
   print(request.headers.get('Content-Type'));
   print(response.status_code);
   print(response.json());
#   return response.json();
   if(request.headers.get('Content-Type')=='application/xml'):
      return json2xml.Json2xml(response.json()).to_xml();
   else:
      return response.json();            
      
      
@api.representation('application/xml')
@app.delete('/delete/<id>')
def delete_user(id):
   response = requests.delete("https://reqres.in/api/users/"+id)
   print(request.headers.get('Content-Type'));
   print(response.status_code);
   print(response.json());
#   return response.json();
   if(request.headers.get('Content-Type')=='application/xml'):
      return json2xml.Json2xml(response.json()).to_xml();
   else:
      return response;                  
   
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7271)  # run our Flask app