from app.services.vector_store import add_documents

docs = [
    "High CPU usage is often caused by browser tabs or background processes.",
    "Memory spikes may indicate memory leaks or too many applications running.",
    "Disk usage issues can slow down the system significantly."
]

add_documents("laptop_metrics", docs)

print("Documents ingested!")
