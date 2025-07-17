import bpy

# オペレータ ICO球生成
class MYADDON_OT_create_ico_sphere(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_create_object"
    bl_label = "ICO球生成"
    bl_description = "ICO球生成を生成します"
    bl_options = {"REGISTER",'UNDO'}

    #メニューを実行したときに呼ばれる関数
    def execute(self,context):
        bpy.ops.mesh.primitive_ico_sphere_add()
        print("ICO球生成を生成しました。");
        # オペレータの命令終了を通知
        return{'FINISHED'}
    