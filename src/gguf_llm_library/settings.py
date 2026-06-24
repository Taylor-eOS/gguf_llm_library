MODELS = [
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-IQ4_XS.gguf", #940MB, tiny but doesn't restrict output to requested words
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf", #1.46GB
    },
    {
        "repo_id": "squ11z1/Mythos-nano", #3B
        "filename": "mythos-nano-Q4_K_M.gguf", #1.93GB
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-IQ3_M.gguf", #3.29GB, possible Pi size
    },
    {
        "repo_id": "Jackrong/Qwopus3.5-9B-Coder-GGUF", #claims class leader
        "filename": "Qwopus3.5-9B-coder-Exp-IQ4_XS.gguf", #5.23GB
    },
]
N_CTX = 4 * 1024
N_THREADS = 6
N_GPU_LAYERS = 0
MAX_TOKENS = None #default None
TEMPERATURE = 0.7 #default 0.8
REPEAT_PENALTY = 1.1 #default 1.0
DEFAULT_MODEL = 0
SYSTEM_PROMPT = "You are a processing tool that is called from a script. Respond with a single string containing your response. Do not include anything other than the response itself."
