pos=0
def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()[pos]=i
            return True
    else:
        return False


list = [12, 3, 56, 78, 9, 0]
n = 12
if search(list, n):
    print("Found",pos+1)
else:
    print("Not found")
