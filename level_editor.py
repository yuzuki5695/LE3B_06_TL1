import bpy
import math
import bpy_extras
import gpu
import gpu_extras.batch
import copy

# ブレンダーに登録するアドオン情報
bl_info = {
    "name": "レベルエディタ",
    "author": "Taro kamata",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    "wiki_url": "",      
    "tracker_url": "",
    "category": "Object"
}  

#コライダー描画
class DrawCollider:
    
    #描画ハンドル
    handle = None
    
    #3Dビューに登録する描画関数
    def draw_collider():
        print("draw_collider呼ばれました")

        #頂点データ   
        vertices = {"pos":[[0,0,0],[2,2,2]]}
        #インデックスデータ
        indices = [[0,1]]
   
        # ビルトインのシェーダを取得
        shader = gpu.shader.from_builtin("3D_UNIFORM_COLOR")


        # バッチを作成(引数: シェーダ,トポロジー, 頂点データ,インデックスデータ)
        batch = gpu_extras.batch.batch_for_shader(shader, "LINES", vertices, indices=indices)


        #シェーダのパラメータ設定
        color = [0.5, 1.0, 1.0, 1.0]
        shader.bind()
        shader.uniform_float("color", color)
        #描画
        batch.draw(shader)

# オペレータ 頂点を伸ばす
class MYADDON_OT_stretch_vertex(bpy.types.Operator):
    bl_idname ="myaddon.myaddon_ot_stretch_vertex"
    bl_label = "頂点を伸ばす"
    bl_description ="頂点座標を引っ張って伸ばします"
    #リドゥ アンドゥ可能オプション
    bl_options = {'REGISTER','UNDO'}
    
    #メニューを実行したときに呼ばれるコールバック関数
    def execute(self,context):
        bpy.data.objects["Cube"].data.vertices[0].co.x += 1.0
        print("頂点を伸ばしました。")
        
        # オペレータの命令終了を通知
        return{'FINISHED'}
    
#オペレータ ICO球生成
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
    
#オペレータ シーン出力
class MYADDON_OT_export_scene(bpy.types.Operator, bpy_extras.io_utils.ExportHelper):
    bl_idname ="myaddon.myaddon_ot_export_scene"
    bl_label = "シーン出力"
    bl_description = "シーン出力をExportします"
    #出力するファイルの拡張子
    filename_ext = ".scene"
    
    def write_and_print(self,file,str):
        print(str)

        file.write(str)
        file.write('\n')

    def parse_scene_recursive(self,file,object,level):
        """シーン解析用再起関数"""
        
        #深さ分インデントする (タブを挿入)
        indent = ''
        for i in range(level):
            indent += "\t"

        #オブジェクト名書き込み
        self.write_and_print(file,indent + object.type)
        trans,rot,scale = object.matrix_local.decompose()
        #回転をQuaternion から Euler (3軸での回転軸) に変換
        rot = rot.to_euler()
        #ラジアンから度数法に変換
        rot.x = math.degrees(rot.x)
        rot.y = math.degrees(rot.y) 
        rot.z = math.degrees(rot.z)
        #トランスフォーム情報を表示
        self.write_and_print(file, indent + "T(%f,%f,%f)" % (trans.x,trans.y,trans.z))
        self.write_and_print(file, indent + "R(%f,%f,%f)" % (rot.x,rot.y,rot.z))
        self.write_and_print(file, indent + "S(%f,%f,%f)" % (scale.x,scale.y,scale.z))
        #カスタムプロパティ'file_name'
        if "file_name" in object:
              self.write_and_print(file,indent + "N %s" % object["file_name"])
        self.write_and_print(file,indent + 'END')
        self.write_and_print(file, '') 
         
        #子ノードへ進(深さが1上がる)
        for child in object.children:
            self.parse_scene_recursive(file,child,level + 1)

    def export(self):
        """ファイルに出力"""

        print("シーン情報出力開始... %r " % self.filepath)

        #ファイルをテキスト形式で書き出し用にオープン
        #スコープを抜けると自動的にクローズされる
        with open(self.filepath, "wt") as file:

            #ファイルに文字列を書き込む
            file.write("SCENE\n")
            #シーン内の全オブジェクトについて
            for object in bpy.context.scene.objects:
                #親オブジェクトがあるものはスキップ (代わりに親から呼び出すから)
                if(object.parent):
                    continue
                #シーン直下のオブジェクトをルートノード(深さ0)とし、再起関数で走査
                self.parse_scene_recursive(file,object,0)

    def execute(self,context):
        print("シーン情報をExportします")
        
        #ファイルに出力
        self.export()

        self.report({'INFO'},"シーン情報をExportしました")
        print("シーン情報をExportしました")

        return{'FINISHED'}

 # メニュー項目描画
def draw_menu_manual(self,context):
    self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')
    
#トップバーの拡張メニュー 
class TOPBAR_MT_my_menu(bpy.types.Menu):
    #Blenderがクラスを識別する為の固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"
    #メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    #著者表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]    
     
    #サブメニューの描画
    def draw(self, context):
        # トップバーの[エディターメニュー]に項目 (オペレータ) を追加
        # self.layout.operator("wm.url_open_preset", text="Manual", icon='HELP')
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname,
                             text = MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ico_sphere.bl_idname,
                             text = MYADDON_OT_create_ico_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname,
                             text = MYADDON_OT_export_scene.bl_label)

    # 既存メニューにサブメニューを追加
    def submenu(self, context):
        # ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)

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

#パネルファイル名
class OBJECT_PT_file_name(bpy.types.Panel):
    """オブジェクトのファイルネームパネル"""
    bl_idname = "OBJECT_PT_file_name"
    bl_label = "FileName"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    #サブメニューの描画
    def draw(self, context):
        #パネルに項目を追加
        if "file_name" in context.object:
            #既にプロパティがあれば、プロパティを表示
            self.layout.prop(context.object,'["file_name"]',text=self.bl_label)
        else:
            #プロパティがなければ、プロパティ追加ボタンを表示
            self.layout.operator(MYADDON_OT_add_filename.bl_idname)

# Blenderに登録するクラスリスト
classes = (
    MYADDON_OT_export_scene,
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    TOPBAR_MT_my_menu,
    MYADDON_OT_add_filename,
    OBJECT_PT_file_name,
    )
    
# Add-On有効化時コールバック
def register():
    #Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    #メニューに項目を追加 
    bpy.types.TOPBAR_MT_editor_menus.append(TOPBAR_MT_my_menu.submenu)
    # 3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(
    DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました")

# Add-On無効化時コールバック
def unregister():
    #メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(TOPBAR_MT_my_menu.submenu)
    #3Dビューから描画関数を削除
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    # Blenderからクラスを削除
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました")
    
if __name__ == "__main__":
    register()