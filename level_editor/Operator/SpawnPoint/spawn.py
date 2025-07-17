import bpy
import os

#オペレータ 出現ポイントのシンボルを読み込む
class MYADDON_OT_spawn_import_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_import_symbol"
    bl_label = "出現ポイントシンボルImport"
    bl_description = "出現ポイントのシンボルをImportします"
    
    prototype_object_name = "PrototypePlayerSpawn"
    
    def execute(self,context):
        print("出現ポイントのシンボルをImportします")
        # スクリプトが配置されているディレクトリの名前を取得する
        addon_directory = os.path.dirname(__file__)
        # ディレクトリからのモデルファイルの相対パスを記述
        relative_path = os.path.join("player/player.obj")
        # 合成してモデルファイルのフルパスを得る
        full_path = os.path.join(addon_directory, relative_path)
        
        # オブジェクトファイルをインポート
        bpy.ops.wm.obj_import('EXEC_DEFAULT',
         filepath=full_path,display_type='THUMBNAIL',
         forward_axis='Z', up_axis='Y')
        
        # 回転を適用
        bpy.ops.object.transform_apply(location=False,
        rotation=True, scale=False,properties=False,
        isolate_users=False) 

        # アクティブなオブジェクトを取得
        object= bpy.context.active_object
        # オブジェクト名を変更
        object.name = "PlayerSpawn"
        # オブジェクトの種類を設定
        object["type"] = MYADDON_OT_spawn_import_symbol.prototype_object_name

        return{'FINISHED'}