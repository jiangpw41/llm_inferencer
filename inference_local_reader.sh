inference_start --local_or_remote local \
                --server_or_reader reader \
                --prompt_list_from_path /home/jiangpeiwen2/jiangpeiwen2/projects/TKGT/code_example/Hybird_RAG/temp/cpl/cpl_data_try_cell_all_prompt_list.pickle \
                --predict_list_to_path /home/jiangpeiwen2/jiangpeiwen2/cpl_data_cell_all_predict_list.pickle \
                --model_name ChatGLM3-6B \
                --gpu_list 0,2,3,4,5 \
                --local_engine vllm