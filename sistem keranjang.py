
print("="*25)
print("="*5,"Sistem keranjang","="*2)
print("="*25)
print('====== daftar produk ====')
produk = ['roll','buku','mouse','keyboard']
harga = [1000,5000,7000,20000]
keranjang=[]
nilai = 0
while(nilai < len(produk)):
    print(produk[nilai],'Rp',harga[nilai])
    nilai += 1
# for i  in range(len(art)):
#     print(f'{produk[i]} Rp {harga[i]}')
while True:
   
    pilih = int(input('masukan pilihan :'))-1
    
    if str(pilih).isdigit()== 0:
            break
        
    if  pilih < len(produk):
        print(f"{produk[pilih]} Telah ditambah kan")

    keranjang.append({"produk" : produk[pilih],"harga":harga[pilih]})

print("\nYg di keranjang")
print("="*25)
for i in keranjang:
    print ("produk:",i['produk'],"Rp.",i['harga'])
    