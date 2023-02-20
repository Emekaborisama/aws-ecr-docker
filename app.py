#  this is a sample rest api script for testing


from flask import Flask,jsonify
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("TsinghuaAI/CPM-Generate")

model = AutoModelForCausalLM.from_pretrained("TsinghuaAI/CPM-Generate")
print(model)

app = Flask(__name__)



@app.route("/home")
def index():
  return("welcome to app")



if __name__ == '__main__':
    app.run(host= '0.0.0.0', port = 8000, debug=True)
