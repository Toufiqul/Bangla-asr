import pandas as pd
from pydub import AudioSegment

def splice_audio(input_wav, output_folder, segments_df):
    audio = AudioSegment.from_wav(input_wav)
    
    for index, row in segments_df.iterrows():
        start_time = row['Start Time'] * 1000  # Convert to milliseconds
        end_time = row['End Time'] * 1000      # Convert to milliseconds
        annotation_text = row['Annotation Text']
        segment = audio[start_time:end_time]
        output_file = f"{output_folder}/{annotation_text}.wav"
        segment.export(output_file, format="wav")

if __name__ == "__main__":
    input_wav = "path/to/your/input.wav"
    csv_file = "path/to/your/annotations.csv"
    output_folder = "path/to/output/folder"
    
    # Read time segments from CSV
    segments_df = pd.read_csv(csv_file)
    
    # Splice audio segments
    splice_audio(input_wav, output_folder, segments_df)
    print("Audio segments have been extracted successfully.")
