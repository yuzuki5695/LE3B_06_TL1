print("Hello,Yuzuki Onodera!")

import bpy

#関数定義
def moveVertex():
    #頂点を移動
    bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0
    
for i in range(10):
    #関数呼び出し
    moveVertex()