import bpy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Taro kamata",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "wiki_url": "",      
    "tracker_url": "",
    "category": "Object"
}  

 # メニュー項目描画
def draw_menu_manual(self,context):
    self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')
    
#トップバーの拡張メニュー 
class TOPBAR_MT_my_menu(bpy.types.Menu):
    #Blenderがクラスを識別する為の固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"
    #メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    #著者表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]    
     
    #サブメニューの描画
    def draw(self, context):
        # トップバーの[エディターメニュー]に項目 (オペレータ) を追加
        self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')

    # 既存メニューにサブメニューを追加
    def submenu(self, context):
        # ID指定でサブメニューを追加
        self.layout.meun(TOPBAR_MT_my_menu.bl_idname)
           
# Blenderに登録するクラスリスト
classes = (TOPBAR_MT_my_menu,)
    
# アドオン有効化時コールバック
def register():
     #メニューに項目を追加
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    print("レベルエディタが有効化されました")

# アドオン無効化時コールバック
def unregister():
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
     # Blenderからクラスを削除
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました")

if __name__ == "__main__":
    register()