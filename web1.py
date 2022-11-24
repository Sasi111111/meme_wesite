from flask import Flask, render_template 
import requests
import json
app = Flask(__name__)
def meme():
      url = "https://meme-api.herokuapp.com/gimme"
      response = requests.get(url).text
      response1 = json.loads(response)
      subreddit=response1['subreddit']
      meme = response1['preview'][0]
      return subreddit,meme


@app.route("/")
def main():
    subreddit,meme_pic = meme()
    return render_template("index.html",meme=meme_pic)

if __name__ =="__main__":
    app.run(debug=True)