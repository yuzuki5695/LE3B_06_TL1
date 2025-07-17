import bpy

#オペレータ カスタムプロパティ['file_name']追加
class MYADDON_OT_add_filename(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_add_filename"
    bl_label = "FileName 追加"
    bl_description = "['file_name']カスタムプロパティを追加します"
    bl_options = {"REGISTER",'UNDO'}

    def execute(self,context):

        #['file_name']カスタムプロパティを追加
        context.object['file_name'] = ""
        return{'FINISHED'}
    