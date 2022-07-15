# flask_template

From what I have been able to determine, this is the most "proper" way to start a flask application, using the application factory.

I chose to set up environment variables from .flaskenv instead of Config objects as I do not want all of the information for differnet environments in a single location. Each environment will get its own file, which has been added to the .gitignore file. 
