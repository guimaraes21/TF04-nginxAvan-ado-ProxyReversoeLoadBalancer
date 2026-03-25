import os

INSTANCE_ID = os.environ.get("INSTANCE_ID", "unknown")
INSTANCE_NAME = os.environ.get("INSTANCE_NAME", "backend")
PORT = int(os.environ.get("PORT", 5000))
