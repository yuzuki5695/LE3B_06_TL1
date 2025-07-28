import bpy

from .add_disableoption import MYADDON_OT_add_disableoption

#パネル 無効オプション
class MYADDON_PT_disable_option(bpy.types.Panel):
    """オブジェクトの無効オプションパネル"""
    bl_idname = "MYADDON_PT_disable_option"
    bl_label = "Disabled"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):
        layout = self.layout
        obj = context.object
        if obj is None:
            layout.label(text="オブジェクトが選択されていません")
            return
        
        # 'disabled' プロパティがなければ、追加ボタンを表示
        if "disabled" not in obj:
            layout.operator(MYADDON_OT_add_disableoption.bl_idname, text="Add Disabled")
        else:
            # プロパティがあればチェックボックスを表示
            # 表示/非表示を切り替え
            layout.prop(obj, '["disabled"]', text="無効化")
            layout.operator("myaddon.toggle_visibility", text="レイアウトに反映")
