from flask import Flask
import random


app = Flask(__name__)
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]


@app.route("/")
def index():
    return f'<h1>Di halaman ini, kita akan mempelajari fakta tentang ketergantungan teknologi</h1>  <a href="/random_fact">View a random fact!</a>  <a href="/password_generator">Generate a random password!</a>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p> <a href="/">Go to main page</a>'

@app.route("/password_generator")
def genpass():
    elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""

    for i in range(10):
        password += random.choice(elements)

    return f'<p>{password}</p>  <a href="/">Go to main page</a>'

app.run(debug=True)