from flask import Flask, render_template, request

app = Flask(__name__)

# דף הבית
@app.route('/')
def home():
    return render_template('index.html')

# עמוד עוגות עם הקטגוריות
@app.route('/cakes')
def cakes():
    return render_template('cakes.html')  # קובץ HTML שיכלול את כל הקטגוריות



# סדנאות
@app.route('/workshops')
def workshops():
    return render_template('workshops.html')
#עלינו
@app.route('/A_little_about_us')
def A_little_about_us():
    return render_template('A_little_about_us.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # קבלת נתונים מהטופס
        name = request.form['name']
        email = request.form['email']
        phone = request.form.get('phone')  # קבלת מספר טלפון
        message = request.form['message']
        
        
        # יצירת קישור ל-WhatsApp
        whatsapp_message = f"שלום {name}, תודה שיצרת קשר! ההודעה שלך: {message}"
        whatsapp_link = f"https://wa.me/{phone}?text={whatsapp_message}"
        
        # מעבירים נתונים לדף התודה
        return render_template(
            'thank_you.html',
            name=name,
            email=email,
            message=message,
            whatsapp_link=whatsapp_link
        )
    
    # טופס יצירת קשר
    return render_template('base.html')






if __name__ == '__main__':
    app.run(debug=True)
