import streamlit as st
import base64

def add_navigation_bar():
    # 添加导航栏
    st.markdown(
        """
        <style>
        /* 消除页面和导航栏的空隙 */
        .stApp {
            margin: 0;
            padding: 0;
        }
        /* 导航栏样式 */
        .navbar {
            display: flex;
            justify-content: flex-end; /* 改进：将内容靠右对齐 */
            align-items: center;
            background-color: #008fd2; /* 蓝色背景 */
            padding: 15px 220px 15px 0; /* 改进：右侧留下120px空隙 */
            font-size: 18px; /* 增大字体 */
            width: 100%; /* 确保导航栏占满宽度 */
            box-sizing: border-box; /* 防止padding影响宽度 */
        }
        /* 导航链接样式 */
        .navbar a {
            margin: 0 20px; /* 增加间距 */
            text-decoration: none;
            color: white;
            transition: color 0.3s ease; /* 平滑过渡效果 */
        }
        .navbar a:hover {
            color: black; /* 鼠标悬停时变为黑色 */
        }
        /* 下拉菜单样式 */
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }
        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }
        .dropdown:hover .dropdown-content {
            display: block;
        }
        </style>
        <div class="navbar">
            <a href="/">Home</a>
            <a href="/Leaderboard">Leaderboard</a>
            <a href="/Dataset">Dataset</a>
            <a href="/Polymer_notation">Polymer notation</a>
            <div class="dropdown">
                <a href="#">AI</a>
                <div class="dropdown-content">
                    <a href="/Machine_Learning">Machine Learning</a>
                    <a href="/Deep_Learning">Deep Learning</a>
                </div>
            </div>
            <a href="/Guide">Guide</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# 获取 GIF 图片文件的 base64 编码
def get_image_base64(file_path):
    with open(file_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')