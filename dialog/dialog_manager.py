import subprocess


def escape(text):
    return text.replace("\"", "") \
        .replace("\'", "") \
        .replace("\\", "")


def show(src_text, dst_text):
    title = "translate result"

    src = escape(src_text)
    dst = escape(dst_text)
    body = src + "\n" + dst
    args = ['osascript', '-e',
            'tell app "System Events" to display dialog \"' + body + '\"  with title \"' + title + '\"']
    subprocess.call(args)


def show_text(text):
    title = "translate result"
    body = escape(text)
    args = ['osascript', '-e',
            'tell app "System Events" to display dialog \"' + body + '\"  with title \"' + title + '\"']
    subprocess.call(args)
