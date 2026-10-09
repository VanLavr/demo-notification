"""Доменные модели: данные, с которыми работает бизнес-логика.

Это обычные dataclass, без FastAPI, Pydantic, HTTP или SQL. Входной DTO
преобразуется в NotificationData в controller; repository возвращает Notification.
"""
