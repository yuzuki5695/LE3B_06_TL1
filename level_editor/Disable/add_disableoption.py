import bpy

#オペレータ 無効オプションを追加する
class MYADDON_OT_add_disableoption(bpy.types.Operator):
    """選択中のオブジェクトを非表示にするオペレータ"""
    bl_idname = "myaddon.myaddon_ot_add_disableoption"
    bl_label = "Add Disabled"
    bl_description = "['option']カスタムプロパティを追加します"
    bl_options = {"REGISTER",'UNDO'}

    def execute(self, context):
        for obj in context.selected_objects:
            obj["disabled"] = False  # 初期状態は表示
        self.report({'INFO'}, "'disabled' を追加しました")
        return {'FINISHED'}
