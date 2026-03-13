# Agent Research

A research project focused on AI agent development and experimentation.

## Overview

This repository contains research and development work related to intelligent agent systems, including:

- **Agent Architecture**: Modular base classes for building custom agents
- **Task Planning**: Automated task decomposition and execution planning
- **Tool Integration**: Extensible tool system for agent capabilities
- **Memory Management**: Persistent and contextual memory systems
- **LLM-Powered Decision Making**: Foundation for AI-driven task execution

## Project Structure

```
AgentResearch/
├── README.md              # Project documentation
├── src/                   # Source code
│   ├── __init__.py
│   ├── agents/            # Agent implementations
│   │   ├── __init__.py
│   │   └── base_agent.py  # BaseAgent, TaskPlanningAgent, ToolUsingAgent
│   └── tools/             # Tool integrations
│       ├── __init__.py
│       └── base_tool.py   # BaseTool, WebSearchTool, FileTool, CodeAnalysisTool
└── examples/              # Usage examples
    └── basic_usage.py     # Complete usage demonstrations
```

## Features

- **Modular Agent Design**: Abstract base classes for flexible agent architecture
- **Tool Integration**: Plug-and-play tool system with automatic task matching
- **Task Planning**: Built-in planning agent for task decomposition
- **Memory Management**: Key-value memory storage for context persistence
- **Extensible Architecture**: Easy to add new agents and tools

## Installation

```bash
# Clone the repository
git clone https://github.com/TechGuyTest/AgentResearch.git

# Navigate to the project directory
cd AgentResearch

# No external dependencies required for core functionality
# The project uses only Python standard library
```

## Quick Start

### Task Planning Agent

```python
from src.agents import TaskPlanningAgent

agent = TaskPlanningAgent(name="Planner")
result = agent.execute("Build a web scraper for news articles")

print(f"Plan ID: {result['plan_id']}")
for step in result['steps']:
    print(f"  {step['step']}. {step['action']}: {step['description']}")
```

### Tool-Using Agent

```python
from src.agents import ToolUsingAgent
from src.tools import WebSearchTool, FileTool, CodeAnalysisTool

agent = ToolUsingAgent(name="ToolMaster")
agent.add_tool(WebSearchTool())
agent.add_tool(FileTool())
agent.add_tool(CodeAnalysisTool())

result = agent.execute("Search for latest AI news")
```

### Agent Memory

```python
from src.agents import BaseAgent

agent = BaseAgent(name="MemoryBot")
agent.store_memory("user_preference", "dark_mode")
preference = agent.retrieve_memory("user_preference")
```

## Available Agents

| Agent | Description |
|-------|-------------|
| `BaseAgent` | Abstract base class with memory and tool management |
| `TaskPlanningAgent` | Decomposes tasks into executable steps |
| `ToolUsingAgent` | Routes tasks to appropriate tools automatically |

## Available Tools

| Tool | Description | Triggers |
|------|-------------|----------|
| `WebSearchTool` | Web search functionality | "search", "find", "look up", "query" |
| `FileTool` | File read/write operations | "read", "write", "file", "save", "load" |
| `CodeAnalysisTool` | Code review and analysis | "analyze", "review", "code", "lint", "check" |

## Running Examples

```bash
cd examples
python basic_usage.py
```

This runs three demonstrations:
1. Task planning with step decomposition
2. Tool-using agent with multiple tools
3. Agent memory storage and retrieval

## Development

### Adding a New Agent

```python
from src.agents import BaseAgent

class MyCustomAgent(BaseAgent):
    def execute(self, task: str, context: dict = None) -> any:
        # Implement your agent logic here
        pass
```

### Adding a New Tool

```python
from src.tools import BaseTool

class MyCustomTool(BaseTool):
    name = "my_tool"
    description = "My custom tool description"
    
    def can_handle(self, task: str) -> bool:
        # Return True if this tool can handle the task
        pass
    
    def execute(self, task: str, context: dict = None) -> any:
        # Implement tool logic here
        pass
```

## License

This project is proprietary and confidential.

## Contact

For questions or contributions, please open an issue or contact the repository maintainer.
