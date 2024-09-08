from flask import Flask, request, send_file
import yt_dlp as youtube_dl  # استخدام yt-dlp بدلاً من youtube_dl
import os

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download_video():
    """
    Handles the video download request from the provided URL.
    
    This function extracts the URL from the POST request, 
    uses yt_dlp to download the video in the best available quality,
    and then sends the downloaded video file to the client as an attachment.
    
    If an error occurs during the download process, an error message is returned
    with a status code of 400.
    """
    # Retrieve the URL from the POST request form data
    url = request.form['url']
    # Define the path where the downloaded video will be saved
    output_path = 'downloaded_video.mp4'

    # Options for yt_dlp
    ydl_opts = {
        'outtmpl': output_path,  # Output file template
        'format': 'best',        # Download the best available quality
    }

    try:
        # Create a YoutubeDL instance with the specified options
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            # Download the video from the provided URL
            ydl.download([url])
        # Send the downloaded video file to the client
        return send_file(output_path, as_attachment=True)
    except Exception as e:
        # Return an error message if the download fails
        return str(e), 400

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True)
