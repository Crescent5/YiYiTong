import streamlit as st

st.set_page_config(
    page_title="你好，欢迎使用医易通",
    page_icon="👋",
)

st.write("# 欢迎使用医易通! 👋")

st.sidebar.success("在上方选择一个功能。")

st.markdown(
    """
    医易通是一个专为中医知识科普和中医专业学生日常学习而构建的开源应用框架。

    **👈 从侧边栏选择一个功能**，看看**医易通**能做什么吧！
    ### 想了解更多吗？
    - 查看 [医易通简介](https://streamlit.io)
    - 阅读我们的 [功能介绍](https://docs.streamlit.io)
    - 在我们的 [社区论坛](https://discuss.streamlit.io) 提问
    ### 查看医易通发展规划
    - [未来功能开发](https://discuss.streamlit.io)
"""
)
