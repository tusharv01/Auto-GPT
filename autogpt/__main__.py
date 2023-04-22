"""Auto-GPT: A GPT powered AI Assistant"""
import autogpt.cli

if __name__ == "__main__":
    autogpt.cli.main()

    
    # Set the encoding for the input string
input_string = "comunicação"
encoded_input = input_string.encode("utf-8")

# Use the encoded string as input to Auto-GPT
output = model.predict(encoded_input)

# Decode the output back into a string
decoded_output = output.decode("utf-8")
