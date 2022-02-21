from flask import Flask, request
from observador import getArticle as getArticle


app = Flask(__name__)

@app.route("/{url}", methods = ["GET"])
def getArt(url):


    if request.method == "GET":

        return getArticle(url)



if __name__ == '__main__':
    app.run()