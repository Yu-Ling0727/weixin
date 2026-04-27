import streamlit as st
import time

# --- 1. 页面设置 ---
st.set_page_config(page_title="好友鉴定中心", page_icon="🕵️", layout="centered")

# 隐藏默认的页眉页脚
hide_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# --- 2. 标题区域 ---
st.title("🕵️ 好友品质鉴定中心 🕵️")
st.markdown("### 请输入您的真实姓名，系统将自动分析您的品格与运势")
st.markdown("---")

# --- 3. 输入框 ---
name = st.text_input("请输入姓名：", placeholder="在此输入...")

# --- 4. 核心逻辑判断 ---
if st.button("开始鉴定", type="primary"):

    # 定义恶搞名单（不区分大小写更稳妥，这里直接匹配）
    bad_names = ['王楦博', '陈明凯']

    # 背景音乐链接 (这里使用网络直链，您可以换成自己喜欢的)
    # 喜庆音乐
    happy_music = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
    # 搞怪/悲伤音乐 (比如“猪八戒背媳妇”或者搞笑笑声)
    funny_music = "https://www.soundjay.com/human/sounds/laugh-male-1.mp3"

    # 判断逻辑
    if name in bad_names:
        # --- 恶搞模式 ---
        st.markdown("""
        <div style="background-color:#ffcccc; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:red;">⚠️ 警告 ⚠️</h1>
        <h2 style="color:black;">检测到智商不足！</h2>
        <p style="font-size:20px; color:grey;">建议立刻充值智商...</p>
        </div>
        """, unsafe_allow_html=True)

        # 显示一张搞笑图片 (网络素材链接，可替换)
        st.image("https://img.zcool.cn/community/0142135d3980b9a801213f26c7c875.gif", caption=f"{name} 的真实面目",
                 use_column_width=True)

        st.markdown(f"### 😂 对不起 **{name}** 同学，你是笨蛋！")
        st.audio(funny_music, format="audio/mp3")  # 播放搞笑音乐

        # 加一个无限加载动画吓唬人（实际只会转几秒）
        with st.spinner('系统正在尝试修复你的智商...修复失败...'):
            time.sleep(3)
        st.error("修复失败，请放弃治疗！🤣")

    else:
        # --- 祝福模式 ---
        st.markdown("""
        <div style="background-color:#ccffcc; padding:20px; border-radius:10px; text-align:center;">
        <h1 style="color:green;">✨ 完美 ✨</h1>
        <h2 style="color:black;">天选之人</h2>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### 🎉 恭喜 **{name}** 同学！")
        st.markdown("#### 经系统鉴定，您是一位：")
        st.markdown("# 💖 善良、美丽、智慧的天使 💖")

        # 撒花特效
        st.balloons()

        # 鲜花图片
        st.image("https://img.zcool.cn/community/015d365544d0b9000001bf729cdce5.jpg@1280w_1l_2o_100sh.jpg",
                 caption="送给你最美的花", use_column_width=True)

        st.markdown("#### 愿你三冬暖，愿你春不寒！")
        st.audio(happy_music, format="audio/mp3")  # 播放喜庆音乐
