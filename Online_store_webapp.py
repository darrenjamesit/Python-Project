from flask import Flask, render_template, request
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Store_databse",
    user="postgres",
    password="hAv3eleFant77@%$"
)

