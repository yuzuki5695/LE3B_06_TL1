import bpy

# スポーンモジュールのインポート
from .spawn_import_symbol import MYADDON_OT_spawn_import_symbol

# オペレータ 出現ポイントのシンボルを作成・配置する
class MYADDON_OT_spawn_create_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_create_symbol"
    bl_label = "出現ポイントシンボルの作成"
    bl_description = "出現ポイントのシンボルを作成します"
    bl_options = {'REGISTER', 'UNDO'}
    
    # オブジェクト名
    object_name = "PlayerSpawn"
    
    def execute(self,context):
        #読み込み済みのコピー元オブジェクトを検索
        spawn_object = bpy.data.objects.get(MYADDON_OT_spawn_import_symbol.prototype_object_name)

        # まだ読み込んでいない場合
        if spawn_object is None:
            # 読み込みオペレータを実行
            bpy.ops.myaddon.myaddon_ot_spawn_import_symbol('INVOKE_DEFAULT')
            # 再検索。今度は見つかるはず
            spawn_object = bpy.data.objects.get(MYADDON_OT_spawn_import_symbol.prototype_object_name)
        
        print("出現ポイントのシンボルを作成します")
        
        # Blenderでの選択をする
        bpy.ops.object.select_all(action='DESELECT')
        
        # 複製元の非表示オブジェクトを複製する
        object = spawn_object.copy()

        # 複製したオブジェクトを現在のシーンにリンク (出現させる)
        bpy.context.collection.objects.link(object)
        
        # オブジェクト名を変更
        object.name = MYADDON_OT_spawn_create_symbol.object_name

        return{'FINISHED'}