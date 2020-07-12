from app import app
import os
from selenium import webdriver
from flask import render_template

## Variable definitions


@app.route("/")
def index():
    app_name = os.getenv("APP_NAME")

    if app_name:
        return f"Hello from {app_name} running in a Docker container behind Nginx!"

    return "Hello from Flask"

