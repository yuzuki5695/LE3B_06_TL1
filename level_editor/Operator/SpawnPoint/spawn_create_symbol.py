import bpy


from .spawnNames import SpawnNames

# オペレータ 出現ポイントのシンボルを作成・配置する
class MYADDON_OT_spawn_create_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_create_symbol"
    bl_label = "出現ポイントシンボルの作成"
    bl_description = "出現ポイントのシンボルを作成します"
    bl_options = {'REGISTER', 'UNDO'}

    #プロパティ(引数として渡せる)
    type: bpy.props.StringProperty(name = "Type", default = "Player")

    def execute(self,context):
        # 読み込み済みのコピー元オブジェクトを検索
        spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])

        # まだ読み込んでいない場合
        if spawn_object is None:
            # 読み込みオペレータを実行
            bpy.ops.myaddon.myaddon_ot_spawn_import_symbol('INVOKE_DEFAULT')
            # 再検索。今度は見つかるはず
            spawn_object = bpy.data.objects.get(SpawnNames.names[self.type][SpawnNames.PROTOTYPE])
        
        print("出現ポイントのシンボルを作成します")
      
         # Blenderでの選択をする
        bpy.ops.object.select_all(action='DESELECT')
        
        # 複製元の非表示オブジェクトを複製する
        object = spawn_object.copy()

        # 複製したオブジェクトを現在のシーンにリンク (出現させる)
        bpy.context.collection.objects.link(object)
        
        # オブジェクト名を変更
        object.name = SpawnNames.names[self.type][SpawnNames.INSTANCE]
        
        return {'FINISHED'}