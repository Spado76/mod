import speech_recognition

import mc_socket
from mc_socket import MCSocket
import speech_recognition as sr
import argparse

# Original Mod From Here:
"""
https://github.com/ketan-ryan/MCRecog/tree/1.19.2
"""

parser = argparse.ArgumentParser()
parser.add_argument("-m", "--Microphone", help="Manually select microphone", action='store_true')
arguments = parser.parse_args()

r = sr.Recognizer()
r.energy_threshold = 700

mic_idx = None
if arguments.Microphone:
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"Microphone with name {name} found for `Microphone(device_index={index})`")

    mic_idx = int(input("Please input the device index of your primary microphone: "))

mic = sr.Microphone(mic_idx)
mc = MCSocket(7777)
print("Ready to begin speech recognition!")


def get_response(response):
    res = response
    response = str(resp).replace(" ", "").lower()
    print(response)

    ret = []
    if "njir" in response:
        ret.append("Explode and die")
    if "meledak" in response:
        ret.append("Explode and die")
    if 'dahlah' in response:
        ret.append("Explode and die")
    if "asu" in response:
        ret.append("Explode and die")
    if "badjingan" in response:
        ret.append("Explode and die")
    if "goblok" in response:
        ret.append("Explode and die")
    if "makan" in response:
        ret.append("Lose all hunger")
    if "bebek" in response:
        ret.append("Lose something random")
    if "ilang" in response:
        ret.append("Lose something random")
    if "gali" in response:
        ret.append("Big hole")
    if 'memek' in response:
        ret.append("Big hole")
    if 'lubang' in response:
        ret.append("Big hole")
    if 'belahan' in response:
        ret.append("Big hole")
    if 'ngewe' in response:
        ret.append("Big hole")
    if 'awasjatuh' in response:
        ret.append("Big hole")
    if 'apaitu' in response:
        ret.append("Spawn supercharged creeper")
    if 'tahi' in response:
        ret.append("Spawn supercharged creeper")
    if 'mampus' in response:
        ret.append("Spawn supercharged creeper")
    if 'gelap' in response:
        ret.append("Set on fire")
    if 'panas' in response:
        ret.append("Set on fire")
    if 'tolong' in response:
        ret.append("Lava source block")
    if 'iron' in response:
        ret.append("Spawn aggro iron golem")
    if 'diamond' in response:
        ret.append("Set to half a heart")
    if 'cobacek' in response:
        ret.append("Shuffle inventory")
    if 'susahini' in response:
        ret.append("Shuffle inventory")
    if 'pindah' in response:
        ret.append("Teleport randomly")
    if 'kaliankemana' in response:
        ret.append("Teleport randomly")
    if 'kesini' in response:
        ret.append("Teleport randomly")
    if 'rene' in response:
        ret.append("Teleport randomly")
    if 'lompat' in response:
        ret.append("Launched in the air")
    if 'keatas' in response:
        ret.append("Launched in the air")
    if 'diatas' in response:
        ret.append("Launched in the air")
    if 'padakemana' in response:
        ret.append("Launched in the air")
    if 'terbang' in response:
        ret.append("Launched in the air")
    if 'bakuhantam' in response:
        ret.append("Surround in obsidian")
    if 'satulawansatu' in response:
        ret.append("Surround in obsidian")
    if 'anjing' in response:
        ret.append("Random explosion")
    if 'perhatian' in response:
        ret.append("Random explosion")
    if 'jebluk' in response:
        ret.append("Random explosion")
    if 'tolol' in response:
        ret.append("Lightning")
    if 'kaget' in response:
        ret.append("Lightning")
    if 'gacor' in response:
        ret.append("Lightning")
    if 'zeus' in response:
        ret.append("Lightning")
    if 'kelihatan' in response:
        ret.append("Ink Splat")
    if 'lihatdeh' in response:
        ret.append("Ink Splat")
    if 'lihatsini' in response:
        ret.append("Ink Splat")
    if 'ireng' in response:
        ret.append("Ink Splat")
    if 'hitam' in response:
        ret.append("Ink Splat")
    if 'pukul' in response:
        ret.append("Knockback")
    if 'mental' in response:
        ret.append("Knockback")
    if 'kontol' in response:
        ret.append("Instant death")
    if 'mati' in response:
        ret.append("Instant death")
    if 'modar' in response:
        ret.append("Instant death")
    if 'kocak' in response:
        ret.append("Instant death")
    if 'kampret' in response:
        ret.append("Instant death")
    if 'buang' in response:
        ret.append("Drop inventory")
    if 'kasihaku' in response:
        ret.append("Drop inventory")
    if 'hatihati' in response:
        ret.append("Drop inventory")

    print(response, ret)

    ret.append(res)
    return ret


while 1:
    try:
        with mic as src:
            r.adjust_for_ambient_noise(src)
            audio = r.listen(src, phrase_time_limit=5)
            resp = r.recognize_google(audio, language="id-ID")
            cmd = get_response(resp)

            mc.stream(cmd)

    except speech_recognition.UnknownValueError as e:
        print("Audio tidak terdeteksi: {0}".format(e))
        pass
