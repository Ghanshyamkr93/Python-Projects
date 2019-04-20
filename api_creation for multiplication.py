# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:55:18 2019

@author: ghans_000
"""
import time
from flask import Flask
app = Flask(__name__)

@app.route('/<float:x>')
def table(x):
    
        a="" 
        for i in range(1,11):
            time.sleep()
            b = x*i
            mul = "{} X {} = {}<br> ".format(i,x,b)
            a=a+mul  
        return a
    



if __name__ == "__main__":
    app.run()
