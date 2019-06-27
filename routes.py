from app import app2
@app.route('/')
@app.route('/index')
def index():
 user={'username':'Muskaan'}
return '''
<html>
<head>
<title>homepage-microblog</title>
</head>
<body>
<h1>Hello,'''+user['username']+'''!<h11>
</body>
<html>'''
