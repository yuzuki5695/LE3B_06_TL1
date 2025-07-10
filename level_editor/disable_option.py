import bpy

from .add_disableoption import MYADDON_OT_add_disableoption

#パネル 無効オプション
class MYADDON_OT_disable_option(bpy.types.Panel):
    """オブジェクトの無効オプションパネル"""
    bl_idname = "MYADDON_OT_disable_option"
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

        #パネルに項目を追加
        if "Disabled" in context.object:
            #既にプロパティがあれば、プロパティを表示
            layout.operator(MYADDON_OT_add_disableoption.bl_idname, text="Add Disabled")
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_disableoption.bl_idname)

            # チェックボックスの表示
            layout.prop(obj, '["disabled"]', text=self.bl_label)

            # チェック状態に応じて表示状態を制御
            if obj["disabled"]:
                obj.hide_viewport = True
                obj.hide_render = True
            else:
                obj.hide_viewport = False
                obj.hide_render = False