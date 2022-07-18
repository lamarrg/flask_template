# <app name> is most likely enclosing folder name
from app import create_app
from dotenv import load_dotenv

load_dotenv('.env')

app = create_app()  #Flask(__name__)

if __name__=="__main__":
    app.run()

