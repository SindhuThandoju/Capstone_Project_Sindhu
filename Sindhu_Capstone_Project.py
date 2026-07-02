{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPNEhz3UsVxFQ/verqPlBOl"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "C28t3KWAk2s3"
      },
      "outputs": [],
      "source": [
        "!pip install -q streamlit pyngrok google-generativeai"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%writefile app.py\n",
        "\n",
        "import streamlit as st\n",
        "import google.generativeai as genai\n",
        "\n",
        "# Configure Gemini API\n",
        "genai.configure(api_key=\"AQ.Ab8RN6IUrSXVxgTWa96UZNSKdLSNA68pl1sth_9W3StPIDwjeA\")\n",
        "\n",
        "model = genai.GenerativeModel(\"gemini-2.5-flash\")\n",
        "\n",
        "st.set_page_config(page_title=\"AI Learning Buddy Sindhu\", page_icon=\"🎓\")\n",
        "\n",
        "st.title(\"🎓 AI Learning Buddy Sindhu\")\n",
        "\n",
        "topic = st.text_input(\"Enter a Topic\")\n",
        "\n",
        "option = st.selectbox(\n",
        "    \"Choose Activity\",\n",
        "    [\n",
        "        \"Explain Concept\",\n",
        "        \"Real-Life Example\",\n",
        "        \"Generate Quiz\",\n",
        "        \"Ask Anything\"\n",
        "    ]\n",
        ")\n",
        "\n",
        "if st.button(\"Generate\"):\n",
        "\n",
        "    if topic == \"\":\n",
        "        st.warning(\"Please enter a topic.\")\n",
        "    else:\n",
        "\n",
        "        if option == \"Explain Concept\":\n",
        "            prompt = f\"Explain {topic} in simple language for a beginner.\"\n",
        "\n",
        "        elif option == \"Real-Life Example\":\n",
        "            prompt = f\"Give one simple real-life example of {topic}.\"\n",
        "\n",
        "        elif option == \"Generate Quiz\":\n",
        "            prompt = f\"Create 5 MCQs on {topic} with answers.\"\n",
        "\n",
        "        else:\n",
        "            prompt = topic\n",
        "\n",
        "        response = model.generate_content(prompt)\n",
        "\n",
        "        st.write(response.text)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l9ioxsSapVS4",
        "outputId": "d354beba-573e-4708-9729-dd6176e2030f"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting app.py\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!nohup streamlit run app.py --server.port 8501 &"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MdX8NK3IqJKJ",
        "outputId": "1f9da2ca-a1ff-46a1-a2be-dfaef20a5717"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "nohup: appending output to 'nohup.out'\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import time"
      ],
      "metadata": {
        "id": "tD5iPaaNqkIP"
      },
      "execution_count": 27,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "time.sleep(10)\n"
      ],
      "metadata": {
        "id": "g0bSxzsCqlCi"
      },
      "execution_count": 28,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!cat nohup.out"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OLYPJz8aq99d",
        "outputId": "1fd2e7ae-6617-447a-d713-d7c1d07aaeaa"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 18:48:40.956 Uvicorn server started on 0.0.0.0:8501\n",
            "\n",
            "  You can now view your Streamlit app in your browser.\n",
            "\n",
            "  Local URL: http://localhost:8501\n",
            "  Network URL: http://172.28.0.12:8501\n",
            "  External URL: http://34.29.150.92:8501\n",
            "\n",
            "/content/app.py:3: FutureWarning: \n",
            "\n",
            "All support for the `google.generativeai` package has ended. It will no longer be receiving \n",
            "updates or bug fixes. Please switch to the `google.genai` package as soon as possible.\n",
            "See README for more details:\n",
            "\n",
            "https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md\n",
            "\n",
            "  import google.generativeai as genai\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 18:53:23.232 Port 8501 is not available\n",
            "  Stopping...\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 19:56:10.073 Uvicorn server started on 0.0.0.0:8501\n",
            "\n",
            "  You can now view your Streamlit app in your browser.\n",
            "\n",
            "  Local URL: http://localhost:8501\n",
            "  Network URL: http://172.28.0.12:8501\n",
            "  External URL: http://34.29.150.92:8501\n",
            "\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 20:01:46.970 Port 8501 is not available\n",
            "  Stopping...\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 20:04:36.970 Uvicorn server started on 0.0.0.0:8501\n",
            "\n",
            "  You can now view your Streamlit app in your browser.\n",
            "\n",
            "  Local URL: http://localhost:8501\n",
            "  Network URL: http://172.28.0.12:8501\n",
            "  External URL: http://34.29.150.92:8501\n",
            "\n",
            "/content/app.py:3: FutureWarning: \n",
            "\n",
            "All support for the `google.generativeai` package has ended. It will no longer be receiving \n",
            "updates or bug fixes. Please switch to the `google.genai` package as soon as possible.\n",
            "See README for more details:\n",
            "\n",
            "https://github.com/google-gemini/deprecated-generative-ai-python/blob/main/README.md\n",
            "\n",
            "  import google.generativeai as genai\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 21:49:13.056 Port 8501 is not available\n",
            "\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.\n",
            "\n",
            "2026-07-02 22:21:46.108 Port 8501 is not available\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q pyngrok"
      ],
      "metadata": {
        "id": "xMo4X1vVrHi1"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from pyngrok import ngrok\n",
        "\n",
        "ngrok.set_auth_token(\"3FrBNzcGLHxCu0wO0kROA0R9dtY_FC6MLcZBgz8gdHsCvLuk\")"
      ],
      "metadata": {
        "id": "UrhyoGTOrO51"
      },
      "execution_count": 31,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "public_url = ngrok.connect(8501)\n",
        "\n",
        "\n",
        "print(public_url)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3VqofiN7rryL",
        "outputId": "a698f627-d350-45c6-a645-ab3d9b772130"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "NgrokTunnel: \"https://democrat-attendee-marmalade.ngrok-free.dev\" -> \"http://localhost:8501\"\n"
          ]
        }
      ]
    }
  ]
}