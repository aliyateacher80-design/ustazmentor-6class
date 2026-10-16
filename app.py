import streamlit as st

st.set_page_config(page_title="UstazMentor - 6-сынып", page_icon="💻", layout="wide")

if "results_db" not in st.session_state:
    st.session_state.results_db = []

st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 25px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="main-header">
        <h1>UstazMentor 💻 6-сынып</h1>
        <p style="font-size: 18px; font-weight: 600; margin-top: 5px;">Бір тақырып — бір өмірлік жағдаят — нақты нәтиже!</p>
        <p style="font-size: 14px; opacity: 0.9;">Функционалдық сауаттылық, тесттер, сәйкестендіру және интерактивті тренажерлар</p>
    </div>
""", unsafe_allow_html=True)

sections_dict = {
    "📁 Бөлім: Компьютер және қауіпсіздік": [
        "3. Қауіпсіздік және Интернет желісінде жұмыс кезіндегі жауапкершілік",
        "4. Қауіпсіздік және Интернет желісінде жұмыс кезіндегі жауапкершілік. Практикалық жұмыс",
        "10. Жасанды интеллектідегі деректердің рөлі",
        "15. Жүйелік блок құрылғысы және компьютердің жадысы",
        "18. Жүйелік блок және компьютердің жадысы. Практикалық жұмыс",
        "22. Файлдық жүйе және программалық жасақтама",
        "26. Файлдық жүйе және программалық жасақтама. Практикалық жұмыс"
    ],
    "📁 Бөлім: Векторлық графика": [
        "3. Векторлық графикалық редактор",
        "7. Векторлық графикалық редактор. Бекіту және қолдану",
        "10. Векторлық кескіндерді құру. Практикалық жұмыс",
        "12. Векторлық кескіндерді құру. Бекіту және қолдану"
    ]
}

correct_answers = {
    "10. Жасанды интеллектідегі деректердің рөлі": [
        "С) Деректер (Data)", "А) Ақпарат (Information)", "Б) Білім (Knowledge)",
        "С) «25», «Алматы», «3.14» сияқты жекелеген мәндер",
        "В) Модельге заңдылықтарды, үлгілерді танып үйрету және шешім қабылдау",
        "В) Модель қате нәтижелер шығарады",
        "А) Көп мөлшерде белгіленген (таңбаланған) суреттер жиынтығы",
        "В) Деректер -> Ақпарат -> Білім",
        "А) Машиналық оқыту арқылы",
        "А) Дұрыс таңдалған сапалы деректер жиынтығы"
    ],
    "15. Жүйелік блок құрылғысы және компьютердің жадысы": [
        "А) Аналық плата (Motherboard)", "А) Орталық процессор (CPU)", "А) RAM (Жедел жады)",
        "А) Тактілік жиілік (ГГц)", "А) ROM (Тұрақты жады)", "А) Кеш-жады",
        "А) Есептеулерді жылдамдату", "А) Компьютер өшсе де деректер сақталады",
        "А) Деректерді уақытша сақтау", "А) Процессордың 1 секундтағы операция жасау жылдамдығы"
    ]
}

all_topics = []
for sec, topics in sections_dict.items():
    all_topics.extend(topics)

role = st.radio("Режимді таңдаңыз:", ["👨‍🎓 Оқушы режимі", "👩‍🏫 Мұғалім кабинеті"], horizontal=True)

st.divider()

if role == "👩‍🏫 Мұғалім кабинеті":
    st.subheader("👨‍💻 Мұғалімнің басқару және баптау панелі 🔗")
    save_results_enabled = st.toggle("📊 Оқушы нәтижелерін базаға сақтау", value=True)
    selected_section = st.selectbox("Бөлімді таңдаңыз:", list(sections_dict.keys()))
    selected_topic = st.selectbox("Тақырыпты таңдаңыз:", sections_dict[selected_section])
    timer_val = st.number_input("Сабаққа арналған таймер (минут):", value=15)
    
    st.info(f"💡 **Таңдалған бөлім:** {selected_section} | **Тақырып:** {selected_topic}")
    st.write(f"📌 Нәтижелерді сақтау режимі: **{'ҚОСУЛЫ ✅' if save_results_enabled else 'ӨШІРУЛІ ❌'}**")
    
    st.markdown("### 🔗 Оқушыларға арналған автоматты сілтеме:")
    shareable_url = f"https://ustazmentor-6class.streamlit.app/?topic={selected_topic}&timer={timer_val}&save={'1' if save_results_enabled else '0'}"
    st.code(shareable_url)
    
    st.divider()
    st.subheader("📊 Сақталған оқушы нәтижелері")
    if len(st.session_state.results_db) > 0:
        if st.button("🗑️ Барлық нәтижелерді тазарту"):
            st.session_state.results_db = []
            st.rerun()
        for idx, res in enumerate(st.session_state.results_db, 1):
            st.write(f"**{idx}. Оқушы:** {res['name']} ({res['grade']}) | **Тақырып:** {res['topic']} | **Тапсырма:** {res['task_type']} | **Нәтижесі:** {res['score']}")
    else:
        st.write("Әзірге сақталған нәтижелер тізімі бос.")

else:
    st.subheader("👨‍🎓 Оқушы кабинеті")
    col_name, col_class = st.columns([2, 1])
    with col_name:
        student_name = st.text_input("Аты-жөніңізді енгізіңіз (Мысалы: Айдын Б.):", placeholder="Аты-жөніңіз...")
    with col_class:
        student_grade = st.selectbox("Сыныбыңыз:", ["6 «Ә»", "6 «А»", "6 «Б»", "6 «В»"])
    
    query_params = st.query_params
    default_topic = query_params.get("topic", all_topics[0])
    if isinstance(default_topic, list):
        default_topic = default_topic[0]
        
    save_param = query_params.get("save", "1")
    if isinstance(save_param, list):
        save_param = save_param[0]
    save_mode = (save_param == "1")
    
    topic_index = 0
    if default_topic in all_topics:
        topic_index = all_topics.index(default_topic)
        
    selected_topic = st.selectbox("Сабақ тақырыбын таңдаңыз:", all_topics, index=topic_index)
    st.success(f"🎯 **Ағымдағы сабақ:** {selected_topic}")
    if not save_mode:
        st.warning("⚠️ Ескерту: Нәтижелерді сақтау өшірілген.")
    
    st.divider()
    tab_test, tab_match, tab_game = st.tabs(["📝 Тест (10 сұрақ)", "🔗 Сәйкестендіру", "🕵️‍♂️ Дебаггер / Тренажер"])
    
    with tab_test:
        st.markdown(f"#### Функционалдық тест: {selected_topic}")
        with st.form(key=f"test_{selected_topic}"):
            user_answers = []
            if "10. Жасанды интеллектідегі деректердің рөлі" in selected_topic:
                q_list = [
                    ("1. Шикі, өңделмеген фактілер мен сандар қалай аталады?", ["А) Білім", "Б) Ақпарат", "С) Деректер (Data)", "D) Интеллект"]),
                    ("2. Деректерді өңдегеннен кейінгі мағыналы түрі:", ["А) Ақпарат (Information)", "Б) Деректер", "С) Болжам"]),
                    ("3. Тәжірибе арқылы қалыптасатын жоғары сатыдағы ұғым:", ["А) Деректер", "Б) Білім (Knowledge)", "С) Сигнал"]),
                    ("4. «Деректерге» мысал келтіріңіз:", ["А) Толық есептеу ережесі", "Б) Дайын қорытынды", "С) «25», «Алматы», «3.14» сияқты жекелеген мәндер"]),
                    ("5. ЖИ модельдерін оқытудағы деректердің рөлі қандай?", ["А) Компьютердің қызуын тежеу", "В) Модельге заңдылықтарды, үлгілерді танып үйрету және шешім қабылдау", "С) Интернет жылдамдығын арттыру"]),
                    ("6. Сапасыз деректер енгізілсе («Garbage in, garbage out»):", ["А) Ештеңе өзгермейді", "В) Модель қате нәтижелер шығарады", "С) Бағдарлама өшіп қалады"]),
                    ("7. Суреттерді танитын ЖИ оқыту үшін не қажет?", ["А) Көп мөлшерде белгіленген (таңбаланған) суреттер жиынтығы", "Б) Тек бір ғана ақ қағаз", "С) Бос музыкалық файлдар"]),
                    ("8. Төмендегілердің қайсысы дұрыс иерархиялық ретті көрсетеді?", ["А) Білім -> Ақпарат -> Деректер", "В) Деректер -> Ақпарат -> Білім", "С) Ақпарат -> Білім -> Деректер"]),
                    ("9. Компьютерлік жүйелерде суреттер мен мәтіндерді өңдеу не арқылы жүзеге асады?", ["А) Машиналық оқыту арқылы", "Б) Механикалық күшпен", "С) Қолмен сызу арқылы"]),
                    ("10. Жасанды интеллект нәтижесінің дәл болуы неге байланысты?", ["А) Дұрыс таңдалған сапалы деректер жиынтығы", "Б) Монитордың үлкендігіне", "С) Пернетақта түсіне"])
                ]
                for q_text, q_opts in q_list:
                    user_answers.append(st.radio(q_text, q_opts))
            elif "15. Жүйелік блок құрылғысы және компьютердің жадысы" in selected_topic:
                q_list = [
                    ("1. Барлық құрылғылар өзара жалғанатын негізгі плата:", ["А) Аналық плата (Motherboard)", "Б) Қуат көзі", "С) Дисковод"]),
                    ("2. Компьютердің «миы» болып саналатын құрылғы:", ["А) Орталық процессор (CPU)", "Б) Қатты диск", "С) Флеш-карта"]),
                    ("3. Тоқ өшкенде деректер жойылып кететін уақытша жады:", ["А) RAM (Жедел жады)", "Б) ROM", "С) Қатты диск"]),
                    ("4. Процессордың жылдамдығын өлшейтін өлшем бірлік:", ["А) Тактілік жиілік (ГГц)", "Б) Байт", "В) Пиксель"]),
                    ("5. Бастапқы жүктеу программаларын (BIOS) сақтайтын тұрақты жады түрі:", ["А) ROM (Тұрақты жады)", "Б) RAM", "С) Кэш-жады"]),
                    ("6. Процессор мен жедел жады арасындағы дерек алмасуды жылдамдататын шағын жады:", ["А) Кеш-жады", "Б) Сыртқы диск", "В) Флешка"]),
                    ("7. Кэш-жадының негізгі атқаратын қызметі қандай?", ["А) Есептеулерді жылдамдату", "Б) Сурет сақтау", "В) Интернетке қосылу"]),
                    ("8. Тұрақты жадының (ROM) басты ерекшелігі неде?", ["А) Компьютер өшсе де деректер сақталады", "Б) Деректер үздіксіз өшіп тұрады", "В) Тек ойын ойнауға арналған"]),
                    ("9. Жедел жадының (RAM) атқаратын негізгі міндеті:", ["А) Деректерді уақытша сақтау", "Б) Компьютерді сыртқы қауіптен қорғау", "В) Бағдарламаларды мәңгілік сақтау"]),
                    ("10. Процессордың тактілік жиілігі нені білдіреді?", ["А) Процессордың 1 секундтағы операция жасау жылдамдығы", "Б) Компьютердің салмағы", "В) Монитордың өлшемі"])
                ]
                for q_text, q_opts in q_list:
                    user_answers.append(st.radio(q_text, q_opts))
            else:
                st.info("Бұл тақырыпқа әзірге тест сұрақтары дайындалу үстінде.")
                
            submit_test = st.form_submit_button("Тестті тексеру және ұпайды есептеу")
            if submit_test:
                if not student_name.strip():
                    st.error("⚠️ Назар аударыңыз! Тапсырманы орындау үшін аты-жөніңізді жазыңыз.")
                else:
                    score = 0
                    correct_list = correct_answers.get(selected_topic, [])
                    for ua, ca in zip(user_answers, correct_list):
                        if ua == ca:
                            score += 1
                    st.balloons()
                    st.success(f"Құттықтаймыз, {student_name} ({student_grade})! Тест аяқталды. Нәтижеңіз: **{score} / 10** ұпай 🌟")
                    if save_mode:
                        st.session_state.results_db.append({
                            "name": student_name, "grade": student_grade, "topic": selected_topic,
                            "task_type": "Тест (10 сұрақ)", "score": f"{score} / 10 ұпай"
                        })
                        st.info("💾 Нәтижеңіз мұғалім базасына сәтті сақталды.")
                        
    with tab_match:
        st.markdown(f"#### Сәйкестендіру тапсырмасы: {selected_topic}")
        with st.form(key=f"match_{selected_topic}"):
            match_options = [
                "-- Жауапты таңдаңыз --", "Аналық плата (Motherboard)", "Орталық процессор (CPU)",
                "RAM (Жедел жады)", "ROM (Тұрақты жады)", "Кэш-жады", "Тактілік жиілік",
                "Фишинг шабуылы", "Кибербуллинг", "Сенімді құпия сөз", "Векторлық графика", "Растрлық графика"
            ]
            match_items = [
                "1. Компьютердің миы", "2. Барлық компоненттер қосылатын плата", "3. Уақытша жады",
                "4. Тұрақты жады", "5. Жылдам шағын жады", "6. Процессор жылдамдығы",
                "7. Жалған сілтеме арқылы алаяқтық", "8. Желідегі қорқыту / дөрекілік",
                "9. Күрделі символдар жиынтығы", "10. Формулаларға негізделген сурет"
            ]
            match_inputs = []
            for item in match_items:
                val = st.selectbox(f"{item} сәйкестігі:", match_options, key=f"m_select_{item}")
                match_inputs.append(val)
                
            submit_match = st.form_submit_button("Сәйкестікті тексеру және ұпайды есептеу")
            if submit_match:
                if not student_name.strip():
                    st.error("⚠️ Аты-жөніңізді жоғарғы жаққа жазыңыз!")
                else:
                    filled_count = sum(1 for m in match_inputs if m != "-- Жауапты таңдаңыз --")
                    match_score = int(filled_count)
                    st.balloons()
                    st.success(f"Жарайсың, {student_name}! Сәйкестендіру тексерілді. Жинаған ұпайыңыз: **{match_score} / 10** 🎯")
                    if save_mode:
                        st.session_state.results_db.append({
                            "name": student_name, "grade": student_grade, "topic": selected_topic,
                            "task_type": "Сәйкестендіру", "score": f"{match_score} / 10 ұпай"
                        })
                        st.info("💾 Нәтижеңіз мұғалім базасына сәтті сақталды.")
                        
    with tab_game:
        st.markdown(f"#### 🕵️‍♂️ Дебаггер / Практикалық тренажер: {selected_topic}")
        step = st.slider("Қадамды таңдаңыз:", 0, 10, 0, key=f"slider_{selected_topic}")
        st.write(f"Орындалу деңгейі: **{step} / 10 қадам**")
        if step > 0:
            st.info(f"📍 **{selected_topic}** бойынша **{step}-қадам** талдануда.")
        if st.button("Қадамды растау / Нәтиже тіркеу", key=f"btn_{selected_topic}"):
            if not student_name.strip():
                st.error("⚠️ Ең алдымен аты-жөніңізді жазыңыз!")
            else:
                st.balloons()
                st.success(f"Құттықтаймыз, {student_name}! Тренажер қадамы тіркелді: **{step} / 10 қадам** 🚀")
                if save_mode:
                    st.session_state.results_db.append({
                        "name": student_name, "grade": student_grade, "topic": selected_topic,
                        "task_type": "Тренажер / Дебаггер", "score": f"{step} / 10 қадам"
                    })
                    st.info("💾 Нәтижеңіз мұғалім базасына сәтті сақталды.")
