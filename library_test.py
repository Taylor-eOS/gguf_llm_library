from gguf_llm_library import ask_llm

input_line = "You are a smart robot toy. Briefly introduce yourself."
result = ask_llm(input_line)
print(result)
input_line2 = "Name a good thing about smart robot toys."
result2 = ask_llm(input_line2)
print(result2)
