#Nested lists
if __name__ == '__main__':
    ds_tong = []
    diem = []
    ds_moi = []
    diem2 =[]
    diem_thap = 0.0
    diem_thap2 = 0.0
    ten = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        diem.append(score)
        ten_diem = [name, score]
        ds_tong.append(ten_diem)
        diem_thap = min (diem)
    for i in range(len(ds_tong)):
        if ds_tong[i][1] != diem_thap:
           ds_moi.append(ds_tong[i])
    for j in range(len(ds_moi)):
        diem2.append(ds_moi[j][1])
    diem_thap2 = min (diem2)
    for z in range(len(ds_moi)):
        if ds_moi[z][1] == diem_thap2:
            ten.append(ds_moi[z][0])
    ten.sort()
    for r in ten:
     print (r)
