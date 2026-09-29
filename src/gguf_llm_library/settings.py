MODELS = [
    {
        "repo_id": "bartowski/SmolLM2-1.7B-Instruct-GGUF",
        "filename": "SmolLM2-1.7B-Instruct-Q6_K_L.gguf", #1.4GB
    },
    {
        "repo_id": "Qwen/Qwen2.5-1.5B-Instruct-GGUF",
        "filename": "qwen2.5-1.5b-instruct-q6_k.gguf", #1.5GB
    },
    {
        "repo_id": "unsloth/gemma-4-E2B-it-GGUF",
        "filename": "gemma-4-E2B-it-UD-Q4_K_XL.gguf", #3.2GB
    },
    {
        "repo_id": "bartowski/Mistral-7B-Instruct-v0.3-GGUF",
        "filename": "Mistral-7B-Instruct-v0.3-Q3_K_S.gguf", #3.8GB
    },
    {
        "repo_id": "unsloth/gemma-4-E4B-it-GGUF",
        "filename": "gemma-4-E4B-it-UD-Q4_K_XL.gguf", #5.1GB
    },
    {
        "repo_id": "bartowski/ibm-granite_granite-4.1-8b-GGUF",
        "filename": "ibm-granite_granite-4.1-8b-Q4_K_M.gguf", #5.5GB
    },
    {
        "repo_id": "yuxinlu1/gemma-4-12B-coder-fable5-composer2.5-v1-GGUF",
        "filename": "gemma4-coding-Q4_K_M.gguf", #7.4GB
    },
]
N_CTX = 4 * 1024
N_THREADS = 6
N_GPU_LAYERS = 0
MAX_TOKENS = None #default None
TEMPERATURE = 0.7 #default 0.8
REPEAT_PENALTY = 1.1 #default 1.0
DEFAULT_MODEL = 1
SYSTEM_PROMPT = "This is a text processing script. Do not include anything other than the requested response itself."
