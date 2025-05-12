# 📰 News Article Summarizer

This is a web-based application for summarizing news articles using state-of-the-art Natural Language Processing (NLP) techniques. It leverages the `facebook/bart-large-cnn` model for generating high-quality, concise summaries.

## 🚀 Features
- 📝 Enter a news article to get an instant summary.
- 🔍 Built with `Streamlit` for an interactive web interface.
- ⚡ Fast processing with the pre-trained `BART` transformer model.
- 🌐 Deployable both locally and online.

## 📦 Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/news-summarizer.git
    cd news-summarizer
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    streamlit run app.py
    ```

## 🔄 Model and Dataset
- **Model**: `facebook/bart-large-cnn`
- **Dataset**: `CNN/DailyMail` subset

## 🌐 Deployment
To deploy this app online:
1. **Streamlit Community Cloud** (Free and Permanent)
   - Go to [Streamlit Cloud](https://streamlit.io/cloud)
   - Click **New App** → Select your GitHub repo
   - Choose `app.py` as the entry point
   - Click **Deploy**

2. **Ngrok for Temporary Access** (Optional)
3. **Heroku for Long-term Hosting** (Optional)

## 🤖 Usage
1. Enter the news article text in the input box.
2. Click **Summarize**.
3. Get the summarized version instantly.

## 🛠️ Requirements
- `streamlit`
- `transformers`
- `torch`

## 👨‍💻 Author
- Rami B.
- Programming II Exam Project

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
