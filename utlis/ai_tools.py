from langchain_core.tools import tool


class AITools:

    @tool
    def output_name_tool(data):
        """return all the data in a structured output"""
        return data
