a = list(input().split())
st = []
for el in a:
  if el.isdigit():
    st.append(int(el))
  else:
    s = st.pop()
    f = st.pop()
    if el == '+':
      st.append(s + f)
    elif el == '-':
      st.append(f - s)
    elif el == '*':
      st.append(f * s)
print(*st)