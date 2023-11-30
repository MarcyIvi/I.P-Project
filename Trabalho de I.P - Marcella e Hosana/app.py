import streamlit as st 

st.title('hello')

num1 = st.mumber_input('Digite o primeiro número: ')
num2 = st.number_input('Digite o segundo número: ')

if st.button('soma'):

    resultado = num1 + num2

    st.text('resultado:')
    st.title(resultado)

elif st.button('subtração'):

    resultado = num1 - num2

    st.text('resultado')
    st.title(resultado)

elif st.button('multiplicação'):
    resultado = num1 * num2

    st.text('resultado')
    st.title(resultado)

elif st.button('divisão'):

    resultado = num1 / num2

    st.text('resultado')
    st.title(resultado)