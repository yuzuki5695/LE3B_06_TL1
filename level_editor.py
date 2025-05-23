import bpy
import gpu
from gpu_extras.batch import batch_for_shader

class DrawCollider:
    handle = None

    @staticmethod
    def draw_collider():
        print("draw_collider呼ばれました")
        shader = gpu.shader.from_builtin("UNIFORM_COLOR")
        vertices = {"pos": [(0, 0, 0), (5, 0, 0)]}
        indices = [(0, 1)]
        batch = batch_for_shader(shader, "LINES", vertices, indices=indices)
        shader.bind()
        shader.uniform_float("color", (0.0, 1.0, 1.0, 1.0))
        batch.draw(shader)

def register():
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(
        DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("登録されました")

def unregister():
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")
    print("解除されました")

if __name__ == "__main__":
    register()
