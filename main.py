# This is a sample Python script.
from flask import Flask, request, render_template
import requests, base64
from base64io import Base64IO
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""host1 = 'judge0-ce.p.rapidapi.com'
host2 = 'https://ce.judge0.com/authenticate'
myCode = "int main(){ std::cout >> 'a';return 0;}"
myCode2 = """"""#include <stdio.h> int main(void) {char name[10]; scanf("%s", name);printf("hello, %s\n", name); return 0;}"""
"""submission1 = {
    "language_id": 52,
    "source_code": myCode,
    "stdin": "SnVkZ2Uw",
    "expected_output": "a"
}
submission2 = {
    "language_id": 52,
    "source_code": myCode2,
    "stdin": "Judge0",
    "expected_output": "Judge0"
}
submission3 = {
    "language_id": 52,
    "source_code": myCode2,
    "stdin": "SnVkZ2Uw",
    "expected_output": "SnVkZ2Uw"
}
dats = {"submissions": [submission1, submission2, submission3]}

s_c = "I2luY2x1ZGUgPHN0ZGlvLmg+CgppbnQgbWFpbih2b2lkKSB7CiAgY2hhciBuYW1lWzEwXTsKICBzY2FuZigiJXMiLCBuYW1lKTsKICBwcmludGYoImhlbGxvLCAlc1xuIiwgbmFtZSk7CiAgcmV0dXJuIDA7Cn0="


app = Flask(__name__)

tok_n = '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7'
#resp1 = requests.post(host2, headers = {'X-Auth-Token': '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7', 'Authorization': '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7'})
resp2 = requests.request("POST", 'https://' + host1 + '/submissions/batch', headers = {'Content-Type': 'application/json', 'X-RapidAPI-Key': tok_n, 'X-RapidApi-Host': 'judge0-ce.p.rapidapi.com'}, json = dats, params = {"base64_encoded": "true"}).json()
#decision_token =  resp2['token'] #'1756b8c4-c565-42e2-bf60-290b60036be2'

print(resp2)

#resp3 = requests.request("GET", 'https://' + host1 + '/submissions/' + decision_token, headers = {'Content-Type': 'application/json', 'X-RapidAPI-Key': tok_n, 'X-RapidApi-Host': 'judge0-ce.p.rapidapi.com'}, params = {"base64_encoded": "true", "fields": "*"}).json()
"""
app = Flask(__name__)

sent_adress = 'https://judge0-ce.p.rapidapi.com/submissions/'
tok_n = '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7'
heads = {
    'Content-Type': 'application/json',
    'X-RapidAPI-Key': tok_n,
    'X-RapidApi-Host': 'judge0-ce.p.rapidapi.com'}

