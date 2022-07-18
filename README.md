# flask_template

From what I have been able to determine, this is the most "proper" way to start a flask application, using the application factory.

I chose to set up environment variables from .flaskenv instead of Config objects as I do not want all of the information for differnet environments in a single location. Each environment will get its own file (.env, .flaskenv & settings.py), which has been added to the .gitignore file. 

Once the virtualenv is activated, Flask and python-dotenv will need to be installed for the this base iteration to work.

After the repo cloned to the desired location... 
- rename "env.txt" to ".env"
- rename "flaskenv.txt to ".flaskenv"
- rename "app/config-.py" to "app/config.py"
- rename "app/settings-.py" to "app/settings.py"

These adjustments were needed to get the files uploaded and part of the template. They are are hidden files and/or included in the .gitignore as they may contain sensitive information. 
