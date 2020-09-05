a=["asdf",["qwer",10]]
b=a
print(id(a),id(b))
b[0]="123"
print(id(a),id(b))
print(a,b)