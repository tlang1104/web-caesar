from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG']=True


form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
		<form action = "/" method = "post">
			Rotate by: 
			<input name ="rot" type ="text" value = 0>
			<br><br>
			<textarea name = "text" rows="4" cols="50">{0}</textarea>
			<br><br>
			<input type ="submit">
  
		</form>
    </body>
</html>
    """

@app.route("/")
def index():
    return form.format("")


@app.route("/",methods = ['POST'])
def encrypt():
    rotate= int(request.form['rot'])
    message=request.form['text']
    jumble=rotate_string(message,rotate)
    #return "<<h1>"+ jumble +"</h1>"
    return form.format(jumble)

if __name__=="__main__":
    app.run()