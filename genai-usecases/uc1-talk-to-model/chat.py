import boto3

# Bedrock Runtime is the client for *using* models (vs "Bedrock" client which manages model access/config)
client = boto3.client("bedrock-runtime", region_name="eu-central-1")

def ask_claude(prompt: str) -> str:
    response = client.converse(
        modelId="eu.anthropic.claude-sonnet-4-5-20250929-v1:0",
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}]
            }
        ],
        inferenceConfig={
            "maxTokens": 512,      # cap response length (cost control)
            "temperature": 0.7,    # 0 = deterministic/focused, 1 = more creative/random
        }
    )
    return response["output"]["message"]["content"][0]["text"]

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ("exit", "quit"):
            break
        reply = ask_claude(user_input)
        print(f"\nClaude: {reply}")
