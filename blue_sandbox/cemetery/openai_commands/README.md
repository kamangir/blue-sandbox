# 🛠️ sentence -> image

```bash
@select - open; \
@openai generate image \
  ~dryrun,height=1024,width=1024 \
  carrot - \
  "an orange carrot walking on Mars."
```

![image](https://raw.githubusercontent.com/kamangir/openai-commands/main/assets/carrot.png)

# 🛠️ code generation

example notebooks to [generate python functions](../../notebooks/completion_ai_function_py.ipynb), special case for [image to image python functions](../../notebooks/completion_i2i_function.ipynb), and to [write a bash script](../../notebooks/completion_ai_function_bash.ipynb) to use a script, for example, [vancouver-watching](https://github.com/kamangir/vancouver-watching).

![image](https://github.com/kamangir/openai-commands/blob/main/assets/completion_i2i_function.png?raw=true)