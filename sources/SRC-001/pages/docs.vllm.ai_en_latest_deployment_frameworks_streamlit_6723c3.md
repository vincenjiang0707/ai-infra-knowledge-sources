source: https://docs.vllm.ai/en/latest/deployment/frameworks/streamlit/
lastmod: 2026-09-23

# Streamlit[¶](https://docs.vllm.ai#streamlit)

[Streamlit](https://github.com/streamlit/streamlit) lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps.

It can be quickly integrated with vLLM as a backend API server, enabling powerful LLM inference via API calls.

## Prerequisites[¶](https://docs.vllm.ai#prerequisites)

Set up the vLLM environment by installing all required packages:

## Deploy[¶](https://docs.vllm.ai#deploy)

-
Start the vLLM server with a supported chat completion model, e.g.

-
Use the script:

[examples/applications/chatbot/streamlit_openai_chatbot_webserver.py](https://github.com/vllm-project/vllm/blob/main/examples/applications/chatbot/streamlit_openai_chatbot_webserver.py) -
Start the streamlit web UI and start to chat:

[streamlit run streamlit_openai_chatbot_webserver.py](https://docs.vllm.ai#__codelineno-2-1)[# or specify the VLLM_API_BASE or VLLM_API_KEY](https://docs.vllm.ai#__codelineno-2-3)[VLLM_API_BASE="http://vllm-server-host:vllm-server-port/v1" \](https://docs.vllm.ai#__codelineno-2-4)[streamlit run streamlit_openai_chatbot_webserver.py](https://docs.vllm.ai#__codelineno-2-5)[# start with debug mode to view more details](https://docs.vllm.ai#__codelineno-2-7)[streamlit run streamlit_openai_chatbot_webserver.py --logger.level=debug](https://docs.vllm.ai#__codelineno-2-8)