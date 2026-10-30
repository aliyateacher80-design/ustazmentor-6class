import streamlit as st
import pandas as pd

# 1. Беттің баптаулары
st.set_page_config(
    page_title="UstazMentor - 6-сынып | Modern Glassmorphism Edition", 
    page_icon="💻", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Дерекқор сессиясын бастау
if "results_db" not in st.session_state:
    st.session_state.results_db = []

# 2. MODERN GLASSMORPHISM ПРЕМИУМ СТИЛЬДЕРІ (CSS)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311045 100%) !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        color: #f1f5f9 !important;
    }

    [data-testid="stHeader"], [data-testid="stSidebar"] {
        display: none !important;
    }

    /* SaaS Hero Banner Glassmorphism стилінде */
    .main-header {
        background: rgba(30, 41, 59, 0.7) !important;
        backdrop-filter: blur(16px) !important;
        -webkit-backdrop-filter: blur(16px) !important;
        padding: 35px;
        border-radius: 24px;
        color: white;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
        margin-bottom: 25px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .main-header h1 {
        font-size: 2.7rem;
        font-weight: 800;
        background: linear-gradient(90deg, #38bdf8 0%, #a855f7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 8px;
    }

    /* Ойын карточкасы мен Сценарий боксы (Glass Card) */
    .scenario-box {
        background: rgba(30, 41, 59, 0.6) !important;
        backdrop-filter: blur(12px) !important;
        border: 1px solid rgba(56, 189, 248, 0.3) !important;
        border-radius: 20px !important;
        padding: 22px !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3) !important;
        margin-bottom: 20px !important;
        color: #e2e8f0 !important;
    }

    /* Статистика бейдждері */
    .stat-badge {
        background: rgba(15, 23, 42, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(234, 179, 8, 0.4);
        border-radius: 16px;
        padding: 14px;
        text-align: center;
        font-weight: 700;
        color: #facc15;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        margin-bottom: 15px;
    }

    /* Премиум SaaS Батырмалары */
    .stButton > button, div[data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%) !important;
        color: #ffffff !important;
        font-weight: 700 !important;
        font-size: 1.05rem !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 14px !important;
        padding: 0.75rem 2rem !important;
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        width: 100%;
    }
    .stButton > button:hover, div[data-testid="stFormSubmitButton"] > button:hover {
        background: linear-gradient(135deg, #2563eb 100%, #7c3aed 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 15px 30px rgba(139, 92, 246, 0.5) !important;
    }

    /* Енгізу өрістері мен Selectbox */
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div,
    .stNumberInput > div > div > input {
        background: rgba(15, 23, 42, 0.6) !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        border-radius: 14px !important;
        color: #ffffff !important;
        font-weight: 600 !important;
        padding: 10px 15px !important;
    }

    /* DataFrame & Tables */
    [data-testid="stDataFrame"] {
        background: rgba(30, 41, 59, 0.5);
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Басты декоративті Hero Section
st.markdown(
    """
    <div class="main-header">
        <h1>UstazMentor 💻 6-сынып</h1>
        <p style="font-size: 17px; font-weight: 600; color: #38bdf8; margin-top: 5px;">⭐ Бір тақырып — бір өмірлік жағдаят — нақты нәтиже!</p>
        <p style="font-size: 13px; color: #94a3b8; margin-top: 5px;">Modern Glassmorphism • Интерактивті Дебаггер • SaaS Мониторинг</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Тақырыптар тізімі
sections_dict = {
    "📁 Бөлім: Компьютерлік жүйелер және қауіпсіздік": [
        "1. Қауіпсіздік және Интернет желісінде жұмыс кезіндегі жауапкершілік — 🕵️‍♂️ Дебаггер",
        "2. Қауіпсіздік және Интернет желісінде жұмыс кезіндегі жауапкершілік (Практикалық жұмыс) — 🎮 Мини-ойын",
        "3. Жасанды интеллектідегі деректердің рөлі — 📝 Тест",
        "4. Жүйелік блок құрылғысы және компьютердің жадысы — 🕵️‍♂️ Дебаггер",
        "5. Жүйелік блок құрылғысы және компьютердің жадысы (Практикалық жұмыс) — 🔗 Сәйкестендіру",
        "6. Файлдық жүйе және программалық жасақтама — 🧩 Виртуалды конструктор (Файлдарды сұрыптау)",
        "7. Файлдық жүйе және программалық жасақтама (Практикалық жұмыс) — 🎮 Ойын",
    ],
    "📁 Бөлім: Векторлық және растрлық графика": [
        "8. Векторлық графикалық редактор — 🧩 Виртуалды конструктор (Графиканы ажырату)",
        "9. Векторлық графикалық редактор (Бекіту және қолдану) — 📝 Тест",
        "10. Векторлық кескіндерді құру (Практикалық жұмыс) — 🔗 Сәйкестендіру (Құралдар)",
        "11. Векторлық кескіндерді құру (Бекіту және қолдану) — 🎨 Мини-ойын: Қабаттарды құтқар",
    ],
}

all_topics = []
for sec, topics in sections_dict.items():
    all_topics.extend(topics)

# Навигация батырмасы
role = st.radio(
    "🎯 Платформа режимін таңдаңыз:", ["👨‍🎓 Оқушы режимі (Game Hub)", "👩‍🏫 Мұғалім кабинеті (SaaS Dashboard)"], horizontal=True
)
st.divider()

# ==========================================
# 👩‍🏫 МҰҒАЛІМ КАБИНЕТІ (SaaS Dashboard)
# ==========================================
if role == "👩‍🏫 Мұғалім кабинеті (SaaS Dashboard)":
    st.subheader("👨‍💻 Мұғалімнің басқару және мониторинг панелі 🔗")
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        save_results_enabled = st.toggle("📊 Оқушы нәтижелерін базаға сақтау", value=True)
        selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict.keys()))
        selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict[selected_section])
    with col_m2:
        timer_val = st.number_input("Сабаққа арналған таймер (минут):", value=15)
        st.info(f"💡 **Таңдалған сабақ:** {selected_topic}")
    
    st.markdown("### 🔗 Оқушыларға арналған автоматты сілтеме:")
    shareable_url = f"https://ustazmentor-6class.streamlit.app/?topic={selected_topic}&timer={timer_val}&save={'1' if save_results_enabled else '0'}"
    st.code(shareable_url)
    
    st.divider()
    st.subheader("📊 Оқушылардың нәтижелері мен статистикасы")
    
    if len(st.session_state.results_db) > 0:
        df_results = pd.DataFrame(st.session_state.results_db)
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            filter_grade = st.selectbox("Сыныбы бойынша сүзу:", ["Барлығы"] + list(df_results["grade"].unique()))
        with col_f2:
            filter_topic = st.selectbox("Тақырыбы бойынша сүзу:", ["Барлығы"] + list(df_results["topic"].unique()))
            
        filtered_df = df_results.copy()
        if filter_grade != "Барлығы":
            filtered_df = filtered_df[filtered_df["grade"] == filter_grade]
        if filter_topic != "Барлығы":
            filtered_df = filtered_df[filtered_df["topic"] == filter_topic]
            
        st.dataframe(filtered_df, use_container_width=True)
        
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Нәтижелерді Excel (CSV) форматында жүктеу",
            data=csv_data,
            file_name="ustazmentor_6class_results.csv",
            mime="text/csv",
        )
        
        if st.button("🗑️ Барлық нәтижелерді тазарту"):
            st.session_state.results_db = []
            st.rerun()
    else:
        st.info("ℹ️ Әзірге сақталған нәтижелер тізімі бос. Оқушылар тапсырма орындап жіберген соң осында кесте түрінде шығады.")

# ==========================================
# 👨‍🎓 ОҚУШЫ РЕЖИМІ (Game Hub)
# ==========================================
else:
    # Статистика бейдждері
    col_stat1, col_stat2, col_stat3 = st.columns(3)
    with col_stat1:
        st.markdown('<div class="stat-badge">🥉 Бронза деңгейі<br><span style="font-size:0.8rem; color:#94a3b8;">Бастаушы Кодшы</span></div>', unsafe_allow_html=True)
    with col_stat2:
        st.markdown('<div class="stat-badge">🥈 Күміс деңгейі<br><span style="font-size:0.8rem; color:#94a3b8;">Жетілдіруші Хакер</span></div>', unsafe_allow_html=True)
    with col_stat3:
        st.markdown('<div class="stat-badge">🥇 Алтын деңгей<br><span style="font-size:0.8rem; color:#94a3b8;">IT Магистрі</span></div>', unsafe_allow_html=True)

    st.subheader("👨‍🎓 Оқушы кабинеті")
    col_name, col_class = st.columns([2, 1])
    with col_name:
        student_name = st.text_input(
            "Аты-жөніңізді енгізіңіз (Мысалы: Айдын Б.):",
            placeholder="Аты-жөніңіз...",
        )
    with col_class:
        student_grade = st.selectbox(
            "Сыныбыңыз:", ["6 «Ә»", "6 «А»", "6 «Б»", "6 «В»"]
        )

    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics)
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_topic}")
    st.divider()

    # --- 1. ҚАУІПСІЗДІК ДЕБАГГЕРІ ---
    if "1. Қауіпсіздік" in selected_topic and "Дебаггер" in selected_topic:
        st.markdown(
            """
            <div class="scenario-box">
                <b>📜 Шынайы өмірлік жағдаят (Сценарий):</b><br>
                «Оқушы Арман интернетте отырып төмендегідей әрекеттер жасады:<br>
                1. Барлық әлеуметтік желілердегі аккаунттарына кіру үшін бір ғана оңай құпия сөз қолданды: <code>"12345678"</code>.<br>
                2. Поштасына бейтаныс біреуден «Сіз смартфон ұтып алдыңыз, тез арада мына сілтемеге өтіп жеке деректеріңіз мен банк картаңызды жазыңыз» деген хат келгенде, қуанып кетіп бірден сілтемеге өтті.<br>
                3. Интернетте біреу оны мазақ етіп жазған кезде, ол өзін жоғалтпай, жауап ретінде ол балаға басқаларды қорлайтын дөрекі сөздер мен арсыз хаттар жазып қайтарды.»
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("debug_sec"):
            ans1 = st.radio(
                "1-қате (Құпия сөз): Арманның құпия сөзінде қандай қате кетті?",
                [
                    "-- Жауапты таңдаңыз --",
                    "А) Қате жоқ, бұл өте ыңғайлы құпия сөз.",
                    "Б) Құпия сөз тым әлсіз (12345678), оны әріптер, цифрлар және арнайы таңбалардың араласуынан тұратын күрделі сөзге ауыстыру керек.",
                    "В) Құпия сөзді тек туған жылмен алмастыру керек.",
                ],
            )
            ans2 = st.radio(
                "2-қате (Фишинг): Бейтаныс адамнан келген ұтыс туралы хат пен сілтемеге қатысты Арманның қатесі неде?",
                [
                    "-- Жауапты таңдаңыз --",
                    "А) Арман дереу сілтемеге өтіп, жеке деректерін беруі дұрыс болды.",
                    "Б) Бұл — фишинг (алаяқтық) қаупі. Күмәнді сілтемелерге жеке деректерді жазуға болмайды, дереу хатты өшіру немесе ескерту керек.",
                    "В) Тек банк картасының нөмірін ғана жазу керек еді.",
                ],
            )
            ans3 = st.radio(
                "3-қате (Кибербуллинг): Мазақтаған балаға жауап ретінде дөрекі сөздер жазуы неліктен қате?",
                [
                    "-- Жауапты таңдаңыз --",
                    "А) Бұл ешқандай қате емес, өзін қорғаудың жолы.",
                    "Б) Бұл кибербуллингтің өршуіне әкеледі. Интернетте де әдеп нормаларын сақтап, үлкендерге немесе мұғалімге хабарлау қажет.",
                    "В) Тек смайлик жіберу жеткілікті еді.",
                ],
            )

            if st.form_submit_button("Дебаггерді тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    c = 0
                    if (
                        "Б) Құпия сөз тым әлсіз" in ans1
                        and "Б) Бұл — фишинг" in ans2
                        and "Б) Бұл кибербуллингтің" in ans3
                    ):
                        c = 3
                    elif (
                        "Б) Құпия сөз тым әлсіз" in ans1
                        or "Б) Бұл — фишинг" in ans2
                        or "Б) Бұл кибербуллингтің" in ans3
                    ):
                        c = 2
                    st.balloons()
                    st.success(
                        f"🎉 Құттықтаймыз, {student_name}! Табылған қателер саны: {c} / 3"
                    )
                    st.session_state.results_db.append({
                        "name": student_name,
                        "grade": student_grade,
                        "topic": selected_topic,
                        "task_type": "Дебаггер (Қауіпсіздік)",
                        "score": f"{c} / 3 қате",
                    })

    # --- 2. ПРАКТИКАЛЫҚ ЖҰМЫС (Векторлық ойын сілтемесі) ---
    elif "2. Қауіпсіздік" in selected_topic and "Мини-ойын" in selected_topic:
        st.markdown("#### 🎮 Практикалық тапсырма (Интерактивті мини-ойын)")
        st.info("Бұл тапсырма сыртқы интерактивті платформа арқылы орындалады.")
        st.link_button("Ойынды ашу 🚀", "https://aliyateacher80-design.github.io/vektor-game-6/")

    # --- 3. ЖАСАНДЫ ИНТЕЛЛЕКТ ДЕРЕКТЕРІ (ТЕСТ) ---
    elif "3. Жасанды интеллектідегі деректердің рөлі" in selected_topic:
        st.markdown("#### 📝 Тест: «Жасанды интеллектідегі деректердің рөлі»")
        with st.form("ai_test"):
            q1 = st.radio(
                "1. Шикі, өңделмеген фактілер, сандар, өлшемдер немесе белгілер қалай аталады?",
                ["А) Білім", "В) Ақпарат", "С) Деректер (Data)", "D) Интеллект"],
            )
            q2 = st.radio(
                "2. «Деректердің» белгілі бір контекстке қойылып, өңделгеннен кейінгі мағыналы түрі:",
                ["А) Ақпарат (Information)", "В) Деректер", "С) Болжам", "D) Алгоритм"],
            )
            q3 = st.radio(
                "3. Ақпаратты түсініп, тәжірибеде қолдану арқылы қалыптасатын жоғары сатыдағы ұғым:",
                ["А) Деректер", "В) Білім (Knowledge)", "С) Бастапқы код", "D) Сигнал"],
            )
            q4 = st.radio(
                "4. Төмендегілердің қайсысы «деректерге» мысал бола алады?",
                [
                    "А) «Бүгінгі ауа райы – +25 градус, күн ашық» деген есептеу есебі",
                    "В) «Астана – Қазақстанның елордасы» деген анықтама",
                    "С) «25», «Алматы», «3.14», «мектеп» сияқты жекелеген мәндер мен сандар",
                    "D) Компьютерді қалай жөндеу керектігі туралы нұсқаулық",
                ],
            )
            q5 = st.radio(
                "5. ЖИ модельдерін оқытуда деректердің негізгі рөлі қандай?",
                [
                    "А) ЖИ моделінің өлшемін кішірейту үшін",
                    "В) Модельге заңдылықтарды, үлгілерді (паттерндерді) танып үйрету және шешім қабылдауға негіз болу үшін",
                    "С) Тек компьютердің жадын толтыру үшін",
                    "D) Интернет жылдамдығын арттыру үшін",
                ],
            )
            q6 = st.radio(
                "6. ЖИ жүйесіне оқыту үшін сапасыз немесе қате деректер берілсе, не болады?",
                ["А) Модель әлдеқайда ақылды болады", "В) Модель қате нәтижелер шығарады («Garbage in, garbage out»)", "С) Модель өздігінен түзетіліп кетеді", "D) Ешқандай өзгеріс болмайды"],
            )
            q7 = st.radio(
                "7. Суреттерді танитын ЖИ моделін оқыту үшін ең бірінші не қажет?",
                ["А) Көп мөлшерде белгіленген (таңбаланған) суреттер жиынтығы", "В) Қымбат бағалы пернетақта", "С) Тек мәтіндік кітаптар", "D) Жылдам принтер"],
            )
            q8 = st.radio(
                "8. «Деректер», «ақпарат» және «білім» ұғымдарының дұрыс иерархиялық реті:",
                ["А) Білім → Ақпарат → Деректер", "В) Деректер → Ақпарат → Білім", "С) Ақпарат → Деректер → Білім", "D) Деректер → Білім → Ақпарат"],
            )
            q9 = st.radio(
                "9. Компьютерлік жүйелерде суреттер мен мәтіндерді өңдеу не арқылы жүзеге асады?",
                ["А) Машиналық оқыту арқылы", "Б) Механикалық күшпен", "С) Қолмен сызу арқылы", "Д) Тек сымсыз желімен"],
            )
            q10 = st.radio(
                "10. Жасанды интеллект нәтижесінің дәл болуы неге байланысты?",
                ["А) Дұрыс таңдалған сапалы деректер жиынтығы", "Б) Монитордың үлкендігіне", "С) Пернетақта түсіне", "Д) Бөлме жарығына"],
            )

            if st.form_submit_button("Тестті тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    score = 0
                    if "С) Деректер (Data)" in q1: score += 1
                    if "А) Ақпарат (Information)" in q2: score += 1
                    if "В) Білім (Knowledge)" in q3: score += 1
                    if "С) «25», «Алматы»" in q4: score += 1
                    if "В) Модельге заңдылықтарды" in q5: score += 1
                    if "В) Модель қате нәтижелер" in q6: score += 1
                    if "А) Көп мөлшерде белгіленген" in q7: score += 1
                    if "В) Деректер → Ақпарат → Білім" in q8: score += 1
                    if "А) Машиналық оқыту арқылы" in q9: score += 1
                    if "А) Дұрыс таңдалған сапалы" in q10: score += 1

                    st.balloons()
                    st.success(f"🎉 Нәтижеңіз, {student_name}: **{score} / 10** ұпай 🌟")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Тест (ЖИ деректері)", "score": f"{score} / 10"
                    })

    # --- 4. ЖҮЙЕЛІК БЛОК ДЕБАГГЕРІ ---
    elif "4. Жүйелік блок" in selected_topic and "Дебаггер" in selected_topic:
        st.markdown(
            """
            <div class="scenario-box">
                <b>📜 Мәтіндегі 4 қатені табу (Дебаггер тапсырмасы):</b><br>
                «Арман информатика кабинетінде компьютердің құрылысын зерттеді. Ол жүйелік блоктың ішіндегі барлық құрылғылар өзара жалғанатын негізгі бөлшек – <u>қуат көзі</u> екенін анықтады. Компьютердің есептеулерін жүзеге асыратын «миы» – <u>қатты диск</u> болып табылады. Арман интернеттен маңызды ақпаратты көшіріп алып, компьютерді өшіріп тастады. Ол деректер тек <u>RAM (тұрақты жадыда)</u> қалады деп сенді, өйткені бұл жады түрі электр тогы өшсе де мәліметті сақтай береді. Сондай-ақ процессордың жұмыс жылдамдығы оның <u>сыртқы түсімен</u> өлшенетінін білді.»
            </div>
            """,
            unsafe_allow_html=True,
        )

        with st.form("hw_debug"):
            d1 = st.text_input("1. Негізгі плата қалай аталуы керек?")
            d2 = st.text_input("2. Компьютердің «миы» (процессор)?")
            d3 = st.text_input("3. Тоқ өшсе де сақталатын тұрақты жады?")
            d4 = st.text_input("4. Процессор жылдамдығының өлшем бірлігі?")

            if st.form_submit_button("Дебаггерді тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    c = 0
                    if "аналық" in d1.lower() or "motherboard" in d1.lower(): c += 1
                    if "процессор" in d2.lower() or "cpu" in d2.lower(): c += 1
                    if "rom" in d3.lower() or "тұрақты" in d3.lower(): c += 1
                    if "гц" in d4.lower() or "жиілік" in d4.lower(): c += 1

                    st.balloons()
                    st.success(f"🎉 Жарайсың, {student_name}! Табылған дұрыс түзетулер: {c} / 4")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Дебаггер (Аппараттық)", "score": f"{c} / 4 қате түзелді"
                    })

    # --- 5. ЖҮЙЕЛІК БЛОК СӘЙКЕСТЕНДІРУІ ---
    elif "5. Жүйелік блок" in selected_topic and "Сәйкестендіру" in selected_topic:
        st.markdown("#### 🔗 Сәйкестендіру: Компьютер құрылғылары және жады түрлері")
        with st.form("hw_match"):
            m1 = st.selectbox("1. Орталық процессор (CPU)", ["-- Таңдаңыз --", "Г) Барлық есептеулерді орындайтын және компьютердің жұмысын басқаратын негізгі «миы».", "А) Уақытша жады"])
            m2 = st.selectbox("2. RAM (Жедел жады)", ["-- Таңдаңыз --", "Г) Миы", "А) Компьютер қосулы тұрғанда деректерді уақытша сақтайды, өшкенде жойылады."])
            m3 = st.selectbox("3. ROM (Тұрақты жады)", ["-- Таңдаңыз --", "Б) Компьютерді қосқан кезде іске қосылатын бастапқы бағдарламаларды (BIOS) сақтайды.", "В) Кэш"])
            m4 = st.selectbox("4. Кэш-жады", ["-- Таңдаңыз --", "В) Процессор мен жедел жады арасындағы мәлімет алмасуды жылдамдататын өте жылдам жады.", "Д) Жылу"])
            m5 = st.selectbox("5. Тактілік жиілік", ["-- Таңдаңыз --", "Д) Процессордың 1 секундта қанша операция жасай алатынын көрсететін сипаттамасы.", "Г) Миы"])

            if st.form_submit_button("Сәйкестікті тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    sc = 0
                    if "Г)" in m1: sc += 1
                    if "А)" in m2: sc += 1
                    if "Б)" in m3: sc += 1
                    if "В)" in m4: sc += 1
                    if "Д)" in m5: sc += 1
                    st.balloons()
                    st.success(f"🎉 Нәтижеңіз: **{sc} / 5** дұрыс сәйкестік 🎯")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Сәйкестендіру (Аппараттық)", "score": f"{sc} / 5"
                    })

    # --- 6. ФАЙЛДЫҚ ЖҮЙЕ КОНСТРУКТОРЫ ---
    elif "6. Файлдық жүйе" in selected_topic:
        st.markdown("#### 🧩 Виртуалды конструктор: «Файлдарды қалталарға орналастыру»")
        with st.form("file_sort"):
            f1 = st.selectbox("📄 сабақ_жоспары.docx", ["-- Қалтаны таңдаңыз --", "📁 Мәтіндер мен кестелер", "📁 Мультимедиа", "📁 Графика", "📁 Программалар"])
            f2 = st.selectbox("📄 оқушылар_тізімі.xlsx", ["-- Қалтаны таңдаңыз --", "📁 Мәтіндер мен кестелер", "📁 Мультимедиа", "📁 Графика", "📁 Программалар"])
            f3 = st.selectbox("🎵 қоңырау_әуені.mp3", ["-- Қалтаны таңдаңыз --", "📁 Мәтіндер мен кестелер", "📁 Мультимедиа", "📁 Графика", "📁 Программалар"])
            f4 = st.selectbox("🖼️ аватарка.jpg", ["-- Қалтаны таңдаңыз --", "📁 Мәтіндер мен кестелер", "📁 Мультимедиа", "📁 Графика", "📁 Программалар"])
            f5 = st.selectbox("💻 ойын.py", ["-- Қалтаны таңдаңыз --", "📁 Мәтіндер мен кестелер", "📁 Мультимедиа", "📁 Графика", "📁 Программалар"])

            st.markdown("---")
            st.write("**Файл атын қою ережесі кейсі:**")
            naming_case = st.radio("Қай файл аты дұрыс жазылған?", ["Менің үй тапсырмам.docx", "Tabys_2026.xlsx", "esep*.txt"])

            if st.form_submit_button("Конструкторды тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    c = 0
                    if f1 == "📁 Мәтіндер мен кестелер": c += 1
                    if f2 == "📁 Мәтіндер мен кестелер": c += 1
                    if f3 == "📁 Мультимедиа": c += 1
                    if f4 == "📁 Графика": c += 1
                    if f5 == "📁 Программалар": c += 1
                    if naming_case == "Tabys_2026.xlsx": c += 1

                    st.balloons()
                    st.success(f"🎉 Конструктор нәтижесі, {student_name}: **{c} / 6** дұрыс 🧩")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Виртуалды конструктор (Файлдар)", "score": f"{c} / 6"
                    })

    # --- 7. ПРАКТИКАЛЫҚ ЖҰМЫС (Файлдық жүйе ойын сілтемесі) ---
    elif "7. Файлдық жүйе" in selected_topic:
        st.markdown("#### 🎮 Практикалық тапсырма (Интерактивті ойын)")
        st.info("Бұл сабақ сыртқы платформадағы ойын арқылы орындалады.")
        st.link_button("Ойынды ашу 🚀", "https://aliyateacher80-design.github.io/game-6-klass/")

    # --- 8. ВЕКТОРЛЫҚ ГРАФИКА КОНСТРУКТОРЫ ---
    elif "8. Векторлық графикалық редактор" in selected_topic:
        st.markdown("#### 🧩 Виртуалды конструктор: «Растрлық және векторлық графиканы ажырат»")
        with st.form("gfx_sort"):
            g1 = st.radio("1. «Суретті қанша үлкейтсеңіз де, сапасы мен анықтығы еш өзгермейді»", ["-- Таңдаңыз --", "Растрлық графика", "Векторлық графика"])
            g2 = st.radio("2. «Суретті тым қатты үлкейткен кезде ұсақ шаршыларға (пиксельдерге) бөлінеді»", ["-- Таңдаңыз --", "Растрлық графика", "Векторлық графика"])
            g3 = st.radio("3. «Негізі математикалық формулалар мен геометриялық пішіндерге негізделген»", ["-- Таңдаңыз --", "Растрлық графика", "Векторлық графика"])
            g4 = st.radio("4. «Файл көлемі өте кішкентай, жеңіл болады (SVG, CorelDRAW)»", ["-- Таңдаңыз --", "Растрлық графика", "Векторлық графика"])

            if st.form_submit_button("Графиканы ажыратуды тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    sc = 0
                    if g1 == "Векторлық графика": sc += 1
                    if g2 == "Растрлық графика": sc += 1
                    if g3 == "Векторлық графика": sc += 1
                    if g4 == "Векторлық графика": sc += 1
                    st.balloons()
                    st.success(f"🎉 Нәтижеңіз: **{sc} / 4** дұрыс 🎯")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Конструктор (Графика)", "score": f"{sc} / 4"
                    })

    # --- 9. ВЕКТОРЛЫҚ ГРАФИКА ТЕСТІ ---
    elif "9. Векторлық графикалық редактор" in selected_topic:
        st.markdown("#### 📝 Тест: «Растрлық және векторлық графика» (10 сұрақ)")
        with st.form("gfx_test"):
            t1 = st.radio("1. Растрлық графиканың ең кішкентай элементі (нүктесі) қалай аталады?", ["А) Вектор", "В) Пиксель", "С) Формула", "D) Контур"])
            t2 = st.radio("2. Векторлық графиканың негізін не құрайды?", ["А) Тек пиксельдер", "В) Математикалық формулалар, сызықтар мен геометриялық пішіндер", "С) Фотосуреттер", "D) Жарық пен көлеңке"])
            t3 = st.radio("3. Суретті тым қатты үлкейткен кезде ұсақ шаршыларға бөлінетін графика:", ["А) Векторлық графика", "В) Растрлық графика", "С) 3D графика", "D) Фракталдық"])
            t4 = st.radio("4. Векторлық графиканың басты артықшылығы қандай?", ["А) Фотосуретті жақсы береді", "В) Суретті қанша үлкейтсеңіз де, сапасы еш өзгермейді", "С) Файл көлемі әрқашан үлкен", "D) Тек интернет үшін"])
            t5 = st.radio("5. Растрлық графиканың кең таралған форматтары:", ["А) SVG, AI", "В) CDR, EPS", "С) JPEG, PNG", "D) PDF, DXF"])
            t6 = st.radio("6. Логотиптер мен сызбаларды жасауда көбінесе қандай графика қолданылады?", ["А) Растрлық графика", "В) Векторлық графика", "С) Мәтіндік редактор", "D) Кесте"])
            t7 = st.radio("7. Растрлық графиканың басты кемшілігі неде?", ["А) Көлемі кішкентай", "В) Суретті ұлғайтқан кезде сапасы жоғалып, пиксельденіп кетеді", "С) Тек ақ-қара", "D) Сызу қиын"])
            t8 = st.radio("8. Адамның шынайы фотосуретін өңдеуге қай графика ыңғайлы?", ["А) Векторлық графика", "В) Растрлық графика", "С) Сызбалық", "D) Геометриялық"])
            t9 = st.radio("9. Векторлық графикалық редакторға жататын программа:", ["А) Adobe Photoshop", "В) CorelDRAW немесе Adobe Illustrator", "С) Paint", "D) Microsoft Photos"])
            t10 = st.radio("10. Векторлық суреттердің файл көлемі әдетте қандай болады?", ["А) Өте үлкен", "В) Әлдеқайда кіші әрі жеңіл", "С) Бірдей", "D) Өзгереді"])

            if st.form_submit_button("Тестті тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    sc = 0
                    if "В) Пиксель" in t1: sc += 1
                    if "Математикалық формулалар" in t2: sc += 1
                    if "В) Растрлық графика" in t3: sc += 1
                    if "сапасы еш өзгермейді" in t4: sc += 1
                    if "С) JPEG, PNG" in t5: sc += 1
                    if "В) Векторлық графика" in t6: sc += 1
                    if "пиксельденіп кетеді" in t7: sc += 1
                    if "В) Растрлық графика" in t8: sc += 1
                    if "CorelDRAW" in t9: sc += 1
                    if "Әлдеқайда кіші" in t10: sc += 1

                    st.balloons()
                    st.success(f"🎉 Тест нәтижесі, {student_name}: **{sc} / 10** ұпай 🌟")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Тест (Графика)", "score": f"{sc} / 10"
                    })

    # --- 10. ВЕКТОРЛЫҚ ҚҰРАЛДАР СӘЙКЕСТЕНДІРУІ ---
    elif "10. Векторлық кескіндерді құру" in selected_topic and "Практикалық" in selected_topic:
        st.markdown("#### 🔗 Сәйкестендіру тапсырмасы: «Векторлық редактор құралдары»")
        with st.form("tool_match"):
            u1 = st.selectbox("1. Pen tool (Қалам)", ["-- Таңдаңыз --", "В) Нүктелер мен иіл сызықтар (кривые Безье) арқылы күрделі пішіндер салу.", "А) Тіктөртбұрыш"])
            u2 = st.selectbox("2. Геометриялық пішіндер", ["-- Таңдаңыз --", "А) Тіктөртбұрыш, дөңгелек, эллипс және көпбұрыш сияқты элементтер.", "Б) Бояу"])
            u3 = st.selectbox("3. Fill / Толтыру", ["-- Таңдаңыз --", "Б) Тұйықталған контурлардың ішін түстермен немесе градиентпен бояу.", "В) Сызу"])
            u4 = st.selectbox("4. Text tool (Мәтін құралы)", ["-- Таңдаңыз --", "Г) Әр түрлі қаріптермен атаулар, тақырыптар енгізу.", "Д) Нобай"])
            u5 = st.selectbox("5. Contour / Контур", ["-- Таңдаңыз --", "Д) Векторлық объектінің сыртқы шекарасы немесе сызық нобайы.", "Г) Мәтін"])

            if st.form_submit_button("Сәйкестікті тексеру 🚀"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    sc = 0
                    if "В)" in u1: sc += 1
                    if "А)" in u2: sc += 1
                    if "Б)" in u3: sc += 1
                    if "Г)" in u4: sc += 1
                    if "Д)" in u5: sc += 1
                    st.balloons()
                    st.success(f"🎉 Нәтижеңіз: **{sc} / 5** дұрыс сәйкестік 🎯")
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Сәйкестендіру (Құралдар)", "score": f"{sc} / 5"
                    })

    # --- 11. МИНИ-ОЙЫН: ҚАБАТТАРДЫ ҚҰТҚАР! ---
    elif "11. Векторлық кескіндерді құру" in selected_topic and "Мини-ойын" in selected_topic:
        st.markdown("""
            <div class="scenario-box">
                <b>🎨 Мини-ойын: «Дизайнер Айдынның қатесін түзет!»</b><br>
                «Айдын векторлық редакторда «Эко-үй» салып жатып, қабаттардың ретін шатастырып жіберді. 
                Нәтижесінде үйдің шатыры қабырғаны жауып, ал терезелер мүлде көрінбей қалды! 
                Суретті қайтадан дұрыс шығару үшін элементтерді <b>ең астыңғы қабаттан (1) ең үстіңгі қабатқа (5) қарай</b> дұрыс ретпен орналастырып, Айдынға көмектес!»
            </div>
            """, unsafe_allow_html=True)

        with st.form("mini_game_layers"):
            st.write("🕹️ **Қабаттарды басқару панелі (Layers Hub):**")
            
            p1 = st.selectbox("1-қабат (Ең астыңғы негіз - Фон):", ["-- Элементті таңдаңыз --", "Үйдің қабырғасы", "Фон (Аспан мен жер)", "Үйдің шатыры", "Есік пен терезе", "Алдыңғы пландағы ағаш"])
            p2 = st.selectbox("2-қабат:", ["-- Элементті таңдаңыз --", "Үйдің қабырғасы", "Фон (Аспан мен жер)", "Үйдің шатыры", "Есік пен терезе", "Алдыңғы пландағы ағаш"])
            p3 = st.selectbox("3-қабат:", ["-- Элементті таңдаңыз --", "Үйдің қабырғасы", "Фон (Аспан мен жер)", "Үйдің шатыры", "Есік пен терезе", "Алдыңғы пландағы ағаш"])
            p4 = st.selectbox("4-қабат:", ["-- Элементті таңдаңыз --", "Үйдің қабырғасы", "Фон (Аспан мен жер)", "Үйдің шатыры", "Есік пен терезе", "Алдыңғы пландағы ағаш"])
            p5 = st.selectbox("5-қабат (Ең үстіңгі қабат):", ["-- Элементті таңдаңыз --", "Үйдің қабырғасы", "Фон (Аспан мен жер)", "Үйдің шатыры", "Есік пен терезе", "Алдыңғы пландағы ағаш"])

            if st.form_submit_button("🎮 Ойынды аяқтау және тексеру"):
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді енгізіңіз!")
                else:
                    game_score = 0
                    if p1 == "Фон (Аспан мен жер)": game_score += 1
                    if p2 == "Үйдің қабырғасы": game_score += 1
                    if p3 == "Есік пен терезе": game_score += 1
                    if p4 == "Үйдің шатыры": game_score += 1
                    if p5 == "Алдыңғы пландағы ағаш": game_score += 1

                    if game_score == 5:
                        st.balloons()
                        st.success(f"🏆 Керемет, {game_score}/5 ұпай! Сіз дизайнер Айдынның қатесін толық түзедініз! 🎉")
                    else:
                        st.warning(f"⚠️ Ойын аяқталды! Жинаған ұпайыңыз: {game_score}/5. Кейбір қабаттардың орны қате, қайта көріңізші!")

                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Мини-ойын (Қабаттар)", "score": f"{game_score} / 5"
                    })
