from app.app import *
from app.assets import user

@app.get('/')
def get_home():
    return render_template("home.html")

