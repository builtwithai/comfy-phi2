

class AINode:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "prompt": ("STRING", {
                    "multiline": True,
                    "default": "Write a joke on developers"
                }),
            },
            "optional": {
                "seed": ("INT", {"display": "number" , "default": 0}),
                "max_tokens": ("INT", {"display": "slider", "min": 100, "max": 100000, "step": 10, "default": 1000}),
                "temp": ("FLOAT", {"display": "slider", "min": 0.0, "max": 1.0, "step": 0.1, "default": 0.9}),
            },
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "askllm"

    # OUTPUT_NODE = False

    CATEGORY = "LLM"

    def askllm(self, prompt, max_tokens, temp, seed):
        from .old import ask
        output = ask("custom_nodes/cui-ai-nodes/mlx_model",
                     prompt, max_tokens, temp, seed )
        return (output,)


NODE_CLASS_MAPPINGS = {
    "AINode": AINode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "AINode": "AI Node"
}