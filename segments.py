import pandas as pd
from pydub import AudioSegment


def splice_audio(input_wav, output_folder, segments_df):
    audio = AudioSegment.from_wav(input_wav)
    
    for index, row in segments_df.iterrows():
        start_time = row['Start Time'] * 1000  # Convert to milliseconds
        end_time = row['End Time'] * 1000      # Convert to milliseconds
        segment_id = f"{start_time}_{end_time}"  # Use start and end times as segment ID
        segment = audio[start_time:end_time]
        output_file = f"{output_folder}/segment_{segment_id}.wav"  # Create file name with segment ID
        segment.export(output_file, format="wav")  #name of output file will be "segment_{start_time}_{end_time}.wav"


if __name__ == "__main__":
    input_wav = "test/debate_2.wav"
    csv_file = "test/output.csv"
    output_folder = "folder"
    
    # Read time segments from CSV
    segments_df = pd.read_csv(csv_file)
    
    # Splice audio segments
    splice_audio(input_wav, output_folder, segments_df)
    print("Audio segments have been extracted successfully.")
