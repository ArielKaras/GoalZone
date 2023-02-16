from flask import Flask
from landing_page.views.main import landing_page, register

app = Flask(__name__)
app.config.from_object('config')


app.add_url_rule('/', view_func=landing_page)
app.add_url_rule('/register', view_func=register, methods=['POST'])
