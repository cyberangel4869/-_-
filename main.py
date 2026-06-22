import tkinter as tk
from tkinter import ttk

class area:
    def __init__(self,name,addition,skill):
        self.name=name
        self.addition = addition
        self.skill = skill

    def Find(self,add,skill):
        if add in self.addition and skill in self.skill:
            return self.name
        else:
            return ""

print("基质刷取地区筛选程序测试")
    
area1=area(name="首墩",\
            addition=["攻击提升","物理伤害提升","灼热伤害提升","电磁伤害提升",
                      "自然伤害提升","暴击率提升","终结技充能效率提升","法术伤害提升"],\
            skill=["强攻","追击","昂扬","残暴",
                   "附术","夜幕","流转","效益"])
area2=area(name="清波寨",\
            addition=["生命提升","物理伤害提升","电磁伤害提升","寒冷伤害提升",
                      "源石技艺提升","终结技充能效率提升","法术伤害提升","治疗效率提升"],\
            skill=["压制","粉碎","昂扬","巧技",
                    "医疗","切骨","迸发","夜幕"])
area3=area(name="藏剑谷",\
            addition=["攻击提升","生命提升","物理伤害提升","灼热伤害提升",
                      "寒冷伤害提升","自然伤害提升","源石技艺提升","治疗效率提升"],\
            skill=["强攻","追袭","昂扬","巧技",
                   "医疗","切骨","迸发","效益"])
area4=area(name="实验园区",\
            addition=["生命提升","灼热伤害提升","电磁伤害提升","寒冷伤害提升",
                     "自然伤害提升","源石技艺提升","终结技充能效率提升","治疗效率提升"],\
            skill=["压制","粉碎","巧技","残暴",
                   "附术","切骨","夜幕","流转"])
area5=area(name="武陵观测站",\
            addition=["攻击提升","生命提升","电磁伤害提升","寒冷伤害提升",
                     "暴击率提升","终结技充能效率提升","法术伤害提升","治疗效率提升"],\
            skill=["强攻","粉碎","残暴","医疗",
                   "切骨","迸发","夜幕","流转"])

additions=set(area1.addition+area2.addition+area3.addition+area4.addition+area5.addition)
skills=set(area1.skill+area2.skill+area3.skill+area4.skill+area5.skill)
print("附加属性列表:",additions)
print("技能属性列表:",skills)

# 创建主窗口
root = tk.Tk()
root.title("终末地基质刷取点筛选器")

# 设置窗口大小（增加高度）
root.geometry("300x280")  # 改大了高度和宽度

# 创建标签
label1 = tk.Label(root, text="附加属性:", width=10)
label1.grid(row=0, column=0, pady=5, sticky="e")

label2 = tk.Label(root, text="技能属性:", width=10)
label2.grid(row=1, column=0, pady=5, sticky="e")

label3 = tk.Label(root, text="基质刷取点:", width=10)
label3.grid(row=2, column=0, pady=5, sticky="e")

# 创建下拉框
addition_list = list(additions)
selected_addition = tk.StringVar()
selected_addition.set(addition_list[0])
dropdown1 = tk.OptionMenu(root, selected_addition, *additions)
dropdown1.grid(row=0, column=1, pady=5, padx=5)

skill_list = list(skills)
selected_skill = tk.StringVar()
selected_skill.set(skill_list[0])
dropdown2 = tk.OptionMenu(root, selected_skill, *skills)
dropdown2.grid(row=1, column=1, pady=5, padx=5)

# 创建结果显示框
result_var = tk.StringVar()
result_var.set("单击下方的按键查找")
result_txt = tk.Label(root, textvariable=result_var, width=25, height=5, 
                      relief="solid", bg="light yellow")  # 添加边框和背景色
result_txt.grid(row=2, column=1, pady=5, padx=5)

def search():
    selected_addition_value = selected_addition.get()
    selected_skill_value = selected_skill.get()
    print("附加属性:", selected_addition_value, "技能属性:", selected_skill_value)
    
    # 遍历所有地区
    areas = [area1, area2, area3, area4, area5]
    result = ""
    for area in areas:
        if area.Find(selected_addition_value, selected_skill_value) != "":
            result = area.Find(selected_addition_value, selected_skill_value)
            break
    
    if result:
        result_var.set(result)
    else:
        result_var.set("未找到匹配的地区")

# 创建按钮（放在第3行，跨两列居中）
button = tk.Button(root, text="查找基质刷取点", command=search, 
                   width=20, bg="light blue")
button.grid(row=3, column=0, columnspan=2, pady=15)  # columnspan让按钮跨越两列

# 运行主循环
root.mainloop()