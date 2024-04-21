from langchain.agents import AgentExecutor, create_openai_tools_agent


class AiAgent:

    def return_agent_executor(chat, tools, promt):
        agent = create_openai_tools_agent(chat, tools, promt)
        agent_executor = AgentExecutor(
            agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
        )
        return agent_executor
