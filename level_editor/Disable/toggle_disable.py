import bpy

# パネル 無効オプション
class MYADDON_OT_toggle_visibility(bpy.types.Operator):
    """disabled フラグに応じて表示/非表示を切り替える"""
    bl_idname = "myaddon.toggle_visibility"
    bl_label = "Apply Disabled State"

    def execute(self, context):
        obj = context.object
        if obj is not None and "disabled" in obj:
            is_disabled = obj["disabled"]
            obj.hide_viewport = is_disabled
            obj.hide_render = is_disabled
            return {'FINISHED'}
        return {'CANCELLED'}