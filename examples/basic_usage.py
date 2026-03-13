"""
Basic Usage Examples

This file demonstrates how to use the agent system.
"""

import sys
sys.path.insert(0, '..')

from src.agents import BaseAgent, TaskPlanningAgent, ToolUsingAgent
from src.tools import WebSearchTool, FileTool, CodeAnalysisTool


def example_task_planning():
    """Example: Using TaskPlanningAgent"""
    print("=" * 50)
    print("Example 1: Task Planning Agent")
    print("=" * 50)
    
    agent = TaskPlanningAgent(name="Planner")
    result = agent.execute("Build a web scraper for news articles")
    
    print(f"Task: {result['task']}")
    print(f"Plan ID: {result['plan_id']}")
    print("Steps:")
    for step in result['steps']:
        print(f"  {step['step']}. {step['action']}: {step['description']}")
    print()


def example_tool_using():
    """Example: Using ToolUsingAgent"""
    print("=" * 50)
    print("Example 2: Tool Using Agent")
    print("=" * 50)
    
    agent = ToolUsingAgent(name="ToolMaster")
    
    # Add tools to the agent
    agent.add_tool(WebSearchTool())
    agent.add_tool(FileTool())
    agent.add_tool(CodeAnalysisTool())
    
    # Execute tasks
    tasks = [
        "Search for latest AI news",
        "Read the configuration file",
        "Review the main module code"
    ]
    
    for task in tasks:
        print(f"Task: {task}")
        result = agent.execute(task)
        print(f"Status: {result['status']}")
        if result['results']:
            for r in result['results']:
                print(f"  Tool: {r['tool']}")
        print()


def example_memory():
    """Example: Using Agent Memory"""
    print("=" * 50)
    print("Example 3: Agent Memory")
    print("=" * 50)
    
    agent = BaseAgent(name="MemoryBot")
    
    # Store some memories
    agent.store_memory("user_preference", "dark_mode")
    agent.store_memory("last_task", "code_review")
    agent.store_memory("session_count", 42)
    
    # Retrieve memories
    print(f"User preference: {agent.retrieve_memory('user_preference')}")
    print(f"Last task: {agent.retrieve_memory('last_task')}")
    print(f"Session count: {agent.retrieve_memory('session_count', 0)}")
    print(f"Unknown key: {agent.retrieve_memory('unknown', 'default_value')}")
    print()


if __name__ == "__main__":
    example_task_planning()
    example_tool_using()
    example_memory()
    print("All examples completed!")
