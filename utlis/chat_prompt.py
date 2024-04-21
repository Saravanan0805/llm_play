from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


class ChatPromt:

    def return_chat_prompt(prompt_text):
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    prompt_text,
                ),
                MessagesPlaceholder(variable_name="messages"),
                MessagesPlaceholder(variable_name="agent_scratchpad"),
            ]
        )
        return prompt
