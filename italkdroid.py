#!/usr/bin/env python
## iTalkDroid.py
import android as a
droid = a.Android()
d = droid
speech = d.recognizeSpeech("Talk Now", None, None)
print = speech[1]
d.ttsSpeak(speech[1])
##If Speech Recognition Is OFF, An Alert Prompt Appears For You To Turn Speech Recognition ON.
