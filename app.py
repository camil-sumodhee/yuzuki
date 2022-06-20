from flask import Flask, render_template, send_from_directory, url_for
import os

app = Flask(__name__, static_folder='static')

# WEBSITE_HOSTNAME exists only in production environment
if not 'WEBSITE_HOSTNAME' in os.environ:
   # local development, where we'll use environment variables
   print("Loading config.development and environment variables from .env file.")
   app.config.from_object('azureproject.development')
else:
   # production
   print("Loading config.production.")
   app.config.from_object('azureproject.production')


@app.route('/', methods=['GET'])
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/resultat/<id>', methods=['GET'])
def details(id):
   if id == "LRr7NFfJ4HTKGOhvfqCJURsW66s1txd339tIc1ueyhXYbNdcgOHd3bsTpu0HdefvuQHwkyjeUobDSsKiSgKEPYYRGzjG0L0k2suk":
      return render_template('result.html')
   else:
      return render_template('not_found.html')

if __name__ == '__main__':
   app.run()