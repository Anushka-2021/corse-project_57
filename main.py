# This is a sample Python script.
from flask import Flask, request, render_template, session
import requests, base64, sqlite3, datetime
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

app = Flask(__name__)

sent_adress = 'https://judge0-ce.p.rapidapi.com/submissions/'
tok_n = '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7'

conn = sqlite3.connect("base57.db", check_same_thread=False)
cursor = conn.cursor()

#cursor.execute("""CREATE TABLE IF NOT EXISTS table57
#(des_token UNIQUE, lang, code, input, exp_output, output, time)
#""")
#conn.commit()

heads = {
    'Content-Type': 'application/json',
    'X-RapidAPI-Key': tok_n,
    'X-RapidApi-Host': 'judge0-ce.p.rapidapi.com'}

#langs = requests.request("GET", "https://judge0-ce.p.rapidapi.com/languages", headers = heads).json()
langes = [{'id': 45, 'name': 'Assembly (NASM 2.14.02)'}, {'id': 46, 'name': 'Bash (5.0.0)'}, {'id': 47, 'name': 'Basic (FBC 1.07.1)'}, {'id': 75, 'name': 'C (Clang 7.0.1)'}, {'id': 76, 'name': 'C++ (Clang 7.0.1)'}, {'id': 48, 'name': 'C (GCC 7.4.0)'}, {'id': 52, 'name': 'C++ (GCC 7.4.0)'}, {'id': 49, 'name': 'C (GCC 8.3.0)'}, {'id': 53, 'name': 'C++ (GCC 8.3.0)'}, {'id': 50, 'name': 'C (GCC 9.2.0)'}, {'id': 54, 'name': 'C++ (GCC 9.2.0)'}, {'id': 86, 'name': 'Clojure (1.10.1)'}, {'id': 51, 'name': 'C# (Mono 6.6.0.161)'}, {'id': 77, 'name': 'COBOL (GnuCOBOL 2.2)'}, {'id': 55, 'name': 'Common Lisp (SBCL 2.0.0)'}, {'id': 56, 'name': 'D (DMD 2.089.1)'}, {'id': 57, 'name': 'Elixir (1.9.4)'}, {'id': 58, 'name': 'Erlang (OTP 22.2)'}, {'id': 44, 'name': 'Executable'}, {'id': 87, 'name': 'F# (.NET Core SDK 3.1.202)'}, {'id': 59, 'name': 'Fortran (GFortran 9.2.0)'}, {'id': 60, 'name': 'Go (1.13.5)'}, {'id': 88, 'name': 'Groovy (3.0.3)'}, {'id': 61, 'name': 'Haskell (GHC 8.8.1)'}, {'id': 62, 'name': 'Java (OpenJDK 13.0.1)'}, {'id': 63, 'name': 'JavaScript (Node.js 12.14.0)'}, {'id': 78, 'name': 'Kotlin (1.3.70)'}, {'id': 64, 'name': 'Lua (5.3.5)'}, {'id': 89, 'name': 'Multi-file program'}, {'id': 79, 'name': 'Objective-C (Clang 7.0.1)'}, {'id': 65, 'name': 'OCaml (4.09.0)'}, {'id': 66, 'name': 'Octave (5.1.0)'}, {'id': 67, 'name': 'Pascal (FPC 3.0.4)'}, {'id': 85, 'name': 'Perl (5.28.1)'}, {'id': 68, 'name': 'PHP (7.4.1)'}, {'id': 43, 'name': 'Plain Text'}, {'id': 69, 'name': 'Prolog (GNU Prolog 1.4.5)'}, {'id': 70, 'name': 'Python (2.7.17)'}, {'id': 71, 'name': 'Python (3.8.1)'}, {'id': 80, 'name': 'R (4.0.0)'}, {'id': 72, 'name': 'Ruby (2.7.0)'}, {'id': 73, 'name': 'Rust (1.40.0)'}, {'id': 81, 'name': 'Scala (2.13.2)'}, {'id': 82, 'name': 'SQL (SQLite 3.27.2)'}, {'id': 83, 'name': 'Swift (5.2.3)'}, {'id': 74, 'name': 'TypeScript (3.7.4)'}, {'id': 84, 'name': 'Visual Basic.Net (vbnc 0.0.0.5943)'}]
app.secret_key = '1806363f0fmshf3926631702e101p1eda9ajsn5e10975d9be7'

@app.route('/login', methods =['GET', 'POST'])
def login():
    #после отправки формы
    if request.method == 'POST':
        #если не войдено
        if 'username' not in session:
            username = request.form['username']
            cursor.execute("SELECT * FROM users_table_1 WHERE username=?", (username,))
            #если это имя есть в таблице пользователей
            if cursor.fetchone():
                session['username'] = username
                cursor.execute("SELECT role FROM users_table_1 WHERE username=?", (session['username'],))
                session['role'] = cursor.fetchone()
                return render_template('login.html', deta = 'Hello, ' + request.form['username'], role = session['role'], logInfo = 'Logout')
            else:
                return render_template('login.html', deta = 'You are not registered')
        else:
            return render_template('login.html', deta = 'You are already in as ' + session['username'], logInfo = 'Logout')
    else:
        return render_template('login.html')

