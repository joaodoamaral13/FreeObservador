from flask import Flask, request
from observador import getArticle as getArticle


app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():

    return "FreeObservador"

@app.route("/getarticle", methods = ["GET"])
def getarticle():


    if request.method == "GET":

        url = request.args.get("url")
        
        if url != "":
            article = getArticle(url)

            if article == "":
                article = "Não foi possivel buscar o artigo"
        else:
            article = "Não foi possivel buscar o artigo"

        return article 



if __name__ == '__main__':
    app.run()