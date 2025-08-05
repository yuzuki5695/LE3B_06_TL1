import bpy
# オペレータのインポート
from .Operator.stretch_vertex import MYADDON_OT_stretch_vertex
from .Operator.create_ico_sphere import MYADDON_OT_create_ico_sphere
from .Operator.export_scene import MYADDON_OT_export_scene
from .Operator.SpawnPoint.spawn_create_player_symbol import MYADDON_OT_spawn_create_player_symbol
from .Operator.SpawnPoint.spawn_create_enemy_symbol import MYADDON_OT_spawn_create_enemy_symbol
from .info import bl_info
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
        # self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,
                             text = MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,
                             text = MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,
                             text = MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_spawn_create_player_symbol.bl_idname,
                             text = MYADDON_OT_spawn_create_player_symbol.bl_label)
        self.layout.operator(MYADDON_OT_spawn_create_enemy_symbol.bl_idname,
                             text = MYADDON_OT_spawn_create_enemy_symbol.bl_label)
    # 既存メニューにサブメニューを追加
    def submenu(self, context):
        # ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)