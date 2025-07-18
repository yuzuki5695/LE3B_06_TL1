import bpy
import os

# オペレータ 出現ポイントの
class SpawnNames():

    # インデックス
    PROTOTYPE = 0   # プロトタイプのオブジェクト名
    INSTANCE = 1    # 量産時のオブジェクト名
    FILENAME = 2    # リソースファイル名

    names = {}
    # names["キー"] = (プロトタイプのオブジェクト名, 量産時のオブジェクト名, リソースファイル名)
    names["Enemy"] = ("PrototypeEnemySpawn", "EnemySpawn", "enemy/Enemy.obj")
    names["Player"] = ("PrototypePlayerSpawn", "PlayerSpawn", "player/player.obj")


# オペレータ 出現ポイントのシンボルを読み込む
class MYADDON_OT_spawn_import_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_import_symbol"
    bl_label = "出現ポイントシンボルImport"
    bl_description = "出現ポイントのシンボルをImportします"
    
    def load_obj(self, type):
        # 重複ロード防止
        spawn_object = bpy.data.objects.get(SpawnNames.names[type][SpawnNames.PROTOTYPE])
        if spawn_object is not None:
            return {'CANCELLED'}
         
        # スクリプトが配置されているディレクトリの名前を取得する
        addon_directory = os.path.dirname(__file__)
        # ディレクトリからのモデルファイルの相対パスを記述
        relative_path = os.path.join(SpawnNames.names[type][SpawnNames.FILENAME])
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
        object.name =  SpawnNames.names[type][SpawnNames.PROTOTYPE]
        # オブジェクトの種類を設定
        object["type"] =  SpawnNames.names[type][SpawnNames.PROTOTYPE]
      
        # メモリ上においておくがシーンから外す
        bpy.context.collection.objects.unlink(object)

        return{'FINISHED'}
    
    def execute(self,context):
        # Enemyオブジェクト読み込み
        self.load_obj("Enemy")
        # Playerオブジェクト読み込み
        self.load_obj("Player")

        return{'FINISHED'}