
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

model_name = "google/flan-t5-base"
# hface_token = ""
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def suggest_titles(blog_content):
    prompt = f"Generate 3 short and catchy blog post titles (max 8-10 words) for this content:\n{blog_content}"
    input_ids = tokenizer(prompt, return_tensors="pt", max_length = 512, truncation=True).input_ids
    outputs = model.generate(input_ids, max_length=20, num_return_sequences=3, do_sample=True, top_k=60, top_p = 0.95, temperature=0.9)
    titles = [tokenizer.decode(output, skip_special_tokens=True).strip() for output in outputs]
    return titles

if __name__ == "__main__":
    blog_text = input("Enter your blog content:\n")
    suggestions = suggest_titles(blog_text)
    
    print("\nSuggested Titles:")
    for idx, title in enumerate(suggestions, 1):
        print(f"{idx}. {title}")