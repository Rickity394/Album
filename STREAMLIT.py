import streamlit as st
from sklearn.linear_model import LinearRegression
import feedparser
st.sidebar.title("Danh sách nghệ sĩ ")
selected_artist = st.sidebar.radio("chọn nghệ sĩ: ", ["Đen Vâu", "Hà Anh Tuấn", "Sơn Tùng M-TP"])

videos = {
    "Đen Vâu": [
        ("Bữa ăn cho em", "https://www.youtube.com/watch?v=ukHK1GVyr0I"),
        ("Mang tiền về cho mẹ", "https://www.youtube.com/watch?v=UVbv-PJXm14"),
        ("Trời hôm nay nhiều mây cực!", "https://www.youtube.com/watch?v=MBaF0l-PcRY"),
        ("Hai triệu năm", "https://www.youtube.com/watch?v=LSMDNL4n0kM")
    ],
    "Hà Anh Tuấn" : [
        ("Tuyết rơi mùa hè", "https://www.youtube.com/watch?v=pTh3KCD7Euc"),
        ("Nước ngoài", "https://www.youtube.com/watch?v=pU3O9Lnp-Z0"),
        ("Tháng tư là lời nói dối của em", "https://www.youtube.com/watch?v=UCXao7aTDQM"),
        ("Xuân thì", "https://www.youtube.com/watch?v=3s1r_g_jXNs")        
    ],
    "Sơn Tùng M-TP": [
        ("Lạc trôi", "https://www.youtube.com/watch?v=Llw9Q6akRo4"),
        ("Chúng ta không thuộc về nhau", "https://www.youtube.com/watch?v=qGRU3sRbaYw"),
        ("Muộn rồi mà sao còn", "https://www.youtube.com/watch?v=xypzmu5mMPY"),
        ("Hãy trao cho anh", "https://www.youtube.com/watch?v=knW7-x7Y7RE")
    ]
}
st.title(" ứng dụng giải trí và sức khỏe ")

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["MV yêu thích", "Dự đoán giờ đi ngủ", "Đọc báo", "Gia Vang","BMI calculations", "Walking Steps", "Height"])
with tab1:
    st.header(f"Các bài hát của {selected_artist} ")
    for title, url in videos[selected_artist]:
        st.subheader(title)
        st.video(url)
with tab2:
    st.header(f"songs: {selected_artist}")
    x = [
        [10, 1, 8],
        [20, 5, 6],
        [25, 8, 3],
        [30, 6, 5],
        [35, 2, 9],
        [40, 4, 3]
    ]
    y = [10, 8, 6, 7, 9.5, 9], [12, 5, 3, 8, 1, 4], [10, 8, 6, 7, 9.5, 9], [12, 5, 3, 8, 1, 4], [10, 8, 6, 7, 9.5, 9], [12, 5, 3, 8, 1, 4]
    model = LinearRegression()
    model.fit(x,y)
    st.write("Write ur Info: ")
    age = st.number_input("Age: ", min_value=5, max_value=100, value=25)
    activity = st.slider("Activity period: (1 = low, 10 = much)", 1, 10, 5)
    screen_time = st.number_input("Screen time: (1 = good, 10 = bad)", min_value = 0, max_value = 24, value=6)
    if st.button("guess the day: "):
        input_data = [[age, activity, screen_time]]
        result = model.predict(input)[0]
        st.success(f"You should sleep around {result: 1f}hours per night")
        if result < 6.5:
            st.warning("Maybe you should sleep more to gain energy")
        elif result > 9:
            st.info("Maybe u are now good")
        else:
            st.success("W sleep")
with tab3:
    st.header("hot infos from VnExpress")
    feed = feedparser.parse("https://vnexpress.net/rss/tin-moi-nhat.rss")
    for entry in feed.entries[:5]:
        st.subheader(entry.title)
        st.write(entry.published)
        st.write(entry.link)
with tab4:
    st.header("💰 Cập nhật giá vàng từ Vietnamnet")

    feed = feedparser.parse("https://vietnamnet.vn/rss/kinh-doanh.rss")
    gold_news = [entry for entry in feed.entries if "vàng" in entry.title.lower() or "giá vàng" in entry.summary.lower()]

    if gold_news:
        for entry in gold_news[:5]:  # Hiện 5 bài gần nhất
            st.subheader(entry.title)
            st.write(entry.published)
            st.write(entry.link)
    else:
        st.warning("Không tìm thấy bản tin giá vàng gần")

with tab5:
    st.header("check BMI")
    weight = st.number_input("Write your weight: (kg)", min_value=10.0, max_value=200.0, value=60.0, step=0.1)
    height = st.number_input("Write your height: (kg)", min_value=1.0, max_value=2.5, value=1.7, step=0.01)
    
    if st.button("BMI calculation"):
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi: .2f}")

        if bmi < 18.5:
            st.warning("You need wight donkey, eat more vro")
        elif 18.5 <= bmi < 25:
            st.info("You have normal weight, keep going")
        elif 25 <= bmi < 30:
            st.warning("You are a little slight off weight, try to eat less")
        else:
            st.error("You are fat, eat less bro")
with tab6:
    st.header("Amount of walking steps")
    age2 = st.number_input("Write your age: ", min_value=0.0, max_value=130.0, value=18.0, step=1.0)
    if st.button("Check walking steps"):
        st.success(f"Your age: {int(age2)}")

    if age2 < 18:
        st.info("Bạn nên đi từ 12000 - 15000 bước mỗi ngày. ")
    elif 18 <= age2 < 40:
        st.info("Bạn nên đi từ 8000 bước đến 10000 bước mỗi ngày. ")
    elif 40 <= age2 < 65:
        st.warning("bạn nên đi từ 7000 bước đến 9000 bước mỗi ngày. ")
    elif age2 >= 65:
        st.warning("Bạn nên đi từ 6000 bước đến 8000 bước mỗi ngày")
    else:
        st.error("tuổi không hợp lệ ")
with tab7:
    st.header("Checking height")
    age = st.number_input("Enter age: ", min_value = 0, max_value = 120, step=1)
    height = st.number_input("Enter height: ", min_value=30.0, max_value = 250.0, step=0.1)
    if st.button("check"):
        if age < 5:
            min_height, max_height = 90, 100
        elif 5 <= age <= 7:
            min_height, max_height = 110, 130
        elif 8 <= age <= 10:
            min_height, max_height = 130, 140
        elif 11 <= age <= 13:
            min_height, max_height = 140, 150
        elif 14 <= age <= 16:
            min_height, max_height = 150, 170
        elif age > 16:
            min_height, max_height = 160, 180
        else:
            st.warning("no standard height data vailable for this age. ")
            st.stop()
        if height < min_height:
            st.error("Your height is below the standard")
        elif height > max_height:
            st.warning("Your height is above standard")
        else:
            st.success("Your height is within the standard range")
