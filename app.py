import streamlit as st
import numpy as np
import plotly.graph_objects as go
import time

# --- 1. 页面基础设置 ---
st.set_page_config(page_title="浪漫爱心", page_icon="❤️", layout="wide")

# 隐藏 Streamlit 默认的边栏和页眉页脚，实现全屏浪漫效果
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)


# --- 2. 生成 3D 爱心数据 (数学公式) ---
def generate_heart_points(scale=1, density=100):
    # 使用 3D 爱心参数方程
    u = np.linspace(0, 2 * np.pi, density)
    v = np.linspace(0, np.pi, density)
    x = scale * 16 * np.sin(v) ** 3
    y = scale * (13 * np.cos(v) - 5 * np.cos(2 * v) - 2 * np.cos(3 * v) - np.cos(4 * v))
    z = scale * 16 * np.cos(u) * np.sin(v) ** 3

    # 为了画出形状，我们需要生成网格
    # 这��我们使用参数方程的变体生成一个漂亮的表面
    phi = np.linspace(0, np.pi, 50)
    theta = np.linspace(0, 2 * np.pi, 50)
    phi, theta = np.meshgrid(phi, theta)

    # 爱心数学方程
    x = 16 * (np.sin(theta) ** 3) * np.sin(phi)
    y = 13 * np.cos(theta) - 5 * np.cos(2 * theta) - 2 * np.cos(3 * theta) - np.cos(4 * theta)
    z = 16 * (np.sin(theta) ** 3) * np.cos(phi)

    return x, y, z


# --- 3. 绘图设置 ---
x, y, z = generate_heart_points()

# 创建 3D 散点图 (看起来更像粒子效果)
fig = go.Figure(data=go.Scatter3d(
    x=x.flatten(),
    y=y.flatten(),
    z=z.flatten(),
    mode='markers',
    marker=dict(
        size=4,
        color=y.flatten(),  # 根据高度变色，更有层次感
        colorscale='Reds',  # 红色渐变
        opacity=0.8,
        line=dict(width=0.5, color='DarkRed')  # 给粒子加个边框
    )
))

# --- 4. 布局美化 (背景、视角、动画) ---
fig.update_layout(
    scene=dict(
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        zaxis=dict(visible=False),
        bgcolor='rgba(0,0,0,0)'  # 透明背景，配合 Streamlit 背景
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=0, b=0),
    scene_camera=dict(eye=dict(x=0, y=0, z=2))  # 初始视角
)

# 设置自动旋转动画
fig.update_layout(
    scene_camera=dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1.5, y=1.5, z=0.5)
    )
)

# --- 5. 页面排版与配文 ---

# 设置背景色为深色浪漫主题
st.markdown("""
<style>
body {
    background-color: #0e1117;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# 使用 CSS 动画让文字缓慢浮现
text_style = """
<style>
.fading-text {
    font-family: 'Songti SC', 'SimSun', serif;
    font-size: 28px;
    color: #ffb6c1;
    text-align: center;
    margin-top: 50px;
    animation: fadeIn 3s;
}
@keyframes fadeIn {
    0% { opacity: 0; }
    100% { opacity: 1; }
}
</style>
"""
st.markdown(text_style, unsafe_allow_html=True)

# 渲染标题和配文
st.title("")
st.title("")
st.markdown('<p class="fading-text">朝暮与岁月并往<br>愿我们一同行至天光</p>', unsafe_allow_html=True)

# 渲染 3D 爱心
st.plotly_chart(fig, use_container_width=True)

# 底部署名
st.markdown("""
<p style="text-align: center; color: grey; font-size: 12px;">
Made with Python ❤️
</p>
""", unsafe_allow_html=True)

# 添加简单的交互按钮（彩蛋）
with st.expander("💌 点击这里，送你一朵花"):
    st.write("🌸 愿你的生活常有花香与暖阳 🌸")
    st.balloons()