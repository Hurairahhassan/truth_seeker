import streamlit as st
import requests
from PIL import Image
from io import BytesIO

API_URL = "https://api-inference.huggingface.co/models/umm-maybe/AI-image-detector"
HEADERS = {"Authorization": "Bearer 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"}

def query_api(image_bytes):
    response = requests.post(API_URL, headers=HEADERS, data=image_bytes)
    return response.json()

def main():
    st.title("Image Classifier App")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

        if st.button("Classify"):
            st.spinner("Classifying...")

            # Convert the image to bytes
            image_bytes = BytesIO()
            image.save(image_bytes, format="JPEG")
            image_bytes = image_bytes.getvalue()

            # Query the Hugging Face API
            result = query_api(image_bytes)
            # Display the result 0 index
            st.success(result[0]["label"])

            st.success("Classification Result:")
            st.json(result)




from serpapi import GoogleSearch

def get_visual_matches(api_key, url):
    params = {
        "engine": "google_lens",
        "url": url,
        "api_key": api_key  # Pass the API key here
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    visual_matches = results.get("visual_matches", [])  # Use get() to handle cases where "visual_matches" key may be missing
    return visual_matches

# Streamlit App
st.title("BawdicSoft Truth Seeker Images Viewer")

# Input URL
url = st.text_input("Enter Image URL:")

if url:
    # Set your API key here
    api_key = "a77a244ef93d7edeb016d71a2d894eeb4610646c1f922797080d36bbe07ad100"

    # Get Visual Matches
    visual_matches = get_visual_matches(api_key, url)

    # Display Visual Matches
    if visual_matches:
        st.subheader("Visual Matches:")
        for item in visual_matches:
            st.write(f"Position {item['position']}: Link - {item['link']}, Source - {item['source']}")
    else:
        st.warning("No visual matches found.")
else:
    st.warning("Please enter an image URL.")


if __name__ == "__main__":
    main()
