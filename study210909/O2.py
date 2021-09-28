# 하기 단어들 중 at로 끝나는 세글자짜리 단어만 리스트로 반환해보세요
import re

words = """
cat
goat
gloat
spat
at
too
kar
stat
brat
zoo
swat
frat
pat
rat
boo
moat
vat
mat
tat
wheat
moo
cheat
fiat
squat
hat
carat
bat
rabat
"""

p = re.compile('\s(.at$)', re.M)
r = p.findall(words)
print(r)