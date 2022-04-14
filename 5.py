#階層判斷
layernum = int(input("請輸入階層值M："))
layer = sum = 1
while sum<layernum:
    layer += 1
    sum *= layer
print("最小超過階層值Mㄉ為：",layer)
