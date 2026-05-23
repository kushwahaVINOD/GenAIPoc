
import requests

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "qwen3.5:9b-mlx",  # Change to your preferred model name (e.g., llama2, mistral, etc.)
        "prompt": prompt,
        "stream": False     # Set to True if you want stream output instead
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
        result = response.json()
        return result.get("response", "No response from Ollama.")
    
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to Ollama. Make sure it's running at http://localhost:11434"
    except requests.exceptions.JSONDecodeError:
        return "Error: Invalid response from Ollama."
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Main interaction loop
if __name__ == "__main__":
    print("Ollama Chat with Python")
    print("=" * 50)
    
    while True:
        user_input = input("\nEnter your prompt (or 'quit' to exit): ")
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Exiting...")
            break
        
        response = call_ollama(user_input)
        print(f"\n🤖 Ollama: {response}")
'''
### How to Use

1. **Ensure Ollama is running locally**  
   Run in your terminal:
   ```bash
   ollama serve
   ```
   
2. **Load a model (optional)**  
   You may need to load the model before using it:
   ```bash
   ollama pull llama2
   # Or whichever model you're using
   ```

3. **Run the Python script**  
   ```bash
   python ollama_chat.py
```
'''
