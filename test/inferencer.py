from wayne_utils import load_data, save_data, get_ROOT_PATH
import os
import sys

_ROOT_PATH = get_ROOT_PATH( 2, __file__)
sys.path.insert(  0, _ROOT_PATH)
from llm_inferencer import Inferencer

def ins_inferencer():
    kwargs = {
        "local_or_remote" : "local",
        "server_or_reader" : "server",
        "model_name" : "ChatGLM3-6B",
        "gpu_list" : "0,3,4,5",
        "local_engine": "vllm"
    }
    inferencer = Inferencer( kwargs )
    inferencer.local_inference()
    return inferencer

inferencer = ins_inferencer()

print("******************************************************************************")
result = inferencer.request( "你好", 1)
print( f"回复为：{result}")