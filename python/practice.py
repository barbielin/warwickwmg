def count_case(text):
    m = 0
    n = 0
    for i in text:
        if i.isupper()==True:
            m+=1
        elif i.islower()== True:
            n+=1
    print("UpperWord count is",m)
    print("LowerWord count is",n)

print(count_case("HAndsome"))
  