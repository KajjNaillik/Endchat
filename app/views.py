from app import app
from flask import Flask, render_template, request, redirect, flash, jsonify
from app import controller as ctl
import json

@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
def     route_index():
    return render_template("index.html", title="SALUT")
