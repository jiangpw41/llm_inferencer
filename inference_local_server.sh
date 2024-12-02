inference_start --local_or_remote local \
                --server_or_reader server \
                --model_name ChatGLM3-6B \
                --gpu_list 0,2,3,4,5 \
                --local_engine vllm