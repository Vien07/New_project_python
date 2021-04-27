from nhan_vien_demo import Nhan_Vien

nv1 = Nhan_Vien(ma_nv= "01", ten_nv= "Luka", luong_nv= 1000)

# Gán thông tin dữ liệu cho một đối tượng

# nv1.ten_nhan_vien = "Luka"
# nv1.ma_nhan_vien = "007"
# nv1.luong_nhan_vien = 7000

# nv2

nv2 = Nhan_Vien()
nv2.ten_nhan_vien = "Bayo"
nv2.ma_nhan_vien = "02"
nv2.luong_nhan_vien = 2000
#nv3
nv3 = Nhan_Vien(ma_nv= "03", ten_nv= "Ceza", luong_nv= 3000)
# Truy xuất thông tin đối tượng

print(nv1.ten_nhan_vien,nv2.ten_nhan_vien)

#Dùng vòng lặp để truy xuất
ds_nv = [nv1,nv2,nv3]
print(ds_nv)
for i in range(0,len(ds_nv)):
    print(ds_nv[i].ten_nhan_vien)

# def xoa_nv(a):
#     ds = []
#     for i in range(0,len(ds_nv)):
#         if a not in ds_nv[i].ten_nhan_vien:
#             ds.append(ds_nv[i])
#     if ds != []:
#         for i in range(0,len(ds)):
#             print(ds[i].ten_nhan_vien, end= ' ')

def xoa_nv(a,b):
    ds = []
    for i in range(0,len(ds_nv)):
        if a in ds_nv[i].ten_nhan_vien:
            ds.append(i)
    ds = list(reversed(ds))
    for i in ds:
        b = b.remove(b[i])
    return b

xoa_nv("Luka",ds_nv)

print(ds_nv)
print(xoa_nv)
