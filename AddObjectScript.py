bl_info = { 
    "name" : "Object Adder",
    "author" : "Pushpak Talukder",
    "version" : (1, 0),
    "blender" : (2, 80, 0),
    "location" : "View3D > Toolbar > Object Adder",
    "description" : "Add objects and other functions",
    "warning" : "",
    "wiki_url" : "",
    "category" : "Add Mesh",
    
}


import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Object Adder"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    
    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.label(text= "Add an object", icon= "OBJECT_ORIGIN") 
        row = layout.row()
        row.operator("mesh.primitive_cube_add", icon= "CUBE") 
        row = layout.row()
        row.operator("mesh.primitive_uv_sphere_add", icon= "SPHERE")
        row = layout.row()
        row.operator("object.text_add", icon= "FILE_FONT", text= "Font Button")
         
         

class PanelA(bpy.types.Panel):
    bl_label = "PanelA"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_option = {"DEFAULT_CLOSED"}
    
    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.label(text= "This is panel A", icon= "FONT_DATA") 
        
        
        
class PanelB(bpy.types.Panel):
    bl_label = "PanelB"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "My 1st Addon"
    bl_parent_id = "PT_TestPanel"
    bl_option = {"DEFAULT_CLOSED"}
    
    
    def draw(self, context):
        layout = self.layout
    
        row = layout.row()
        row.label(text= "This is panel B", icon= "COLOR_BLUE") 








def register():
    bpy.utils.register_class(TestPanel)
    bpy.utils.register_class(PanelA)
    bpy.utils.register_class(PanelB)

def unregister():
    bpy.utils.unregister_class(TestPanel)
    bpy.utils.unregister_class(PanelA)
    bpy.utils.unregister_class(PanelB)



if __name__ == "__main__":
    register()
