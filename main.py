import subprocess

def run_script(script_name):
    """Run a regular Python script synchronously."""
    try:
        print(f"Running {script_name}...")
        subprocess.run(["python3", script_name], check=True)
        print(f"{script_name} completed.\n")
    except subprocess.CalledProcessError as e:
        print(f"Error while running {script_name}: {e}")
        exit(1)

def run_streamlit_app(script_name):
    """Launch a Streamlit app (chatbot2.py)."""
    try:
        print(f"Launching Streamlit app: {script_name} ...")
        subprocess.run(["streamlit", "run", script_name], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to launch Streamlit app: {e}")
        exit(1)

if __name__ == "__main__":
    # Step 1: Run BM25 retrieval logic
    run_script("BM_25.py")

    # Step 2: Launch chatbot2.py with Streamlit
    run_streamlit_app("chatbot2.py")
