# Work with different LLMs and parameters

A Python implementation task to work with different LLMs (Large Language Models) and request parameters via DIAL API

## 🎓 Learning Goals

By completing these tasks, you will learn:
- How to work with different LLMs through DIAL API
- How can we configure LLM output via request parameters (`temperature`, `n`, `seed`, etc...)


## 📋 Requirements

- Python 3.11+
- pip
- API key for DIAL service
- Basic understanding of HTTP requests and async/await

## 🔧 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key:**
    - Ensure that you connected to the EPAM VPN
    - Get the DIAL API key here: https://support.epam.com/ess?id=sc_cat_item&table=sc_cat_item&sys_id=910603f1c3789e907509583bb001310c
    - Get available models from: https://ai-proxy.lab.epam.com/openai/models

3. **Project structure:**
   ```
   task/
   ├── models/
   │   ├── conversation.py          # ✅ Complete
   │   ├── message.py               # ✅ Complete  
   │   └── role.py                  # ✅ Complete   
   ├── app/
   │   ├── main.py                  # ✅ Complete
   │   └── client.py                # ✅ Complete
   ├── 1-task-models.py             # 🚧 TODO
   ├── 2-task-n.py                  # 🚧 TODO
   ├── 3-task-temperature.py        # 🚧 TODO
   ├── 4-task-seed.py               # 🚧 TODO
   ├── 5-task-max_tokens.py         # 🚧 TODO
   ├── 6-task-frequency_penalty.py  # 🚧 TODO
   ├── 7-task-presence_penalty.py   # 🚧 TODO
   └── 8-task-stop.py               # 🚧 TODO
   ```

## 📝 Your Tasks

Implement all tasks from these files:
- 1-task-models.py 
- 2-task-n.py 
- 3-task-temperature.py 
- 4-task-seed.py     
- 5-task-max_tokens.py   
- 6-task-frequency_penalty.py 
- 7-task-presence_penalty.py
- 8-task-stop.py     


# <img src="dialx-banner.png">