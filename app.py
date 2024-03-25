#!/usr/bin/env python
# coding: utf-8

# In[3]:


from flask import Flask,render_template,request

import google.generativeai as palm
import replicate
import os

os.environ["REPLICATE_API_TOKEN"]="787f515cb0624813736c11e7fefec66473394f02"

palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
defaults = { 'model': "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/palm",methods=["GET","POST"])
def palm():
    return(render_template("palm.html"))

@app.route("/mj",methods=["GET","POST"])
def mj():
    return(render_template("mj.html"))

@app.route("/musicgen",methods=["GET","POST"])
def musicgen():
    return(render_template("musicgen.html"))

@app.route("/zeroscope",methods=["GET","POST"])
def zeroscope():
    return(render_template("zeroscope.html"))

@app.route("/result_palm",methods=["GET","POST"])
def result_palm():
    q = request.form.get("q")
    import google.generativeai as palm
    r = palm.chat(**defaults,messages=q)
    return(render_template("result_palm.html",r=r.last))

@app.route("/result_mj",methods=["GET","POST"])
def result_mj():
    q = request.form.get("q")
    r = replicate.run(
        "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
        input={
        "prompt": q,
        }
    )
    return(render_template("result_mj.html",r=r[0]))

@app.route("/result_musicgen",methods=["GET","POST"])
def result_musicgen():
    q = request.form.get("q")
    r = replicate.run(
        "meta/musicgen:7be0f12c54a8d033a0fbd14418c9af98962da9a86f5ff7811f9b3423a1f0b7d7",
        input={
        "prompt": q,
        "duration": 1,
        }
    )
    return(render_template("result_musicgen.html",r=r))

@app.route("/result_zeroscope",methods=["GET","POST"])
def result_zeroscope():
    q = request.form.get("q")
    r = replicate.run(
        "anotherjesse/zeroscope-v2-xl:9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351",
        input={
        "prompt": q,
        "num_frames": 4,
        }
    )
    return(render_template("result_zeroscope.html",r=r[0]))

@app.route("/end",methods=["GET","POST"])
def end():
    print("end")
    return(render_template("end.html"))

if __name__ == "__main__":
    app.run()


# In[ ]:




