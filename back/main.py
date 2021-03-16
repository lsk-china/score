import sys
sys.path.append("lib")
from lib.advpymysql.core.annotations import *
from lib.advpymysql.core.tools import setupConnection
from flask import Flask,request
from lib.pytools.pyLog import Logger
from lib.pytools.pyBases import *

app = Flask(__name__)
log = Logger("main",enableDebug=false)

def clacLevel(score):
	if 0 <= score <= 50:
		return "小萌新"
	elif 50 < score <= 100:
		return "初出茅庐"
	elif 100 < score <= 200:
		return "普通员工"
	elif 200 < score <= 300:
		return "高级员工"
	elif 300 < score <= 500:
		return "特级员工"
	elif 500 < score <= 1000:
		return "超级员工"
	elif 1000 < score <= 2000:
		return "专家程序员"
	elif 2000 < score <= 2500:
		return "小bug程序员"
	elif 2500 < score <= 3000:
		return "大bug程序员"
	elif 3000 < score <= 4000:
		return "员工长"
	elif 4000 < score <= 5000:
		return "副室长"
	else:
		return "秘书"

@Select("select * from table1 where name=#{name}")
def queryUserByName(name):
	pass
@Select("select * from table1 where id=#{id}")
def queryUserById(id):
	pass
@Update("update table1 set score=#{score},level=#{level} where id=#{id}")
def updateUser(score,level,id):
	pass
@Insert("insert into table1(name) values(#{name})")
def newUser(name):
	pass

@app.route("/queryUser",methods=["POST"])
def queryUser():
	name = request.values['username']
	log.debug(name)
	dbUser = queryUserByName(name)
	if not len(dbUser) == 1:
		return "User doesn't exists."
	user = dbUser[0]
	log.debug(user)
	return {
		"id": user[0],
		"name": user[1],
		"level": user[2],
		"score": user[3]
	}

@app.route("/incScore")
def incScore():
	id = int(request.values["id"])
	add = int(request.values["add"])
	dbUser = queryUserById(id)
	if not len(dbUser) == 1:
		return "User doesn't exists."
	user = dbUser[0]
	score = user[3]
	score += add
	level = clacLevel(score)
	log.debug(level)
	updateUser(score,level,id)
	return "Success"

@app.route("/addUser",methods=["POST"])
def addUser():
	name = request.values["name"]
	dbUser = queryUserByName(name)
	if not len(dbUser) == 0:
		return "User exists."
	newUser(name)
	return "Success"
@app.route("/decScore")
def decScore():
	id = int(request.values["id"])
	dec = int(request.values["dec"])
	dbUser = queryUserById(id)
	if not len(dbUser) == 1:
		return "User doesn't exists."
	user = dbUser[0]
	score = user[3]
	score -= dec
	level = clacLevel(score)
	log.debug(level)
	updateUser(score, level, id)
	return "Success"

if __name__ == "__main__":
	setupConnection("connection.properties")
	app.run(host='0.0.0.0')