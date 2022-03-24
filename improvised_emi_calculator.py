# Write the code for creating the Improvised EMI calculator app
import streamlit as st
def calculate_emi(p,n,r):
  a = r/100
  emi = p * a * ((1 + a)**n)/(((1 + a)**n) - 1)
  return emi

def calculate_outstanding_emi(p,n,r,m):
  a = r/100
  balance = (p * ((1 + a)**n) - ((1 + a)**m))/((1 + a)**n - 1)
  return balance

st.title("Improvised EMI Calculator")
p = st.sidebar.slider("The value of principal or p: ", 1000,1000000)
n = st.sidebar.slider("The value of tenure per annum: ", 1,30) * 12
r = st.sidebar.slider("The value of roi per annum: ", 1,15)/12
m = st.sidebar.slider("The value of m: ", 1, n)

if st.sidebar.button("Calculate EMI"):
  st.write("The EMI is: ", calculate_emi(p,n,r))

if st.sidebar.button("Calculate Outstanding Balance"):
  st.write("The Calculate Outstanding Balance is: ", calculate_outstanding_emi(p,n,r,m))