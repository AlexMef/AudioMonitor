import logging
import os
import sounddevice as sd
import wavio as wv
from datetime import datetime
import vlc

# uncomment to enable testing
T_test_dir = "src"

C_rec_template = "recording" # common name for recording
C_freq = 44100 # discretization value
C_duration = 10 # default recording duration

# print(os.getcwd())
# recording = sd.rec(int(c_freq * c_duration), samplerate=c_freq, channels=2) # create recording using
# sd.wait()
# wv.write("recording2.wav", recording, c_freq, sampwidth=2)

# sd.play(recording, freq)
# sd.wait()


def aumon_record():
    recording = sd.rec(int(C_freq * C_duration), samplerate=C_freq, channels=2)  # create recording using
    sd.wait()
    try:
        rec_name_builder = C_rec_template
        current_time = str(datetime.now().strftime("%H-%M-%S"))

        print(current_time)
        print(type(current_time))
        # print(current_time.strftime("%H:%M:%S"))
        # rec_name_builder.join(str(current_time.strftime("%H-%M-%S")))
        rec_name_builder = rec_name_builder + "-" + current_time + ".wav"
        print(rec_name_builder)
        print(type(rec_name_builder))
        wv.write(rec_name_builder, recording, C_freq, sampwidth=2)
    except PermissionError:
        logging.Logger.error("Not enough rights to write. Check write permissions")


def aumon_play(recording):
    sd.play(recording, C_freq)


def aumon_list_recordings():
    record_files = []
    all_files = os.listdir(os.getcwd())

    if len(all_files) != 0:
        for x in all_files:
            if x.lower()[0:len(C_rec_template)] == C_rec_template.lower():
                record_files.append(x)
        for x in record_files:
            print(x)
    return record_files


if __name__ == '__main__':
    aumon_record()
    aumon_record()
    aumon_list_recordings()
