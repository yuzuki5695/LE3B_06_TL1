import bpy

# オペレータ 敵専用出現ポイントシンボル作成
class MYADDON_OT_spawn_create_enemy_symbol(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_spawn_create_enemy_symbol"
    bl_label = "敵出現ポイントシンボルの作成"
    bl_description = "敵出現ポイントのシンボルを作成します"

    def execute(self, context):
        # 出現ポイントのシンボルを作成するオペレータを呼び出す
        bpy.ops.myaddon.myaddon_ot_spawn_create_symbol('EXEC_DEFAULT', type="Enemy")
        
        return {'FINISHED'}