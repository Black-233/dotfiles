#!/usr/bin/python

import os
import sys
import shutil


shittyfiles = [
    '~/.python_history',                    # Python命令行历史记录
    '~/.dotnet/',                           # AUR仓库编译C#程序生成的目录
    '~/.gradle/',                           # 编译Java程序生成的目录
    '~/.local/share/recently-used.xbel',
    '~/.nv/',
    '~/.java/',
    '~/.oracle_jre_usage/',
    '~/.local/share/Trash/'                 # Vscode中删除的文件会放在这
]


def yesno(question, default="n"):
    # 询问使用者是否进行删除操作

    prompt = "%s (y/[n]) " % question

    ans = input(prompt).strip().lower()

    if not ans:
        ans = default

    if ans == "y":
        return True
    return False


def rmshit():
    print("发现垃圾文件：")
    found = []
    for f in shittyfiles:
        absf = os.path.expanduser(f)
        if os.path.exists(absf):
            found.append(absf)
            print("    %s" % f)

    if len(found) == 0:
        print("未发现垃圾文件 :)")
        return

    if yesno("删除所有？", default="n"):
        for f in found:
            if os.path.isfile(f):
                os.remove(f)
            else:
                shutil.rmtree(f)
        print("清理完成")
    else:
        print("未删除任何文件")


if __name__ == '__main__':
    rmshit()
