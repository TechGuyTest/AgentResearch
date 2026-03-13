# Agent Research

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: Proprietary](https://img.shields.io/badge/license-proprietary-red.svg)](LICENSE)

A research project focused on AI agent development and experimentation.

> 🤖 Build intelligent agents with modular architecture, tool integration, and autonomous task planning capabilities.

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

## Requirements

- Python 3.8 or higher
- No external dependencies required (uses Python standard library only)

## Installation

```bash
# Clone the repository
git clone https://github.com/TechGuyTest/AgentResearch.git

# Navigate to the project directory
cd AgentResearch

# No external dependencies required for core functionality
# The project uses only Python standard library
```

### Optional: Create a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
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
1. **Task Planning Agent** - Decomposes complex tasks into executable steps
2. **Tool Using Agent** - Routes tasks to appropriate tools automatically
3. **Agent Memory** - Demonstrates context persistence and retrieval

### Expected Output

```
==================================================
Example 1: Task Planning Agent
==================================================
Task: Build a web scraper for news articles
Plan ID: <uuid>
Steps:
  1. analyze: Analyze task: Build a web scraper for news articles
  2. execute: Execute planned actions
  3. validate: Validate results
```

## Testing

Run the examples to verify the installation:

```bash
cd examples
python basic_usage.py
```

All examples should complete without errors.

## Development

### Code Structure

```
src/
├── agents/           # Agent implementations
│   ├── __init__.py
│   └── base_agent.py # BaseAgent, TaskPlanningAgent, ToolUsingAgent
└── tools/            # Tool integrations
    ├── __init__.py
    └── base_tool.py  # BaseTool, WebSearchTool, FileTool, CodeAnalysisTool
```

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

## Best Practices

1. **Keep Agents Focused**: Each agent should have a single responsibility
2. **Tool Naming**: Use descriptive, lowercase names with underscores (e.g., `web_search`)
3. **Context Passing**: Use the context dictionary to share state between tool executions
4. **Memory Management**: Clear memory when starting new sessions to avoid stale data
5. **Error Handling**: Implement proper error handling in tool execution

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Import errors | Ensure you're running from the `examples` directory or add `src` to PYTHONPATH |
| Tool not triggering | Check that your task contains keywords from the tool's `can_handle` method |
| Memory not persisting | Memory is session-based; use external storage for long-term persistence |

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is proprietary and confidential.

## Contact

For questions or contributions, please open an issue or contact the repository maintainer.

---

**Built with ❤️ for AI Agent Research**
