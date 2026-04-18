import eel
from engine.command import *

# -------------------------
# ✅ INIT EEL
# -------------------------
eel.init("www")

print("✅ Jarvis Started...")

# -------------------------
# ✅ START EEL
# -------------------------
eel.start(
    "index.html",
    mode="edge",        # browser auto open hoga
    host="localhost",
    port=8080,          # 🔥 port change (error fix)
    block=True
)