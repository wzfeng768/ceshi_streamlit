import streamlit as st
from navigation import add_navigation_bar  # 导入导航栏组件
from navigation import get_image_base64    # 导入图片解析函数
import os
import pathlib

# 设置页面标题和布局
st.set_page_config(
    page_title="Benchmark Platform for Polymer",
    layout="wide",
    initial_sidebar_state="collapsed"  # 初始状态下隐藏侧边栏
)
# 添加导航栏
add_navigation_bar()

# 获取 GIF 文件的绝对路径
current_dir = os.path.dirname(__file__)
image_path = os.path.join(current_dir, "image", "VCG211529742878.gif")
gif_base64 = get_image_base64(image_path)

image_folder = os.path.join(current_dir, "image")
icon_folder = os.path.join(image_folder, "icon")

# Load icon images
left_icon_path = os.path.join(icon_folder, "left_icon.png")
right_icon_path = os.path.join(icon_folder, "right_icon.png")
left_icon_base64 = get_image_base64(left_icon_path)
right_icon_base64 = get_image_base64(right_icon_path)

with st.container():
    # HTML 和 CSS
    html_code = f"""
    <style>
        .blue-background {{
            background-color: #008fd2;
            height: 35vh;
            position: relative;
            overflow: visible;
            border-bottom-left-radius: 15px;
            border-bottom-right-radius: 15px;
            display: flex;
            align-items: center;
        }}
        .gif-image {{
            position: absolute;
            top: 15%;
            left: 55%;
            height: 90%;
            width: auto;
        }}
        .content-text {{
            margin-left: 350px;
            color: white;
            width: 35%;
        }}
        .content-text h3 {{
            font-size: 36px;
        }}
        .content-text p {{
            font-size: 24px;
            width: 70%;
        }}
        .window {{
            border: 1px solid #ccc;
            padding: 0px;
            margin-top: 0px;
            text-align: center;
        }}
    </style>

    <div class="blue-background">
        <div class="gif-container">
            <img src="data:image/gif;base64,{gif_base64}" class="gif-image" alt="GIF Image">
        </div>
        <div class="content-text">
            <h3>Benchmark Platform for Polymer</h3>
            <p>Use AI to predict polymer properties to 
            facilitate new material development and industrial applications!</p>
        </div>
    </div>
    """

    # 在 Streamlit 中显示 HTML
    st.markdown(html_code, unsafe_allow_html=True)

# 添加空隙调整布局
st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)

# 最新资讯窗口
with st.container():
    # List of content with image paths, text, and links
    contents = [
        {
            "image": os.path.join(image_folder, "image1.png"),
            "text": "Content 1 text",
            "link": "https://example.com/content1"
        },
        {
            "image": os.path.join(image_folder, "image2.jpg"),
            "text": "Content 2 text",
            "link": "https://example.com/content2"
        },
        {
            "image": os.path.join(image_folder, "image3.jpg"),
            "text": "Content 3 text",
            "link": "https://example.com/content3"
        }
    ]

    # Initialize session state
    if "current_index" not in st.session_state:
        st.session_state.current_index = 0

    # Create columns
    col1, col2, col3, col4, col5 = st.columns([1.5, 2, 3, 2, 1.5])

    # Column 2: Latest News
    with col2:
        st.markdown("### Latest News & Updates")
        st.subheader("10-14-20")
        # Add more news items as needed

    # Column 4: Slider to select content
    with col4:
        # Add a 200px margin above the slider
        st.markdown('<div style="margin-top: 100px;"></div>', unsafe_allow_html=True)
        # Slider to select content
        st.session_state.current_index = st.slider("Select Content", 0, len(contents)-1, st.session_state.current_index)

    # Column 3: Display current content image and text
    with col3:
        current_content = contents[st.session_state.current_index]
        st.markdown(
            f'<a href="{current_content["link"]}" target="_blank">'
            f'<div style="display: flex; align-items: center; margin-bottom: 20px;">'
            f'   <img src="data:image/png;base64,{get_image_base64(current_content["image"])}" '
            f'        style="width: 400px; height: 200px; object-fit: cover;" />'
            f'   <p style="margin-left: 20px; vertical-align: middle;">{current_content["text"]}</p>'
            f'</div>'
            f'</a>',
            unsafe_allow_html=True
        )

