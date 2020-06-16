import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import os

# 创建一个主窗口
win = tk.Tk()
# 设置主窗口的大小
win.geometry("1440x540+20+20")
# 防止用户调整尺寸
win.resizable(0, 0)
# 设置主窗口的标题
win.title("超级变变变")

# 定义全局变量：原始图像，效果图像，风格图像
original = Image.new('RGB', (300, 400))
final = Image.new('RGB', (300, 400))
style = Image.new('RGB', (300, 400))
global select_img
global final_original
img1 = tkinter.Label(win)
img2 = tkinter.Label(win)
img3 = tkinter.Label(win)


# 定义选择图像函数
def choose_img():
    global select_img
    select_img = tk.filedialog.askopenfilename(title='选择图片')
    # e.set(select_img)
    global original
    original = Image.open(select_img)
    global final
    final = Image.open(select_img)
    width = original.size[0]  # 获取宽度
    height = original.size[1]  # 获取高度
    ratio_w = 200 / width
    ratio_h = 200 / height
    if width > 200 or height > 200:
        if ratio_w >= ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    else:
        if ratio_w <= ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    original = original.resize((int(width * ratio), int(height * ratio)), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(original)
    global img1
    img1.destroy()
    img1 = tkinter.Label(win, image=render)
    img1.image = render
    img1.place(relx=0.2, rely=0.5, anchor="center")


# 定义加载风格图像函数
def load_img(*args):
    path = 'images/styles/' + comboxlist.get() + '.jpg'
    global style
    style = Image.open(path)
    width = style.size[0]  # 获取宽度
    height = style.size[1]  # 获取高度
    ratio_w = 200 / width
    ratio_h = 200 / height
    if width > 200 or height > 200:
        if ratio_w >= ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    else:
        if ratio_w <= ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    style = style.resize((int(width * ratio), int(height * ratio)), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(style)
    global img2
    img2.destroy()
    img2 = tkinter.Label(win, image=render)
    img2.image = render
    img2.place(relx=0.5, rely=0.5, anchor="center")


# 定义图像风格迁移函数
def transfer_img():
    name = comboxlist.get()  # 得到下拉菜单所选择的风格名字 string
    models_path = "models/" + name + ".pth"
    os.system("python stylized-image.py {} {}".format(select_img,models_path))
    #给final赋值为 生成的图片
    final_path="images/outputs/"+models_path.split("/")[-1]+"-"+select_img.split("/")[-1]
    global final
    final = Image.open(final_path)
    global final_original
    final_original=final
    #输出图片
    width = final.size[0]   # 获取宽度
    height = final.size[1]   # 获取高度
    ratio_w = 200/width
    ratio_h = 200/height
    if width >200 or height >200:
        if ratio_w>=ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    else:
        if ratio_w<=ratio_h:
            ratio = ratio_w
        else:
            ratio = ratio_h
    final = final.resize((int(width*ratio), int(height*ratio)), Image.ANTIALIAS)
    render = ImageTk.PhotoImage(final)
    global img3
    img3.destroy()
    img3 = tkinter.Label(win,image=render)
    img3.image = render
    img3.place(relx=0.8,rely=0.5,anchor="center")



# 定义保存图像函数
def save_img():
    fname = tkinter.filedialog.asksaveasfilename(title='保存文件', filetypes=[("PNG", ".png")])
    global final_original
    final_original.save(str(fname) + '.png', 'PNG')


# 创建按钮
button1 = tkinter.Button(win, text="选择图像", command=choose_img)
button1.place(relx=0.2, rely=0.9, anchor="center")

button2 = tkinter.Button(win, text="风格迁移", command=transfer_img)
button2.place(relx=0.5, rely=0.9, anchor="center")

button3 = tkinter.Button(win, text="保存图像", command=save_img)
button3.place(relx=0.8, rely=0.9, anchor="center")

# 创建下拉列表
comvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
comboxlist = ttk.Combobox(win, width=9, textvariable=comvalue)  # 初始化
comboxlist["values"] = ("starry_night", "Chengbao", "cuphead", "Dongm", "Fangao", "Mon", "mosaic", "Nahan", "XPY")
comboxlist["state"] = 'readonly'
comboxlist.current(0)  # 选择第一个
comboxlist.bind("<<ComboboxSelected>>", load_img)  # 绑定事件,下拉列表框被选中时，绑定load_img()函数
comboxlist.place(relx=0.5, rely=0.1, anchor="center")

# 初始化打开风格图像
style = Image.open('images/styles/starry_night.jpg')
width = style.size[0]  # 获取宽度
height = style.size[1]  # 获取高度
ratio_w = 200 / width
ratio_h = 200 / height
if width > 200 or height > 200:
    if ratio_w >= ratio_h:
        ratio = ratio_w
    else:
        ratio = ratio_h
else:
    if ratio_w <= ratio_h:
        ratio = ratio_w
    else:
        ratio = ratio_h
style = style.resize((int(width * ratio), int(height * ratio)), Image.ANTIALIAS)
render = ImageTk.PhotoImage(style)
img2.destroy()
img2 = tkinter.Label(win, image=render)
img2.image = render
img2.place(relx=0.5, rely=0.5, anchor="center")

# 启动窗口并消息循环
win.mainloop()
