import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# === van Genuchten model ===
def van_genuchten(h, theta_r, theta_s, alpha, n):
    m = 1 - 1 / n
    return theta_r + (theta_s - theta_r) / ((1 + (alpha * h)**n)**m)

# === Load data ===
df = pd.read_excel('Example 1.xlsx', sheet_name='Feuil1')
h = df.iloc[:, 0].values
theta = df.iloc[:, 1].values

# === Fit van Genuchten model ===
initial_guess = [0.05, 0.45, 0.01, 1.5]
params, _ = curve_fit(van_genuchten, h, theta, p0=initial_guess, bounds=(0, [1, 1, 1, 10]))
theta_r, theta_s, alpha, n = params
theta_fit = van_genuchten(h, *params)

# === R² for van Genuchten fit ===
ss_res = np.sum((theta - theta_fit)**2)
ss_tot = np.sum((theta - np.mean(theta))**2)
r2_vg = 1 - (ss_res / ss_tot)

# === Linear regression: Measured vs Fitted ===
model = LinearRegression().fit(theta_fit.reshape(-1, 1), theta.reshape(-1, 1))
a = model.coef_[0][0]
b = model.intercept_[0]
r2_lin = model.score(theta_fit.reshape(-1, 1), theta.reshape(-1, 1))

# === Export to Excel ===
results = pd.DataFrame({
    'Pressure Head (h)': h,
    'Measured θ': theta,
    'Fitted θ (VG)': theta_fit
})

parameters = pd.DataFrame({
    'Parameter': ['theta_r', 'theta_s', 'alpha', 'n', 'R² (VG)', 'a (lin)', 'b (lin)', 'R² (lin)'],
    'Value': [theta_r, theta_s, alpha, n, r2_vg, a, b, r2_lin]
})

with pd.ExcelWriter('fitted_results.xlsx') as writer:
    results.to_excel(writer, sheet_name='Fitted Data', index=False)
    parameters.to_excel(writer, sheet_name='Parameters', index=False)

# === Plot 1: van Genuchten Fit (Only R²) ===
plt.figure()
plt.scatter(h, theta, label='Measured', color='blue')
plt.plot(h, theta_fit, label='Fitted (VG)', color='red')
plt.xlabel('Pressure Head (h) [cm]')
plt.ylabel('Water Content (θ)')
plt.title('van Genuchten Model Fit')
plt.legend()
plt.grid(True)
plt.text(0.05 * max(h), 0.95 * max(theta), f"R² = {r2_vg:.4f}",
         fontsize=9, bbox=dict(facecolor='white', alpha=0.7))

# === Plot 2: Correlation (with regression eq.) ===
plt.figure()
plt.scatter(theta_fit, theta, label='Measured vs Fitted', color='green')
theta_fit_sorted = np.sort(theta_fit)
plt.plot(theta_fit_sorted, a * theta_fit_sorted + b, color='black', label='Linear Fit')
plt.xlabel('Fitted θ (VG)')
plt.ylabel('Measured θ')
plt.title('Correlation: Measured vs Fitted θ')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"θ = {a:.4f} × θ_fit + {b:.4f}\nR² = {r2_lin:.4f}",
         transform=plt.gca().transAxes,
         fontsize=9, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.7))

plt.show()
