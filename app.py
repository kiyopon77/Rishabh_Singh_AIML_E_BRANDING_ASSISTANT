from flask import Flask, request, render_template
from groq import Groq
import os

app = Flask(__name__)

# ✅ Set your Groq API key securely
os.environ["GROQ_API_KEY"] = "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"
client = Groq()

# 🌈 Branding prompt using LLaMA
def generate_branding_idea(business_info):
    prompt = (
        f"You are a branding expert. Based on the following business description, suggest: "
        f"1. A color palette (in simple terms like 'pastel pink and navy blue') "
        f"2. Font type recommendations (serif/sans-serif and example fonts) "
        f"3. A short brand personality summary (3-4 lines max). "
        f"Business Info: {business_info}"
    )
    
    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.9,
        max_tokens=300,
        top_p=1,
        stream=False
    )
    
    return completion.choices[0].message.content.strip()

# 🎨 Main route for branding UI
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendation = None
    if request.method == 'POST':
        business_info = request.form.get('business_info')
        if business_info:
            recommendation = generate_branding_idea(business_info)
    return render_template('branding_form.html', result=recommendation)

if __name__ == '__main__':
    app.run(debug=True)

