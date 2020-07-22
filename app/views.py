from app import app
from flask import render_template, request, redirect, flash, url_for, session, logging
from passlib.hash import sha256_crypt
from flask_mysqldb import MySQL

mysql = MySQL(app)



@app.route('/')
def index():
    return 'Public View'

