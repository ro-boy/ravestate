import rclpy
from ravestate.module import Module
from ravestate.constraint import s
from ravestate.state import state
from ravestate.receptor import receptor
from ravestate.property import PropertyBase
from std_msgs.msg import String


rclpy.init()
node = rclpy.create_node("vision_node")

<<<<<<< HEAD
with Module(name="facerec"):
=======

@state(cond=s(":startup"))
def facerec_run(ctx):
>>>>>>> b21a042c31198e97e854d4b01b4d5aa74679bb54

    face = PropertyBase(name="face", default_value="")

    @state(cond=s(":startup"))
    def facerec_run(ctx):

        @receptor(ctx_wrap=ctx, write="facerec:face")
        def face_recognition_callback(ctx, msg):
            ctx["facerec:face"] = msg

        node.create_subscription(String, "/roboy/vision/recognized_faces", face_recognition_callback)
        rclpy.spin(node)


<<<<<<< HEAD
    @state(cond=s(":shutdown"))
    def facerec_shutdown():
        node.destroy_node()
        rclpy.shutdown()
=======
registry.register(
    name="facerec",
    props=PropertyBase(name="face", default_value=""),
    states=(facerec_run, facerec_shutdown))
>>>>>>> b21a042c31198e97e854d4b01b4d5aa74679bb54
