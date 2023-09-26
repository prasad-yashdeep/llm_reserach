from llama_cpp import Llama
llm = Llama(model_path="ggml-model-q4_0.bin")
# model = AutoModelForCausalLM.from_pretrained(
#     "TheBloke/Llama-2-7B-Chat-GGUF",
# )
output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True,n_gpu_layers= 25 )
print(output)