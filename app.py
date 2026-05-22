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

# GIRLY COLOR SCHEME HTML - Pink & Purple Theme 💕
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Regula Falsi Method ✨</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            font-family: 'Segoe UI', 'Quicksand', Arial, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background: linear-gradient(135deg, #ffe9f4 0%, #ffe0f0 50%, #fce4ec 100%);
            min-height: 100vh;
        }
        .card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 25px;
            padding: 25px;
            margin-bottom: 25px;
            box-shadow: 0 8px 25px rgba(255, 105, 180, 0.15);
            border: 1px solid rgba(255, 192, 203, 0.5);
            transition: transform 0.2s;
        }
        .card:hover {
            transform: translateY(-3px);
        }
        h1 { 
            color: #d43f8d; 
            font-size: 2.2em;
            text-shadow: 2px 2px 4px rgba(255, 105, 180, 0.2);
        }
        h2 { 
            color: #e85d9e; 
            border-bottom: 3px solid #ffb3d9;
            padding-bottom: 12px;
            font-size: 1.5em;
        }
        h3 { 
            color: #c4458a; 
            margin-top: 15px;
        }
        input, select, button {
            padding: 12px;
            margin: 8px 0;
            width: 100%;
            max-width: 300px;
            border: 2px solid #ffc0cb;
            border-radius: 25px;
            font-size: 14px;
            transition: all 0.3s;
            background: white;
        }
        input:focus, select:focus {
            border-color: #e85d9e;
            outline: none;
            box-shadow: 0 0 8px rgba(232, 93, 158, 0.3);
        }
        button {
            background: linear-gradient(135deg, #e85d9e 0%, #c4458a 100%);
            color: white;
            border: none;
            cursor: pointer;
            font-weight: bold;
            font-size: 16px;
            width: auto;
            min-width: 150px;
        }
        button:hover {
            background: linear-gradient(135deg, #f06aaa 0%, #d84f96 100%);
            transform: scale(1.02);
            box-shadow: 0 5px 15px rgba(232, 93, 158, 0.3);
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
            border-radius: 15px;
            overflow: hidden;
        }
        th, td {
            border: 1px solid #ffd9e8;
            padding: 10px;
            text-align: center;
        }
        th { 
            background: linear-gradient(135deg, #f8bbd0 0%, #f48fb1 100%);
            color: #6b2e4a;
            font-weight: bold;
        }
        tr:nth-child(even) {
            background-color: #fff5f8;
        }
        tr:hover {
            background-color: #ffe0ef;
        }
        .result { 
            background: linear-gradient(135deg, #e8f5e9 0%, #f1f8e9 100%);
            padding: 18px;
            border-radius: 20px;
            margin-top: 20px;
            border-left: 6px solid #81c784;
        }
        .error { 
            background: linear-gradient(135deg, #ffebee 0%, #ffcdd2 100%);
            color: #c62828;
            padding: 15px;
            border-radius: 20px;
            margin-top: 15px;
            border-left: 6px solid #e57373;
        }
        .example { 
            background: linear-gradient(135deg, #f3e5f5 0%, #ede7f6 100%);
            padding: 20px;
            border-radius: 20px;
            margin: 15px 0;
            border: 1px solid #e1bee7;
        }
        .math {
            background: linear-gradient(135deg, #fff0f5 0%, #ffe4f0 100%);
            padding: 20px;
            border-radius: 20px;
            font-size: 18px;
            text-align: center;
            font-family: monospace;
            border: 1px solid #ffc0cb;
        }
        .formula-box {
            background: linear-gradient(135deg, #fce4ec 0%, #f8bbd0 100%);
            padding: 20px;
            border-radius: 20px;
            margin: 15px 0;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #ad1457;
        }
        label {
            font-weight: bold;
            color: #ad1457;
            margin-top: 10px;
            display: inline-block;
        }
        ::placeholder {
            color: #ffb6c1;
        }
        .heart {
            color: #e85d9e;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="card" style="text-align: center;">
        <h1>📐 Regula Falsi (False Position) Method 💕</h1>
        <p>A root-finding algorithm that combines the bisection and secant methods. ✨</p>
        <p class="heart">🌸 mathematics is beautiful 🌸</p>
    </div>

    <!-- FIGURE 1: MATHEMATICAL DISCUSSION -->
    <div class="card">
        <h2>📖 Mathematical Discussion</h2>
        
        <div class="formula-box">
            <strong>✨ Formula ✨</strong><br>
            c = [a × f(b) - b × f(a)] / [f(b) - f(a)]
        </div>
        
        <p><strong>🎀 Algorithm Steps:</strong></p>
        <ol>
            <li>Find two points a and b such that f(a) and f(b) have opposite signs</li>
            <li>Calculate c using the formula: c = [a × f(b) - b × f(a)] / [f(b) - f(a)]</li>
            <li>Evaluate f(c)</li>
            <li>If |f(c)| is less than tolerance, c is the root</li>
            <li>If f(a) × f(c) is less than 0, set b = c, otherwise set a = c</li>
            <li>Repeat steps 2-5 until convergence</li>
        </ol>
        
        <p><strong>💖 Convergence:</strong> The Regula Falsi method converges linearly, but is often faster than the bisection method for many functions.</p>
    </div>

    <!-- FIGURE 2: WORKED EXAMPLE 1 -->
    <div class="card">
        <h2>📝 Worked Example 1: x³ - x - 2 = 0</h2>
        <div class="example">
            <p><strong>Step 1:</strong> Find interval [a, b] where f(a) and f(b) have opposite signs.</p>
            <p>🌸 f(1) = 1³ - 1 - 2 = -2 (negative)</p>
            <p>🌸 f(2) = 8 - 2 - 2 = 4 (positive)</p>
            <p>✓ Root lies in [1, 2] since signs are opposite.</p>
            
            <p><strong>Step 2:</strong> Apply Regula Falsi formula:</p>
            <p>c = [1 × 4 - 2 × (-2)] / [4 - (-2)] = [4 + 4] / 6 = 8/6 = 1.3333</p>
            
            <p><strong>Step 3:</strong> Evaluate f(c):</p>
            <p>f(1.3333) = (1.3333)³ - 1.3333 - 2 = 2.370 - 1.3333 - 2 = -0.9633</p>
            
            <p><strong>Step 4:</strong> Update interval: Since f(1.3333) is negative and f(2) is positive, new interval is [1.3333, 2]</p>
            
            <p><strong>Step 5:</strong> Continue iterations until convergence:</p>
            <p>After several iterations, the root converges to:</p>
            <p><strong>🎯 Final Root:</strong> x ≈ 1.52137971</p>
            <p>💜 Verification: f(1.52138) ≈ 0 ✓</p>
        </div>
    </div>

    <!-- FIGURE 3: WORKED EXAMPLE 2 -->
    <div class="card">
        <h2>📝 Worked Example 2: x² - 4 = 0</h2>
        <div class="example">
            <p><strong>Step 1:</strong> Find interval [a, b] with sign change.</p>
            <p>🌸 f(1) = 1 - 4 = -3 (negative)</p>
            <p>🌸 f(3) = 9 - 4 = 5 (positive)</p>
            <p>✓ Root lies in [1, 3].</p>
            
            <p><strong>Step 2:</strong> First iteration:</p>
            <p>c = [1 × 5 - 3 × (-3)] / [5 - (-3)] = [5 + 9] / 8 = 14/8 = 1.75</p>
            <p>f(1.75) = (1.75)² - 4 = 3.0625 - 4 = -0.9375</p>
            
            <p><strong>Step 3:</strong> Second iteration using [1.75, 3]:</p>
            <p>c = [1.75 × 5 - 3 × (-0.9375)] / [5 - (-0.9375)] = [8.75 + 2.8125] / 5.9375 = 11.5625/5.9375 = 1.9474</p>
            <p>f(1.9474) = 3.792 - 4 = -0.208</p>
            
            <p><strong>Step 4:</strong> Continue iterations:</p>
            <p><strong>🎯 Final Root:</strong> x = 2.00000000</p>
            <p>💜 Verification: f(2) = 4 - 4 = 0 ✓</p>
        </div>
    </div>

    <!-- FIGURES 4 & 5: CALCULATOR -->
    <div class="card">
        <h2>🧮 Interactive Calculator ✨</h2>
        <form method="POST">
            <label>🎀 Select Function:</label>
            <select name="function">
                <option>x³ - x - 2</option>
                <option>x² - 4</option>
                <option>cos(x) - x</option>
                <option>e^(-x) - x</option>
                <option>x³ - 2x - 5</option>
            </select>
            
            <label>📐 Lower bound (a):</label>
            <input type="number" name="a" step="any" required placeholder="e.g., 1">
            
            <label>📐 Upper bound (b):</label>
            <input type="number" name="b" step="any" required placeholder="e.g., 2">
            
            <label>⚡ Tolerance:</label>
            <input type="number" name="tol" step="any" value="1e-6" placeholder="0.000001">
            
            <button type="submit">💖 Calculate Root 💖</button>
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
            
            if root is not None:
                result_html = f'''
                <div class="result">
                    <h3>💖 Root Found! 💖</h3>
                    <p><strong>🎯 Root:</strong> x = {root:.8f}</p>
                    <p><strong>✨ Iterations:</strong> {iterations}</p>
                    <h3>📊 Iteration Details:</h3>
                    <div style="overflow-x: auto;">
                        <table>
                            <thead>
                                <tr><th>Iter</th><th>a</th><th>b</th><th>c</th><th>f(c)</th></tr>
                            </thead>
                            <tbody>
                '''
                for step in steps:
                    result_html += f'''
                        <tr>
                            <td>{step["iteration"]}</td>
                            <td>{step["a"]}</td>
                            <td>{step["b"]}</td>
                            <td>{step["c"]}</td>
                            <td>{step["f_c"]}</td>
                        </tr>
                    '''
                result_html += '''
                            </tbody>
                        </table>
                    </div>
                </div>
                '''
            else:
                result_html = f'<div class="error"><p>💔 Error: f({a}) and f({b}) must have opposite signs! Please choose different a and b values. 💔</p></div>'
                
        except Exception as e:
            result_html = f'<div class="error"><p>💔 Error: {str(e)} 💔</p></div>'
    
    return HTML.replace('{result_html}', result_html)

app.debug = False