@app.route('/logout', methods = ['GET', 'POST'])
def logout():
    session.pop('username', None)
    return render_template('lk.html', logInfo = 'Login')

@app.route('/register', methods =['GET', 'POST'])
def register():
    if request.method == 'POST':
        if 'username' not in session:
            session['username'] = request.form['username']
            username = session['username']
            email = request.form['email']
            role = request.form['role']
            cursor.execute("SELECT * FROM users_table_1")
            noun = 0
            f = cursor.fetchone()
            while f:
                noun+=1
                f = cursor.fetchone()
            user_id = noun + 1
            cursor.execute("INSERT OR REPLACE INTO users_table_1(user_id, username, role, email) VALUES (?, ?, ?, ?)", (user_id, username, role, email))
            conn.commit()
            f = cursor.execute("SELECT * FROM users_table_1")
            for i in f:
                print(i)
            print()
            return render_template('login.html', deta = 'Hello, ' + request.form['username'], role = session['role'], logInfo = 'Logout')
        else:
            return render_template('login.html', deta = 'You are already in as ' + session['username'], role = session['role'], logInfo = 'Logout')
    return render_template('login.html', logInfo = 'Register')


@app.route('/person', methods = ['GET', 'POST'])
def personal():
    if 'username' not in session:
        return render_template("lk.html", data = 'You are not in')
    cursor.execute("SELECT * FROM table572")
    noun = 0
    f = cursor.fetchone()
    while f:
        noun+=1
        f = cursor.fetchone()
    return render_template("lk.html", data = noun)

@app.route('/person/today', methods = ['GET', 'POST'])
def personal_today():
    now = datetime.datetime.now()
    day = now.strftime("%d/%m/%y")
    todays_subs = []
    cursor.execute("SELECT lang, code, input, exp_output, output, time FROM table572 WHERE day=?", (day,))
    todays_subs.append(cursor.fetchall())
    print(todays_subs)
    if todays_subs is None:
        return render_template('lk.html', datas = "None")
    else:
        #task_id = 0;
        #cols = todays_subs[2]
        #rows = todays_subs['stdout']
        #print(todays_subs)
        return render_template('lk.html', datas = todays_subs)#, task_id=task_id, cols = cols, rows = rows)

    #f = cursor.fetchone()
    #for i in f:
    #    if i['day'] is day:
    #
    #    f = cursor.fetchone()

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        myCode = request.form.get('code_area')
        mC = myCode.encode("UTF-8")
        Code = base64.b64encode(mC)
        Cd = Code.decode("UTF-8")
        myCodeLanguage = request.form.get('language')
        myCin = request.form.get('in')
        #Cd = base64.b64decode(myCode)
        dats = {
            "language_id": myCodeLanguage,
            "source_code": Cd,
            "stdin": "SnVkZ2Uw",
            "expected_output": ""
        }
        resp = requests.request("POST", sent_adress, headers = heads, json = dats, params = {"base64_encoded": "true"}).json()
        print(resp)
        #return render_template("sent.html", rets = resp)
        decision_tok_n = resp['token']
        answer = requests.request("GET", sent_adress + decision_tok_n, headers = heads, params = {"base64_encoded": "true"}).json()
        print(answer['status'], " ", answer['stdout'])
        rets = answer['compile_output']
        if rets is None:
            if answer['stdout'] is None:
                rs = "None"
            else:
                rts = base64.b64decode(answer['stdout'].encode("UTF-8"))
                rs = rts.decode("UTF-8")
        #    return render_template("sent.html", langs = langes, rets = "None")
        else:
            rts = base64.b64decode(rets.encode("UTF-8"))
            rs = rts.decode("UTF-8")

        """inserting time of submission"""
        now = datetime.datetime.now()
        time = now.strftime("%H:%M:%S")
        day = now.strftime("%d/%m/%y")

        cursor.execute("INSERT OR REPLACE INTO table572(des_token, lang, code, input, output, time, day) VALUES (?, ?, ?, ?, ?, ?, ?)", (decision_tok_n, myCodeLanguage, myCode, myCin, rs, time, day))
        conn.commit()
        noun = 0
        cursor.execute("SELECT * FROM table572")
        f = cursor.fetchone()
        while f:
            noun+=1
            f = cursor.fetchone()
            print(f)
        print("You tried to submit this task", noun, "times")
        #cursor.execute("SELECT ")
        return render_template("sent.html", langs = langes, rets = rs)
    else:
        q = 1
        langs = []
        for i in langes:
            langs.append(i['name'])
            q = q + 1
        return render_template("sent.html", langs = langes)#, langs = langs)

if __name__ == '__main__':
    cursor.execute("""CREATE TABLE IF NOT EXISTS table572
    (des_token UNIQUE, lang, code, input, exp_output, output, time, day)
    """)
    conn.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users_table_1
    (user_id UNIQUE, username, role, password, email)
    """)
    conn.commit()


    app.run(debug=True)

