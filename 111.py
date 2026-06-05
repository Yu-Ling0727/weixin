import streamlit as st
import numpy as np
import matplotlib.pyplot as plt


def draw_gradient_heart():
    # 定义爱心轮廓的参数方程
    t = np.linspace(0, 2 * np.pi, 500)
    x = 16 * np.sin(t) ** 3
    y = (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))
    # 缩放使爱心适合绘图区
    x /= 20
    y /= 20

    # 创建画布和轴
    fig, ax = plt.subplots(figsize=(6, 6))

    # 创建渐变色：粉色到白色
    gradient = np.linspace(0, 1, 256).reshape(1, -1)  # 线性渐变

    # 显示渐变作为背景
    extent = [x.min(), x.max(), y.min(), y.max()]

    # 由于用fill不会自动渐变，所以用imshow实现背景渐变
    ax.imshow(gradient, extent=extent, origin='lower',
              cmap=plt.LinearSegmentedColormap.from_list('pink_white', ['#FFC0CB', '#FFFFFF']),
              aspect='auto')

    # 绘制爱心轮廓，透明填充
    from matplotlib.patches import PathPatch
    from matplotlib.path import Path

    vertices = np.column_stack((x, y))
    path = Path(vertices)
    patch = plt.matplotlib.patches.PathPatch(path, facecolor='pink', edgecolor='red', linewidth=2)
    ax.add_patch(patch)

    # 设定显示范围
    ax.set_xlim(x.min() - 0.01, x.max() + 0.01)
    ax.set_ylim(y.min() - 0.01, y.max() + 0.01)
    ax.set_aspect('equal')
    ax.axis('off')

    return fig


# 在Streamlit中展示
st.title("粉白渐变爱心")
fig = draw_gradient_heart()
st.pyplot(fig)