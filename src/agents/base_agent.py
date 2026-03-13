"""
Base Agent Implementation

This module provides the core agent architecture for task planning and execution.
"""

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
import uuid


class BaseAgent(ABC):
    """
    Abstract base class for all agent implementations.
    
    Attributes:
        agent_id: Unique identifier for the agent
        name: Human-readable name for the agent
        tools: List of available tools for the agent
    """
    
    def __init__(self, name: str = "BaseAgent", tools: Optional[List[Any]] = None):
        self.agent_id = str(uuid.uuid4())
        self.name = name
        self.tools = tools or []
        self.memory: Dict[str, Any] = {}
    
    @abstractmethod
    def execute(self, task: str, context: Optional[Dict] = None) -> Any:
        """
        Execute a given task with optional context.
        
        Args:
            task: The task description to execute
            context: Optional context dictionary for the task
            
        Returns:
            The result of task execution
        """
        pass
    
    def add_tool(self, tool: Any) -> None:
        """Add a tool to the agent's toolkit."""
        self.tools.append(tool)
    
    def remove_tool(self, tool_name: str) -> bool:
        """Remove a tool by name from the agent's toolkit."""
        for i, tool in enumerate(self.tools):
            if getattr(tool, 'name', None) == tool_name:
                self.tools.pop(i)
                return True
        return False
    
    def store_memory(self, key: str, value: Any) -> None:
        """Store a value in the agent's memory."""
        self.memory[key] = value
    
    def retrieve_memory(self, key: str, default: Any = None) -> Any:
        """Retrieve a value from the agent's memory."""
        return self.memory.get(key, default)
    
    def clear_memory(self) -> None:
        """Clear all stored memory."""
        self.memory.clear()


class TaskPlanningAgent(BaseAgent):
    """
    Agent specialized in task planning and decomposition.
    """
    
    def __init__(self, name: str = "TaskPlanningAgent", **kwargs):
        super().__init__(name=name, **kwargs)
        self.plans: Dict[str, List[Dict]] = {}
    
    def execute(self, task: str, context: Optional[Dict] = None) -> Dict:
        """
        Execute task by creating a plan and returning execution details.
        """
        plan_id = str(uuid.uuid4())
        plan = self._create_plan(task, context)
        self.plans[plan_id] = plan
        
        return {
            "plan_id": plan_id,
            "task": task,
            "steps": plan,
            "status": "planned"
        }
    
    def _create_plan(self, task: str, context: Optional[Dict] = None) -> List[Dict]:
        """Create a step-by-step plan for the task."""
        # Placeholder implementation - to be extended
        return [
            {
                "step": 1,
                "action": "analyze",
                "description": f"Analyze task: {task}"
            },
            {
                "step": 2,
                "action": "execute",
                "description": "Execute planned actions"
            },
            {
                "step": 3,
                "action": "validate",
                "description": "Validate results"
            }
        ]


class ToolUsingAgent(BaseAgent):
    """
    Agent that can utilize tools to accomplish tasks.
    """
    
    def __init__(self, name: str = "ToolUsingAgent", **kwargs):
        super().__init__(name=name, **kwargs)
        self.tool_results: List[Dict] = []
    
    def execute(self, task: str, context: Optional[Dict] = None) -> Dict:
        """Execute task using available tools."""
        results = []
        
        for tool in self.tools:
            if hasattr(tool, 'can_handle') and tool.can_handle(task):
                result = tool.execute(task, context)
                results.append({
                    "tool": getattr(tool, 'name', 'unknown'),
                    "result": result
                })
                self.tool_results.append(results[-1])
        
        return {
            "task": task,
            "results": results,
            "status": "completed" if results else "no_suitable_tool"
        }
