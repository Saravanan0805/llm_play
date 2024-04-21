from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
import os
from rest_framework import status
import json
from llm_play import settings
from llm_serve.serializers import LLMInputSerializer
from utlis import prompts, ai_tools, chat_prompt, agent
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


chat = settings.chat


class OnboardAPI(APIView):
    def post(self, request: Request):
        serializer = LLMInputSerializer(data=request.data)
        if serializer.is_valid():
            prompt_text = prompts.prompt_text
            tools = [ai_tools.AITools.output_name_tool]
            prompt = chat_prompt.ChatPromt.return_chat_prompt(prompt_text)
            messages = serializer.validated_data["messages"]
            message_input = []

            for message in messages:
                if message["role"] == "human":
                    message_input.append(HumanMessage(content=message["content"]))
                elif message["role"] == "system":
                    message_input.append(AIMessage(content=message["content"]))

            agent_executor = agent.AiAgent.return_agent_executor(chat, tools, prompt)
            data = agent_executor.invoke(
                {
                    "messages": message_input,
                }
            )
            return Response({"data": data["output"]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
