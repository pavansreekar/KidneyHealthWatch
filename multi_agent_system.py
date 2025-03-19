import time
import threading

# Define agent functions
def data_analysis_agent():
    for _ in range(5):  # Run only 5 times
        print("[DataAnalysisAgent] Analyzing patient data...")
        time.sleep(2)

def outreach_agent():
    for _ in range(5):
        print("[OutreachAgent] Sending alerts for at-risk patients...")
        time.sleep(2)

def scheduling_agent():
    for _ in range(5):
        print("[SchedulingAgent] Scheduling follow-up appointments...")
        time.sleep(2)

def monitoring_agent():
    for _ in range(5):
        print("[MonitoringAgent] Monitoring for new patient data...")
        time.sleep(2)

# Create agent threads
agents = [
    threading.Thread(target=data_analysis_agent),
    threading.Thread(target=outreach_agent),
    threading.Thread(target=scheduling_agent),
    threading.Thread(target=monitoring_agent)
]

# Start agents
for agent in agents:
    agent.start()

# Wait for all agents to complete
for agent in agents:
    agent.join()

print("\n✅ Multi-Agent System Execution Completed!")