#langs = requests.request("GET", "https://judge0-ce.p.rapidapi.com/languages", headers = heads).json()
langes = [{'id': 45, 'name': 'Assembly (NASM 2.14.02)'}, {'id': 46, 'name': 'Bash (5.0.0)'}, {'id': 47, 'name': 'Basic (FBC 1.07.1)'}, {'id': 75, 'name': 'C (Clang 7.0.1)'}, {'id': 76, 'name': 'C++ (Clang 7.0.1)'}, {'id': 48, 'name': 'C (GCC 7.4.0)'}, {'id': 52, 'name': 'C++ (GCC 7.4.0)'}, {'id': 49, 'name': 'C (GCC 8.3.0)'}, {'id': 53, 'name': 'C++ (GCC 8.3.0)'}, {'id': 50, 'name': 'C (GCC 9.2.0)'}, {'id': 54, 'name': 'C++ (GCC 9.2.0)'}, {'id': 86, 'name': 'Clojure (1.10.1)'}, {'id': 51, 'name': 'C# (Mono 6.6.0.161)'}, {'id': 77, 'name': 'COBOL (GnuCOBOL 2.2)'}, {'id': 55, 'name': 'Common Lisp (SBCL 2.0.0)'}, {'id': 56, 'name': 'D (DMD 2.089.1)'}, {'id': 57, 'name': 'Elixir (1.9.4)'}, {'id': 58, 'name': 'Erlang (OTP 22.2)'}, {'id': 44, 'name': 'Executable'}, {'id': 87, 'name': 'F# (.NET Core SDK 3.1.202)'}, {'id': 59, 'name': 'Fortran (GFortran 9.2.0)'}, {'id': 60, 'name': 'Go (1.13.5)'}, {'id': 88, 'name': 'Groovy (3.0.3)'}, {'id': 61, 'name': 'Haskell (GHC 8.8.1)'}, {'id': 62, 'name': 'Java (OpenJDK 13.0.1)'}, {'id': 63, 'name': 'JavaScript (Node.js 12.14.0)'}, {'id': 78, 'name': 'Kotlin (1.3.70)'}, {'id': 64, 'name': 'Lua (5.3.5)'}, {'id': 89, 'name': 'Multi-file program'}, {'id': 79, 'name': 'Objective-C (Clang 7.0.1)'}, {'id': 65, 'name': 'OCaml (4.09.0)'}, {'id': 66, 'name': 'Octave (5.1.0)'}, {'id': 67, 'name': 'Pascal (FPC 3.0.4)'}, {'id': 85, 'name': 'Perl (5.28.1)'}, {'id': 68, 'name': 'PHP (7.4.1)'}, {'id': 43, 'name': 'Plain Text'}, {'id': 69, 'name': 'Prolog (GNU Prolog 1.4.5)'}, {'id': 70, 'name': 'Python (2.7.17)'}, {'id': 71, 'name': 'Python (3.8.1)'}, {'id': 80, 'name': 'R (4.0.0)'}, {'id': 72, 'name': 'Ruby (2.7.0)'}, {'id': 73, 'name': 'Rust (1.40.0)'}, {'id': 81, 'name': 'Scala (2.13.2)'}, {'id': 82, 'name': 'SQL (SQLite 3.27.2)'}, {'id': 83, 'name': 'Swift (5.2.3)'}, {'id': 74, 'name': 'TypeScript (3.7.4)'}, {'id': 84, 'name': 'Visual Basic.Net (vbnc 0.0.0.5943)'}]
#w = 0
#for i in langes:
 #   w = w + 1
#print(w)
#langs = [w]
#for i in langs:
    #print(i['id'], "   ", i['name'])

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        myCode = request.form.get('Code')
        myCode = request.form.get('qwerty')
        mC = myCode.encode("UTF-8")
        Code = base64.b64encode(mC)
        Cd = Code.decode("UTF-8")
        myCodeLanguage = request.form.get('language')
        myCin = request.form.get('in')
        #Cd = base64.b64decode(myCode)
        dats = {
            "language_id": myCodeLanguage,
            "source_code": Cd,
            "stdin": "SnVkZ2Uw"
            #"expected_output": ""
        }
        resp = requests.request("POST", sent_adress, headers = heads, json = dats, params = {"base64_encoded": "true"}).json()
        print(resp)
        #return render_template("sent.html", rets = resp)
        decision_tok_n = resp['token']
        answer = requests.request("GET", sent_adress + decision_tok_n, headers = heads, params = {"base64_encoded": "true"}).json()
        rets = answer['compile_output']
        if rets is None:
            return render_template("sent.html", langs = langes, rets = "None")

        else:
            rts = base64.b64decode(rets.encode("UTF-8"))
            rs = rts.decode("UTF-8")
            return render_template("sent.html", langs = langes, rets = rs)
    else:
        q = 1
        langs = []
        for i in langes:
            langs.append(i['name'])
            q = q + 1
        return render_template("sent.html", langs = langes)#, langs = langs)

#print(resp3)
if __name__ == '__main__':
    app.run(debug=True)

