from flask import Flask, render_template, request, redirect, abort
from logging import getLogger, ERROR
from dotenv import load_dotenv

load_dotenv()

log = getLogger('werkzeug')
log.setLevel(ERROR)


app = Flask(__name__, template_folder="..\\templates", static_folder="..\\public")
