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

# Complete HTML with CORRECTED Mathematical Discussion
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
            max-width: 1000px;
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
        h1 { color: #333; }
        h2 { color: #555; border-bottom: 2px solid #007bff; padding-bottom: 10px; }
        h3 { color: #666; margin-top: 15px; }
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
        .math {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            text-align: center;
        }
        .formula {
            font-size: 24px;
            background: #e8f4f8;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>📐 Regula Falsi (False Position) Method</h1>
        <p>A root-finding algorithm that combines the bisection and secant methods.</p>
    </div>

    <!-- MATHEMATICAL DISCUSSION SECTION - FIGURE 1 -->
    <div class="card">
        <h2>📖 Mathematical Discussion</h2>
        
        <div class="formula">
            <strong>Formula:</strong>
            <p>\[ c = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)} \]</p>
        </div>
        
        <p><strong>Algorithm Steps:</strong></p>
        <ol>
            <li>Find two points \(a\) and \(b\) such that \(f(a)\) and \(f(b)\) have opposite signs</li>
            <li>Calculate \(c\) using the formula: \(c = \frac{a \cdot f(b) - b \cdot f(a)}{f(b) - f(a)}\)</li>
            <li>Evaluate \(f(c)\)</li>
            <li>If \(|f(c)| &lt; \text{tolerance}\), \(c\) is the root</li>
            <li>If \(f(a) \cdot f(c) &lt; 0\), set \(b = c\), otherwise set \(a = c\)</li>
            <li>Repeat steps 2-5 until convergence</li>
        </ol>
        
        <p><strong>Convergence:</strong> The Regula Falsi method converges linearly, but is often faster than the bisection method for many functions.</p>
    </div>

    <!-- WORKED EXAMPLE 1 - FIGURE 2 -->
    <div class="card">
        <h2>📝 Worked Example 1: \(x^3 - x - 2 = 0\)</h2>
        <div class="example">
            <p><strong>Step 1:</strong> Find interval \([a,b]\) where \(f(a)\) and \(f(b)\) have opposite signs.</p>
            <p>\(f(1) = 1^3 - 1 - 2 = -2\) (negative)</p>
            <p>\(f(2) = 8 - 2 - 2 = 4\) (positive)</p>
            <p>✓ Root lies in \([1, 2]\) since signs are opposite.</p>
            
            <p><strong>Step 2:</strong> Apply Regula Falsi formula:</p>
            <p>\(c = \frac{1 \times 4 - 2 \times (-2)}{4 - (-2)} = \frac{4 + 4}{6} = \frac{8}{6} = 1.3333\)</p>
            
            <p><strong>Step 3:</strong> Evaluate \(f(c)\):</p>
            <p>\(f(1.3333) = (1.3333)^3 - 1.3333 - 2 = 2.370 - 1.3333 - 2 = -0.9633\)</p>
            
            <p><strong>Step 4:</strong> Update interval: Since \(f(1.3333)\) is negative and \(f(2)\) is positive, new interval is \([1.3333, 2]\)</p>
            
            <p><strong>Step 5:</strong> Continue iterations until convergence:</p>
            <p>After several iterations, the root converges to:</p>
            <p><strong>Final Root:</strong> \(x \approx 1.52137971\)</p>
            <p><strong>Verification:</strong> \(f(1.52138) \approx 0\) ✓</p>
        </div>
    </div>

    <!-- WORKED EXAMPLE 2 - FIGURE 3 -->
    <div class="card">
        <h2>📝 Worked Example 2: \(x^2 - 4 = 0\)</h2>
        <div class="example">
            <p><strong>Step 1:</strong> Find interval \([a,b]\) with sign change.</p>
            <p>\(f(1) = 1 - 4 = -3\) (negative)</p>
            <p>\(f(3) = 9 - 4 = 5\) (positive)</p>
            <p>✓ Root lies in \([1, 3]\).</p>
            
            <p><strong>Step 2:</strong> First iteration:</p>
            <p>\(c = \frac{1 \times 5 - 3 \times (-3)}{5 - (-3)} = \frac{5 + 9}{8} = \frac{14}{8} = 1.75\)</p>
            <p>\(f(1.75) = (1.75)^2 - 4 = 3.0625 - 4 = -0.9375\)</p>
            
            <p><strong>Step 3:</strong> Second iteration using \([1.75, 3]\):</p>
            <p>\(c = \frac{1.75 \times 5 - 3 \times (-0.9375)}{5 - (-0.9375)} = \frac{8.75 + 2.8125}{5.9375} = \frac{11.5625}{5.9375} = 1.9474\)</p>
            <p>\(f(1.9474) = 3.792 - 4 = -0.208\)</p>
            
            <p><strong>Step 4:</strong> Continue iterations:</p>
            <p><strong>Final Root:</strong> \(x = 2.00000000\)</p>
            <p><strong>Verification:</strong> \(f(2) = 4 - 4 = 0\) ✓</p>
        </div>
    </div>

    <!-- CALCULATOR - FIGURES 4 & 5 -->
    <div class="card">
        <h2>🧮 Interactive Calculator</h2>
        <form method="POST">
            <label>Select Function:</label>
            <select name="function">
                <option>x³ - x - 2</option>
                <option>x² - 4</option>
                <option>cos(x) - x</option>
                <option>e^(-x) - x</option>
                <option>x³ - 2x - 5</option>
            </select>
            
            <label>Lower bound (a):</label>
            <input type="number" name="a" step="any" required>
            
            <label>Upper bound (b):</label>
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
            
            if root is not None:
                result_html = f'''
                <div class="result">
                    <h3>✅ Root Found!</h3>
                    <p><strong>Root:</strong> x = {root:.8f}</p>
                    <p><strong>Iterations:</strong> {iterations}</p>
                    <h3>Iteration Details:</h3>
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
                result_html = f'<div class="error"><p>Error: f({a}) and f({b}) must have opposite signs!</p></div>'
                
        except Exception as e:
            result_html = f'<div class="error"><p>Error: {str(e)}</p></div>'
    
    return HTML.replace('{result_html}', result_html)

app.debug = False
