from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
import logging
import time
import json
from datetime import datetime

logger = logging.getLogger(__name__)


class AgentBase(ABC):
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.execution_history: List[Dict[str, Any]] = []
        self.metrics: Dict[str, Any] = {
            "total_executions": 0,
            "successful_executions": 0,
            "failed_executions": 0,
            "total_execution_time": 0.0,
            "average_execution_time": 0.0
        }
        self._validate_config()
        logger.info(f"{self.__class__.__name__} initialized")
    
    @abstractmethod
    def run(self, input_data: Any) -> Dict[str, Any]:
        raise NotImplementedError("Subclasses must implement run()")
    
    def get_config(self) -> Dict[str, Any]:
        return self.config.copy()
    
    def update_config(self, new_config: Dict[str, Any]) -> None:
        self.config.update(new_config)
        self._validate_config()
        logger.info("Configuration updated")
    
    def get_metrics(self) -> Dict[str, Any]:
        return self.metrics.copy()
    
    def get_execution_history(self, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        if limit:
            return self.execution_history[-limit:]
        return self.execution_history.copy()
    
    def clear_history(self) -> None:
        self.execution_history.clear()
        self.metrics = {
            "total_executions": 0,
            "successful_executions": 0,
            "failed_executions": 0,
            "total_execution_time": 0.0,
            "average_execution_time": 0.0
        }
        logger.info("History cleared")
    
    def _track_execution(self, input_data: Any, result: Dict[str, Any], 
                        execution_time: float, success: bool) -> None:
        execution_entry = {
            "timestamp": datetime.now().isoformat(),
            "input": str(input_data)[:100],
            "success": success,
            "execution_time": execution_time,
            "result_summary": str(result).get("status", "unknown")
        }
        
        self.execution_history.append(execution_entry)
        
        self.metrics["total_executions"] += 1
        if success:
            self.metrics["successful_executions"] += 1
        else:
            self.metrics["failed_executions"] += 1
        
        self.metrics["total_execution_time"] += execution_time
        self.metrics["average_execution_time"] = (
            self.metrics["total_execution_time"] / self.metrics["total_executions"]
        )
    
    def _validate_config(self) -> None:
        if "region" in self.config:
            valid_regions = ["us-east-1", "us-west-2", "eu-west-1", "ap-southeast-1"]
            if self.config["region"] not in valid_regions:
                logger.warning(f"Unusual AWS region: {self.config['region']}")
        
        if "temperature" in self.config:
            temp = self.config["temperature"]
            if not 0.0 <= temp <= 1.0:
                raise ValueError(f"Temperature must be between 0.0 and 1.0, got {temp}")
    
    def _safe_config(self) -> Dict[str, Any]:
        safe = self.config.copy()
        sensitive_keys = ["api_key", "secret", "password", "token"]
        for key in sensitive_keys:
            if key in safe:
                safe[key] = "***REDACTED***"
        return safe
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(config={self._safe_config()})"
    
    def __str__(self) -> str:
        return f"{self.__class__.__name__} with {len(self.config)} config parameters"

