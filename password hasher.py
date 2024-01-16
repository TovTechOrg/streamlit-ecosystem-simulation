import streamlit_authenticator as stauth

hashed_passwords = stauth.Hasher(['1234']).generate()
print(hashed_passwords)