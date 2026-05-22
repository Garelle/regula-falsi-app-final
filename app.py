from flask import Flask, request
import math

app = Flask(__name__)

def regula_falsi(f, a, b, tol=1e-6, max_iter=50):
    """Regula Falsi Method"""
    steps = []
    
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        return None, 0, []
    
    for i in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)
        
        steps.append({
            "iteration": i + 1,
            "a": round(a, 6),
            "b": round(b, 6),
            "c": round(c, 6),
            "f_c": round(fc, 6)
        })
        
        if abs(fc) < tol or abs(b - a) < tol:
            return c, i + 1, steps
        
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    return c, max_iter, steps

# Functions
def f1(x): return x**3 - x - 2
def f2(x): return x**2 - 4
def f3(x): return math.cos(x) - x
def f4(x): return math.exp(-x) - x
def f5(x): return x**3 - 2*x - 5

FUNCTIONS = {
    "x³ - x - 2": f1,
    "x² - 4": f2,
    "cos(x) - x": f3,
    "e^(-x) - x": f4,
    "x³ - 2x - 5": f5
}

# Simple HTML (no complex templates)
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Regula Falsi Method</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background: #f0f0f0;
        }
        .card {
            background: white;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        h1, h2 { color: #333; }
        input, select, button {
            padding: 10px;
            margin: 5px 0;
            width: 100%;
            max-width: 300px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        button {
            background: #007bff;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover { background: #0056b3; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 10px;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }
        th { background: #007bff; color: white; }
        .result { background: #d4edda; padding: 15px; border-radius: 5px; margin-top: 15px; }
        .error { background: #f8d7da; color: #721c24; padding: 15px; border-radius: 5px; margin-top: 15px; }
        .example { background: #e7f3ff; padding: 15px; border-radius: 5px; margin: 10px 0; }
    </style>
</head>
<body>
    <div class="card">
        <h1>📐 Regula Falsi (False Position) Method</h1>
        <p>A root-finding algorithm that combines the bisection and secant methods.</p>
    </div>

    <div class="card">
        <h2>📝 Example 1: x³ - x - 2 = 0</h2>
        <div class="example">
            <p>f(1) = -2, f(2) = 4 → Root in [1,2]</p>
            <p>After iterations: Root ≈ <strong>1.52138</strong></p>
        </div>
        
        <h2>📝 Example 2: x² - 4 = 0</h2>
        <div class="example">
            <p>f(1) = -3, f(3) = 5 → Root in [1,3]</p>
            <p>After iterations: Root = <strong>2.00000</strong></p>
        </div>
    </div>

    <div class="card">
        <h2>🧮 Calculator</h2>
        <form method="POST">
            <label>Function:</label>
            <select name="function">
                <option>x³ - x - 2</option>
                <option>x² - 4</option>
                <option>cos(x) - x</option>
                <option>e^(-x) - x</option>
                <option>x³ - 2x - 5</option>
            </select>
            
            <label>a (lower bound):</label>
            <input type="number" name="a" step="any" required>
            
            <label>b (upper bound):</label>
            <input type="number" name="b" step="any" required>
            
            <label>Tolerance:</label>
            <input type="number" name="tol" step="any" value="1e-6">
            
            <button type="submit">Calculate Root</button>
        </form>
        
        {result_html}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result_html = ""
    
    if request.method == 'POST':
        try:
            func_name = request.form.get('function')
            a = float(request.form.get('a'))
            b = float(request.form.get('b'))
            tol = float(request.form.get('tol', 1e-6))
            
            f = FUNCTIONS[func_name]
            root, iterations, steps = regula_falsi(f, a, b, tol)
            
            if root:
                result_html = f'''
                <div class="result">
                    <h3>✅ Root Found!</h3>
                    <p><strong>Root:</strong> x = {root:.8f}</p>
                    <p><strong>Iterations:</strong> {iterations}</p>
                    <h3>Iteration Details:</h3>
                    <table>
                        <tr><th>Iter</th><th>a</th><th>b</th><th>c</th><th>f(c)</th></tr>
                '''
                for step in steps[:10]:  # Show first 10 iterations
                    result_html += f'''
                        <tr>
                            <td>{step["iteration"]}</td>
                            <td>{step["a"]}</td>
                            <td>{step["b"]}</td>
                            <td>{step["c"]}</td>
                            <td>{step["f_c"]}</td>
                        </tr>
                    '''
                result_html += '</table></div>'
            else:
                result_html = f'<div class="error"><p>Error: f({a}) and f({b}) must have opposite signs!</p></div>'
                
        except Exception as e:
            result_html = f'<div class="error"><p>Error: {str(e)}</p></div>'
    
    return HTML.replace('{result_html}', result_html)

# This is required for Vercel
app.debug = False
