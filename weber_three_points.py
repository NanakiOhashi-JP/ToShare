import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.optimize import minimize

# n = 3として地点j の座標(x_j, y_j)を求める
# 三点の座標を(2, 2), (8, 2), (5, 3*sqrt(3)+2)
# としたとき、これらを図示し、ウェーバー点の座標を求める

# 3点の座標を定義
x1, y1 = 2, 2
x2, y2 = 8, 2
x3, y3 = 5, 3 * math.sqrt(3) + 2

# 3点の座標をリストに格納
points = [(x1, y1), (x2, y2), (x3, y3)]

# 各点の座標を表示
for i, (x, y) in enumerate(points):
    print(f"Point {i+1}: ({x:.6f}, {y:.6f})")

# ウェーバー点の座標を求める関数（総距離を最小化する点）
def total_distance(coords, points):
    """
    指定された点から全てのポイントまでの距離の合計を計算
    """
    x, y = coords
    total = 0
    for px, py in points:
        total += math.sqrt((x - px)**2 + (y - py)**2)
    return total

# 数値最適化でウェーバー点を求める
initial_guess = [5, 5]  # 初期値
result = minimize(total_distance, initial_guess, args=(points,), method='L-BFGS-B')

if result.success:
    weber_x, weber_y = result.x
    print(f"Weber Point: ({weber_x:.6f}, {weber_y:.6f})")
    print(f"Total distance: {result.fun:.6f}")
else:
    print("最適化に失敗しました")
    weber_x, weber_y = 5, 5

# グラフの描画
plt.figure(figsize=(10, 8))

# 各点のプロット
for i, (x, y) in enumerate(points):
    plt.scatter(x, y, color='blue', s=100)
    plt.text(x+0.1, y+0.1, f'Point {i+1} ({x:.2f}, {y:.2f})', fontsize=12)

# ウェーバー点のプロット
plt.scatter(weber_x, weber_y, color='red', s=100)
plt.text(weber_x+0.1, weber_y+0.1, f'Weber Point ({weber_x:.4f}, {weber_y:.4f})', fontsize=12)

# 各点とウェーバー点を結ぶ線
for x, y in points:
    plt.plot([x, weber_x], [y, weber_y], 'k--', alpha=0.5)

# グラフの設定
plt.grid(True)
plt.title('Weber Point Problem')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')  # アスペクト比を等しくする

# 各点から伸びる線が120度の角度を成すことを確認するための補助線（オプション）
# これはウェーバー点の特徴である
angles = [0, 120, 240]  # 120度ずつの角度
r = 1  # 補助線の長さ
for angle in angles:
    rad = math.radians(angle)
    plt.plot([weber_x, weber_x + r * math.cos(rad)], 
             [weber_y, weber_y + r * math.sin(rad)], 'g-', alpha=0.7)

# グラフ表示
plt.savefig('weber_point.png')
plt.show()

# 解析解と比較（このケースでは対称性から厳密解がわかる）
exact_x = 5
exact_y = 2 + math.sqrt(3)
print(f"Exact solution: ({exact_x:.6f}, {exact_y:.6f})")
print(f"Difference: ({weber_x-exact_x:.6f}, {weber_y-exact_y:.6f})")
