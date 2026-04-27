import streamlit as st

# 1. 设置网页标题
st.title('我的第一个微信工具')

# 2. 添加输入框
# 这里用 st.number_input 创建一个输入框，并给它起个名字
a = st.number_input('请输入第一个数字', value=0)
b = st.number_input('请输入第二个数字', value=0)

# 3. 添加按钮和逻辑
# 当用户点击按钮时，进行计算
if st.button('点击计算'):
    result = a + b
    # 在网页上显示结果
    st.success(f'计算结果是：{result}')