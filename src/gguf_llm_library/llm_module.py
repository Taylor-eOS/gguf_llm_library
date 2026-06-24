from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from . import settings

_llm = None
_model_index = None

def _get_llm(model):
    global _llm, _model_index
    index = int(model) if model is not None else settings.DEFAULT_MODEL
    if index < 0 or index >= len(settings.MODELS):
        raise ValueError(f"Model index {index} out of range (0-{len(settings.MODELS)-1})")
    if _llm is not None:
        if index != _model_index:
            raise RuntimeError(f"Model {index} requested but model {_model_index} is already loaded")
        return _llm
    entry = settings.MODELS[index]
    path = hf_hub_download(repo_id=entry["repo_id"], filename=entry["filename"])
    _llm = Llama(model_path=path, n_ctx=settings.N_CTX, n_threads=settings.N_THREADS, n_gpu_layers=settings.N_GPU_LAYERS, verbose=False)
    _model_index = index
    return _llm

def ask_llm(prompt, model=None):
    llm = _get_llm(model)
    messages = [
        {"role": "user", "content": settings.SYSTEM_PROMPT + "\n" + prompt},
    ]
    result = llm.create_chat_completion(
        messages=messages,
        stream=False,
        max_tokens=settings.MAX_TOKENS,
        temperature=settings.TEMPERATURE,
        repeat_penalty=settings.REPEAT_PENALTY,
    )
    return result["choices"][0]["message"]["content"].strip()
