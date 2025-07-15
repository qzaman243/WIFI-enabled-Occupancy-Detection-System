# # watcher.py

# import importlib.util
# import sys
# import time
# import os
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# from predictor import predict_from_numpy # type: ignore





# class CSIFileHandler(FileSystemEventHandler):
#     def __init__(self, room_type="small"):
#         self.room_type = room_type

#     def on_created(self, event):
#         if event.src_path.endswith(".pcap"):
#             print(f"[📥] New file detected: {event.src_path}")
#             try:
#                 np_data = preprocess_pcap(event.src_path)
#                 result = predict_from_numpy(np_data, self.room_type)
#                 print(f"[✅] Prediction: {result}")

#                 # Optional: log results
#                 with open("logs/predictions.log", "a") as log:
#                     log.write(f"{time.ctime()} | {os.path.basename(event.src_path)} | {result}\n")

#                 os.remove(event.src_path)  # Clean up

#             except Exception as e:
#                 print(f"[❌] Error: {e}")

# def start_watcher(folder="incoming_data", room_type="small"):
#     os.makedirs(folder, exist_ok=True)
#     os.makedirs("logs", exist_ok=True)

#     event_handler = CSIFileHandler(room_type)
#     observer = Observer()
#     observer.schedule(event_handler, folder, recursive=False)
#     observer.start()
#     print(f"[👀] Watching folder: {folder} (Room type: {room_type})")

#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
