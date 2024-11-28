from wayne_utils import load_data, save_data, get_ROOT_PATH
import os
import sys

from llm_inferencer import Register

reg = Register()
reg.empty_list()
# 注册本地模型
reg.add_local_model( "ChatGLM3-6B", "/home/jiangpeiwen2/jiangpeiwen2/workspace/LLMs/ChatGLM3-6B/ZhipuAI/chatglm3-6b")
reg.add_local_model( "Baichuan2-7B-Chat", "/home/jiangpeiwen2/jiangpeiwen2/workspace/LLMs/Baichuan2-7B-Chat")
reg.add_local_model( "Chinese-Mistral-7B-Instruct-v0.1", "/home/jiangpeiwen2/jiangpeiwen2/workspace/LLMs/Chinese-Mistral-7B-Instruct-v0.1")

# 注册API
reg.add_remote_model( "NL2GQL", "sk-t4Mv9tJa0ftMCcKqKMAlqJmq3x5Da83Pk4U4Jq2M98C57GZG", 
                    model_list=['gpt-3.5-turbo',
                                'gpt-3.5-turbo-1106',
                                'gpt-4',
                                'gpt-4-0125-preview',
                                'gpt-4-turbo',
                                'gpt-4o',
                                'gpt-4o-2024-08-06',
                                'claude-2',
                                'claude-3-5-sonnet',
                                'llama-3-70b'
                                ])
reg.list_models()

"""
inference_start --local_or_remote local --server_or_reader server --model_name ChatGLM3-6B --gpu_list 0,2,3,4,5 --local_engine vllm
"""