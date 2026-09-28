from memory import retain_memory, recall_memory

print("Storing test memory...")

retain_memory(
    """
    Customer requested WhatsApp notifications.
    The product team previously rejected this feature
    because customer demand was too low.
    """
)

print("Memory stored successfully!")

print("\nRecalling memory...")

memories = recall_memory(
    "What happened previously with WhatsApp notifications?"
)

print("\nHINDSIGHT RESULTS:")

for memory in memories:
    print("-", memory.get("text", memory))