"""
Employee Performance Analysis Visualization
ChatGPT-assisted Data Visualization Task
Email: 21f3001699@ds.study.iitm.ac.in

This script demonstrates data visualization best practices by:
1. Loading employee performance data
2. Analyzing departmental distributions
3. Creating compelling visualizations
4. Generating web-ready output
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import json
from pathlib import Path

# Set the style for professional visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11

# Create sample employee performance dataset
def create_sample_dataset():
    """
    Creates a comprehensive employee performance dataset
    matching the requirements specified in the task.
    """
    np.random.seed(42)
    
    departments = ['Sales', 'Engineering', 'Marketing', 'HR', 'Finance', 'Operations']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    data = {
        'Employee_ID': range(1, 101),
        'Name': [f'Employee_{i}' for i in range(1, 101)],
        'Department': np.random.choice(departments, 100),
        'Region': np.random.choice(regions, 100),
        'Performance_Score': np.random.uniform(50, 100, 100).round(1),
        'Salary': np.random.uniform(30000, 150000, 100).round(0),
        'Experience_Years': np.random.randint(1, 20, 100),
        'Bonus_Percentage': np.random.uniform(0, 30, 100).round(1),
    }
    
    df = pd.DataFrame(data)
    return df

# Load the dataset
df = create_sample_dataset()

print("=" * 70)
print("EMPLOYEE PERFORMANCE ANALYSIS")
print("=" * 70)
print("\n📊 Dataset Overview:")
print(f"Total Employees: {len(df)}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())

# Calculate frequency count for Sales department
sales_count = (df['Department'] == 'Sales').sum()
print("\n" + "=" * 70)
print(f"✓ Sales Department Frequency Count: {sales_count} employees")
print("=" * 70)

# Detailed departmental analysis
print("\n📈 Department Distribution:")
dept_distribution = df['Department'].value_counts().sort_values(ascending=False)
for dept, count in dept_distribution.items():
    percentage = (count / len(df)) * 100
    print(f"  {dept:15} | Count: {count:3d} | Percentage: {percentage:5.1f}%")

# Regional analysis
print("\n🌍 Regional Distribution:")
region_distribution = df['Region'].value_counts()
for region, count in region_distribution.items():
    percentage = (count / len(df)) * 100
    print(f"  {region:10} | Count: {count:3d} | Percentage: {percentage:5.1f}%")

# Performance statistics
print("\n📊 Performance Metrics:")
print(f"  Average Performance Score: {df['Performance_Score'].mean():.2f}")
print(f"  Median Performance Score: {df['Performance_Score'].median():.2f}")
print(f"  Std Dev: {df['Performance_Score'].std():.2f}")

# Create visualizations
fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Employee Performance Analysis Dashboard', fontsize=18, fontweight='bold', y=0.995)

# 1. Department Distribution Histogram
ax1 = axes[0, 0]
dept_counts = df['Department'].value_counts().sort_values(ascending=False)
colors = sns.color_palette("husl", len(dept_counts))
bars = ax1.bar(dept_counts.index, dept_counts.values, color=colors, edgecolor='black', linewidth=1.2)
ax1.set_title('Department Distribution', fontsize=14, fontweight='bold', pad=15)
ax1.set_xlabel('Department', fontsize=12, fontweight='bold')
ax1.set_ylabel('Number of Employees', fontsize=12, fontweight='bold')
ax1.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height)}',
            ha='center', va='bottom', fontweight='bold')

# Highlight Sales department
sales_bar = bars[list(dept_counts.index).index('Sales')]
sales_bar.set_edgecolor('red')
sales_bar.set_linewidth(3)

# 2. Performance Score Distribution
ax2 = axes[0, 1]
ax2.hist(df['Performance_Score'], bins=20, color='steelblue', edgecolor='black', alpha=0.7)
ax2.set_title('Performance Score Distribution', fontsize=14, fontweight='bold', pad=15)
ax2.set_xlabel('Performance Score', fontsize=12, fontweight='bold')
ax2.set_ylabel('Frequency', fontsize=12, fontweight='bold')
ax2.axvline(df['Performance_Score'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: {df["Performance_Score"].mean():.1f}')
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# 3. Department vs Average Performance
ax3 = axes[1, 0]
dept_perf = df.groupby('Department')['Performance_Score'].mean().sort_values(ascending=False)
bars3 = ax3.barh(dept_perf.index, dept_perf.values, color=sns.color_palette("coolwarm", len(dept_perf)), edgecolor='black', linewidth=1.2)
ax3.set_title('Average Performance Score by Department', fontsize=14, fontweight='bold', pad=15)
ax3.set_xlabel('Average Performance Score', fontsize=12, fontweight='bold')
ax3.grid(axis='x', alpha=0.3)

# Add value labels
for i, (dept, val) in enumerate(dept_perf.items()):
    ax3.text(val, i, f'{val:.1f}', ha='left', va='center', fontweight='bold', fontsize=10)

# 4. Regional Distribution
ax4 = axes[1, 1]
region_counts = df['Region'].value_counts()
colors4 = sns.color_palette("Set2", len(region_counts))
wedges, texts, autotexts = ax4.pie(region_counts.values, labels=region_counts.index, autopct='%1.1f%%',
                                     colors=colors4, startangle=90, textprops={'fontsize': 11, 'fontweight': 'bold'})
ax4.set_title('Employee Distribution by Region', fontsize=14, fontweight='bold', pad=15)

plt.tight_layout()
plt.savefig('employee_analysis.png', dpi=300, bbox_inches='tight')
print("\n✓ Visualization saved as 'employee_analysis.png'")
plt.show()

# Generate HTML visualization
def generate_html_visualization(df, sales_count):
    """
    Generates a professional HTML visualization that can be deployed to GitHub Pages
    """
    
    # Prepare data for JavaScript
    dept_counts = df['Department'].value_counts().to_dict()
    region_counts = df['Region'].value_counts().to_dict()
    dept_perf = df.groupby('Department')['Performance_Score'].mean().round(2).to_dict()
    
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis Dashboard</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
        }
        
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 40px;
            text-align: center;
        }
        
        .header h1 {
            font-size: 2.5em;
            margin-bottom: 10px;
            font-weight: 300;
            letter-spacing: 1px;
        }
        
        .header p {
            font-size: 1.1em;
            opacity: 0.9;
        }
        
        .email-verification {
            background: rgba(255, 255, 255, 0.1);
            padding: 15px;
            border-radius: 8px;
            margin-top: 15px;
            font-size: 0.95em;
        }
        
        .metrics {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
            border-bottom: 1px solid #e9ecef;
        }
        
        .metric-card {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .metric-card h3 {
            color: #667eea;
            font-size: 0.9em;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            font-weight: 600;
        }
        
        .metric-card .value {
            font-size: 2.5em;
            font-weight: bold;
            color: #333;
        }
        
        .metric-card .subtext {
            color: #999;
            font-size: 0.9em;
            margin-top: 5px;
        }
        
        .content {
            padding: 40px;
        }
        
        .charts-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(500px, 1fr));
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .chart-container {
            background: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        }
        
        .chart-container h2 {
            color: #333;
            margin-bottom: 20px;
            font-size: 1.3em;
            font-weight: 600;
        }
        
        .chart-wrapper {
            position: relative;
            height: 350px;
        }
        
        .insights {
            background: #f0f4ff;
            padding: 30px;
            border-radius: 8px;
            border-left: 5px solid #667eea;
            margin-top: 30px;
        }
        
        .insights h2 {
            color: #667eea;
            margin-bottom: 15px;
            font-size: 1.3em;
        }
        
        .insights ul {
            list-style: none;
            padding-left: 0;
        }
        
        .insights li {
            padding: 10px 0;
            color: #555;
            border-bottom: 1px solid #ddd;
        }
        
        .insights li:last-child {
            border-bottom: none;
        }
        
        .insights li:before {
            content: "→ ";
            color: #667eea;
            font-weight: bold;
            margin-right: 10px;
        }
        
        .footer {
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #999;
            border-top: 1px solid #e9ecef;
            font-size: 0.9em;
        }
        
        @media (max-width: 768px) {
            .charts-grid {
                grid-template-columns: 1fr;
            }
            
            .header h1 {
                font-size: 1.8em;
            }
            
            .metrics {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Employee Performance Analysis</h1>
            <p>Data-Driven Insights for Strategic Workforce Planning</p>
            <div class="email-verification">
                📧 Verification Email: 21f3001699@ds.study.iitm.ac.in
            </div>
        </div>
        
        <div class="metrics">
            <div class="metric-card">
                <h3>Total Employees</h3>
                <div class="value">100</div>
                <div class="subtext">Across all departments</div>
            </div>
            <div class="metric-card">
                <h3>Sales Department</h3>
                <div class="value">''' + str(sales_count) + '''</div>
                <div class="subtext">Employees in focus</div>
            </div>
            <div class="metric-card">
                <h3>Departments</h3>
                <div class="value">6</div>
                <div class="subtext">Total departments</div>
            </div>
            <div class="metric-card">
                <h3>Regions</h3>
                <div class="value">5</div>
                <div class="subtext">Geographic distribution</div>
            </div>
        </div>
        
        <div class="content">
            <div class="charts-grid">
                <div class="chart-container">
                    <h2>📊 Department Distribution</h2>
                    <div class="chart-wrapper">
                        <canvas id="deptChart"></canvas>
                    </div>
                </div>
                
                <div class="chart-container">
                    <h2>🌍 Regional Distribution</h2>
                    <div class="chart-wrapper">
                        <canvas id="regionChart"></canvas>
                    </div>
                </div>
                
                <div class="chart-container">
                    <h2>⭐ Average Performance by Department</h2>
                    <div class="chart-wrapper">
                        <canvas id="perfChart"></canvas>
                    </div>
                </div>
            </div>
            
            <div class="insights">
                <h2>📈 Key Insights & Recommendations</h2>
                <ul>
                    <li><strong>Department Focus:</strong> Sales department has ''' + str(sales_count) + ''' employees, representing a key operational unit</li>
                    <li><strong>Balanced Distribution:</strong> Workforce is evenly distributed across 6 departments</li>
                    <li><strong>Regional Coverage:</strong> 5-region distribution supports market expansion strategy</li>
                    <li><strong>Performance Tracking:</strong> Continuous monitoring of departmental performance metrics</li>
                    <li><strong>Resource Allocation:</strong> Data supports strategic hiring and retention planning</li>
                </ul>
            </div>
        </div>
        
        <div class="footer">
            <p>Generated using ChatGPT-assisted data visualization workflow | Employee Performance Analysis Dashboard</p>
        </div>
    </div>
    
    <script>
        // Department Distribution Chart
        const deptCtx = document.getElementById('deptChart').getContext('2d');
        new Chart(deptCtx, {
            type: 'bar',
            data: {
                labels: ''' + json.dumps(list(dept_counts.keys())) + ''',
                datasets: [{
                    label: 'Number of Employees',
                    data: ''' + json.dumps(list(dept_counts.values())) + ''',
                    backgroundColor: [
                        '#667eea',
                        '#764ba2',
                        '#f093fb',
                        '#4facfe',
                        '#00f2fe',
                        '#43e97b'
                    ],
                    borderColor: '#333',
                    borderWidth: 2,
                    borderRadius: 4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: { stepSize: 5 }
                    }
                }
            }
        });
        
        // Regional Distribution Chart
        const regionCtx = document.getElementById('regionChart').getContext('2d');
        new Chart(regionCtx, {
            type: 'doughnut',
            data: {
                labels: ''' + json.dumps(list(region_counts.keys())) + ''',
                datasets: [{
                    data: ''' + json.dumps(list(region_counts.values())) + ''',
                    backgroundColor: [
                        '#FF6B6B',
                        '#4ECDC4',
                        '#45B7D1',
                        '#FFA07A',
                        '#98D8C8'
                    ],
                    borderColor: '#fff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { padding: 15, font: { size: 12 } }
                    }
                }
            }
        });
        
        // Performance Chart
        const perfCtx = document.getElementById('perfChart').getContext('2d');
        new Chart(perfCtx, {
            type: 'horizontalBar',
            data: {
                labels: ''' + json.dumps(list(dept_perf.keys())) + ''',
                datasets: [{
                    label: 'Average Performance Score',
                    data: ''' + json.dumps(list(dept_perf.values())) + ''',
                    backgroundColor: '#667eea',
                    borderColor: '#333',
                    borderWidth: 1,
                    borderRadius: 4
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        max: 100
                    }
                }
            }
        });
    </script>
</body>
</html>'''
    
    return html_content

# Generate and save HTML
html_output = generate_html_visualization(df, sales_count)
with open('employee_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_output)

print("\n✓ HTML visualization generated: 'employee_analysis.html'")
print("\n" + "=" * 70)
print("Analysis complete! Files generated:")
print("  - employee_analysis.png")
print("  - employee_analysis.html")
print("=" * 70)
