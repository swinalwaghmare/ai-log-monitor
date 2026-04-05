def is_error(log: dict) -> bool:
    """Detect if log is an error"""
    return log.get("level") == "ERROR"