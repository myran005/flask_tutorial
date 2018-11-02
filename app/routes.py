from app import app

@app.route('/')
@app.route('/index')
def index():
    users = {'username' : 'Scott' }
    return f'''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1> Hello, {users['username']}!</h1>
    </body>
</html>

'''