st.markdown('<div style="height:50px;"></div>', unsafe_allow_html=True)

#概述窗口
with st.container():
    # Create columns
    col1, col2, col3, col4 = st.columns([1.5, 2, 5, 1.5])
    with col2:
        st.markdown("### Overview")
    with col3:
        st.write("The Open Catalyst Project is a collaborative research effort between Fundamental AI Research (FAIR) at Meta and Carnegie Mellon University's (CMU) Department of Chemical Engineering. The aim is to use AI to model and discover new catalysts for use in renewable energy storage to help in addressing climate change.")
        st.write("")
        st.write("Scalable and cost-effective solutions to renewable energy storage are essential to addressing the world's rising energy needs while reducing climate change. As we increase our reliance on renewable energy sources such as wind and solar, which produce intermittent power, storage is needed to transfer power from times of peak generation to peak demand. This may require the storage of power for hours, days, or months. One solution that offers the potential of scaling to nation-sized grids is the conversion of renewable energy to other fuels, such as hydrogen. To be widely adopted, this process requires cost-effective solutions to running chemical reactions.")
        st.write("")
        st.write("An open challenge is finding low-cost catalysts to drive these reactions at high rates. Through the use of quantum mechanical simulations (density functional theory), new catalyst structures can be tested and evaluated. Unfortunately, the high computational cost of these simulations limits the number of structures that may be tested. The use of AI or machine learning may provide a method to efficiently approximate these calculations, leading to new approaches in finding effective catalysts.")
        st.write("")
        st.write("The Open Catalyst Project is a research collaboration between FAIR and CMU to develop machine learning models to accelerate the discovery of new catalysts for renewable energy storage. The project aims to use AI to model and discover new catalysts for use in renewable energy storage to help in addressing climate change.")
        st.write("---")
        col1_overview, col2_overview, col3_overview = st.columns([3, 1, 6])
        with col1_overview:
                st.markdown("**Click to see the details, which describe the algorithm, polymer notation, evaluation metrics, and data sets.**")
        with col3_overview:
            html_content = '''
            <style>
                .custom-link {
                    color: black;
                }
                .custom-link:hover {
                    text-decoration: underline;
                    color: red;
                }
            </style>
            <ul>
                <li><a href="/Leaderboard" class="custom-link">Leaderboard</a></li>
                <li><a href="/Dataset" class="custom-link">Dataset</a></li>
                <li><a href="/Polymer_notation" class="custom-link">Polymer notation</a></li>
                <li><a href="/Machine_Learning" class="custom-link">Machine Learning</a></li>
                <li><a href="/Deep_Learning" class="custom-link">Deep Learning</a></li>
            </ul>
            '''
            st.markdown(html_content, unsafe_allow_html=True)

st.markdown('<div style="height:50px;"></div>', unsafe_allow_html=True)

#例子窗口
with st.container():

    # Create columns
    col1, col2, col3, col4 = st.columns([1.5, 2, 5, 1.5])
    with col2:
        st.markdown("### Examples")
    with col3:
        # Embed the video with specified width and height
        # Construct the path to the video file
        video_path = pathlib.Path(__file__).parent / "video" / "my_video.mp4"

        # Embed the video in the Streamlit app
        st.video(str(video_path))


st.markdown('<div style="height:100px;"></div>', unsafe_allow_html=True)

with st.container():
    # 联系信息
    st.markdown('<h3 style="text-align:center; margin-top:100px;">Contact Us</h3>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">Email: info@softuidesignsystem.com</p>', unsafe_allow_html=True)
    st.markdown('<p style="text-align:center;">Phone: +1 123 456 7890</p>', unsafe_allow_html=True)


