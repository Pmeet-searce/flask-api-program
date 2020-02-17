from flask import Flask,render_template,request
from flask import make_response,jsonify
import json
app=Flask(__name__)


f_read=open("employees.json","r")  
em=json.load(f_read)  

@app.route('/')
def hello():
    return render_template("index.htm")

@app.route("/employees", methods=["GET"])
def employees():
    f_read=open("employees.json","r")  
    em=json.load(f_read)  
    res = make_response(jsonify(em),200)
    f_read.close()
    return res


@app.route('/employees/<team>',methods=["POST"])
def create_employee(team):
    f_read=open("employees.json","r")  
    em=json.load(f_read) 
    req = request.get_json()
    
    if team in em:
        res = make_response(jsonify({"error":"Team already exists"}),400)
        f_read.close()
        return res
    else:
        em.update({team:req})
        res = make_response(jsonify({"message":"Team Created"}),201)
        f_write=open("employees.json","w")
        print(em)
        json.dump(em,f_write)
        f_write.close()
        f_read.close()
        return res
        
     
        
@app.route('/employees/<team>',methods=["PUT"])
def update_employee(team):
    f_read=open("employees.json","r")  
    em=json.load(f_read)  

    req = request.get_json()
    
    if team in em:
        em[team]=req
        res = make_response(jsonify({"message":"Team replaced"}),200)
        f_write=open("employees.json","w")
        json.dump(em,f_write)
        f_write.close()
        f_read.close()  
        return res
    em[team] = req
    res = make_response(jsonify({"message":"Team created"}),201)
    f_write=open("employees.json","w")
    json.dump(em,f_write)
    f_write.close()
    f_read.close()
    return res


@app.route('/employees/<team>',methods=["DELETE"])
def delete_employee(team):
    f_read=open("employees.json","r")  
    em=json.load(f_read)  

    if team in em:
        del em[team]
        res = make_response(jsonify({}),204)
        f_write=open("employees.json","w")
        json.dump(em,f_write)
        f_write.close()
        f_read.close()
        return res
    
    res = make_response(jsonify({"error":"Collection not found"}),404)
    f_read.close()
    return res