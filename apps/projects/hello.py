import gradio as gr
from mymath.add import addition

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity) + str(addition(1,2 ))

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demo.launch()
