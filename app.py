import streamlit as st
st.title("Культура и ЗОЖ(Спорт и тупые качки)")
tab1, tab2 = st.tabs(["индекс массы итела","на крайний случай остается:"])
with tab1:
    weight = st.number_input("Вес")
    height = st.number_input("Рост")
    if st.button("Индекс массы тела"):
        st.info(weight/height)
with tab2:
    st.title("При переизбытке веса вам следует просто умереть")
    st.image("369be487735301.5dc16da0835fa.jpg")
    st.title("При низком весе вам следует тоже просто умереть")
    st.image("369be487735301.5dc16da0835fa.jpg")
