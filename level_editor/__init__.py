import bpy

# モジュールのインポート
###-----------------オペレータ関連-----------------###
from .Operator.stretch_vertex import MYADDON_OT_stretch_vertex
from .Operator.create_ico_sphere import MYADDON_OT_create_ico_sphere
from .Operator.export_scene import MYADDON_OT_export_scene
#スポーン関連
from .Operator.SpawnPoint.spawn import MYADDON_OT_spawn_import_symbol
###-----------------カスタムプロパティ関連-----------------###
# ファイル名関連
from .FileName.add_filename import MYADDON_OT_add_filename
from .FileName.file_name import OBJECT_PT_file_name
# コライダー関連
from .Collider.add_collider import MYADDON_OT_add_collider
from .Collider.collider import OBJECT_PT_collider
from .Collider.draw_collider import DrawCollider
from .my_menu import TOPBAR_MT_my_menu
# 無効オプション関連
from .Disable.add_disableoption import MYADDON_OT_add_disableoption
from .Disable.toggle_disable import MYADDON_OT_toggle_visibility
from .Disable.disable_option import MYADDON_OT_disable_option

# Blenderに登録するクラスリスト
classes = (
    MYADDON_OT_export_scene,
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    TOPBAR_MT_my_menu,
    MYADDON_OT_add_filename,
    OBJECT_PT_file_name,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
    MYADDON_OT_add_disableoption,
    MYADDON_OT_toggle_visibility,
    MYADDON_OT_disable_option,
    MYADDON_OT_spawn_import_symbol,
    )
    
    
# Add-On有効化時コールバック
def register():
    #Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニューに項目を追加 
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    # 3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(
    DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました")

# Add-On無効化時コールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    # Blenderからクラスを削除
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました")
    
if __name__ == "__main__":
    register()