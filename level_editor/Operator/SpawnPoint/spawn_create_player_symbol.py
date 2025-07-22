import bpy

# オペレータ 自キャラ専用出現ポイントシンボル作成
class MYADDON_OT_spawn_create_player_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_create_player_symbol"
    bl_label = "プレイヤー出現ポイントシンボルの作成"
    bl_description = "プレイヤー出現ポイントのシンボルを作成します"

    def execute(self, context):
        # 出現ポイントのシンボルを作成するオペレータを呼び出す
        bpy.ops.myaddon.myaddon_ot_spawn_create_symbol('EXEC_DEFAULT', type="Player")
        
        return {'FINISHED'}