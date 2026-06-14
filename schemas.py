from pydantic import BaseModel


class Incidents(BaseModel):
    incident_id: str | None = None
    service: str | None = None
    severity: str | None = None
    date: str | None = None
    summary: str | None = None
    impact: str | None = None
    detection: str | None = None
    root_cause: str | None = None
    resolution: str | None = None
    page_number: int | None = None
    prevention_actions: str | None = None
    