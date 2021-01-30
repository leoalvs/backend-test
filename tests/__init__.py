from mongoengine import connect

connect('mongoenginetest', host='mongomock://localhost', alias='default')