"""Offline checks for the learner-facing episode bundle."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).parents[1]
trace = json.loads((ROOT / "trace.json").read_text())
events = trace["events"]
assert trace["schema_version"] == "trace/v0.1"
assert [event["logical_time"] for event in events] == list(range(len(events)))
ids = {event["id"] for event in events}
assert all(parent in ids for event in events for parent in event["causal_parents"])
assert len(trace["assertions"]) == 4
assert all(item["status"] == "pass" for item in trace["assertions"])
print("PASS: bounded agent-loop episode has ordered events, causal parents, and explicit verification evidence")
